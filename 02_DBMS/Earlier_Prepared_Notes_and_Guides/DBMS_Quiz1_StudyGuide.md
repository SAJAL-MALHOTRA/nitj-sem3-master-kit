# DBMS Quiz-I Study Guide — ITDC0207 (NIT Jalandhar)
Covers: Introduction to DBMS + ER Model (syllabus units 1–2), mapped to your Quiz-I PYQ pattern.

---

## 1. DBMS vs File System

A **file system** stores data in separate files/folders (like the "customer stored in separate folders in filing cabinets" idea from Q16 of your quiz). Problems with this approach:

| Problem | Why it happens |
|---|---|
| Data redundancy & inconsistency | Same data duplicated across files, updated in one place but not another |
| Difficulty accessing data | Need a new program for every new query |
| Data isolation | Data scattered in different formats/files |
| Integrity problems | Constraints (e.g. balance > 0) buried in application code, easy to miss |
| Atomicity problems | A crash mid-operation can leave data half-updated |
| Concurrent access anomalies | Multiple users writing simultaneously corrupt data |
| Security problems | Hard to enforce who can see/edit what |

A **DBMS** (Database Management System) is software that solves all of this: it manages data centrally, enforces integrity, controls concurrent access, and provides a query language instead of custom programs per request.

---

## 2. Three-Schema Architecture

Every DBMS is (conceptually) organized into 3 levels:

- **External level (view level)** — how individual users see the data (different views for different users; a bank teller sees different fields than an auditor).
- **Conceptual level (logical level)** — the whole database's logical structure as seen by the DBA: what entities exist, what relationships, what constraints. Independent of physical storage.
- **Internal level (physical level)** — how data is *actually* stored on disk: file structures, indexes, storage blocks.

**Why this matters:** it gives **data independence**:
- **Logical data independence** — you can change the conceptual schema (e.g. add a new table/attribute) without changing external views/application programs.
- **Physical data independence** — you can change how data is stored physically (e.g. switch index type, move to a new disk) without changing the conceptual schema.

---

## 3. Data Models, Schema, Instance

- **Data model** — a collection of concepts to describe data structure, relationships, and constraints (e.g. ER model, Relational model, Hierarchical model, Network model, Object-oriented model). Q16 in your quiz tests exactly this — recognizing which model matches a description (tree-like folder-style storage = **hierarchical**).
- **Schema** — the overall *design/logical structure* of the database — described once, doesn't change often. (Q7: "schema" = **logical structure or design of a database**.)
- **Instance** — the actual *data* stored in the database at a particular moment — changes constantly as data is inserted/updated/deleted.

Analogy: schema = blueprint of a house; instance = the house with furniture in it right now.

---

## 4. Database Languages & Interfaces

| Language | Full form | Purpose | Example commands |
|---|---|---|---|
| **DDL** | Data Definition Language | Define/alter schema structure | `CREATE`, `ALTER`, `DROP` |
| **DML** | Data Manipulation Language | Query and modify data (Q18 in your quiz) | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Data Control Language | Control access/permissions | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manage transactions | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

The DBMS itself acts as the **interface between the application/user and the physical database** (Q19) — the user/application never touches raw files directly.

---

## 5. ER Model — Core Concepts

The **Entity-Relationship (ER) model** describes the world as **entities**, their **attributes**, and **relationships** between entities.

### 5.1 Entities & Entity Sets
- **Entity** — a real-world object distinguishable from others (a specific student, a specific course).
- **Entity set** — collection of similar entities (all students).
- **Strong entity set** — has its own primary key, doesn't depend on another entity for identification.
- **Weak entity set** — does **not** have a full primary key of its own; it depends on a **owner/identifying entity** for identification. It has only a **partial key (discriminator)**.
  - **Key rule (Q1 of your quiz):** the weak entity set **must have total participation** in its identifying relationship with the owner entity — every weak entity instance *must* be linked to an owner, because that's the only way to identify it. The owner (strong) entity does NOT need total participation.
  - Example: `Dependent` is weak, identified by `(EmployeeID, DependentName)` — DependentName alone isn't unique, but combined with the owning Employee's key it is.

### 5.2 Attributes
| Type | Meaning | Example |
|---|---|---|
| Simple | Cannot be divided further | Age |
| Composite | Can be divided into sub-parts | Name → (FirstName, LastName) |
| Single-valued | One value per entity | SSN |
| Multi-valued | Can have multiple values | PhoneNumbers |
| Derived | Computed from other attributes | Age derived from DateOfBirth |
| Key attribute | Uniquely identifies the entity | RollNumber |

**Important for relational mapping:** in a relational **table row**, every attribute value must be **atomic (single-valued)** — a row cell cannot hold multiple values or be left with "more than one value" (this is exactly Q13's trick: *"In a row of a relational table, an attribute can have more than one value"* is **INCORRECT**, because relational tables require atomic values — this is called 1st Normal Form).

### 5.3 Relationships
- **Relationship** — an association among two or more entities.
- **Degree of a relationship** — number of entity sets participating:
  - **Unary (degree 1)** — entity related to itself (Employee `manages` Employee)
  - **Binary (degree 2)** — most common (Student `enrolls` Course)
  - **Ternary (degree 3)** — three entities together (Supplier, Part, Project in a supply relationship)
  - **N-ary (higher degree)** — syllabus explicitly mentions this ("relationships of higher degree")

### 5.4 Mapping Cardinalities (Constraints)
Describes how many entities on one side can relate to entities on the other side:
- **1:1** — one entity of A relates to at most one of B (Person — Passport)
- **1:N** — one entity of A relates to many of B (Department — Employees)
- **M:N** — many entities of A relate to many of B (Student — Course)

### 5.5 Participation Constraints
- **Total participation** — every entity in the set *must* participate in the relationship (double line in ER diagrams).
- **Partial participation** — participation is optional (single line).

---

## 6. Keys

| Key type | Definition | Quiz link |
|---|---|---|
| **Super key** | A set of one or more attributes that, taken together, **uniquely identify** a tuple/record. Can include extra, unnecessary attributes. | Q4, Q17: "a set of attributes that uniquely identify an entity" |
| **Candidate key** | A **minimal** super key — no attribute can be removed without losing uniqueness. There can be multiple candidate keys for one entity/table. | Q11: candidate key **can be used as a primary key** |
| **Primary key** | The candidate key **chosen** by the designer to uniquely identify rows in the actual implementation. | — |
| **Foreign key** | An attribute in one table that references the primary key of another table — **used to link two tables together**. | Q3: foreign key = "link one table to another" (NOT "ensure entity integrity" — that's the primary key's job) |

⚠️ Common trap (your Q5): options like "Tuple Constraint" are **not real integrity constraint types** — the real ones are: **Domain constraint**, **Key constraint**, **Entity integrity constraint** (primary key can't be NULL), **Referential integrity constraint** (foreign key must match an existing primary key value or be NULL — Q9).

**Metadata** (Q12) = "data about data" — e.g., a table's column names, data types, constraints are metadata about the actual data stored.

---

## 7. Generalization, Specialization, Aggregation (Extended ER Model)

- **Specialization** — top-down process: take a higher-level entity (`Vehicle`) and split it into lower-level sub-entities with distinct attributes (`Car`, `Truck`). This is an "IS-A" relationship.
- **Generalization** — bottom-up process: combine common attributes of several lower-level entities into one higher-level entity (`Saver Account` + `Current Account` → `Account`).
- **Aggregation** — treats a **relationship itself** as a higher-level entity, so it can participate in further relationships. Used when a relationship between two entities needs to relate to a third entity.
  - Example: `Employee` `Works_on` `Project` (this relationship) is *monitored by* a `Manager` — aggregation lets `Works_on` be treated as one abstract entity.

---

## 8. Reduction of ER Diagram to Relational Schema (the most exam-critical part)

This is what Q2 and Q10 in your quiz are testing. Rules:

| ER construct | How it becomes a table |
|---|---|
| Strong entity | One table; all its simple attributes become columns; key attribute → primary key |
| Weak entity | One table with its own attributes **+ the primary key of the owner entity as a foreign key**; primary key of the table = (owner's PK + weak entity's partial key) |
| Composite attribute | Flattened — only its simple component attributes become columns (not the composite name itself) |
| Multi-valued attribute | **Separate table** containing the attribute value + the primary key of the owning entity (as foreign key) |
| 1:1 relationship | No separate table usually needed — foreign key placed on either side's table |
| 1:N relationship | No separate table needed — foreign key of the "1" side's primary key placed on the "N" side table |
| M:N relationship | **Requires its own separate table** — containing the primary keys of both participating entities (as foreign keys, together forming the composite primary key) + any relationship's own attributes |
| Ternary/higher-degree relationship | Always needs its own separate table containing the PKs of all participating entities + own attributes |

**Applying this to Q2 of your quiz** (Person –Qualification(M,N)– Exam, with QualifiedDate as a relationship attribute):
- `Person(NID, Name)` ✅ — a valid table
- `Exam(ExamID, ExamName)` ✅ — a valid table
- Since `Qualification` is an **M:N** relationship (it has its own attribute `QualifiedDate`), it **needs its own table**: `Qualification(NID, ExamID, QualifiedDate)` ✅
- **`Exam(ExamID, NID, ExamName)`** ❌ is the one that will **NOT** hold — you can't just cram the foreign key `NID` into the `Exam` table, because one exam can have many qualified persons (M:N) — that relationship needs its own separate table, not a foreign key stuffed into `Exam`.

**Applying the "minimum number of tables" logic (Q10 style questions):**
Count = (number of entities) + (number of M:N or higher-degree relationships that need their own table). 1:1 and 1:N relationships are usually absorbed as foreign keys and don't need extra tables. So if you have entities M, N, P and relationships R1, R2, first check each relationship's cardinality — if both R1 and R2 are 1:N (or 1:1), the answer is just 3 tables (one per entity, with foreign keys embedded); if one of them is M:N, you'd need a 4th table for that relationship.

---

## 9. Types of Database Models (for "which DBMS type" questions like Q16)

| Model | How it organizes data |
|---|---|
| **Hierarchical** | Tree structure — parent-child, like nested folders in filing cabinets |
| **Network** | Graph structure — a record can have multiple parents |
| **Relational** | Data in tables (rows & columns) — connected via keys |
| **Object-oriented** | Data as objects (like OOP) with attributes + methods |

---

## 10. Quick-Fire Answer Key Logic (from your Quiz-I, for self-check)

| # | Concept being tested | Correct answer | Why |
|---|---|---|---|
| Q1 | Weak entity participation | C | Weak entity MUST have total participation in identifying relationship |
| Q2 | ER → relational mapping | D | M:N relationship can't be folded into one entity's table |
| Q3 | Foreign key purpose | D | Links one table to another |
| Q4 | Super key definition | B | Attributes that uniquely identify an entity |
| Q5 | Integrity constraint types | C | "Tuple Constraint" isn't a real category |
| Q6 | What an RDBMS is | C | Collection of tables |
| Q7 | Meaning of "schema" | A | Logical structure/design of a database |
| Q8 | Degree/arity of a relation | A | Number of attributes of its relation schema |
| Q9 | FK values must exist in referenced table | A | Referential integrity constraint |
| Q10 | Min tables for an ERD | B (3) | Entities become tables; 1:1/1:N relationships absorbed as FKs |
| Q11 | Candidate key property | B | Can be used as a primary key |
| Q12 | Data about data | C | Meta data |
| Q13 | Incorrect ER/relational statement | D | A relational table's attribute CANNOT hold more than one value |
| Q14 | Attribute on ternary/many-relationship | B | Belongs to the relationship ("Lodging"), not either entity |
| Q15 | Data types stored in DB | D | All of the above (image, text, audio/video) |
| Q16 | Traditional folder-based storage model | D | Hierarchical DBMS |
| Q17 | Set of attributes uniquely identifying a record | C | Super key |
| Q18 | Query + insert/update/delete language | D | DML |
| Q19 | DBMS's role | C | Interface between application and database |
| Q20 | Dominant vs subordinate entity deletion | B | If dominant (X) deleted, subordinate (Y) also deleted |

---

## 11. Study Tips for Your Next Quiz
1. Master the **keys hierarchy**: super key → candidate key → primary key/foreign key. Most confusion in your paper (Q4, Q5, Q11, Q17) is here.
2. Practice **drawing an ER diagram and converting it to tables** by hand — the mapping rules (Section 8) are the single highest-value topic based on your PYQ pattern.
3. Memorize the **4 integrity constraints**: domain, key, entity integrity, referential integrity — and recognize fake options like "tuple constraint."
4. Be clear on **weak entity total participation** — it's a favorite trick question.
5. Know **DDL vs DML vs DCL vs TCL** cold — one-line definitions with example commands.
