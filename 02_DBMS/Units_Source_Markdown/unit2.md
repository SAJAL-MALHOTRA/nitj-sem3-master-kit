# UNIT 2: Relational Data Model, Relational Algebra, and Advanced SQL

---

## 2.1 Relational Data Model Concepts

The Relational Data Model, introduced by Dr. Edgar F. Codd in his seminal 1970 paper *"A Relational Model of Data for Large Shared Data Banks"*, represents data logically as mathematical **Relations** rather than physical storage pointers.

### 2.1.1 Formal Mathematical Terminology vs. Informal Commercial Terminology

| Formal Mathematical Term | Informal / Commercial RDBMS Term | Conceptual Meaning |
| :--- | :--- | :--- |
| **Relation** | Table | A two-dimensional grid of rows and columns representing an entity or relationship. |
| **Tuple** | Row / Record | A single ordered list of values representing a specific entity instance. |
| **Attribute** | Column / Field | A named property or characteristic describing the relation. |
| **Domain** | Data Type / Permissible Values | The set of all atomic, allowable values for a given attribute. |
| **Relation Schema** $R(A_1, \dots, A_n)$ | Table Definition / Table Structure | The structural blueprint specifying table name and attribute definitions. |
| **Relation State** $r(R)$ | Table Population / Current Data | The snapshot collection of actual tuples residing in the relation at time $t$. |
| **Degree (Arity)** | Column Count | The total number of attributes composing the relation schema. |
| **Cardinality** | Row Count | The total number of tuples currently populated in the relation state. |

### 2.1.2 Formal Mathematical Definition of a Relation
Let $A_1, A_2, \dots, A_n$ be attributes with corresponding domains $\text{dom}(A_1), \text{dom}(A_2), \dots, \text{dom}(A_n)$.
The Cartesian Product of these domains is defined as:
$$\text{dom}(A_1) \times \text{dom}(A_2) \times \dots \times \text{dom}(A_n) = \{ \langle v_1, v_2, \dots, v_n \rangle \mid v_i \in \text{dom}(A_i), 1 \le i \le n \}$$

A **Relation State** $r(R)$ of relation schema $R(A_1, A_2, \dots, A_n)$ is mathematically defined as a subset of the Cartesian product of the domains of its attributes:
$$r(R) \subseteq \text{dom}(A_1) \times \text{dom}(A_2) \times \dots \times \text{dom}(A_n)$$

If the cardinalities of the domains are $|D_1|, |D_2|, \dots, |D_n|$, the total number of conceivable tuples in the Cartesian product is:
$$\text{Total Possible Tuples} = \prod_{i=1}^n |D_i|$$
The relation state $r(R)$ contains a tiny, semantically meaningful subset of these possible tuples at any given instant.

### 2.1.3 Inherent Characteristics of Mathematical Relations
1. **Ordering of Tuples is Immaterial:**
   Because a relation is mathematically defined as a **set** of tuples, and sets in mathematics possess no ordering ($\{t_1, t_2\} \equiv \{t_2, t_1\}$), the logical order of rows in a table has no significance. The DBMS storage manager is free to store them in any physical sequence.
2. **Ordering of Attributes within a Tuple is Logically Immaterial:**
   Although formally a tuple is an $n$-tuple of ordered values, in relational theory each attribute has a distinct name. Therefore, a tuple can be viewed as a mapping from attribute names to domain values: $t[A_i] \to v_i$.
3. **Values in Tuples are Atomic (First Normal Form Assumption):**
   Every value in a tuple must be an indivisible atomic element drawn from the attribute domain. Composite attributes (nested records) and multi-valued attributes (arrays, sets, nested tables) are strictly disallowed in pure relational databases.
4. **No Duplicate Tuples (Set Property):**
   Because a relation is a set, no two identical tuples can exist: $\forall t_1, t_2 \in r(R), t_1 \neq t_2$. Every relation must have a key.

---

## 2.2 Relational Integrity Constraints

Integrity constraints are declarative predicates that must evaluate to `TRUE` for every valid database state. They prevent invalid or corrupt data from being committed.

```
+-----------------------------------------------------------------------------------+
|                        RELATIONAL INTEGRITY CONSTRAINTS                           |
+---------------------+---------------------+------------------+--------------------+
|  Domain Constraints |   Entity Integrity  |   Referential    | Enterprise Rules   |
|                     |     Constraint      |    Integrity     |                    |
+---------------------+---------------------+------------------+--------------------+
| Data types, ranges, | Primary Key != NULL | Foreign Key must | Business rules,    |
| CHECK predicates    | Uniquely identifies | match valid PK   | CHECK constraints, |
| NOT NULL            | every tuple         | or be NULL       | Triggers           |
+---------------------+---------------------+------------------+--------------------+
```

### 2.2.1 Domain Integrity Constraints
- Specifies that the value of each attribute $A$ in tuple $t$ must be an atomic value belonging to the physical domain $\text{dom}(A)$.
- Enforced through:
  - Primitive data types (e.g., `INT`, `VARCHAR`, `DATE`).
  - Domain range checks (`CHECK (salary > 0 AND salary < 1000000)`).
  - Nullability restrictions (`NOT NULL`).

### 2.2.2 Entity Integrity Constraint
- **Formal Definition:** No attribute participating in the **Primary Key** of a base relation schema can accept a `NULL` value in any tuple of $r(R)$:
  $$\forall t \in r(R), \forall A \in \text{PK}(R) : t[A] \neq \text{NULL}$$
- **Mathematical Rationale:**
  The primary key serves as the unique identifier for individual entity instances in the real world. A `NULL` represents an unknown, absent, or inapplicable value. If a primary key attribute were `NULL`, the DBMS could not distinguish whether two rows with null primary keys represented the same physical entity or distinct entities, destroying identity and relational join consistency.

### 2.2.3 Referential Integrity Constraint
- **Formal Definition:** Given two relation schemas $R_1$ and $R_2$, a set of attributes $\text{FK}$ in $R_1$ is a **Foreign Key** referencing the Primary Key $\text{PK}$ of $R_2$ if:
  1. The attributes in $\text{FK}$ have the same domain as the attributes in $\text{PK}$.
  2. For every tuple $t_1 \in r(R_1)$, either:
     - $t_1[\text{FK}] = \text{NULL}$ (if nulls are allowed by domain constraints), OR
     - $\exists t_2 \in r(R_2)$ such that $t_1[\text{FK}] = t_2[\text{PK}]$.
- **Referential Integrity Actions (Handling Deletions and Updates):**
  When a tuple in the referenced relation $R_2$ is deleted or its primary key is updated, any referencing tuples in $R_1$ will become "dangling references". The DBMS enforces one of four declarative actions:

```
+-----------------------------------------------------------------------------------+
|                           FOREIGN KEY VIOLATION ACTIONS                           |
+-------------------+---------------------------------------------------------------+
| ACTION            | SYSTEM BEHAVIOR ON DELETION OF PARENT TUPLE                   |
+-------------------+---------------------------------------------------------------+
| ON DELETE RESTRICT| Rejects and aborts the deletion transaction immediately if    |
| / NO ACTION       | any child record references the parent tuple.                 |
+-------------------+---------------------------------------------------------------+
| ON DELETE CASCADE | Automatically deletes all matching referencing child tuples  |
|                   | in the dependent table.                                       |
+-------------------+---------------------------------------------------------------+
| ON DELETE SET NULL| Sets the foreign key columns in all referencing child tuples  |
|                   | to NULL (requires foreign key column to be nullable).         |
+-------------------+---------------------------------------------------------------+
| ON DELETE SET     | Sets the foreign key columns in all referencing child tuples  |
| DEFAULT           | to a pre-configured default value.                            |
+-------------------+---------------------------------------------------------------+
```

*SQL Syntax Example:*
```sql
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

### 2.2.4 Enterprise (Semantic) Constraints
- Business-specific rules that cannot be captured by simple key or referential constraints.
- *Examples:*
  - "An employee cannot manage more than two projects simultaneously."
  - "The salary of an employee cannot exceed the salary of their direct supervisor."
- Enforced via complex `CHECK` constraints, SQL `ASSERTION` statements, or active procedural `TRIGGERS`.

---

## 2.3 Relational Algebra

Relational Algebra is a formal, **procedural** query language. It consists of a collection of algebraic operators that take one or two relations as input and produce a **new relation** as output. This property is known as **Closure**: because the result of every operation is itself a relation, operations can be arbitrarily nested into complex relational algebraic expressions.

```
                              RELATIONAL ALGEBRA OPERATORS
                                            |
       +------------------------------------+------------------------------------+
       |                                                                         |
       v                                                                         v
+-----------------------------+                           +-----------------------------+
|    FUNDAMENTAL OPERATORS    |                           |      DERIVED OPERATORS      |
+-----------------------------+                           +-----------------------------+
| 1. Select (sigma)           |                           | 1. Set Intersection (cap)   |
| 2. Project (pi)             |                           | 2. Theta Join (bowtie_theta)|
| 3. Union (cup)              |                           | 3. Equi-Join                |
| 4. Set Difference (-)       |                           | 4. Natural Join (bowtie)    |
| 5. Cartesian Product (x)    |                           | 5. Outer Joins (Left, Right)|
| 6. Rename (rho)             |                           | 6. Division (/)             |
+-----------------------------+                           +-----------------------------+
```

### 2.3.1 Fundamental Operations

#### 1. Selection ($\sigma_p(R)$)
- **Concept:** Filters tuples from relation $R$ that satisfy a Boolean selection predicate $p$. It acts as a **horizontal filter**.
- **Formal Definition:**
  $$\sigma_p(R) = \{ t \in R \mid p(t) = \text{TRUE} \}$$
  Predicate $p$ is a propositional formula consisting of terms connected by $\land$ (AND), $\lor$ (OR), and $\neg$ (NOT), where each term is of the form:
  $$\text{Attribute} \text{ op } \text{Constant} \quad \text{or} \quad \text{Attribute}_1 \text{ op } \text{Attribute}_2$$
  with $\text{op} \in \{=, \neq, <, \le, >, \ge\}$.
- **Properties:**
  - $\text{Degree}(\sigma_p(R)) = \text{Degree}(R)$
  - $0 \le |\sigma_p(R)| \le |R|$
  - Commutative: $\sigma_{p_1}(\sigma_{p_2}(R)) \equiv \sigma_{p_2}(\sigma_{p_1}(R)) \equiv \sigma_{p_1 \land p_2}(R)$
- **Example:** Select employees earning more than $50,000 in department 10:
  $$\sigma_{\text{salary} > 50000 \land \text{dept\_id} = 10}(\text{Employee})$$

#### 2. Projection ($\pi_{A_1, A_2, \dots, A_k}(R)$)
- **Concept:** Selects specified columns $A_1, \dots, A_k$ from relation $R$ and discards all other columns. It acts as a **vertical filter**.
- **Crucial Mathematical Rule:** **Duplicate Elimination**. Because a mathematical relation is a set, if projecting out a column leaves identical rows, all duplicate tuples are stripped.
- **Formal Definition:**
  $$\pi_{A_1, \dots, A_k}(R) = \{ t[A_1, \dots, A_k] \mid t \in R \}$$
- **Properties:**
  - $\text{Degree}(\pi_{A_1, \dots, A_k}(R)) = k$
  - $1 \le |\pi_{A_1, \dots, A_k}(R)| \le |R|$ (cardinality is strictly $\le |R|$ due to duplicate removal).
  - Non-commutative with nested projections: $\pi_{L_1}(\pi_{L_2}(R)) \equiv \pi_{L_1}(R)$ where $L_1 \subseteq L_2$.
- **Example:** List distinct salary values:
  $$\pi_{\text{salary}}(\text{Employee})$$

#### 3. Union ($R \cup S$)
- **Concept:** Combines all tuples from relation $R$ and relation $S$ into a single relation, eliminating duplicates.
- **Prerequisite Condition: Union Compatibility (Type Compatibility):**
  Two relations $R$ and $S$ are union-compatible if and only if:
  1. They have the same degree: $\text{Degree}(R) = \text{Degree}(S) = n$.
  2. The domains of the corresponding attributes are compatible: $\text{dom}(A_i) = \text{dom}(B_i)$ for all $1 \le i \le n$.
- **Formal Definition:**
  $$R \cup S = \{ t \mid t \in R \lor t \in S \}$$
- **Properties:**
  - Commutative: $R \cup S \equiv S \cup R$
  - Associative: $(R \cup S) \cup T \equiv R \cup (S \cup T)$
  - Max Cardinality: $|R \cup S| \le |R| + |S|$

#### 4. Set Difference ($R - S$)
- **Concept:** Returns all tuples that appear in relation $R$ but do **not** appear in relation $S$.
- **Prerequisite:** $R$ and $S$ must be **Union Compatible**.
- **Formal Definition:**
  $$R - S = \{ t \mid t \in R \land t \notin S \}$$
- **Properties:**
  - **Not Commutative:** $R - S \neq S - R$
  - Max Cardinality: $|R - S| \le |R|$

#### 5. Cartesian Product (Cross Product) ($R \times S$)
- **Concept:** Concatenates every tuple of relation $R$ with every tuple of relation $S$.
- **Formal Definition:**
  $$R \times S = \{ t_1 \circ t_2 \mid t_1 \in R \land t_2 \in S \}$$
  where $t_1 \circ t_2$ represents tuple concatenation.
- **Properties:**
  - $\text{Degree}(R \times S) = \text{Degree}(R) + \text{Degree}(S)$
  - Cardinality: $|R \times S| = |R| \times |S|$
  - Commutative (up to attribute ordering): $R \times S \cong S \times R$

#### 6. Rename Operation ($\rho$)
- **Concept:** Renames the output relation and/or its attribute names.
- **Syntax Forms:**
  - $\rho_S(R)$: Renames relation $R$ to $S$.
  - $\rho_{S(B_1, B_2, \dots, B_n)}(R)$: Renames relation $R$ to $S$ and renames its attributes to $B_1, \dots, B_n$.
  - $\rho_{(B_1, B_2, \dots, B_n)}(R)$: Renames only the attributes.

---

### 2.3.2 Derived (Additional) Relational Operations

#### 1. Set Intersection ($R \cap S$)
- Returns tuples appearing in both $R$ and $S$. Requires union compatibility.
- Derived algebraically via Set Difference:
  $$R \cap S = R - (R - S)$$
- Commutative: $R \cap S \equiv S \cap R$.

#### 2. Theta Join ($R \bowtie_\theta S$)
- Combines a Cartesian Product with a Selection condition $\theta$:
  $$R \bowtie_\theta S = \sigma_\theta(R \times S)$$
  where $\theta$ is a predicate over attributes of $R$ and $S$.

#### 3. Equi-Join
- A specific variant of Theta Join where all comparison operators in $\theta$ are strictly equalities ($=$).

#### 4. Natural Join ($R \bowtie S$)
- **Concept:** An Equi-join on all attributes common to both $R$ and $S$, followed by projecting out redundant duplicate attribute columns.
- **Formal Procedure:**
  Let $R(A_1, \dots, A_m, C_1, \dots, C_k)$ and $S(C_1, \dots, C_k, B_1, \dots, B_n)$, where $\{C_1, \dots, C_k\} = R \cap S$ are the shared attributes.
  $$R \bowtie S = \pi_{A_1, \dots, A_m, C_1, \dots, C_k, B_1, \dots, B_n}(\sigma_{R.C_1 = S.C_1 \land \dots \land R.C_k = S.C_k}(R \times S))$$
- **Properties:**
  - Associative: $(R \bowtie S) \bowtie T \equiv R \bowtie (S \bowtie T)$
  - Commutative: $R \bowtie S \equiv S \bowtie R$
  - If $R \cap S = \emptyset$, then $R \bowtie S \equiv R \times S$.

#### 5. Outer Joins
Standard joins discard tuples from either relation that fail to satisfy the join predicate. Outer joins retain non-matching tuples, padding missing attributes with `NULL`.
- **Left Outer Join ($R ⟕ S$):** Keeps all tuples from the left relation $R$. If no match exists in $S$, attributes of $S$ are filled with `NULL`.
- **Right Outer Join ($R ⟖ S$):** Keeps all tuples from the right relation $S$.
- **Full Outer Join ($R ⟗ S$):** Keeps all tuples from both $R$ and $S$.

#### 6. Division Operation ($R \div S$)
- **Motivation:** Used for universal quantification queries answering: *"Find entities in $R$ associated with ALL entities in $S$."*
- **Mathematical Preconditions:**
  - Let schema of $R$ be $Z = X \cup Y$.
  - Let schema of $S$ be $Y$.
  - Schema of result $R \div S$ is $X$.
- **Formal Definition:**
  $$R \div S = \{ t[X] \mid t \in R \land \forall s \in S, \exists t' \in R \text{ such that } t'[X] = t[X] \land t'[Y] = s[Y] \}$$
- **Algebraic Derivation using Fundamental Operators:**
  $$R \div S = \pi_X(R) - \pi_X((\pi_X(R) \times S) - R)$$
  *Step-by-step derivation breakdown:*
  1. $\pi_X(R)$ yields all potential candidate values for $X$.
  2. $\pi_X(R) \times S$ represents all conceivable pairings of candidates with every element in $S$.
  3. $(\pi_X(R) \times S) - R$ isolates the pairings that are **missing** from $R$.
  4. $\pi_X((\pi_X(R) \times S) - R)$ yields all candidates that failed to match at least one element in $S$.
  5. Subtracting these disqualified candidates from $\pi_X(R)$ yields strictly those $X$ values that matched **every** element in $S$.

---

## 2.4 SQL Architecture & Command Taxonomy

SQL (Structured Query Language) is the ANSI/ISO standard declarative language for relational database systems.

```
+---------------------------------------------------------------------------------------+
|                                    SQL TAXONOMY                                       |
+---------------------+---------------------+---------------------+---------------------+
|         DDL         |         DML         |         DCL         |         TCL         |
|  (Data Definition)  | (Data Manipulation) |   (Data Control)    | (Transaction Control)|
+---------------------+---------------------+---------------------+---------------------+
| CREATE TABLE        | SELECT              | GRANT               | COMMIT              |
| ALTER TABLE         | INSERT INTO         | REVOKE              | ROLLBACK            |
| DROP TABLE          | UPDATE              |                     | SAVEPOINT           |
| TRUNCATE TABLE      | DELETE FROM         |                     | SET TRANSACTION     |
+---------------------+---------------------+---------------------+---------------------+
```

### 2.4.1 Comprehensive Architectural Breakdown: TRUNCATE vs. DROP vs. DELETE

This is one of the most frequently asked end-term examination questions.

| Parameter / Feature | `DELETE` | `TRUNCATE` | `DROP` |
| :--- | :--- | :--- | :--- |
| **Command Classification** | DML (Data Manipulation) | DDL (Data Definition) | DDL (Data Definition) |
| **Scope of Operation** | Deletes specific rows or all rows matching a `WHERE` filter. | Deletes **all** rows in the table unconditionally. | Destroys the table data **and** the entire table schema. |
| **WHERE Clause Support** | **Yes** (`WHERE condition`) | **No**; operates on entire table. | **No**; removes entire structure. |
| **Transaction Rollback** | Fully rollbackable (`ROLLBACK` restores deleted rows). | Rollbackable in modern RDBMS (PostgreSQL, SQL Server), non-rollbackable in MySQL. | Non-rollbackable (or difficult depending on engine). |
| **Logging Mechanism** | Row-by-row logging: writes each deleted row to the Undo Log. | Page-level deallocation: logs only disk extent deallocations. | Metadata logging: updates system catalog tables. |
| **Execution Speed** | Slow on large tables (high lock overhead and log volume). | Extremely Fast (nearly instantaneous). | Fast (instantaneous). |
| **Triggers Activation** | Fires `ON DELETE` row-level triggers. | **Bypasses** all delete triggers. | Bypasses triggers (may fire DDL drop triggers). |
| **Space Reclamation** | Keeps disk space allocated; does not lower high-water mark. | Deallocates disk pages; resets High-Water Mark (HWM). | Frees all disk tablespace back to OS/tablespace pool. |
| **Identity / Auto-Increment**| Retains current identity seed counter. | Resets identity/auto-increment counter to initial seed. | Entire object removed from catalog. |
| **Referential Integrity** | Permitted if referenced by FK (subject to cascade rules). | **Prohibited** if table is referenced by an active FK constraint. | Fails if referenced by foreign key without `CASCADE`. |

---

## 2.5 SQL Operators, Three-Valued Logic, and Aggregate Functions

### 2.5.1 Three-Valued Logic (3VL) with NULL
In SQL, comparing any value to `NULL` using conventional operators ($=, \neq, <, >$) does not evaluate to `TRUE` or `FALSE`. It evaluates to **`UNKNOWN`**.
Because SQL operates on Three-Valued Logic (`TRUE`, `FALSE`, `UNKNOWN`), conditions in a `WHERE` clause must evaluate strictly to `TRUE` to be included in the output; rows evaluating to `UNKNOWN` are filtered out.

#### 3VL Truth Tables:
$$\begin{array}{|c|c|c|c|}
\hline
\mathbf{AND} & \mathbf{TRUE} & \mathbf{FALSE} & \mathbf{UNKNOWN} \\
\hline
\mathbf{TRUE} & \text{TRUE} & \text{FALSE} & \text{UNKNOWN} \\
\mathbf{FALSE} & \text{FALSE} & \text{FALSE} & \text{FALSE} \\
\mathbf{UNKNOWN} & \text{UNKNOWN} & \text{FALSE} & \text{UNKNOWN} \\
\hline
\end{array}
\quad
\begin{array}{|c|c|c|c|}
\hline
\mathbf{OR} & \mathbf{TRUE} & \mathbf{FALSE} & \mathbf{UNKNOWN} \\
\hline
\mathbf{TRUE} & \text{TRUE} & \text{TRUE} & \text{TRUE} \\
\mathbf{FALSE} & \text{TRUE} & \text{FALSE} & \text{UNKNOWN} \\
\mathbf{UNKNOWN} & \text{TRUE} & \text{UNKNOWN} & \text{UNKNOWN} \\
\hline
\end{array}$$

$$\begin{array}{|c|c|}
\hline
P & \mathbf{NOT}(P) \\
\hline
\text{TRUE} & \text{FALSE} \\
\text{FALSE} & \text{TRUE} \\
\text{UNKNOWN} & \text{UNKNOWN} \\
\hline
\end{array}$$

*Critical Trap:*
```sql
-- This query returns ZERO rows if any salary is NULL, because NULL = NULL evaluates to UNKNOWN!
SELECT * FROM Employee WHERE salary = NULL; 

-- Correct Query:
SELECT * FROM Employee WHERE salary IS NULL;
```

### 2.5.2 Built-In Aggregate Functions and NULL Handling
SQL provides five standard built-in aggregate functions:
1. `COUNT(*)`: Returns the total count of tuples, **including rows with NULLs**.
2. `COUNT(column)`: Returns the count of **non-NULL** values in that column.
3. `SUM(column)`: Calculates the arithmetic total, **ignoring all NULLs**.
4. `AVG(column)`: Calculates $\frac{\sum \text{non-NULL values}}{\text{COUNT(non-NULL values)}}$. It does **not** divide by total rows!
5. `MIN(column)` / `MAX(column)`: Finds minimum/maximum value, ignoring NULLs.

*Important Mathematical Nuance:*
If a column contains values `(10, 20, NULL)`:
- `COUNT(*)` $= 3$
- `COUNT(salary)` $= 2$
- `SUM(salary)` $= 30$
- `AVG(salary)` $= 30 / 2 = 15$ (NOT $30 / 3 = 10$).

---

## 2.6 The SQL Query Execution Pipeline: GROUP BY and HAVING

The logical execution order of an SQL query differs completely from its lexical (written) order:

```
LEXICAL (WRITTEN) ORDER:          LOGICAL (EXECUTION) ENGINE PIPELINE:
  1. SELECT                         1. FROM (Cross Joins, Table scans)
  2. FROM                           2. ON (Join filters)
  3. WHERE                          3. JOIN (Join operations)
  4. GROUP BY                       4. WHERE (Pre-aggregation row filter)
  5. HAVING                         5. GROUP BY (Aggregate partitioning)
  6. ORDER BY                       6. HAVING (Post-aggregation group filter)
  7. LIMIT / OFFSET                 7. SELECT (Expressions, aliases computed)
                                    8. DISTINCT (Duplicate elimination)
                                    9. ORDER BY (Sorting)
                                    10. LIMIT / OFFSET (Paging)
```

### 2.6.1 Crucial Distinction: WHERE vs. HAVING

| Parameter | `WHERE` Clause | `HAVING` Clause |
| :--- | :--- | :--- |
| **Execution Point** | Executes **before** `GROUP BY` grouping occurs. | Executes **after** `GROUP BY` aggregation occurs. |
| **Filtering Level** | Filters individual **rows (tuples)**. | Filters entire **groups of tuples**. |
| **Aggregate Functions** | **Strictly Prohibited** (`WHERE SUM(salary) > 5000` is invalid). | **Allowed and Expected** (`HAVING AVG(salary) > 50000`). |
| **Performance** | High; reduces row count early, saving memory and CPU. | Evaluates after aggregation; heavier memory footprint. |

*Query Example:*
```sql
SELECT dept_id, AVG(salary) AS avg_sal, COUNT(*) AS emp_count
FROM Employee
WHERE status = 'Active'               -- Row-level filter BEFORE grouping
GROUP BY dept_id
HAVING COUNT(*) >= 5                  -- Group-level filter AFTER grouping
   AND AVG(salary) > 60000
ORDER BY avg_sal DESC;
```

---

## 2.7 Joins in SQL

```
+-----------------------------------------------------------------------------------+
|                                  SQL JOIN TYPES                                   |
+---------------------+---------------------+------------------+--------------------+
|     INNER JOIN      |   LEFT OUTER JOIN   | RIGHT OUTER JOIN |  FULL OUTER JOIN   |
| Matching rows only  | All Left + Matched  | Matched + All    | All rows from both |
|                     | Right (or NULL)     | Right (or NULL)  | (Null padded)      |
+---------------------+---------------------+------------------+--------------------+
|     CROSS JOIN      |      SELF JOIN      |                  |                    |
|  Cartesian Product  | Table joined with   |                  |                    |
|  (|R| * |S| rows)   | itself via aliases  |                  |                    |
+---------------------+---------------------+------------------+--------------------+
```

### 2.7.1 ANSI Join Syntaxes and Concrete Walkthrough
Consider two relations:
- `Department(dept_id, dept_name)`: `{(1, 'HR'), (2, 'IT'), (3, 'Sales')}`
- `Employee(emp_id, name, dept_id)`: `{(101, 'Alice', 1), (102, 'Bob', 2), (103, 'Charlie', NULL)}`

1. **INNER JOIN:**
   ```sql
   SELECT E.name, D.dept_name
   FROM Employee E
   INNER JOIN Department D ON E.dept_id = D.dept_id;
   ```
   *Result:* Alice (HR), Bob (IT). Charlie and Sales are omitted.

2. **LEFT OUTER JOIN:**
   ```sql
   SELECT E.name, D.dept_name
   FROM Employee E
   LEFT OUTER JOIN Department D ON E.dept_id = D.dept_id;
   ```
   *Result:* Alice (HR), Bob (IT), Charlie (NULL).

3. **RIGHT OUTER JOIN:**
   ```sql
   SELECT E.name, D.dept_name
   FROM Employee E
   RIGHT OUTER JOIN Department D ON E.dept_id = D.dept_id;
   ```
   *Result:* Alice (HR), Bob (IT), NULL (Sales).

4. **FULL OUTER JOIN:**
   ```sql
   SELECT E.name, D.dept_name
   FROM Employee E
   FULL OUTER JOIN Department D ON E.dept_id = D.dept_id;
   ```
   *Result:* Alice (HR), Bob (IT), Charlie (NULL), NULL (Sales).

5. **SELF JOIN (Hierarchical Queries):**
   ```sql
   -- Find the name of each employee alongside their direct manager's name:
   SELECT E.name AS EmployeeName, M.name AS ManagerName
   FROM Employee E
   LEFT JOIN Employee M ON E.manager_id = M.emp_id;
   ```

---

## 2.8 Nested Subqueries: Correlated vs. Uncorrelated

### 2.8.1 Uncorrelated Subquery
- The inner query is completely self-contained and executes **exactly once** before the outer query runs.
- Its result set is passed to the outer query.
```sql
-- Find employees who earn more than the company-wide average salary:
SELECT name, salary 
FROM Employee 
WHERE salary > (SELECT AVG(salary) FROM Employee);
```

### 2.8.2 Correlated Subquery
- The inner query references an attribute from the outer query relation (e.g., `E.dept_id`).
- The inner query must be re-evaluated **once for every single candidate tuple** processed by the outer query.
- Time Complexity: Conceptually $O(N \times M)$ unless transformed into a join by the query optimizer.
```sql
-- Find employees who earn more than the average salary of THEIR OWN department:
SELECT E.emp_id, E.name, E.salary, E.dept_id
FROM Employee E
WHERE E.salary > (
    SELECT AVG(I.salary)
    FROM Employee I
    WHERE I.dept_id = E.dept_id   -- Correlation condition!
);
```

### 2.8.3 The EXISTS and NOT EXISTS Operators
The `EXISTS` operator returns `TRUE` if the subquery returns at least one tuple, and `FALSE` otherwise. The database engine optimizes `EXISTS` by terminating execution of the subquery as soon as the first matching tuple is found (Early Exit).

```sql
-- Find departments that have at least one employee:
SELECT D.dept_name 
FROM Department D
WHERE EXISTS (
    SELECT 1 
    FROM Employee E 
    WHERE E.dept_id = D.dept_id
);

-- Correlated Anti-Join: Find departments with NO employees:
SELECT D.dept_name 
FROM Department D
WHERE NOT EXISTS (
    SELECT 1 
    FROM Employee E 
    WHERE E.dept_id = D.dept_id
);
```

---

## 2.9 Views in SQL

A **View** is a virtual table whose contents are defined by a stored SQL query. It does not exist as a stored set of data values on disk; instead, its tuples are generated dynamically upon retrieval.

```sql
CREATE VIEW HighEarners AS
SELECT emp_id, name, salary, dept_id
FROM Employee
WHERE salary > 100000;
```

### 2.9.1 Updatability Rules for Views
An SQL view is **updatable** (permits `INSERT`, `UPDATE`, and `DELETE` operations that propagate back to the underlying base table) if and only if:
1. The view query references **exactly one base table** in its `FROM` clause.
2. The `SELECT` clause does **not** contain aggregate functions (`SUM`, `AVG`, `COUNT`, etc.).
3. The query does **not** contain `DISTINCT`.
4. The query does **not** contain `GROUP BY` or `HAVING`.
5. The view projection includes the **Primary Key** of the base table.
6. The query does **not** use `UNION`, `INTERSECT`, or `EXCEPT`.

### 2.9.2 The `WITH CHECK OPTION` Clause
Prevents updates or insertions through the view that produce rows that would not satisfy the view's own `WHERE` clause:
```sql
CREATE VIEW SalesStaff AS
SELECT emp_id, name, dept_id
FROM Employee
WHERE dept_id = 10
WITH CHECK OPTION;

-- This statement will fail with an integrity violation because dept_id != 10:
INSERT INTO SalesStaff VALUES (205, 'John Doe', 20);
```

---

## 2.10 Cursors in SQL and PL/SQL

### 2.10.1 Motivation: The Impedance Mismatch
Relational database systems operate on **sets of tuples** (set-at-a-time processing). Conversely, procedural host languages (C, C++, Java, PL/SQL) process data **one record at a time** using loops and iterative variables. A **Cursor** is a database mechanism that bridges this impedance mismatch by acting as a pointer to the result set, allowing procedural code to fetch and process rows iteratively.

### 2.10.2 Implicit vs. Explicit Cursors
1. **Implicit Cursors:**
   - Automatically created and managed by Oracle/PL-SQL for all DML operations (`INSERT`, `UPDATE`, `DELETE`) and single-row `SELECT INTO` queries.
   - Built-in Cursor Attributes:
     - `SQL%FOUND`: Evaluates to `TRUE` if at least one row was affected.
     - `SQL%NOTFOUND`: Evaluates to `TRUE` if no rows were affected.
     - `SQL%ROWCOUNT`: Returns the integer count of rows affected.
     - `SQL%ISOPEN`: Always evaluates to `FALSE` because implicit cursors close automatically immediately after execution.

2. **Explicit Cursors:**
   - Programmatically declared and controlled by the developer for queries returning multiple rows.

### 2.10.3 The Explicit Cursor Lifecycle (4 Stages)

```
  +--------------+          +--------------+          +--------------+          +--------------+
  |  1. DECLARE  |  ----->  |   2. OPEN    |  ----->  |   3. FETCH   |  ----->  |   4. CLOSE   |
  | Define query |          | Execute query|          | Advance ptr  |          | Release RAM  |
  |  structure   |          | Allocate RAM |          | Retrieve row |          |  resources   |
  +--------------+          +--------------+          +-------+------+          +--------------+
                                                              ^       |
                                                              | Loop  |
                                                              +-------+
```

1. **DECLARE:** Defines the cursor name and its associated `SELECT` query in the declaration section.
2. **OPEN:** Executes the query, binds input variables, identifies the active set of tuples, and sets the internal cursor pointer to point before the first row.
3. **FETCH:** Advances the cursor pointer to the next consecutive row and copies column values into target variables.
4. **CLOSE:** Disables the cursor and deallocates memory resources from the Context Area (Private SQL Area).

### 2.10.4 Fully Annotated PL/SQL Implementation Example

```sql
DECLARE
    -- Stage 1: Declare explicit cursor
    CURSOR cur_emp IS
        SELECT emp_id, name, salary 
        FROM Employee 
        WHERE dept_id = 10
        ORDER BY salary DESC;

    -- Local record variable matching cursor schema
    v_emp_id Employee.emp_id%TYPE;
    v_name   Employee.name%TYPE;
    v_salary Employee.salary%TYPE;

BEGIN
    -- Stage 2: Open cursor and materialize active result set
    OPEN cur_emp;

    LOOP
        -- Stage 3: Fetch current row into variables and advance pointer
        FETCH cur_emp INTO v_emp_id, v_name, v_salary;

        -- Exit loop when cursor finishes all rows
        EXIT WHEN cur_emp%NOTFOUND;

        -- Process row procedurally
        DBMS_OUTPUT.PUT_LINE('Processing Emp: ' || v_name || ' | Current Salary: ' || v_salary);

        -- Give 10% bonus if salary < 40000
        IF v_salary < 40000 THEN
            UPDATE Employee 
            SET salary = salary * 1.10 
            WHERE emp_id = v_emp_id;
        END IF;

    END LOOP;

    DBMS_OUTPUT.PUT_LINE('Total Rows Processed: ' || cur_emp%ROWCOUNT);

    -- Stage 4: Close cursor and free Private SQL memory
    CLOSE cur_emp;

EXCEPTION
    WHEN OTHERS THEN
        IF cur_emp%ISOPEN THEN
            CLOSE cur_emp;
        END IF;
        RAISE;
END;
/
```

---

## 2.11 High-Probability Exam Questions & Student Pitfalls

### High-Probability Exam Questions
1. **Explain the fundamental operations of Relational Algebra with syntax, schema, and concrete examples.** (Must define $\sigma, \pi, \cup, -, \times, \rho$, state union compatibility, and show duplicate elimination in $\pi$).
2. **Derive the Division operator ($\div$) in Relational Algebra using fundamental operators. Provide an illustrative query example.** (Must show $R \div S = \pi_X(R) - \pi_X((\pi_X(R) \times S) - R)$ and explain every step).
3. **Compare and contrast `DELETE`, `TRUNCATE`, and `DROP` across at least seven technical dimensions.** (Must cover DML vs DDL, rollback, trigger firing, high-water mark, and speed).
4. **Explain the execution lifecycle of explicit cursors in PL/SQL. Detail cursor attributes `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN`.**
5. **Differentiate between `WHERE` and `HAVING` clauses. Detail the logical order of query processing in SQL.**

### Common Student Traps & Mistakes
- *Trap 1: Evaluating `NULL = NULL` as TRUE.*
  - **Error:** Expecting `SELECT * FROM T WHERE col = NULL;` to return rows with nulls.
  - **Correction:** Comparisons with NULL always yield `UNKNOWN`. Use `IS NULL`.
- *Trap 2: Assuming `AVG(col)` divides by total table rows.*
  - **Error:** Thinking `AVG` counts nulls as zero.
  - **Correction:** `AVG` completely ignores null rows in both numerator and denominator.
- *Trap 3: Using aggregate functions in a `WHERE` clause.*
  - **Error:** `WHERE MAX(salary) > 50000`.
  - **Correction:** Aggregates cannot be calculated until after rows are filtered. Use `HAVING MAX(salary) > 50000`.
- *Trap 4: Forgetting duplicate elimination in Relational Algebra projection.*
  - **Error:** Assuming $\pi$ preserves duplicate rows like SQL `SELECT`.
  - **Correction:** Pure Relational Algebra projections mathematically strip duplicates.
