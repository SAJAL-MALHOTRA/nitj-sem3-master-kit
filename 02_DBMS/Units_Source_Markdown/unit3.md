# UNIT 3: Relational Database Design and Normalization Theory

---

## 3.1 Pitfalls in Relational Database Design & Informal Guidelines

The primary objective of relational database design is to group attributes into relation schemas such that data redundancy is minimized and update anomalies are prevented, while preserving all information and dependencies.

### 3.1.1 Informal Design Guidelines (Elmasri & Navathe)
1. **Guideline 1 (Clear Semantics):** Design a relation schema so that its attributes correspond naturally to a single real-world entity type or relationship type. Do not combine attributes from multiple distinct entities (e.g., mixing employee details with department details).
2. **Guideline 2 (Reducing Redundant Information):** Design schemas so that tuples do not store redundant data across multiple rows, thereby preventing update anomalies.
3. **Guideline 3 (Reducing NULL Values):** Design relation schemas so that their tuples will have as few `NULL` values as possible. Attributes that frequently take on `NULL` should be segregated into separate relations.
4. **Guideline 4 (Disallowing Spurious Tuples):** Relations must be designed such that they can be joined on primary/foreign key attributes without generating **Spurious Tuples** (false, phantom records that did not exist in the original relation).

### 3.1.2 The Four Devastating Anomalies of Poorly Designed Schemas
Consider an unnormalized, poorly designed relation combining employee and department data:
$$\text{EMP\_DEPT}(\underline{\text{EmpID}}, \text{EmpName}, \text{DeptID}, \text{DeptName}, \text{DeptManager})$$

```
+-------+----------+--------+-----------+-------------+
| EmpID | EmpName  | DeptID | DeptName  | DeptManager |
+-------+----------+--------+-----------+-------------+
| 101   | Alice    | D1     | Research  | Dr. Banner  |
| 102   | Bob      | D1     | Research  | Dr. Banner  |
| 103   | Charlie  | D2     | Marketing | Tony Stark  |
| 104   | David    | D1     | Research  | Dr. Banner  |
+-------+----------+--------+-----------+-------------+
```

1. **Redundancy:**
   - The association between `D1`, `'Research'`, and `'Dr. Banner'` is stored redundantly across three distinct tuples. This wastes disk storage and memory cache.
2. **Insertion Anomaly:**
   - If a new department `D3 ('Logistics', 'Steve Rogers')` is established but has not yet hired any employees, we **cannot insert** this department record! Because `EmpID` is the primary key, inserting `(NULL, NULL, 'D3', 'Logistics', 'Steve Rogers')` directly violates the **Entity Integrity Constraint** ($\text{PK} \neq \text{NULL}$).
3. **Deletion Anomaly:**
   - If employee `103 (Charlie)` leaves the organization and we delete his tuple, we inadvertently and permanently **destroy all record of Department D2 ('Marketing') and its manager Tony Stark** from the database!
4. **Update / Modification Anomaly:**
   - If the manager of the Research department changes from `Dr. Banner` to `Dr. Strange`, we must find and update every single employee tuple belonging to `D1`. If the system crashes midway or an application updates only Alice's row, the database enters an **inconsistent state** where Alice's manager is Dr. Strange while Bob's and David's manager is Dr. Banner.

### 3.1.3 Generation of Spurious Tuples (Lossy Decomposition)
If an engineer attempts to fix `EMP_DEPT` by decomposing it into two schemas that are joined on non-candidate keys:
- $R_1(\text{EmpName}, \text{DeptName})$
- $R_2(\text{DeptName}, \text{DeptManager})$

When multiple employees have the same department and multiple departments share names, performing a Natural Join ($R_1 \bowtie R_2$) synthesizes **spurious tuples** that assert false associations that never existed in the ground truth mini-world. Such a decomposition is termed **Lossy (or Additive)** and is strictly unacceptable.

---

## 3.2 Functional Dependencies (FDs)

Functional dependencies are formal mathematical constraints between sets of attributes derived from the real-world semantics of the application domain.

### 3.2.1 Formal Mathematical Definition
Let $R$ be a relation schema, and let $X, Y \subseteq R$ be subsets of attributes of $R$.
A **Functional Dependency**, denoted by:
$$X \to Y$$
(read as *"X functionally determines Y"* or *"Y is functionally dependent on X"*), specifies that for any valid relation state $r(R)$, whenever two tuples $t_1, t_2 \in r(R)$ agree on their values for attribute set $X$, they **must** also agree on their values for attribute set $Y$.

Formally:
$$\forall t_1, t_2 \in r(R) : \left( t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y] \right)$$

- $X$ is termed the **Determinant** (Left-Hand Side - LHS).
- $Y$ is termed the **Dependent** (Right-Hand Side - RHS).

### 3.2.2 Taxonomy of Functional Dependencies
1. **Trivial Functional Dependency:**
   An FD $X \to Y$ is **trivial** if and only if $Y \subseteq X$.
   *Examples:* $\{A, B\} \to A$, $\{A, B\} \to \{A, B\}$.
   Trivial dependencies are satisfied by *every* relation instance by definition of set identity.
2. **Non-Trivial Functional Dependency:**
   An FD $X \to Y$ is **non-trivial** if $Y \not\subseteq X$.
   *Example:* $\{A, B\} \to C$.
3. **Completely Non-Trivial Functional Dependency:**
   An FD $X \to Y$ is **completely non-trivial** if $X \cap Y = \emptyset$.
   *Example:* $\{A, B\} \to \{C, D\}$.
4. **Semi-Trivial Functional Dependency:**
   An FD $X \to Y$ where $Y \not\subseteq X$, but $X \cap Y \neq \emptyset$.
   *Example:* $\{A, B\} \to \{B, C\}$.

---

## 3.3 Armstrong's Axioms & Inference Rules

Let $F$ be a set of functional dependencies specified on schema $R$. The **Closure of $F$**, denoted $F^+$, is the set of all functional dependencies logically implied by $F$.
William W. Armstrong (1974) proved that three fundamental inference rules are **Sound** (they generate only valid FDs implied by $F$) and **Complete** (repeated application of these rules can derive every valid FD in $F^+$).

```
+---------------------------------------------------------------------------------------+
|                                ARMSTRONG'S PRIMARY AXIOMS                             |
+---------------------+---------------------------------+-------------------------------+
| AXIOM NAME          | FORMAL SYMBOLIC RULE            | MATHEMATICAL INTERPRETATION   |
+---------------------+---------------------------------+-------------------------------+
| IR1: Reflexivity    | If Y is a subset of X,          | Any set of attributes         |
|                     | then X -> Y                     | determines any of its subsets.|
+---------------------+---------------------------------+-------------------------------+
| IR2: Augmentation   | If X -> Y,                      | Adding identical attributes   |
|                     | then XZ -> YZ                   | to both sides preserves the   |
|                     |                                 | dependency.                   |
+---------------------+---------------------------------+-------------------------------+
| IR3: Transitivity   | If X -> Y and Y -> Z,           | Functional determination is   |
|                     | then X -> Z                     | transitive across sets.       |
+---------------------+---------------------------------+-------------------------------+
```

### 3.3.1 Step-by-Step Formal Proofs of Armstrong's Axioms

#### Proof 1: Reflexivity Rule (IR1)
- **Statement:** If $Y \subseteq X$, then $X \to Y$.
- **Proof:**
  1. Let $t_1, t_2 \in r(R)$ such that $t_1[X] = t_2[X]$.
  2. Because $Y \subseteq X$, the values of $t_1$ and $t_2$ on attribute set $Y$ are drawn directly from the components of $t_1[X]$ and $t_2[X]$.
  3. Since $t_1[X] = t_2[X]$, their sub-components on $Y$ must be identical: $t_1[Y] = t_2[Y]$.
  4. By definition of FD, $X \to Y$ holds. $\blacksquare$

#### Proof 2: Augmentation Rule (IR2)
- **Statement:** If $X \to Y$, then $XZ \to YZ$ (where $XZ$ denotes $X \cup Z$).
- **Proof:**
  1. Assume $X \to Y$ holds in $r(R)$.
  2. Let $t_1, t_2 \in r(R)$ such that $t_1[XZ] = t_2[XZ]$.
  3. This implies two conditions:
     - (a) $t_1[X] = t_2[X]$
     - (b) $t_1[Z] = t_2[Z]$
  4. Since $t_1[X] = t_2[X]$ and we know $X \to Y$, it must be that $t_1[Y] = t_2[Y]$.
  5. Combining $t_1[Y] = t_2[Y]$ and $t_1[Z] = t_2[Z]$ gives $t_1[YZ] = t_2[YZ]$.
  6. Therefore, $t_1[XZ] = t_2[XZ] \implies t_1[YZ] = t_2[YZ]$, proving $XZ \to YZ$. $\blacksquare$

#### Proof 3: Transitivity Rule (IR3)
- **Statement:** If $X \to Y$ and $Y \to Z$, then $X \to Z$.
- **Proof:**
  1. Assume $X \to Y$ and $Y \to Z$ both hold in $r(R)$.
  2. Let $t_1, t_2 \in r(R)$ such that $t_1[X] = t_2[X]$.
  3. Because $X \to Y$, $t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$.
  4. Because $Y \to Z$, $t_1[Y] = t_2[Y] \implies t_1[Z] = t_2[Z]$.
  5. By hypothetical syllogism in propositional logic, $t_1[X] = t_2[X] \implies t_1[Z] = t_2[Z]$.
  6. Hence, $X \to Z$ holds. $\blacksquare$

---

### 3.3.2 Secondary Inference Rules (Derived Rules)

#### Rule 4: Decomposition (Projectivity) Rule
- **Statement:** If $X \to YZ$, then $X \to Y$ and $X \to Z$.
- **Proof:**
  1. $YZ \to Y$ (by Reflexivity, since $Y \subseteq YZ$).
  2. $X \to YZ$ (given).
  3. Applying Transitivity to (2) and (1) yields $X \to Y$.
  4. Similarly, $YZ \to Z$ (Reflexivity, $Z \subseteq YZ$).
  5. Applying Transitivity yields $X \to Z$. $\blacksquare$

#### Rule 5: Union (Additive) Rule
- **Statement:** If $X \to Y$ and $X \to Z$, then $X \to YZ$.
- **Proof:**
  1. $X \to Y$ (given).
  2. Augmenting with $X$ gives $XX \to XY$, which simplifies to $X \to XY$.
  3. $X \to Z$ (given).
  4. Augmenting with $Y$ gives $XY \to YZ$.
  5. Applying Transitivity to $X \to XY$ and $XY \to YZ$ yields $X \to YZ$. $\blacksquare$

#### Rule 6: Pseudotransitivity Rule
- **Statement:** If $X \to Y$ and $WY \to Z$, then $WX \to Z$.
- **Proof:**
  1. $X \to Y$ (given).
  2. Augmenting with $W$ gives $WX \to WY$.
  3. $WY \to Z$ (given).
  4. Applying Transitivity to $WX \to WY$ and $WY \to Z$ yields $WX \to Z$. $\blacksquare$

---

## 3.4 The Attribute Closure Algorithm ($X^+$)

Computing the full FD closure $F^+$ is exponential in the number of attributes ($O(2^n)$). Fortunately, testing whether a specific dependency $X \to Y$ is implied by $F$, or finding candidate keys, requires only computing the **Attribute Closure of $X$ under $F$**, denoted **$X^+$**.

### 3.4.1 Formal Definition of Attribute Closure
The Attribute Closure $X^+$ is the set of all attributes functionally determined by $X$ under a set of functional dependencies $F$:
$$X^+ = \{ A \in R \mid F \models X \to A \}$$

### 3.4.2 Formal Algorithm Pseudocode

```
Algorithm: Compute_Attribute_Closure(X, F)
Input:  A set of attributes X, a set of functional dependencies F over schema R
Output: The attribute closure X+ under F

1.  X+ := X;                           // Initialize closure with X itself (Reflexivity)
2.  changed := TRUE;
3.  WHILE (changed = TRUE) DO
4.      changed := FALSE;
5.      FOR EACH functional dependency (Y -> Z) IN F DO
6.          IF (Y is a subset of X+) AND (Z is not a subset of X+) THEN
7.              X+ := X+ UNION Z;      // Add determined attributes to closure
8.              changed := TRUE;
9.          END IF;
10.     END FOR;
11. END WHILE;
12. RETURN X+;
```

### 3.4.3 Applications of the Attribute Closure Algorithm
1. **Testing if an FD is Valid:** To test if $X \to Y$ holds under $F$, compute $X^+$. If $Y \subseteq X^+$, then $X \to Y$ is valid; otherwise it is false.
2. **Determining if $X$ is a Superkey:** If $X^+ = R$ (the closure contains all attributes of the schema), then $X$ is a **Superkey**.
3. **Determining if $X$ is a Candidate Key:** If $X^+ = R$ AND for every proper subset $Y \subset X$, $Y^+ \neq R$, then $X$ is a **Candidate Key**.

---

## 3.5 Systematic Algorithm for Finding All Candidate Keys

Students frequently struggle with finding *all* candidate keys. Use this systematic pruning methodology:

```
+---------------------------------------------------------------------------------------+
|                    ATTRIBUTE PARTITIONING FOR CANDIDATE KEYS                          |
+---------------------+---------------------+---------------------+---------------------+
| CATEGORY L          | CATEGORY R          | CATEGORY M          | CATEGORY N          |
| (LHS Only)          | (RHS Only)          | (Middle: Both sides)| (Neither LHS/RHS)   |
+---------------------+---------------------+---------------------+---------------------+
| Attributes that     | Attributes that     | Attributes that     | Attributes that do  |
| appear ONLY on the  | appear ONLY on the  | appear on BOTH the  | NOT appear anywhere |
| Left-Hand Side.     | Right-Hand Side.    | LHS and RHS.        | in any FD in F.     |
+---------------------+---------------------+---------------------+---------------------+
| MUST BE INCLUDED in | CAN NEVER BE PART   | MAY OR MAY NOT be   | MUST BE INCLUDED in |
| EVERY candidate key!| of any candidate key| in a candidate key. | EVERY candidate key!|
+---------------------+---------------------+---------------------+---------------------+
```

### Systematic Procedure:
1. Identify set $L$ (attributes on LHS only) and set $N$ (attributes not in $F$).
2. Let the core set be $C = L \cup N$.
3. Compute closure $C^+$:
   - If $C^+ = R$, then $C$ is the **unique Candidate Key** of the schema! No other combinations need to be tested.
   - If $C^+ \neq R$, systematically augment $C$ with single attributes from $M$, compute their closures, then pairs from $M$, etc., discarding any superset of an already discovered candidate key.

---

## 3.6 Equivalence of FD Sets & Minimal (Canonical) Cover

Two sets of functional dependencies $F$ and $G$ over schema $R$ are **Equivalent** ($F \equiv G$) if and only if:
$$F^+ = G^+$$
To verify $F \equiv G$, test whether $F$ covers $G$ ($F \models G$, meaning $\forall X \to Y \in G, Y \subseteq X^+_F$) and $G$ covers $F$ ($G \models F$).

### 3.6.1 Minimal Cover (Canonical Cover) Definition
A **Minimal Cover** (or Canonical Cover $F_c$) of a set of dependencies $F$ is an equivalent, minimal set of dependencies that contains no redundancies. A set $F_c$ is minimal if and only if it satisfies **Three Conditions**:
1. **Standard Canonical Form (RHS Singleton):** Every FD in $F_c$ has a single attribute on its right-hand side ($X \to A$).
2. **Left-Reduced (No Extraneous LHS Attributes):** For every FD $X \to A$ in $F_c$, no attribute $B \in X$ can be removed such that $(F_c - \{X \to A\} \cup \{(X - \{B\}) \to A\})$ remains equivalent to $F_c$.
3. **No Redundant FDs:** No functional dependency $X \to A \in $F_c$ can be deleted without altering the closure of $F_c$.

### 3.6.2 Step-by-Step Algorithm to Compute Minimal Cover

```
Algorithm: Compute_Minimal_Cover(F)
Input:  A set of functional dependencies F
Output: An equivalent minimal cover Fc

Step 1: Decompose RHS into Single Attributes (Decomposition Rule)
        For each X -> {A1, A2, ..., Ak} in F:
            Replace with X -> A1, X -> A2, ..., X -> Ak.

Step 2: Remove Extraneous Attributes from LHS (Left-Reduction)
        For each FD X -> A where X contains >= 2 attributes:
            For each attribute B in X:
                Let X' = X - {B}.
                Compute (X')+ under current F.
                If A is in (X')+, then B is EXTRANEOUS on LHS!
                Replace X -> A with X' -> A in F.

Step 3: Remove Redundant Functional Dependencies
        For each FD (X -> A) in F:
            Let G = F - {X -> A}.
            Compute X+ under G.
            If A is in X+G, then (X -> A) is REDUNDANT!
            F := G;  // Permanently discard redundant dependency.

Step 4: (Optional Consolidation)
        Combine FDs with identical LHS: X -> A and X -> B become X -> AB.
```

---

## 3.7 The Normal Forms Based on Primary & Candidate Keys

Normalization is the systematic process of decomposing relations with anomalies into smaller, well-structured relations that satisfy formal normal form constraints.

```
       +-------------------------------------------------------------+
       |               FIRST NORMAL FORM (1NF)                       |
       |  - Atomic attribute domains                                 |
       |  - No multi-valued attributes or nested relations           |
       |                                                             |
       |        +-------------------------------------------+        |
       |        |       SECOND NORMAL FORM (2NF)            |        |
       |        |  - In 1NF                                 |        |
       |        |  - No Partial Dependencies                |        |
       |        |                                           |        |
       |        |      +-----------------------------+      |        |
       |        |      |   THIRD NORMAL FORM (3NF)   |      |        |
       |        |      |  - In 2NF                   |      |        |
       |        |      |  - No Transitive Deps       |      |        |
       |        |      |                             |      |        |
       |        |      |      +---------------+      |      |        |
       |        |      |      |     BCNF      |      |      |        |
       |        |      |      |  Every LHS is |      |      |        |
       |        |      |      |  a Superkey   |      |      |        |
       |        |      |      +---------------+      |      |        |
       |        |      +-----------------------------+      |        |
       |        +-------------------------------------------+        |
       +-------------------------------------------------------------+
```

### 3.7.1 Definitions of Prime vs. Non-Prime Attributes
- **Prime Attribute:** An attribute that is a member of **at least one Candidate Key** of relation schema $R$.
- **Non-Prime Attribute:** An attribute that does **not** participate in any candidate key of $R$.

---

### 3.7.2 First Normal Form (1NF)
- **Formal Definition:** A relation schema $R$ is in **1NF** if and only if the domain of every attribute in $R$ contains only **atomic (indivisible) values**, and the value of any attribute in a tuple is a single value from that domain.
- **Disallows:**
  1. Multi-valued attributes (arrays, sets, lists).
  2. Composite attributes (unflattened records).
  3. Nested relations (tables embedded inside table cells).
- **Techniques to Normalize into 1NF:**
  - *Method 1 (Flattening):* Replicate primary key attributes for each value in the multi-valued set (creates tuple redundancy).
  - *Method 2 (Decomposition - Standard):* Create a separate relation for the multi-valued attribute combining it with the primary key.

---

### 3.7.3 Second Normal Form (2NF)

#### Concept of Full vs. Partial Functional Dependency
- **Full Functional Dependency:** An FD $X \to Y$ is a full functional dependency if removing any attribute $A$ from $X$ causes the dependency to no longer hold:
  $$\forall A \in X, (X - \{A\}) \not\to Y$$
- **Partial Dependency:** An FD $X \to Y$ is a partial dependency if there exists some proper subset $X' \subset X$ such that $X' \to Y$. (A part of the key determines the dependent).

#### Formal Definition of 2NF
- **Primary-Key Definition:** A relation schema $R$ is in 2NF if it is in 1NF and **no non-prime attribute is partially dependent on the primary key**.
- **General Definition (Considering All Candidate Keys):** A relation schema $R$ is in **2NF** if it is in 1NF and **no non-prime attribute is partially dependent on ANY candidate key of $R$**.
  $$\forall X \to A \in F, \text{ if } A \text{ is non-prime, then } \forall \text{ Candidate Key } K, \text{ no proper subset } K' \subset K \text{ determines } A$$

*Note:* If all candidate keys of a relation are **single attributes (simple keys)**, the relation is **automatically in 2NF**! Partial dependencies can only occur when a candidate key is composite (consists of two or more attributes).

---

### 3.7.4 Third Normal Form (3NF)

#### Concept of Transitive Dependency
A functional dependency $X \to Z$ in schema $R$ is a **Transitive Dependency** if there exists a set of attributes $Y$ (which is neither a candidate key nor a subset of any key) such that $X \to Y$ and $Y \to Z$ both hold.

#### Formal Definition of 3NF
A relation schema $R$ is in **Third Normal Form (3NF)** if it is in 2NF and for every non-trivial functional dependency:
$$X \to A$$
at least one of the following two conditions holds:
1. $X$ is a **Superkey** of $R$, OR
2. $A$ is a **Prime Attribute** of $R$ (i.e., $A$ is a member of some candidate key).

#### Why Condition 2 Exists (The Crucial Role of Prime Attributes):
Condition 2 allows dependencies of the form $(\text{Non-Key} \to \text{Prime Attribute})$. This relaxation was intentionally designed by Codd to guarantee that **any relational schema can be decomposed into 3NF while simultaneously guaranteeing both Lossless Join and Functional Dependency Preservation**.

---

### 3.7.5 Boyce-Codd Normal Form (BCNF)

#### Motivation
In 1974, Raymond F. Boyce and Edgar F. Codd observed that schemas in 3NF could still suffer from update anomalies if they possessed **overlapping composite candidate keys**.

#### Formal Definition of BCNF
A relation schema $R$ is in **Boyce-Codd Normal Form (BCNF)** if and only if for every non-trivial functional dependency:
$$X \to A$$
**$X$ is a Superkey of $R$**.

*Strict Structural Difference:* BCNF completely removes Condition 2 of 3NF. In BCNF, $A$ being prime provides no exemption: the determinant $X$ must strictly be a superkey.

---

### 3.7.6 Exhaustive Comparison Matrix: 3NF vs. BCNF

| Feature / Dimension | Third Normal Form (3NF) | Boyce-Codd Normal Form (BCNF) |
| :--- | :--- | :--- |
| **Formal Condition for $X \to A$** | $X$ is a Superkey **OR** $A$ is a Prime Attribute. | $X$ **MUST** be a Superkey (no exceptions). |
| **Strictness** | Less strict (permits $X \to A$ if $A$ is prime). | Stricter than 3NF ($\text{BCNF} \subset \text{3NF}$). |
| **Handling of Overlapping Keys** | May exhibit anomalies if keys overlap. | Eliminates all anomalies arising from FDs. |
| **Lossless Join Guarantee** | Always achievable ($100\%$). | Always achievable ($100\%$). |
| **Dependency Preservation** | **Always achievable ($100\%$)**. | **Not always achievable** (may lose dependencies). |
| **Polynomial Synthesis Algorithm** | Available (Bernstein's 3NF Synthesis). | Decomposition may eliminate valid FDs. |

---

## 3.8 Properties of Relational Decompositions

When a schema $R$ is decomposed into a set of schemas $D = \{R_1, R_2, \dots, R_k\}$ such that $R = R_1 \cup R_2 \cup \dots \cup R_k$, the decomposition must satisfy two foundational properties.

### 3.8.1 Lossless-Join (Non-Additive) Decomposition
- **Formal Definition:** A decomposition $D = \{R_1, R_2, \dots, R_k\}$ of $R$ is a **Lossless-Join Decomposition** with respect to a set of dependencies $F$ if for every valid relation instance $r(R)$:
  $$\pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie \dots \bowtie \pi_{R_k}(r) = r$$
  If the natural join produces spurious tuples ($\pi(r) \bowtie \pi(r) \supset r$), the decomposition is **Lossy**.

#### Binary Decomposition Theorem (Necessary and Sufficient Condition):
A decomposition of schema $R$ into two schemas $R_1$ and $R_2$ ($R = R_1 \cup R_2$) is **lossless** with respect to $F$ if and only if the common attributes $(R_1 \cap R_2)$ functionally determine at least one of the decomposed schemas:
$$(R_1 \cap R_2 \to R_1) \in F^+ \quad \text{OR} \quad (R_1 \cap R_2 \to R_2) \in F^+$$

#### Step-by-Step Formal Proof of the Binary Decomposition Theorem:
Let $R_1 \cap R_2 = C$, $R_1 = C \cup A$, and $R_2 = C \cup B$, where $A, B, C$ are disjoint.
Assume $C \to A$ holds in $F^+$ (i.e., $R_1 \cap R_2 \to R_1$).
1. By definition of projection, $r \subseteq \pi_{R_1}(r) \bowtie \pi_{R_2}(r)$ always holds.
2. We must prove that no spurious tuples exist: $\pi_{R_1}(r) \bowtie \pi_{R_2}(r) \subseteq r$.
3. Let $t = \langle a, b, c \rangle \in \pi_{R_1}(r) \bowtie \pi_{R_2}(r)$.
4. By definition of natural join, there must exist:
   - Tuple $t_1 \in r$ such that $t_1[C] = c$ and $t_1[A] = a$.
   - Tuple $t_2 \in r$ such that $t_2[C] = c$ and $t_2[B] = b$.
5. Notice that $t_1[C] = t_2[C] = c$.
6. Because $C \to A$ holds in $r$, whenever two tuples agree on $C$, they must agree on $A$.
7. Therefore, $t_1[C] = t_2[C] \implies t_1[A] = t_2[A]$.
8. Since $t_1[A] = a$, it follows that $t_2[A] = a$.
9. Examining tuple $t_2$: $t_2[A] = a$, $t_2[B] = b$, and $t_2[C] = c$.
10. Thus, $t_2 = \langle a, b, c \rangle = t$. Since $t_2 \in r$, tuple $t \in r$.
11. Hence, $\pi_{R_1}(r) \bowtie \pi_{R_2}(r) = r$. The decomposition is Lossless. $\blacksquare$

---

### 3.8.2 Testing Lossless Join for Arbitrary $N$-ary Decompositions: The Chase (Tableau) Algorithm

When decomposing into three or more relations ($k \ge 3$), the binary theorem is insufficient. The **Chase Algorithm** constructs a decision matrix:

1. Create a matrix of $k$ rows (one for each relation $R_i$) and $n$ columns (one for each attribute $A_j \in R$).
2. Fill cell $(i, j)$:
   - If attribute $A_j \in R_i$, set cell $(i, j) := a_j$ (distinguished symbol).
   - If attribute $A_j \notin R_i$, set cell $(i, j) := b_{ij}$ (non-distinguished symbol).
3. Repeatedly apply FDs in $F$: For each FD $X \to Y \in F$:
   - Find all rows that have identical symbols in the columns corresponding to $X$.
   - Make their symbols in the columns corresponding to $Y$ identical:
     - If one of the rows contains a distinguished symbol $a_j$, change all other matching rows in that column to $a_j$.
     - If none contain $a_j$, pick one of the $b$-symbols and equate them.
4. **Termination Criterion:**
   - If at any point **a complete row consists entirely of distinguished symbols $\langle a_1, a_2, \dots, a_n \rangle$**, the decomposition is **LOSSLESS**.
   - If no more symbols can be updated and no row contains all $a$'s, the decomposition is **LOSSY**.

---

### 3.8.3 Dependency Preservation Property
- **Formal Definition:** A decomposition $D = \{R_1, R_2, \dots, R_k\}$ preserves dependencies with respect to $F$ if:
  $$\left( \bigcup_{i=1}^k \pi_{R_i}(F) \right)^+ = F^+$$
  where $\pi_{R_i}(F)$ denotes the projection of $F$ onto $R_i$:
  $$\pi_{R_i}(F) = \{ X \to Y \in F^+ \mid X \cup Y \subseteq R_i \}$$
- **Physical Significance:** If dependencies are preserved, the DBMS can enforce all business rules by checking individual table updates locally. If a dependency is lost during decomposition, enforcing that constraint requires computing an expensive inter-table join across disks on every `INSERT` or `UPDATE`.

---

## 3.9 Higher Normal Forms: 4NF and 5NF

```
       +-----------------------------------------------------------------------+
       | MULTIVALUED DEPENDENCY (MVD) & 4NF                                    |
       | - Eliminates independent 1:N facts stored in a single table           |
       | - Condition: For every non-trivial X ->> Y, X must be a Superkey      |
       +-----------------------------------------------------------------------+
                                           |
                                           v
       +-----------------------------------------------------------------------+
       | JOIN DEPENDENCY (JD) & 5NF (Project-Join Normal Form - PJNF)          |
       | - Eliminates n-way cyclic join anomalies                              |
       | - Condition: Every non-trivial Join Dependency *(R1..Rn) is implied   |
       |   by candidate keys                                                   |
       +-----------------------------------------------------------------------+
```

### 3.9.1 Multivalued Dependencies (MVD) and Fourth Normal Form (4NF)
- **Motivation:** BCNF removes all anomalies arising from Functional Dependencies, but tables can still exhibit massive redundancy if an entity has multiple independent multi-valued attributes.
- **Formal Definition of MVD ($X \twoheadrightarrow Y$):**
  Given relation $R$ and subsets $X, Y \subseteq R$, let $Z = R - (X \cup Y)$. The **Multivalued Dependency** $X \twoheadrightarrow Y$ holds on $R$ if and only if for every pair of tuples $t_1, t_2 \in r(R)$ such that $t_1[X] = t_2[X]$, there exist tuples $t_3, t_4 \in r(R)$ such that:
  $$\begin{aligned}
  t_3[X] &= t_4[X] = t_1[X] = t_2[X] \\
  t_3[Y] &= t_1[Y] \quad \text{and} \quad t_3[Z] = t_2[Z] \\
  t_4[Y] &= t_2[Y] \quad \text{and} \quad t_4[Z] = t_1[Z]
  \end{aligned}$$
  *Plain English:* For a given value of $X$, the set of values of $Y$ is determined solely by $X$ and is completely independent of the attributes in $Z$.

- **Formal Definition of 4NF:**
  A relation schema $R$ is in **Fourth Normal Form (4NF)** with respect to a set of dependencies $D$ (including FDs and MVDs) if, for every non-trivial multivalued dependency $X \twoheadrightarrow Y$ in $D^+$:
  **$X$ is a Superkey of $R$**.

*Classical 4NF Violation Example:*
`PROF_DETAILS(ProfID, PhoneNo, SubjectTaught)`
If Professor 101 has 2 phone numbers and teaches 2 subjects, all 4 permutations ($2 \times 2$) must be stored:
`{(101, P1, S1), (101, P1, S2), (101, P2, S1), (101, P2, S2)}`.
Here, $\text{ProfID} \twoheadrightarrow \text{PhoneNo}$ and $\text{ProfID} \twoheadrightarrow \text{SubjectTaught}$ hold, but `ProfID` is not a superkey. Normalizing to 4NF decomposes this into:
- $R_1(\underline{\text{ProfID}}, \underline{\text{PhoneNo}})$
- $R_2(\underline{\text{ProfID}}, \underline{\text{SubjectTaught}})$

### 3.9.2 Join Dependencies (JD) and Fifth Normal Form (5NF / PJNF)
- **Join Dependency Definition:** A relation schema $R$ satisfies a Join Dependency $\Join(R_1, R_2, \dots, R_n)$ if and only if for every legal instance $r(R)$:
  $$\pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie \dots \bowtie \pi_{R_n}(r) = r$$
- **Fifth Normal Form (5NF / Project-Join Normal Form):**
  A relation schema $R$ is in **5NF** if and only if every non-trivial join dependency $\Join(R_1, R_2, \dots, R_n)$ that holds on $R$ is implied by the candidate keys of $R$.
- 5NF deals with cases where a relation can be decomposed losslessly into **three or more** relations, but cannot be decomposed losslessly into any two relations!

---

## 3.10 Inclusion Dependencies and Database Design Approaches

### 3.10.1 Inclusion Dependencies
- **Formal Definition:** An **Inclusion Dependency** between relation schemas $R_1$ and $R_2$ is denoted by:
  $$R_1[X] \subseteq R_2[Y]$$
  where $X$ and $Y$ are attribute lists of equal degree, meaning that the projection $\pi_X(r(R_1))$ is a subset of $\pi_Y(r(R_2))$.
- **Relationship to Referential Integrity:** Inclusion dependencies formalize Foreign Key constraints. When $Y$ is a Candidate Key of $R_2$, $R_1[X] \subseteq R_2[Y]$ represents a standard Referential Integrity constraint.

### 3.10.2 Top-Down vs. Bottom-Up Database Design
1. **Top-Down Design (Decomposition Approach):**
   - Starts with high-level conceptual modeling (ER Diagram).
   - Maps ER models into relational schemas.
   - Evaluates schemas for anomalies and applies successive normalizations (decompositions into 2NF, 3NF, BCNF).
2. **Bottom-Up Design (Attribute Synthesis Approach):**
   - Synthesizes relation schemas directly from a global set of elementary attributes and functional dependencies using Bernstein's 3NF Synthesis Algorithm.

---

## 3.11 Comprehensive Worked Numerical Problems

### Numerical 1: Complete Candidate Key Determination
**Problem Statement:** Let schema $R(A, B, C, D, E, F)$ have functional dependencies:
$$F = \{ AB \to C, \quad C \to D, \quad D \to E, \quad E \to B, \quad F \to A \}$$
Find **ALL Candidate Keys** of relation schema $R$.

**Step-by-Step Solution:**
1. **Attribute Categorization:**
   - Left-Hand Side (LHS) only attributes: $F$ appears only on LHS.
   - Right-Hand Side (RHS) only attributes: None.
   - Both LHS and RHS attributes: $A, B, C, D, E$.
   - Attributes appearing nowhere in $F$: None.
2. **Mandatory Core Set:**
   Attribute $F$ never appears on the RHS of any dependency. Hence, no other attribute can determine $F$.
   Therefore, **$F$ MUST participate in EVERY candidate key!**
3. **Testing Combinations with $F$:**
   - Test $\{F\}^+$:
     $$\{F\}^+ = \{F, A\} \neq R$$
   - Augment with 2-attribute combinations containing $F$:
     - Test $\{A, F\}^+$:
       $$\{A, F\}^+ = \{A, F\} \neq R$$
     - Test $\{B, F\}^+$:
       $$\begin{aligned}
       \{B, F\}^+ &\xrightarrow{F \to A} \{A, B, F\} \\
       &\xrightarrow{AB \to C} \{A, B, C, F\} \\
       &\xrightarrow{C \to D} \{A, B, C, D, F\} \\
       &\xrightarrow{D \to E} \{A, B, C, D, E, F\} = R
       \end{aligned}$$
       $\implies \mathbf{\{B, F\}}$ is a **Candidate Key**!
     - Test $\{C, F\}^+$:
       $$\begin{aligned}
       \{C, F\}^+ &\xrightarrow{F \to A} \{A, C, F\} \\
       &\xrightarrow{C \to D} \{A, C, D, F\} \\
       &\xrightarrow{D \to E} \{A, C, D, E, F\} \\
       &\xrightarrow{E \to B} \{A, B, C, D, E, F\} = R
       \end{aligned}$$
       $\implies \mathbf{\{C, F\}}$ is a **Candidate Key**!
     - Test $\{D, F\}^+$:
       $$\begin{aligned}
       \{D, F\}^+ &\xrightarrow{F \to A} \{A, D, F\} \\
       &\xrightarrow{D \to E} \{A, D, E, F\} \\
       &\xrightarrow{E \to B} \{A, B, D, E, F\} \\
       &\xrightarrow{AB \to C} \{A, B, C, D, E, F\} = R
       \end{aligned}$$
       $\implies \mathbf{\{D, F\}}$ is a **Candidate Key**!
     - Test $\{E, F\}^+$:
       $$\begin{aligned}
       \{E, F\}^+ &\xrightarrow{F \to A} \{A, E, F\} \\
       &\xrightarrow{E \to B} \{A, B, E, F\} \\
       &\xrightarrow{AB \to C} \{A, B, C, E, F\} \\
       &\xrightarrow{C \to D} \{A, B, C, D, E, F\} = R
       \end{aligned}$$
       $\implies \mathbf{\{E, F\}}$ is a **Candidate Key**!
4. **Final Result:**
   The relation schema $R$ has **four distinct candidate keys**:
   $$\mathbf{CK = \{ \{B, F\}, \{C, F\}, \{D, F\}, \{E, F\} \}}$$
   - Prime Attributes: $\{B, C, D, E, F\}$.
   - Non-Prime Attribute: $\{A\}$.

---

### Numerical 2: Minimal (Canonical) Cover Calculation
**Problem Statement:** Compute the Minimal Cover for schema $R(A, B, C, D)$ with FDs:
$$F = \{ A \to BC, \quad B \to C, \quad A \to B, \quad AB \to C \}$$

**Step-by-Step Solution:**
- **Step 1: Decompose RHS into singletons:**
  1. $A \to B$
  2. $A \to C$
  3. $B \to C$
  4. $A \to B$  (duplicate, discard)
  5. $AB \to C$
  Current set $F_1 = \{ A \to B, A \to C, B \to C, AB \to C \}$.

- **Step 2: Remove Extraneous Attributes from LHS:**
  Examine composite determinant $AB \to C$:
  - Check if $A$ is extraneous: Compute $B^+$ under $F_1$:
    $$B^+ = \{B, C\}$$
    Since $C \in B^+$, $B$ alone can determine $C$! Thus, $A$ is **extraneous** in $AB \to C$.
  - Replacing $AB \to C$ with $B \to C$ leaves:
    Current set $F_2 = \{ A \to B, A \to C, B \to C \}$.

- **Step 3: Remove Redundant Functional Dependencies:**
  - Test $A \to B$:
    Remove $A \to B$. Under remaining $\{A \to C, B \to C\}$, $A^+ = \{A, C\}$. Since $B \notin A^+$, $A \to B$ is **NOT redundant**.
  - Test $A \to C$:
    Remove $A \to C$. Under remaining $\{A \to B, B \to C\}$:
    $$A^+ = \{A, B, C\}$$
    Since $C \in A^+$, $A \to C$ is logically implied by transitivity ($A \to B$ and $B \to C$).
    Therefore, **$A \to C$ is REDUNDANT and is deleted!**
  - Test $B \to C$:
    Remove $B \to C$. Under remaining $\{A \to B\}$, $B^+ = \{B\}$. Since $C \notin B^+$, $B \to C$ is **NOT redundant**.

- **Final Minimal Cover:**
  $$\mathbf{F_c = \{ A \to B, \quad B \to C \}}$$

---

### Numerical 3: Decomposing into 3NF (Lossless + Dependency Preserving)
**Problem Statement:** Decompose schema $R(A, B, C, D, E)$ with dependencies:
$$F = \{ A \to BC, \quad CD \to E, \quad B \to D, \quad E \to A \}$$
into 3NF relations guaranteeing both Lossless Join and Dependency Preservation.

**Step-by-Step Solution:**
1. **Find Candidate Keys of $R$:**
   Computing closures:
   - $\{A\}^+ = \{A, B, C, D, E\} = R \implies \{A\}$ is a CK.
   - $\{E\}^+ = \{E, A, B, C, D\} = R \implies \{E\}$ is a CK.
   - $\{C, D\}^+ = \{C, D, E, A, B\} = R \implies \{C, D\}$ is a CK.
   - $\{B, C\}^+ = \{B, C, D, E, A\} = R \implies \{B, C\}$ is a CK.
2. **Compute Minimal Cover $F_c$:**
   - RHS singletons: $\{A \to B, A \to C, CD \to E, B \to D, E \to A\}$.
   - No extraneous LHS attributes exist.
   - No redundant dependencies exist.
   $F_c = \{ A \to B, A \to C, CD \to E, B \to D, E \to A \}$.
3. **Bernstein's 3NF Synthesis Algorithm:**
   - Group FDs with identical LHS:
     - Group 1 ($A$): $A \to BC \implies R_1(\underline{A}, B, C)$
     - Group 2 ($CD$): $CD \to E \implies R_2(\underline{C, D}, E)$
     - Group 3 ($B$): $B \to D \implies R_3(\underline{B}, D)$
     - Group 4 ($E$): $E \to A \implies R_4(\underline{E}, A)$
4. **Lossless Join Check (Candidate Key Check):**
   Does any decomposed relation $R_i$ contain a candidate key of original schema $R$?
   - $R_1(A, B, C)$ contains candidate key $\{A\}$!
   - $R_2(C, D, E)$ contains candidate key $\{C, D\}$!
   - $R_4(E, A)$ contains candidate key $\{E\}$!
   Because at least one relation contains a candidate key of $R$, the decomposition is **guaranteed to be Lossless**.
5. **Final 3NF Decomposition:**
   $$\mathbf{\{ R_1(\underline{A}, B, C), \quad R_2(\underline{C, D}, E), \quad R_3(\underline{B}, D), \quad R_4(\underline{E}, A) \}}$$
   *Properties:* Both Lossless Join and Dependency Preservation are 100% satisfied.

---

### Numerical 4: Decomposing into BCNF & Checking Dependency Preservation
**Problem Statement:** Let schema $R(A, B, C)$ with $F = \{ AB \to C, \quad C \to B \}$.
Determine its normal form and decompose into BCNF.

**Step-by-Step Solution:**
1. **Candidate Keys:**
   - $\{AB\}^+ = \{A, B, C\} \implies \{AB\}$ is a CK.
   - $\{AC\}^+ \xrightarrow{C \to B} \{A, B, C\} \implies \{AC\}$ is a CK.
   - Prime Attributes: $\{A, B, C\}$ (all attributes are prime!).
   - Non-Prime Attributes: None.
2. **Normal Form Analysis:**
   - **Check 3NF:**
     - For $AB \to C$: $AB$ is a superkey (Condition 1 satisfied).
     - For $C \to B$: $C$ is NOT a superkey, BUT $B$ is a **Prime Attribute** (Condition 2 satisfied).
     - Therefore, **$R$ is strictly in 3NF**.
   - **Check BCNF:**
     - For $C \to B$: $C$ is NOT a superkey!
     - Therefore, **$R$ is NOT in BCNF**.
3. **BCNF Decomposition:**
   - Violation is caused by $C \to B$.
   - Decompose $R$ into:
     - $R_1 = C \cup B = \{B, C\}$ with $\text{PK} = \{C\}$.
     - $R_2 = R - (B) = \{A, C\}$ with $\text{PK} = \{AC\}$.
4. **Verifying Properties:**
   - **Lossless Check:** $R_1 \cap R_2 = \{C\}$. Since $C \to B$, $R_1 \cap R_2 \to R_1$. Lossless join is **satisfied**!
   - **Dependency Preservation Check:**
     - In $R_1(B, C)$: $C \to B$ is preserved.
     - In $R_2(A, C)$: No dependencies hold except trivial.
     - The dependency **$AB \to C$ is LOST!**
   - **Conclusion:** Schema $R$ cannot be decomposed into BCNF without losing dependency $AB \to C$. This illustrates the fundamental design trade-off between BCNF and dependency preservation.

---

### Numerical 5: Chase Algorithm Tableau Verification
**Problem Statement:** Schema $R(A, B, C, D, E)$ is decomposed into:
$$D = \{ R_1(A, B, C), \quad R_2(B, C, D), \quad R_3(A, C, E) \}$$
Functional dependencies: $F = \{ A \to B, \quad B \to C, \quad C \to D, \quad D \to E \}$.
Use the Chase Algorithm to test whether decomposition $D$ is **Lossless**.

**Step-by-Step Solution:**
1. **Initial Tableau Construction:**

$$\begin{array}{|c|c|c|c|c|c|}
\hline
\text{Relation} & A & B & C & D & E \\
\hline
R_1(A, B, C) & a_1 & a_2 & a_3 & b_{14} & b_{15} \\
R_2(B, C, D) & b_{21} & a_2 & a_3 & a_4 & b_{25} \\
R_3(A, C, E) & a_1 & b_{32} & a_3 & b_{34} & a_5 \\
\hline
\end{array}$$

2. **Iteration 1: Apply $A \to B$:**
   - Rows $R_1$ and $R_3$ match on $A$ (both have $a_1$).
   - In column $B$, $R_1$ has $a_2$ and $R_3$ has $b_{32}$.
   - Equate them to $a_2$: Update cell $(3, 2) := a_2$.

$$\begin{array}{|c|c|c|c|c|c|}
\hline
\text{Relation} & A & B & C & D & E \\
\hline
R_1(A, B, C) & a_1 & a_2 & a_3 & b_{14} & b_{15} \\
R_2(B, C, D) & b_{21} & a_2 & a_3 & a_4 & b_{25} \\
R_3(A, C, E) & a_1 & \mathbf{a_2} & a_3 & b_{34} & a_5 \\
\hline
\end{array}$$

3. **Iteration 2: Apply $B \to C$:**
   - All three rows have $a_2$ in column $B$. All already have $a_3$ in column $C$. No change.

4. **Iteration 3: Apply $C \to D$:**
   - All three rows match on $C$ ($a_3$).
   - Row $R_2$ has $a_4$ in column $D$.
   - Equate all rows in column $D$ to $a_4$:
     Update cell $(1, 4) := a_4$ and cell $(3, 4) := a_4$.

$$\begin{array}{|c|c|c|c|c|c|}
\hline
\text{Relation} & A & B & C & D & E \\
\hline
R_1(A, B, C) & a_1 & a_2 & a_3 & \mathbf{a_4} & b_{15} \\
R_2(B, C, D) & b_{21} & a_2 & a_3 & a_4 & b_{25} \\
R_3(A, C, E) & a_1 & a_2 & a_3 & \mathbf{a_4} & a_5 \\
\hline
\end{array}$$

5. **Examine Tableau State:**
   - Row 3 ($R_3$) now contains: $\mathbf{\langle a_1, a_2, a_3, a_4, a_5 \rangle}$!
   - Because a complete row consists entirely of distinguished symbols ($a_j$), the Chase terminates successfully.
   - **Conclusion:** The decomposition $D$ is **PROVEN LOSSLESS**. $\blacksquare$

---

## 3.12 High-Probability Exam Questions & Student Pitfalls

### High-Probability Exam Questions
1. **State and prove Armstrong's Axioms (Reflexivity, Augmentation, Transitivity). Derive the Decomposition, Union, and Pseudotransitivity rules.**
2. **Define 1NF, 2NF, 3NF, and BCNF. Provide a schema example that is in 3NF but not in BCNF, explaining why.**
3. **Prove that a binary decomposition $R = (R_1, R_2)$ is lossless if and only if $(R_1 \cap R_2) \to R_1$ or $(R_1 \cap R_2) \to R_2$.**
4. **Explain the Chase Algorithm with a worked tableau example.**
5. **Differentiate between Lossless Join and Dependency Preservation. Explain why BCNF cannot always preserve dependencies.**

### Common Student Traps & Mistakes
- *Trap 1: Forgetting that a relation with simple (single-attribute) candidate keys is automatically in 2NF.*
  - **Mistake:** Spending 10 minutes checking 2NF for relations where candidate keys are single columns.
  - **Rule:** Partial dependency requires a composite key. If keys are single attributes, 2NF is automatically satisfied.
- *Trap 2: Misinterpreting Condition 2 of 3NF.*
  - **Mistake:** Assuming that for $X \to A$ in 3NF, $X$ must be a prime attribute.
  - **Rule:** The condition is that **$A$ (the RHS dependent)** must be a prime attribute, NOT $X$.
- *Trap 3: Stopping after finding one candidate key.*
  - **Mistake:** Finding one key and calculating normal forms based on it.
  - **Rule:** Normal forms (2NF, 3NF) require testing against **ALL Candidate Keys**, not just the primary key!
