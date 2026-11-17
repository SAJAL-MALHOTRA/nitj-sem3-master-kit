# DBMS Mid-Semester Notes — From Scratch to Pro
**ITDC-0207, Database Management Systems | NIT Jalandhar | Units 1 & 2**
*Reference: Database Management Systems — Raghu Ramakrishnan & Johannes Gehrke*

---

## HOW TO USE THIS FILE
- Read Unit 1 → Unit 2 in order, they build on each other.
- Every major topic has a **"Likely to be asked as"** note based on your 2024 & 2025 mid-sem papers.
- Practice Questions section at the end has BOTH previous papers fully organized + extra questions for practice.

---

# UNIT 1: INTRODUCTION & ER MODEL

## 1. What is a DBMS?
A **Database Management System (DBMS)** is software that lets you define, create, maintain, and control access to a database. A **database** is a collection of related, logically coherent data.

**Core functions of a DBMS:**
- Defining structure (schema) for storage of data
- Manipulating data — insert, update, delete, retrieve
- Sharing data among multiple users/applications safely
- Protecting data — security, integrity, backup/recovery

## 2. Database System vs File System
File-processing systems (pre-DBMS era) had major problems that DBMS solves:

| Problem in File System | How DBMS Solves It |
|---|---|
| **Data redundancy & inconsistency** — same data duplicated across files, may go out of sync | Centralized storage, single copy of data |
| **Difficulty accessing data** — need a new program for every new query | Query languages (SQL) allow ad-hoc queries |
| **Data isolation** — data scattered in different files/formats | Unified data model |
| **Integrity problems** — constraints buried in application code, hard to enforce/change | Constraints declared once in the schema |
| **Atomicity problems** — a crash mid-update leaves data in inconsistent state | Transactions with ACID properties |
| **Concurrent access anomalies** — simultaneous updates cause inconsistency | Concurrency control (locking, timestamps) |
| **Security problems** — hard to enforce per-user access in file systems | Authorization & access control at DBMS level |

> **Likely to be asked as:** "Discuss DBMS vs File System" or a variant — write it as a table like above, 5-6 points is enough for 6 marks.

## 3. Database System Concepts and Architecture

### 3.1 Three-Schema (ANSI-SPARC) Architecture
Purpose: achieve **data independence** by separating what users see from how data is physically stored.

1. **External Level (View level)** — how individual users see the data (different views for different users; e.g., a clerk sees only customer names, not salary).
2. **Conceptual Level (Logical level)** — describes the *entire* database structure for the community of users — entities, relationships, constraints — hides physical storage details.
3. **Internal Level (Physical level)** — describes how data is *actually stored*: file organization, indexes, access paths.

```
   [External View 1] [External View 2] [External View 3]
              \             |             /
               \            |            /
                [ Conceptual / Logical Schema ]
                              |
                    [ Internal / Physical Schema ]
                              |
                        [ Stored Database ]
```

### 3.2 Overall Database System Structure (Components)
- **Query Processor** — parses & optimizes queries (DDL interpreter, DML compiler, query evaluation engine)
- **Storage Manager** — interfaces between data stored on disk and applications (authorization/integrity manager, transaction manager, file manager, buffer manager)
- **Disk Storage** — data files, indices, data dictionary (metadata/catalog)
- **DBA (Database Administrator)** — the person who administers all this

> **Likely to be asked as:** "Draw and explain the overall database structure / three-schema architecture" (Unit 1, 6 marks type).

## 4. Data Models
A **data model** is a collection of concepts to describe structure, operations, and constraints of a database.

- **Hierarchical model** — tree structure, parent-child (1:N only)
- **Network model** — graph structure, allows M:N via "sets"
- **Relational model** — data in tables (relations) — *most important for this course*
- **Entity-Relationship (ER) model** — conceptual/high-level model used for *design*, not storage
- **Object-Oriented model** — data as objects with attributes & methods

## 5. Schema vs Instance
- **Schema** = the *design/structure* of the database (like a variable's type) — changes rarely.
- **Instance** = the *actual data* stored at a given point in time (like a variable's value) — changes constantly.

Example: `Student(SID, Name, Major)` is a schema. The current 500 rows of student data is an instance.

## 6. Data Independence
The ability to change a schema at one level without affecting the schema at the level above.

- **Logical Data Independence** — ability to change the *conceptual* schema without changing *external* schemas/application programs. (e.g., adding a new attribute to a table doesn't break existing views). **Harder to achieve.**
- **Physical Data Independence** — ability to change the *internal (physical)* schema without changing the *conceptual* schema. (e.g., changing storage from a heap file to a B+ tree index, or moving to a new disk, doesn't affect logical structure). **Easier to achieve.**

## 7. Database Languages
- **DDL (Data Definition Language)** — defines schema. `CREATE`, `ALTER`, `DROP`, `TRUNCATE`. Generates entries stored in the **data dictionary/catalog**.
- **DML (Data Manipulation Language)** — manipulates data.
  - *Procedural DML* — user specifies *what* data is needed *and how* to get it (e.g., relational algebra).
  - *Non-procedural (Declarative) DML* — user specifies *what* data is needed without saying how (e.g., SQL, relational calculus, tuple/domain calculus).
- (Good to mention even though not explicitly listed) **DCL** — `GRANT`, `REVOKE` (access control). **TCL** — `COMMIT`, `ROLLBACK`, `SAVEPOINT` (transaction control).

> **Likely to be asked as:** "Explain DDL and DML with examples" (appeared in 2024 paper, Q5-ii, 3 marks).

---

## 8. ER MODEL — the most exam-heavy part of Unit 1

### 8.1 Basic Building Blocks
- **Entity** — a real-world object distinguishable from others (e.g., a specific student "Rahul").
- **Entity Set** — collection of entities of the same type sharing the same attributes (e.g., all Students).
- **Attribute** — property of an entity.
  - *Simple* — cannot be divided (e.g., Age)
  - *Composite* — can be divided into sub-parts (e.g., Name → First, Last)
  - *Single-valued* — one value per entity (e.g., SSN)
  - *Multi-valued* — can have many values (e.g., PhoneNumbers) — shown with double ellipse
  - *Derived* — can be computed from other attributes (e.g., Age from DOB) — shown with dashed ellipse
- **Relationship** — association among two or more entities (e.g., Student *Enrolls in* Course).
- **Relationship Set** — collection of relationships of the same type.
- **Degree of a relationship** — number of entity sets participating:
  - *Unary/Recursive* (degree 1) — e.g., Employee *Supervises* Employee
  - *Binary* (degree 2) — most common
  - *Ternary* (degree 3) — e.g., Supplier–Part–Project (see Unit 1 topic "relationships of higher degree")

### 8.2 Keys (VERY frequently asked — appeared as a standalone Q5-iii in 2024 paper)
- **Super Key** — any set of attributes that uniquely identifies a tuple. (A relation can have many super keys.)
- **Candidate Key** — a *minimal* super key (no proper subset of it is also a super key). A relation can have multiple candidate keys.
- **Primary Key** — the candidate key *chosen* by the designer to uniquely identify tuples. Cannot be NULL (entity integrity).
- **Alternate Key** — candidate keys not chosen as primary key.
- **Foreign Key** — an attribute (or set) in one relation that refers to the primary key of another (or same) relation — enforces **referential integrity**.
- **Composite Key** — a key made of two or more attributes together.

Example: In `Student(SID, SSN, Name, Email)`:
- Super keys: {SID}, {SSN}, {SID,Name}, {SID,SSN,Email}...
- Candidate keys: {SID}, {SSN}, {Email} (each independently unique & minimal)
- Primary key: {SID} (the chosen one)

### 8.3 Generalization, Specialization, Aggregation (Extended ER / EER)
- **Specialization** — top-down process: dividing a higher-level entity set (e.g., `Employee`) into lower-level subtypes (e.g., `Manager`, `Engineer`) based on distinguishing characteristics.
- **Generalization** — bottom-up process: combining common attributes of lower-level entity sets (e.g., `Car`, `Truck`) into a higher-level entity set (`Vehicle`). Reverse of specialization.
- **Constraints on Generalization/Specialization:**
  - *Disjoint* — an entity can belong to only ONE subclass (e.g., an Account is either Savings OR Current)
  - *Overlapping* — an entity can belong to more than one subclass (e.g., a Person can be both Student and Employee)
  - *Total participation* — every entity of the superclass MUST belong to some subclass
  - *Partial participation* — some superclass entities may not belong to any subclass
- **Aggregation** — used when a relationship itself needs to participate in another relationship (treats a relationship set as a higher-level entity so it can relate to a third entity). Classic example: `Employee Works_On Project` (relationship), and this combined "Works_On" needs to be *Monitored_by* a `Manager` — you can't directly connect a manager to a relationship, so you aggregate `(Employee, Works_On, Project)` into one abstract entity.

### 8.4 Mapping Cardinality (Cardinality Ratio) & Participation
- **1:1** — one entity of set A relates to at most one entity of set B, and vice versa.
- **1:N (One-to-Many)** — one entity in A relates to many in B, but each in B relates to only one in A.
- **M:N (Many-to-Many)** — entities in A can relate to many in B and vice versa.
- **Total participation** — every entity in the set MUST participate in the relationship (double line in ER diagram).
- **Partial participation** — participation is optional (single line).

### 8.5 ER Diagram Notation Cheat-Sheet
| Symbol | Meaning |
|---|---|
| Rectangle | Entity set |
| Double rectangle | Weak entity set |
| Ellipse | Attribute |
| Double ellipse | Multi-valued attribute |
| Dashed ellipse | Derived attribute |
| Diamond | Relationship set |
| Double diamond | Identifying relationship (for weak entity) |
| Lines | Link entity to attribute/relationship |
| Double line | Total participation |
| Underline | Primary key attribute |

**Weak Entity Set** — an entity set that does NOT have a primary key of its own; it depends on a "owner"/"identifying" strong entity set + a **partial key (discriminator)** to be uniquely identified. E.g., `Dependent` (of an `Employee`) is identified only via `Employee_SSN + Dependent_Name`.

### 8.6 Reduction of an ER Diagram to Tables (Rules — VERY important, asked in Q1 both years)
1. **Strong entity set** → becomes a table with all its simple attributes; composite attributes are flattened into their components; primary key of the entity becomes the primary key of the table.
2. **Weak entity set** → becomes a table whose primary key = (primary key of owner entity) + (its own partial/discriminator key). Owner's key becomes a foreign key.
3. **1:1 relationship** → primary key of either entity can be placed as a foreign key in the other table (usually put it on the side with total participation, or merge into one table).
4. **1:N relationship** → primary key of the "1" side is placed as a foreign key in the table on the "N" side. (No separate table needed unless the relationship has its own descriptive attributes and you want to avoid nulls.)
5. **M:N relationship** → a NEW separate table is created with the primary keys of BOTH participating entities as a composite primary key (and each also as a foreign key), plus any descriptive attributes of the relationship itself.
6. **Multi-valued attribute** → becomes its own separate table with a foreign key referencing the owner entity's primary key (since a single column can't hold multiple values in 1NF).
7. **Generalization/Specialization** → three common strategies:
   - One table per subclass with all inherited + own attributes duplicated (works well if disjoint & total)
   - One table for superclass + one table per subclass containing only subclass-specific attributes + PK (most common, handles overlapping)
   - Single table for everything with a "type" discriminator column and nullable subclass-specific columns
8. **Ternary/n-ary relationship** → always needs its own table with all participating entities' keys as a composite key.

### 8.7 What can't be captured directly in SQL (asked explicitly in 2025 paper, Q1)
When converting an ER diagram to SQL CREATE TABLE statements, some constraints are **hard/impossible to enforce with plain DDL** and usually need `CHECK` constraints, `TRIGGER`s, or application-level logic:
- Complex participation constraints (e.g., "every album must have exactly one producer" — total participation with exact cardinality) usually can't be enforced by a simple `NOT NULL`/FK alone if the relationship is optional from the SQL structural standpoint.
- Disjointness/overlap constraints in generalization (e.g., "an entity cannot be in both subclass A and B") — needs a trigger or check across tables.
- General cardinality constraints beyond 1:1, 1:N, M:N (e.g., "a musician can play at most 3 instruments") — needs a `CHECK`/trigger, plain FK can't count occurrences.
- M:N relationship constraints requiring a minimum number of participants — can't be done with basic FK/PK.
- **Why**: standard SQL DDL (keys + FK + NOT NULL) can only express structural constraints (uniqueness, referential integrity, non-null) — it cannot express *counting* or *mutual-exclusion* business rules without procedural extensions (triggers, assertions, application code).

### 8.8 Relationships of Higher Degree
A relationship need not be binary. A **ternary relationship** (degree 3) connects three entity sets, e.g., `Supplier — supplies — Part` for a `Project`. It is **not** generally equivalent to three binary relationships — a ternary relationship can express a business rule (e.g., "Supplier S supplies Part P to Project J") that three separate binary relationships cannot capture together. When reduced to a table, all three keys form part of the composite primary key.

---

# UNIT 2: RELATIONAL MODEL & SQL

## 1. Relational Data Model — Core Concepts
- **Relation (Table)** — a set of tuples (no duplicate tuples, no ordering of tuples/attributes in theory).
- **Tuple** — a row = one record.
- **Attribute** — a column.
- **Domain** — the set of allowable/legal values for an attribute.
- **Degree** — number of attributes in a relation.
- **Cardinality** — number of tuples in a relation.
- **Relation Schema** — `R(A1, A2, ..., An)` — the structure. **Relation Instance** — actual set of tuples at a time.

## 2. Integrity Constraints (asked as a full 6-mark question in 2024 paper — know WHY they're needed too)
**Why needed:** to ensure the accuracy, validity, and consistency of data in the database, and to prevent accidental damage during updates.

- **Domain Constraint** — every attribute value must be from its defined domain (correct data type & range). E.g., `Age` must be a positive integer.
- **Entity Integrity Constraint** — no attribute participating in the **primary key** can be NULL, ensuring every tuple is uniquely identifiable.
- **Referential Integrity Constraint** — a **foreign key** value must either match an existing primary key value in the referenced relation, or be entirely NULL. Prevents "dangling references." Enforced via `ON DELETE`/`ON UPDATE` (CASCADE, SET NULL, RESTRICT).
- **Key Constraint** — values in a candidate/primary key column(s) must be unique across all tuples.
- (Also mention) **General/Semantic Constraints** — business rules enforced via `CHECK` constraints, e.g., `Salary > 0`.

## 3. Relational Algebra (procedural query language — heavily asked, 6/6 marks both years)
| Operator | Symbol | Meaning |
|---|---|---|
| Select | σ (sigma) | σ<sub>condition</sub>(R) — picks rows satisfying a condition |
| Project | π (pi) | π<sub>attributes</sub>(R) — picks columns, removes duplicates |
| Union | ∪ | R ∪ S — rows in R or S (same schema/union-compatible) |
| Set Difference | − | R − S — rows in R but not in S |
| Cartesian Product | × | R × S — all combinations of tuples |
| Rename | ρ (rho) | ρ<sub>newname</sub>(R) — renames a relation/attributes |
| Intersection | ∩ | R ∩ S (derived: R − (R − S)) |
| Join (theta join) | ⋈<sub>condition</sub> | R ⋈ S — combine on a condition (= Cartesian product + select) |
| Natural Join | ⋈ | join on common attribute names automatically, duplicate columns removed |
| Division | ÷ | R ÷ S — finds tuples in R related to ALL tuples in S (used for "for all" queries) |

**Worked examples (Sailors/Reserves/Boats schema — this exact schema was asked in your 2024 paper):**
```
Sailors(sid, sname, rating, age)
Reserves(sid, bid, day)
Boats(bid, bname, color)
```
i. Sailors who reserved boat 103:
`π sname (σ bid=103 (Reserves ⋈ Sailors))`

ii. Sailors who reserved more than 2 boats — needs a self-comparison via renaming:
`π sname ( σ R1.sid = R2.sid AND R1.bid ≠ R2.bid AND R2.bid ≠ R3.bid AND R1.bid ≠ R3.bid ( ρ R1(Reserves) × ρ R2(Reserves) × ρ R3(Reserves) ) ⋈ Sailors )`
*(Simplify in exam: show the logic — pairwise distinct bid comparison across 3 renamed copies of Reserves, then join with Sailors and project sname.)*

iii. Sailors who reserved a red boat:
`π sname ( σ color='red' (Boats) ⋈ Reserves ⋈ Sailors )`

iv. sname, bid, day for each reservation:
`π sname,bid,day (Reserves ⋈ Sailors)`

v. Sailors who reserved a boat on BOTH Monday and Friday (this needs intersection of sid sets, not a single AND on one row):
`π sname ( ( π sid (σ day='Monday' (Reserves)) ∩ π sid (σ day='Friday' (Reserves)) ) ⋈ Sailors )`

vi. sname, rating of sailors who reserved boats but are older than 40:
`π sname,rating ( σ age>40 (Sailors) ⋈ Reserves )`

> **Tip:** In relational algebra, whenever a query says "reserved on both X and Y" or "all of," think **intersection** or **division** — don't just AND two conditions in one σ (that's wrong, since day is a single-valued attribute per tuple, you can't have day='Monday' AND day='Friday' in the same row).

### 3.1 Relational Calculus (also asked — Q2 in 2025 paper wants TRC & DRC too)
- **Tuple Relational Calculus (TRC):** `{t | P(t)}` — t is a tuple variable ranging over a relation; P(t) is a predicate. Example: names of students in "IT" dept:
  `{t.SName | ∃ s ∈ Student (s.SID = t... ) ...}` — practically: `{t | ∃ s ∈ Student (t.SName = s.SName ∧ s.Major = 'Information Technology')}`
- **Domain Relational Calculus (DRC):** `{<x1,x2,...,xn> | P(x1,...,xn)}` — variables range over domain *values*, not tuples. Example: same query:
  `{<sn> | ∃ id,mj,yr (<id,sn,mj,yr> ∈ Student ∧ mj='Information Technology')}`

## 4. Introduction to SQL

### 4.1 Characteristics & Advantages of SQL
- Non-procedural (declarative) — say WHAT you want, not HOW
- High-level, English-like syntax — easy to learn
- Works on set-at-a-time basis, not record-at-a-time
- Both DDL and DML in one language
- Portable across most RDBMS (standardized by ANSI/ISO)
- Supports client-server architecture, multiple views, embedded/dynamic use in host languages

### 4.2 SQL Data Types & Literals
- **Numeric**: `INT`, `SMALLINT`, `DECIMAL(p,s)`, `FLOAT`, `REAL`
- **Character/String**: `CHAR(n)` (fixed length), `VARCHAR(n)` (variable length)
- **Date/Time**: `DATE`, `TIME`, `TIMESTAMP`
- **Boolean**: `BOOLEAN` (in some RDBMS)
- **Literals**: numeric literals (`25`, `3.14`), character literals (`'abc'`), date literals (`DATE '2025-09-25'`)

### 4.3 Types of SQL Commands
| Category | Commands | Purpose |
|---|---|---|
| **DDL** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` | Define/modify structure |
| **DML** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Manipulate data |
| **DCL** | `GRANT`, `REVOKE` | Control access/permissions |
| **TCL** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Manage transactions |

### 4.4 SQL Operators
- **Arithmetic**: `+ − * /`
- **Comparison**: `= <> < > <= >=`
- **Logical**: `AND OR NOT`
- **Special**: `BETWEEN...AND`, `IN`, `LIKE` (with `%` and `_` wildcards), `IS NULL`, `EXISTS`, `ANY`/`SOME`, `ALL`

### 4.5 Basic Query Structure
```sql
SELECT [DISTINCT] column_list
FROM   table_list
WHERE  condition
GROUP BY column_list
HAVING  group_condition
ORDER BY column_list [ASC|DESC];
```
Logical order of execution: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`

### 4.6 Subqueries
A query nested inside another query, in `WHERE`, `FROM`, or `SELECT` clause.
```sql
-- Students in IT department (subquery example matching your papers' style)
SELECT SName FROM Student
WHERE Major = 'Information Technology';

-- Correlated subquery example: students enrolled in every Mathematics course
SELECT S.SName FROM Student S
WHERE NOT EXISTS (
  SELECT C.CID FROM Course C WHERE C.Department = 'Mathematics'
  EXCEPT
  SELECT E.CID FROM Enroll E WHERE E.SID = S.SID
);
```
This last pattern — "double negation" (NOT EXISTS a course they haven't taken) — is the standard SQL way to express **"for all"/division** queries. Learn it cold; it directly answers questions like Q2(d) in your 2025 paper.

### 4.7 Aggregate Functions
`COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()` — used with `GROUP BY` for per-group aggregation and `HAVING` to filter groups (not `WHERE`, since `WHERE` filters rows before grouping).
```sql
SELECT Department, COUNT(*) AS num_courses
FROM Course
GROUP BY Department
HAVING COUNT(*) > 3;
```

### 4.8 Insert, Update, Delete
```sql
INSERT INTO Student (SID, SName, Major, Year) VALUES (1, 'Vikas', 'IT', 3);

UPDATE Enroll SET Grade = 'A' WHERE SID = 1 AND CID = 'CS201';

DELETE FROM Student WHERE SID = 1;
```

### 4.9 Joins
- **Inner Join** — only matching rows from both tables.
  `SELECT * FROM Enroll E JOIN Student S ON E.SID = S.SID;`
- **Left Outer Join** — all rows from left + matched from right (NULL if no match).
- **Right Outer Join** — all rows from right + matched from left.
- **Full Outer Join** — all rows from both, NULL where no match.
- **Self Join** — a table joined with itself (e.g., find employees & their managers in the same `Employee` table).
- **Natural Join** — automatic join on identically-named columns.

### 4.10 Set Operations in SQL
- `UNION` — combines results of two queries, removes duplicates (`UNION ALL` keeps duplicates).
- `INTERSECT` — rows common to both queries.
- `MINUS` (Oracle) / `EXCEPT` (standard SQL, SQL Server, PostgreSQL) — rows in first query but not in second.
> Both queries must have the **same number of columns with compatible data types (union-compatible)**.

### 4.11 Cursors
A **cursor** is a database object used to retrieve and process rows **one at a time** from a result set (needed because SQL by default works on sets, but procedural logic in PL/SQL etc. often needs row-by-row processing).

Lifecycle:
```sql
DECLARE cur CURSOR FOR SELECT SID, SName FROM Student;
OPEN cur;
FETCH cur INTO :sid, :sname;
-- loop through with FETCH until not found --
CLOSE cur;
DEALLOCATE cur;
```
Types: **Implicit cursors** (auto-created by SQL for every DML statement) vs **Explicit cursors** (declared by programmer for `SELECT` returning multiple rows). Also: static vs dynamic, read-only vs updatable.

---

# PRACTICE QUESTIONS — FROM YOUR ACTUAL PAST PAPERS

## Paper 1: Sept 2025 Mid-Sem (30 marks, 2 questions)

**Q1 (15 marks) — Notown Records ER Design:**
Design a conceptual schema & draw an ER diagram for a record label database given these facts:
- Musicians: SSN, name, address, phone (shared addresses ok, address has ≤1 phone)
- Instruments: unique ID, name, musical key
- Albums: unique ID, title, copyright date, format, album identifier
- Songs: title, author (no song on more than one album)
- Musicians can play several instruments; instruments can be played by several musicians (M:N)
- Each album has multiple songs, but each song belongs to only one album (1:N)
- Songs performed by one or more musicians; musicians perform many songs (M:N)
- Each album has exactly one producer (a musician); a musician can produce several albums (1:N)

*Do:* Draw the ER diagram → identify all keys/cardinalities → write `CREATE TABLE` SQL for every entity & relationship set → explicitly list which constraints (see Section 8.7 above) can't be expressed in plain SQL and why.

**Q2 (15 marks) — Relational Algebra, TRC, DRC** on:
```
Student(SID, SName, Major, Year)
Course(CID, CName, Department)
Enroll(SID, CID, Grade)
Professor(PID, PName, Department)
Teaches(PID, CID, Semester)
```
a) Names of students who took ≥1 course in "Information Technology" dept.
b) Courses (CID, CName) never taken by any student.
c) Names of professors who teach courses that student "Vikas" is enrolled in.
d) Names of students who took ALL courses offered by "Mathematics" dept. (→ **division**)
e) Names & grades of students in "Database Systems" course for "Fall 2025" semester.

## Paper 2: Oct 2024 Mid-Sem (30 marks, 5 questions, 6 marks each)

**Q1.** What are integrity constraints and why are they required? Discuss different types with examples. *(→ Unit 2, Section 2 above)*

**Q2.** On `Sailors(sid,sname,rating,age)`, `Reserves(sid,bid,day)`, `Boats(bid,bname,color)` — write relational algebra for:
i. Sailors who reserved boat 103
ii. Sailors who reserved more than 2 boats
iii. Sailors who reserved a red boat
iv. sname, bid, day for each reservation
v. Sailors who reserved a boat on both Monday and Friday
vi. sname, rating of sailors who reserved boats but are older than 40
*(→ Fully worked out in Unit 2, Section 3 above)*

**Q3.** ER diagram for a University Registrar's office: courses (number, title, credits, syllabus, prerequisites), course offerings (course number, year, semester, section, instructor, timing, classroom), students (id, name, program), instructors (id, name, dept, title), plus enrollment + grades.
*Hint: `Prerequisite` is a recursive (unary) relationship on Course; `Offering` is a weak-entity-like concept dependent on Course+Semester+Section; `Enroll` is an M:N relationship between Student and Offering carrying a Grade attribute.*

**Q4.** On `Suppliers(sid,sname,address)`, `Parts(pid,pname,color)`, `Catalog(sid,pid,cost)` — write SQL for:
i. sids of suppliers who supply some red or green part
ii. sids of suppliers who supply some red part OR are at '221 Packer Street'
iii. pids of parts supplied by at least two different suppliers

```sql
-- i.
SELECT DISTINCT C.sid FROM Catalog C JOIN Parts P ON C.pid = P.pid
WHERE P.color = 'red' OR P.color = 'green';

-- ii.
SELECT DISTINCT S.sid FROM Suppliers S
WHERE S.address = '221 Packer Street'
   OR S.sid IN (SELECT C.sid FROM Catalog C JOIN Parts P ON C.pid=P.pid WHERE P.color='red');

-- iii.
SELECT C1.pid FROM Catalog C1, Catalog C2
WHERE C1.pid = C2.pid AND C1.sid <> C2.sid;
```

**Q5.** Explain: (i) ER diagram notations (ii) DDL and DML commands (iii) Primary and Candidate key.
*(→ All covered above: Section 8.5, Section 7, Section 8.2)*

---

# EXTRA PRACTICE QUESTIONS (for deeper prep)

1. Differentiate between logical and physical data independence with one example each.
2. What is a weak entity set? How is it represented in an ER diagram and mapped to a relational table? Give an example.
3. Explain the difference between generalization and specialization with a real-world example, and describe disjoint vs overlapping constraints.
4. Why is a ternary relationship not always decomposable into three binary relationships? Give an example.
5. For the schema `Employee(eid, ename, salary, dno)`, `Department(dno, dname, mgr_eid)`, `Project(pno, pname, dno)`, `WorksOn(eid, pno, hours)`:
   - Write RA for: employees who work on all projects of department 5 (division!).
   - Write SQL for: department name having the highest total salary expenditure.
6. What is the difference between `WHERE` and `HAVING`? Why can't you use an aggregate function directly in `WHERE`?
7. Explain the difference between `DELETE`, `TRUNCATE`, and `DROP`.
8. What is the difference between a candidate key and a super key? Can a table have zero candidate keys? Justify.
9. Write SQL using a correlated subquery to find the second-highest salary in an `Employee` table without using `LIMIT`/`TOP`.
10. Explain `NATURAL JOIN` vs `JOIN...USING` vs `JOIN...ON` — when do results differ?
11. What are cursors used for? Why does SQL need them if it's a set-based language? List cursor types.
12. Convert the following ER fragment to tables: A `Course` (strong entity) has many `Sections` (weak entity, discriminator = section_no), and a `Student` `Enrolls` in a `Section` with a `Grade` attribute on the relationship.
13. Explain entity integrity vs referential integrity with an example of a constraint violation for each.
14. In relational algebra, express: "Find sailors who have NOT reserved any boat" (hint: set difference on sid).

---

## QUICK-GLANCE FORMULA / SYMBOL SHEET
- σ = Select (rows) | π = Project (columns) | ρ = Rename | × = Cartesian product | ⋈ = Join | ÷ = Division
- Super key ⊇ Candidate key ⊇ {Primary key} (Primary key is ONE chosen candidate key)
- 1NF/normalization isn't in your syllabus for this mid-sem (only up to relational model + SQL) — don't over-prepare it, but do know **why multi-valued attributes need a separate table** (Section 8.6, rule 6) since that's 1NF reasoning in disguise.
- Division (÷) and NOT EXISTS(double negation) both solve "for all" queries — practice both forms since papers ask for RA, TRC, DRC, and SQL versions of the same query.

Good luck with your mid-sem — Units 1 & 2 are largely definitional + ER design + SQL/RA practice, so the ROI is highest on actually writing out 4-5 ER diagrams and 8-10 SQL/RA queries by hand rather than just re-reading.
