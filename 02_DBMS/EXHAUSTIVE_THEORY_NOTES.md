# DATABASE MANAGEMENT SYSTEMS (ITDC0207)
## DEFINITIVE END-SEMESTER THEORY MASTER BOOK
### B.Tech 3rd Semester | Comprehensive Academic Reference Guide

---

> **Academic Rigor Notice:**
> This volume serves as an exhaustive, mathematically rigorous, and completely self-contained theoretical master manual for Course Code **ITDC0207: Database Management Systems**. Every theoretical concept, mathematical formalism, algorithmic proof, relational reduction rule, transaction scheduling mechanism, and security model is presented in comprehensive academic depth without omissions or high-level generalizations.

---

# MASTER TABLE OF CONTENTS

- [UNIT 1: Introduction to Database Systems & Conceptual Data Modeling (ER & EER)](#unit-1-introduction-to-database-systems--conceptual-data-modeling-er--eer)
  - [1.1 Overview of Database Management Systems (DBMS)](#11-overview-of-database-management-systems-dbms)
    - [1.1.1 Foundational Definitions](#111-foundational-definitions)
    - [1.1.2 The Self-Describing Nature of a Database System](#112-the-self-describing-nature-of-a-database-system)
  - [1.2 Database System vs. File-Processing System](#12-database-system-vs-file-processing-system)
    - [1.2.1 Deep Breakdown of the 10 Major Deficiencies of File Systems](#121-deep-breakdown-of-the-10-major-deficiencies-of-file-systems)
    - [1.2.2 Comprehensive Comparison Matrix](#122-comprehensive-comparison-matrix)
  - [1.3 Database System Concepts and Three-Schema Architecture (ANSI/SPARC)](#13-database-system-concepts-and-three-schema-architecture-ansisparc)
    - [1.3.1 The Three Levels of Abstraction](#131-the-three-levels-of-abstraction)
    - [1.3.2 Schema Mappings and Request Transformation](#132-schema-mappings-and-request-transformation)
  - [1.4 Data Independence](#14-data-independence)
    - [1.4.1 Physical Data Independence](#141-physical-data-independence)
    - [1.4.2 Logical Data Independence](#142-logical-data-independence)
    - [1.4.3 Critical Comparison: Why Logical Independence is Harder](#143-critical-comparison-why-logical-independence-is-harder)
  - [1.5 Data Models](#15-data-models)
    - [1.5.1 Relational Data Model](#151-relational-data-model)
    - [1.5.2 Hierarchical Data Model](#152-hierarchical-data-model)
    - [1.5.3 Network Data Model](#153-network-data-model)
    - [1.5.4 Object-Oriented / Object-Relational Data Model](#154-object-oriented--object-relational-data-model)
    - [1.5.5 Comprehensive 4-Way Data Model Comparison Matrix](#155-comprehensive-4-way-data-model-comparison-matrix)
  - [1.6 Database Schemas, Instances, and Database State](#16-database-schemas-instances-and-database-state)
  - [1.7 Database Languages and Interfaces](#17-database-languages-and-interfaces)
    - [1.7.1 Data Definition Language (DDL)](#171-data-definition-language-ddl)
    - [1.7.2 Data Manipulation Language (DML)](#172-data-manipulation-language-dml)
    - [1.7.3 Data Control Language (DCL)](#173-data-control-language-dcl)
    - [1.7.4 Transaction Control Language (TCL)](#174-transaction-control-language-tcl)
    - [1.7.5 DBMS User Interfaces](#175-dbms-user-interfaces)
  - [1.8 Overall Database System Structure (Architectural Blueprint)](#18-overall-database-system-structure-architectural-blueprint)
    - [1.8.1 Deep Dive: Query Processor Components](#181-deep-dive-query-processor-components)
    - [1.8.2 Deep Dive: Storage Manager Components](#182-deep-dive-storage-manager-components)
  - [1.9 Data Modeling Using the Entity-Relationship (ER) Model](#19-data-modeling-using-the-entity-relationship-er-model)
    - [1.9.1 Core Elements: Entities and Entity Sets](#191-core-elements-entities-and-entity-sets)
    - [1.9.2 Strong vs. Weak Entity Sets](#192-strong-vs-weak-entity-sets)
    - [1.9.3 Classification of Attributes](#193-classification-of-attributes)
    - [1.9.4 Relationships, Relationship Sets, and Degree](#194-relationships-relationship-sets-and-degree)
    - [1.9.5 Mapping Cardinalities (Cardinality Ratios)](#195-mapping-cardinalities-cardinality-ratios)
    - [1.9.6 Participation Constraints: Total vs. Partial](#196-participation-constraints-total-vs-partial)
    - [1.9.7 Min-Max Structural Constraints (min, max)](#197-min-max-structural-constraints-min-max)
    - [1.9.8 Comprehensive Taxonomy of Keys](#198-comprehensive-taxonomy-of-keys)
  - [1.10 Extended / Enhanced ER (EER) Model Concepts](#110-extended--enhanced-er-eer-model-concepts)
    - [1.10.1 Specialization and Generalization](#1101-specialization-and-generalization)
    - [1.10.2 Constraints on Specialization and Generalization](#1102-constraints-on-specialization-and-generalization)
    - [1.10.3 Attribute and Relationship Inheritance](#1103-attribute-and-relationship-inheritance)
    - [1.10.4 Union Types / Category](#1104-union-types--category)
    - [1.10.5 Aggregation](#1105-aggregation)
  - [1.11 Reduction / Mapping of ER and EER Diagrams to Relational Tables](#111-reduction--mapping-of-er-and-eer-diagrams-to-relational-tables)
  - [1.12 Comprehensive Case Study: Enterprise System ER-to-Relational Reduction](#112-comprehensive-case-study-enterprise-system-er-to-relational-reduction)
  - [1.13 High-Probability Exam Questions & Student Pitfalls](#113-high-probability-exam-questions--student-pitfalls)

- [UNIT 2: Relational Data Model, Relational Algebra, and Advanced SQL](#unit-2-relational-data-model-relational-algebra-and-advanced-sql)
  - [2.1 Relational Data Model Concepts](#21-relational-data-model-concepts)
    - [2.1.1 Formal Mathematical Terminology vs. Informal Commercial Terminology](#211-formal-mathematical-terminology-vs-informal-commercial-terminology)
    - [2.1.2 Formal Mathematical Definition of a Relation](#212-formal-mathematical-definition-of-a-relation)
    - [2.1.3 Inherent Characteristics of Mathematical Relations](#213-inherent-characteristics-of-mathematical-relations)
  - [2.2 Relational Integrity Constraints](#22-relational-integrity-constraints)
    - [2.2.1 Domain Integrity Constraints](#221-domain-integrity-constraints)
    - [2.2.2 Entity Integrity Constraint](#222-entity-integrity-constraint)
    - [2.2.3 Referential Integrity Constraint](#223-referential-integrity-constraint)
    - [2.2.4 Enterprise (Semantic) Constraints](#224-enterprise-semantic-constraints)
  - [2.3 Relational Algebra](#23-relational-algebra)
    - [2.3.1 Fundamental Operations](#231-fundamental-operations)
    - [2.3.2 Derived (Additional) Relational Operations](#232-derived-additional-relational-operations)
  - [2.4 SQL Architecture & Command Taxonomy](#24-sql-architecture--command-taxonomy)
    - [2.4.1 Comprehensive Architectural Breakdown: TRUNCATE vs. DROP vs. DELETE](#241-comprehensive-architectural-breakdown-truncate-vs-drop-vs-delete)
  - [2.5 SQL Operators, Three-Valued Logic, and Aggregate Functions](#25-sql-operators-three-valued-logic-and-aggregate-functions)
    - [2.5.1 Three-Valued Logic (3VL) with NULL](#251-three-valued-logic-3vl-with-null)
    - [2.5.2 Built-In Aggregate Functions and NULL Handling](#252-built-in-aggregate-functions-and-null-handling)
  - [2.6 The SQL Query Execution Pipeline: GROUP BY and HAVING](#26-the-sql-query-execution-pipeline-group-by-and-having)
    - [2.6.1 Crucial Distinction: WHERE vs. HAVING](#261-crucial-distinction-where-vs-having)
  - [2.7 Joins in SQL](#27-joins-in-sql)
  - [2.8 Nested Subqueries: Correlated vs. Uncorrelated](#28-nested-subqueries-correlated-vs-uncorrelated)
    - [2.8.1 Uncorrelated Subquery](#281-uncorrelated-subquery)
    - [2.8.2 Correlated Subquery](#282-correlated-subquery)
    - [2.8.3 The EXISTS and NOT EXISTS Operators](#283-the-exists-and-not-exists-operators)
  - [2.9 Views in SQL](#29-views-in-sql)
    - [2.9.1 Updatability Rules for Views](#291-updatability-rules-for-views)
    - [2.9.2 The WITH CHECK OPTION Clause](#292-the-with-check-option-clause)
  - [2.10 Cursors in SQL and PL/SQL](#210-cursors-in-sql-and-plsql)
    - [2.10.1 Motivation: The Impedance Mismatch](#2101-motivation-the-impedance-mismatch)
    - [2.10.2 Implicit vs. Explicit Cursors](#2102-implicit-vs-explicit-cursors)
    - [2.10.3 The Explicit Cursor Lifecycle (4 Stages)](#2103-the-explicit-cursor-lifecycle-4-stages)
    - [2.10.4 Fully Annotated PL/SQL Implementation Example](#2104-fully-annotated-plsql-implementation-example)
  - [2.11 High-Probability Exam Questions & Student Pitfalls](#211-high-probability-exam-questions--student-pitfalls)

- [UNIT 3: Relational Database Design and Normalization Theory](#unit-3-relational-database-design-and-normalization-theory)
  - [3.1 Pitfalls in Relational Database Design & Informal Guidelines](#31-pitfalls-in-relational-database-design--informal-guidelines)
    - [3.1.1 Informal Design Guidelines](#311-informal-design-guidelines-elmasri--navathe)
    - [3.1.2 The Four Devastating Anomalies of Poorly Designed Schemas](#312-the-four-devastating-anomalies-of-poorly-designed-schemas)
    - [3.1.3 Generation of Spurious Tuples (Lossy Decomposition)](#313-generation-of-spurious-tuples-lossy-decomposition)
  - [3.2 Functional Dependencies (FDs)](#32-functional-dependencies-fds)
    - [3.2.1 Formal Mathematical Definition](#321-formal-mathematical-definition)
    - [3.2.2 Taxonomy of Functional Dependencies](#322-taxonomy-of-functional-dependencies)
  - [3.3 Armstrong's Axioms & Inference Rules](#33-armstrongs-axioms--inference-rules)
    - [3.3.1 Step-by-Step Formal Proofs of Armstrong's Axioms](#331-step-by-step-formal-proofs-of-armstrongs-axioms)
    - [3.3.2 Secondary Inference Rules (Derived Rules)](#332-secondary-inference-rules-derived-rules)
  - [3.4 The Attribute Closure Algorithm (X+)](#34-the-attribute-closure-algorithm-x)
  - [3.5 Systematic Algorithm for Finding All Candidate Keys](#35-systematic-algorithm-for-finding-all-candidate-keys)
  - [3.6 Equivalence of FD Sets & Minimal (Canonical) Cover](#36-equivalence-of-fd-sets--minimal-canonical-cover)
    - [3.6.1 Minimal Cover (Canonical Cover) Definition](#361-minimal-cover-canonical-cover-definition)
    - [3.6.2 Step-by-Step Algorithm to Compute Minimal Cover](#362-step-by-step-algorithm-to-compute-minimal-cover)
  - [3.7 The Normal Forms Based on Primary & Candidate Keys](#37-the-normal-forms-based-on-primary--candidate-keys)
    - [3.7.1 Definitions of Prime vs. Non-Prime Attributes](#371-definitions-of-prime-vs-non-prime-attributes)
    - [3.7.2 First Normal Form (1NF)](#372-first-normal-form-1nf)
    - [3.7.3 Second Normal Form (2NF)](#373-second-normal-form-2nf)
    - [3.7.4 Third Normal Form (3NF)](#374-third-normal-form-3nf)
    - [3.7.5 Boyce-Codd Normal Form (BCNF)](#375-boyce-codd-normal-form-bcnf)
    - [3.7.6 Exhaustive Comparison Matrix: 3NF vs. BCNF](#376-exhaustive-comparison-matrix-3nf-vs-bcnf)
  - [3.8 Properties of Relational Decompositions](#38-properties-of-relational-decompositions)
    - [3.8.1 Lossless-Join (Non-Additive) Decomposition](#381-lossless-join-non-additive-decomposition)
    - [3.8.2 Testing Lossless Join for Arbitrary N-ary Decompositions: The Chase (Tableau) Algorithm](#382-testing-lossless-join-for-arbitrary-n-ary-decompositions-the-chase-tableau-algorithm)
    - [3.8.3 Dependency Preservation Property](#383-dependency-preservation-property)
  - [3.9 Higher Normal Forms: 4NF and 5NF](#39-higher-normal-forms-4nf-and-5nf)
    - [3.9.1 Multivalued Dependencies (MVD) and Fourth Normal Form (4NF)](#391-multivalued-dependencies-mvd-and-fourth-normal-form-4nf)
    - [3.9.2 Join Dependencies (JD) and Fifth Normal Form (5NF / PJNF)](#392-join-dependencies-jd-and-fifth-normal-form-5nf--pjnf)
  - [3.10 Inclusion Dependencies and Database Design Approaches](#310-inclusion-dependencies-and-database-design-approaches)
  - [3.11 Comprehensive Worked Numerical Problems](#311-comprehensive-worked-numerical-problems)
    - [Numerical 1: Complete Candidate Key Determination](#numerical-1-complete-candidate-key-determination)
    - [Numerical 2: Minimal (Canonical) Cover Calculation](#numerical-2-minimal-canonical-cover-calculation)
    - [Numerical 3: Decomposing into 3NF (Lossless + Dependency Preserving)](#numerical-3-decomposing-into-3nf-lossless--dependency-preserving)
    - [Numerical 4: Decomposing into BCNF & Checking Dependency Preservation](#numerical-4-decomposing-into-bcnf--checking-dependency-preservation)
    - [Numerical 5: Chase Algorithm Tableau Verification](#numerical-5-chase-algorithm-tableau-verification)
  - [3.12 High-Probability Exam Questions & Student Pitfalls](#312-high-probability-exam-questions--student-pitfalls)

- [UNIT 4: Transaction Processing Concepts, Concurrency Control, and Recovery](#unit-4-transaction-processing-concepts-concurrency-control-and-recovery)
  - [4.1 Transaction Concepts & ACID Properties](#41-transaction-concepts--acid-properties)
    - [4.1.1 The ACID Properties & Underlying Architectural Mechanisms](#411-the-acid-properties--underlying-architectural-mechanisms)
  - [4.2 Transaction State Diagram & Lifecycle](#42-transaction-state-diagram--lifecycle)
  - [4.3 Schedules & Serializability](#43-schedules--serializability)
    - [4.3.1 Classification of Schedules](#431-classification-of-schedules)
    - [4.3.2 Conflicting Operations](#432-conflicting-operations)
    - [4.3.3 Conflict Serializability](#433-conflict-serializability)
    - [4.3.4 View Serializability](#434-view-serializability)
  - [4.4 Recoverability of Schedules & Cascading Aborts](#44-recoverability-of-schedules--cascading-aborts)
    - [4.4.1 Unrecoverable Schedule](#441-unrecoverable-schedule-the-worst-concurrency-nightmare)
    - [4.4.2 Recoverable Schedules](#442-recoverable-schedules)
    - [4.4.3 Cascading Rollback & Cascadeless Schedules (ACA)](#443-cascading-rollback--cascadeless-schedules-aca)
    - [4.4.4 Strict Schedules](#444-strict-schedules)
  - [4.5 Concurrency Anomalies Without Control](#45-concurrency-anomalies-without-control)
    - [4.5.1 Detailed Walkthrough of the Four Anomalies](#451-detailed-walkthrough-of-the-four-anomalies)
    - [4.5.2 ANSI SQL Transaction Isolation Levels](#452-ansi-sql-transaction-isolation-levels)
  - [4.6 Lock-Based Concurrency Control Protocols](#46-lock-based-concurrency-control-protocols)
    - [4.6.1 Lock Modes and Compatibility](#461-lock-modes-and-compatibility)
    - [4.6.2 The Two-Phase Locking (2PL) Protocol](#462-the-two-phase-locking-2pl-protocol)
    - [4.6.3 Variations of Two-Phase Locking](#463-variations-of-two-phase-locking)
  - [4.7 Deadlock Handling in Concurrency](#47-deadlock-handling-in-concurrency)
    - [4.7.1 Deadlock Prevention Protocols (Timestamp-Based)](#471-deadlock-prevention-protocols-timestamp-based)
    - [4.7.2 Deadlock Detection: The Wait-For Graph (WFG)](#472-deadlock-detection-the-wait-for-graph-wfg)
    - [4.7.3 Deadlock Recovery (Three Steps)](#473-deadlock-recovery-three-steps)
  - [4.8 Timestamp-Based Protocols & Thomas' Write Rule](#48-timestamp-based-protocols--thomas-write-rule)
    - [4.8.1 Timestamp Ordering (TO) Protocol](#481-timestamp-ordering-to-protocol)
    - [4.8.2 Thomas' Write Rule](#482-thomas-write-rule)
  - [4.9 Multiple Granularity Locking (MGL)](#49-multiple-granularity-locking-mgl)
    - [4.9.1 Intention Locks](#491-intention-locks)
  - [4.10 Database Recovery Techniques](#410-database-recovery-techniques)
    - [4.10.1 Taxonomy of Failures](#4101-taxonomy-of-failures)
    - [4.10.2 Storage Structure Hierarchy](#4102-storage-structure-hierarchy)
    - [4.10.3 The Write-Ahead Logging (WAL) Protocol](#4103-the-write-ahead-logging-wal-protocol)
    - [4.10.4 Intermediate Update Recovery Strategies](#4104-intermediate-update-recovery-strategies)
    - [4.10.5 Shadow Paging Technique](#4105-shadow-paging-technique)
    - [4.10.6 Checkpointing & Log Recovery Algorithm](#4106-checkpointing--log-recovery-algorithm)
    - [4.10.7 Comprehensive Worked Log Trace Problem](#4107-comprehensive-worked-log-trace-problem)
  - [4.11 High-Probability Exam Questions & Student Pitfalls](#411-high-probability-exam-questions--student-pitfalls)

- [UNIT 5: Client/Server Databases, Security, and Repositories](#unit-5-clientserver-databases-security-and-repositories)
  - [5.1 Client/Server Concepts and Architectures](#51-clientserver-concepts-and-architectures)
    - [5.1.1 Two-Tier Architecture ("Fat Client")](#511-two-tier-architecture-fat-client)
    - [5.1.2 Three-Tier Architecture ("Thin Client")](#512-three-tier-architecture-thin-client)
    - [5.1.3 Comprehensive Comparison: Two-Tier vs. Three-Tier](#513-comprehensive-comparison-two-tier-vs-three-tier)
    - [5.1.4 Client-Server Communication Protocols](#514-client-server-communication-protocols)
  - [5.2 Application Programming Interfaces (APIs): ODBC & JDBC](#52-application-programming-interfaces-apis-odbc--jdbc)
    - [5.2.1 Architecture of ODBC](#521-architecture-of-odbc)
    - [5.2.2 Architecture of JDBC & The Four Driver Types](#522-architecture-of-jdbc--the-four-driver-types)
    - [5.2.3 Complete JDBC Lifecycle & Fully Annotated Java Implementation](#523-complete-jdbc-lifecycle--fully-annotated-java-implementation)
  - [5.3 Database Integrity & Declarative Repositories](#53-database-integrity--declarative-repositories)
    - [5.3.1 Non-Procedural vs. Procedural Integrity Constraints](#531-non-procedural-vs-procedural-integrity-constraints)
    - [5.3.2 SQL ASSERTIONS](#532-sql-assertions)
  - [5.4 Database Security Mechanisms](#54-database-security-mechanisms)
    - [5.4.1 Discretionary Access Control (DAC)](#541-discretionary-access-control-dac)
    - [5.4.2 Mandatory Access Control (MAC) & The Bell-LaPadula Model](#542-mandatory-access-control-mac--the-bell-lapadula-model)
    - [5.4.3 Role-Based Access Control (RBAC)](#543-role-based-access-control-rbac)
    - [5.4.4 SQL Injection (SQLi) Attacks and Defense In-Depth](#544-sql-injection-sqli-attacks-and-defense-in-depth)
    - [5.4.5 Audit Trails & Database Encryption](#545-audit-trails--database-encryption)
  - [5.5 High-Probability Exam Questions & Student Pitfalls](#55-high-probability-exam-questions--student-pitfalls)

---


# UNIT 1: Introduction to Database Systems & Conceptual Data Modeling (ER & EER)

---

## 1.1 Overview of Database Management Systems (DBMS)

### 1.1.1 Foundational Definitions
A **Database** is a logically coherent, integrated collection of related data representing some aspect of the real world (often termed the *Mini-world* or *Universe of Discourse (UoD)*). Any changes in the mini-world are automatically reflected in the database.

A **Database Management System (DBMS)** is a complex, generalized software system that facilitates the processes of:
1. **Defining:** Specifying data types, structures, and constraints for the data to be stored (Metadata definition).
2. **Constructing:** The process of storing the data on a persistent storage medium controlled by the DBMS.
3. **Manipulating:** Querying to retrieve specific data, updating the database to reflect changes, and generating reports.
4. **Sharing:** Allowing multiple users and programs to access the database concurrently while guaranteeing consistency and isolation.
5. **Protecting & Maintaining:** System recovery from hardware/software crashes, security enforcement against unauthorized access, and database maintenance over long life cycles.

A **Database System** comprises the four-part ecosystem:
$$\text{Database System} = \text{Database} + \text{DBMS Software} + \text{Application Programs} + \text{Hardware/Users}$$

```
+-----------------------------------------------------------------------+
|                           DATABASE SYSTEM                             |
|                                                                       |
|  +--------------------+     +--------------------------------------+  |
|  |       USERS        | <-> |         APPLICATION PROGRAMS         |  |
|  +--------------------+     +--------------------------------------+  |
|                                                ^                      |
|                                                | SQL / Query API      |
|                                                v                      |
|  +-----------------------------------------------------------------+  |
|  |                 DATABASE MANAGEMENT SYSTEM (DBMS)               |  |
|  |  +---------------------+   +---------------------------------+  |  |
|  |  |   Query Processor   |   |         Storage Manager         |  |  |
|  |  +---------------------+   +---------------------------------+  |  |
|  +-----------------------------------------------------------------+  |
|                                                ^                      |
|                                                | Disk I/O             |
|                                                v                      |
|  +-----------------------------------------------------------------+  |
|  |                          PHYSICAL STORAGE                       |  |
|  |  [ Data Files ]    [ System Catalog / Metadata ]    [ Log Files ]| |
|  +-----------------------------------------------------------------+  |
+-----------------------------------------------------------------------+
```

### 1.1.2 The Self-Describing Nature of a Database System
A fundamental characteristic distinguishing a DBMS from traditional file-processing software is that a database system contains not only the database itself, but also a complete definition or description of the database structure and constraints. 
This definition is stored in the DBMS **System Catalog** (or **Data Dictionary**), which contains **Metadata** ("data about data"). 

In traditional file processing, data structures are embedded inside individual application program code (e.g., C struct declarations or COBOL record definitions). If a single field size changes, every program accessing that file must be manually rewritten, recompiled, and retested. In a DBMS, catalog-driven architecture enables generic query processing software to access any database without recompiling application binaries.

---

## 1.2 Database System vs. File-Processing System

To appreciate why database management systems superseded traditional operating system file processing, consider an enterprise (e.g., a banking or university system) using flat files managed directly by OS file utilities.

### 1.2.1 Deep Breakdown of the 10 Major Deficiencies of File Systems

1. **Data Redundancy and Inconsistency:**
   - *File System:* Different departments maintain their own files. For instance, the University Registrar records a student's address in `STUDENT_ACADEMIC.dat`, while the Accounts Department records the same address in `STUDENT_FEES.dat`. When a student moves, updating one file but forgetting the other leads to data inconsistency where multiple conflicting copies exist.
   - *DBMS:* Data is logically centralized. Redundancy is controlled and minimized through normalization. If redundancy is intentionally maintained for performance (e.g., denormalization or materialized views), the DBMS ensures that updates propagate automatically to preserve consistency.

2. **Data Isolation and Structural Incompatibility:**
   - *File System:* Because data is scattered across multiple files created by different programmers at different times, files may be formatted in incompatible formats (e.g., CSV, fixed-width binary, custom delimited records). Writing an ad-hoc query spanning three files requires writing a custom procedural program to parse three distinct parsing algorithms.
   - *DBMS:* Uniform data representation governed by a formal data model (such as the Relational Model). Data is queried declaratively using SQL without manual file deserialization.

3. **Difficulty in Accessing Data (Lack of Ad-Hoc Query Capability):**
   - *File System:* Conventional file-processing environments do not provide a declarative query language. If the Dean requests: *"Find all computer science majors with a GPA > 3.8 living in zip code 110001"*, an engineer must write, compile, and execute an entire C/C++ or Java program.
   - *DBMS:* The same query requires a single declarative SQL statement:
     ```sql
     SELECT student_id, name 
     FROM Student 
     WHERE major = 'Computer Science' 
       AND gpa > 3.8 
       AND zip_code = '110001';
     ```
     The query optimizer automatically chooses the most efficient access path (e.g., index scan vs. sequential table scan).

4. **Integrity Problems and Constraint Enforcement:**
   - *File System:* Integrity constraints (e.g., `balance >= 0`, `age BETWEEN 18 AND 65`) must be hardcoded inside every application program that writes to the file. If a new application is written and forgets to include this validation check, corrupted data enters the storage. Modifying a constraint requires updating dozens of source code files.
   - *DBMS:* Constraints are declared centrally in the schema via DDL (`CHECK (balance >= 0)`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`). The DBMS execution engine enforces these constraints globally across all transactions, regardless of which user or application initiates the modification.

5. **Atomicity Problems:**
   - *File System:* A financial funds transfer requires two operations: debiting Account A by $500 and crediting Account B by $500. If the system crashes or power fails after the debit but before the credit, the system state is corrupted ($500 vanished). Restoring state in a raw file requires manual file inspection and custom audit scripts.
   - *DBMS:* The transaction management subsystem guarantees **Atomicity** via Write-Ahead Logging (WAL). Either all operations of the transaction complete successfully, or all intermediate modifications are completely undone (aborted/rolled back) via recovery logs.

6. **Concurrent Access Anomalies:**
   - *File System:* To allow multiple users to update files simultaneously, operating systems provide file-level locks. If two programs lock different files simultaneously, deadlocks occur. If OS locks are not used, race conditions cause the **Lost Update Problem** (e.g., two bank clerks simultaneously reading a $1000 balance and writing back $1100 and $1200, resulting in one deposit vanishing).
   - *DBMS:* Fine-grained concurrency control algorithms (e.g., Strict Two-Phase Locking, Multi-Version Concurrency Control) operate at the level of individual pages or rows, allowing hundreds of concurrent readers and writers without data corruption.

7. **Security and Access Control Problems:**
   - *File System:* OS-level security operates coarsely via file permissions (`read`, `write`, `execute` assigned to users or groups). An enterprise cannot easily grant a payroll clerk access to view employee names and departments without also revealing their base salaries if all fields reside in the same file record.
   - *DBMS:* Granular Discretionary Access Control (DAC) and Role-Based Access Control (RBAC). The DBMS can grant read permissions on specific columns, define parameterized views, or restrict access based on content:
     ```sql
     GRANT SELECT (emp_id, emp_name, department) ON Employee TO PayrollClerk;
     ```

8. **Crash Recovery and Durability:**
   - *File System:* File recovery relies on periodic disk backups (e.g., nightly tape dumps). Updates committed between the last backup and the crash are permanently lost.
   - *DBMS:* The recovery manager utilizes non-volatile redo/undo log records and checkpointing algorithms to reconstruct the exact committed state up to the millisecond preceding the failure, ensuring **Durability**.

9. **Program-Data Dependence:**
   - *File System:* The physical storage format (record structure, field lengths, offsets, byte alignment) is hard-coded into application programs. Changing an integer field from 16-bit to 32-bit breaks binary compatibility and mandates recompilation of all client applications.
   - *DBMS:* **Data Independence** decouples application logic from internal physical storage structures. Altering physical indexes or internal layouts does not require altering application queries.

10. **Transaction Management & ACID Guarantees:**
    - *File System:* No built-in concept of a transaction. The programmer must manually implement concurrency locks, rollbacks, validation, and durability.
    - *DBMS:* Full native hardware-level and architectural support for the **ACID** properties (Atomicity, Consistency, Isolation, Durability).

### 1.2.2 Comprehensive Comparison Matrix

| Architectural Feature | File-Processing System | Database Management System (DBMS) |
| :--- | :--- | :--- |
| **Data Redundancy** | High; duplicated across distinct department files. | Minimized and systematically controlled via normalization. |
| **Data Consistency** | Low; uncoordinated updates cause divergence. | High; centralized updates and integrity triggers. |
| **Data Independence** | Absent; tight coupling between code and record layout. | High; two-tier (Physical and Logical) data independence. |
| **Ad-Hoc Querying** | Impossible; requires writing new custom programs. | Built-in via declarative query languages (SQL). |
| **Access Control** | Coarse; OS file-level permissions (Read/Write/Execute). | Fine-grained; column, row, and view-level authorization. |
| **Concurrency Control** | Absent or crude file-level locking; prone to lost updates. | Sophisticated; row-level locks, 2PL, MVCC, serializability. |
| **Crash Recovery** | Manual recovery from periodic backups; data loss common. | Automated WAL, checkpointing, and roll-forward recovery. |
| **Integrity Enforcement** | Application-dependent; easily bypassed by new code. | Centralized schema-level constraints enforced globally. |
| **Cost & Complexity** | Low initial cost; leverages existing OS utilities. | Higher initial software licensing, hardware, and DBA costs. |
| **Data Abstraction** | None; programs deal directly with byte streams/offsets. | Multi-level abstraction (Physical, Conceptual, External). |

---

## 1.3 Database System Concepts and Three-Schema Architecture (ANSI/SPARC)

To provide data independence, simplify user interactions, and secure internal physical details, the ANSI/X3/SPARC study group defined the **Three-Schema Architecture** (also known as the Three-Level Architecture).

```
===================================================================================
                             EXTERNAL LEVEL (User Views)
   +-------------------+      +-------------------+      +-------------------+
   |   External View 1 |      |   External View 2 |      |   External View n |
   |  (e.g., Registrar)|      |   (e.g., Finance) |      |   (e.g., Student) |
   +-------------------+      +-------------------+      +-------------------+
              \                         |                         /
               \                        |                        /
    ===============================================================================
                     EXTERNAL / CONCEPTUAL MAPPING (Transforms Queries)
    ===============================================================================
                                        |
                                        v
   +-----------------------------------------------------------------------------+
   |                              CONCEPTUAL LEVEL                               |
   |   Conceptual Schema (Logical Entities, Attributes, Relationships, Types)    |
   |   e.g., Student(RollNo, Name, Dept, CGPA), Course(CID, Title, Credits)      |
   +-----------------------------------------------------------------------------+
                                        |
    ===============================================================================
                     CONCEPTUAL / INTERNAL MAPPING (Storage Mapping)
    ===============================================================================
                                        |
                                        v
   +-----------------------------------------------------------------------------+
   |                               INTERNAL LEVEL                                |
   |   Internal Schema (Physical Record Layouts, Offsets, B+ Trees, Hashing)      |
   |   e.g., Records stored on Page Blocks, RollNo indexed via B+ Tree           |
   +-----------------------------------------------------------------------------+
                                        |
                                        v
                           +-------------------------+
                           |    PHYSICAL DATABASE    |
                           |   (Storage Media/Disk)  |
                           +-------------------------+
===================================================================================
```

### 1.3.1 The Three Levels of Abstraction

1. **Internal Level (Physical Schema):**
   - Describes the physical storage structure of the database.
   - Employs a physical data model to define record formats, field byte allocations, compression techniques, block organization on disks, access paths, and indexing structures (e.g., $B^+$ Trees, Hash buckets, Ordered Index Files).
   - Purpose: Optimize disk I/O, reduce storage footprint, and accelerate retrieval speeds.

2. **Conceptual Level (Logical Schema):**
   - Describes the logical structure of the entire database for the entire community of users, concealing internal physical storage details.
   - Specifies entities, data types, relationships, constraints, and business rules.
   - Implemented using a logical data model (most commonly the Relational Data Model, representing data as collections of normalized relations/tables).
   - Ignores details such as record offsets, memory pointers, or index allocations.

3. **External Level (View Schema):**
   - Describes the part of the database that a specific user group or application is interested in, concealing the remainder of the database.
   - A single database supports multiple distinct external views.
   - Provides security (hiding sensitive columns like salary or medical history) and cognitive simplification (tailoring field names or aggregated metrics to user expectations).

### 1.3.2 Schema Mappings and Request Transformation
The true power of the three-schema architecture lies in the **Mappings** between levels:
- **External/Conceptual Mapping:** Translates a query expressed on a specific external view into an equivalent query on the global conceptual schema.
- **Conceptual/Internal Mapping:** Translates the conceptual operation into physical disk block read/write operations, utilizing internal record layouts and index access paths.

When data is requested:
$$\text{User Query (External)} \xrightarrow{\text{Ext/Conc Mapping}} \text{Conceptual Query} \xrightarrow{\text{Conc/Int Mapping}} \text{Physical Disk Blocks}$$

---

## 1.4 Data Independence

**Data Independence** is the capacity to modify a schema definition at one level of the database system without necessitating modifications to the schema definitions at the next higher level or rewriting application programs.

```
       +-------------------------------------------------------+
       |             External Schemas / Applications           |
       +-------------------------------------------------------+
                                   ^
                                   |  <-- LOGICAL DATA INDEPENDENCE
       +-------------------------------------------------------+
       |                   Conceptual Schema                   |
       +-------------------------------------------------------+
                                   ^
                                   |  <-- PHYSICAL DATA INDEPENDENCE
       +-------------------------------------------------------+
       |                    Internal Schema                    |
       +-------------------------------------------------------+
```

### 1.4.1 Physical Data Independence
- **Definition:** The capacity to modify the internal schema without requiring changes to the conceptual schema, external schemas, or existing application programs.
- **Modifications at the Internal Level Include:**
  - Creating new secondary access paths (e.g., adding a $B^+$ tree index on `Employee(Salary)`).
  - Switching file organization techniques (e.g., switching from unordered heap files to hash partitioning).
  - Reorganizing disk block allocations, upgrading storage hardware (e.g., migrating from HDD to NVMe SSD arrays), or enabling page-level compression.
- **Mechanism:** Only the *Conceptual/Internal Mapping* must be rewritten by the DBMS. The conceptual schema and external queries remain untouched.

### 1.4.2 Logical Data Independence
- **Definition:** The capacity to modify the conceptual schema without requiring changes to external schemas or existing application programs.
- **Modifications at the Conceptual Level Include:**
  - Adding a new entity type or relationship.
  - Adding new attributes to an existing relation (e.g., adding `MiddleName` to `Student`).
  - Splitting an existing table into two normalized tables (e.g., decomposing `Employee(EmpID, Name, DeptName, DeptLocation)` into `Employee(EmpID, Name, DeptID)` and `Department(DeptID, DeptName, DeptLocation)`).
- **Mechanism:** The *External/Conceptual Mapping* is updated. By constructing views that mimic the old schema structure (e.g., defining a view named `Employee` that joins the newly decomposed tables), existing application queries continue executing without modification.

### 1.4.3 Critical Comparison: Why Logical Independence is Harder
Logical data independence is far more challenging to achieve than physical data independence. 
- *Physical Independence:* Conceptual schemas describe data abstractly; physical alterations merely change performance access paths. Queries still receive the exact same logical inputs and produce identical logical outputs.
- *Logical Independence:* Conceptual schema changes directly alter the structural definition of the mini-world. While additions (new attributes) are easily masked through projection views, structural decompositions (such as splitting tables or altering relationship cardinalities) frequently restrict view updateability (e.g., views with outer joins or multi-table projections cannot always accept `INSERT` or `UPDATE` statements). Thus, application programs performing data modifications often require refactoring.

---

## 1.5 Data Models

A **Data Model** is an integrated collection of conceptual tools for describing:
1. **Data Structures:** The structural elements used to represent data (e.g., tables, records, trees, graphs).
2. **Operations:** The formal operations allowed on these structures (e.g., retrieval, projections, joins, pointer traversals).
3. **Integrity Constraints:** Rules ensuring valid states (e.g., domain constraints, referential integrity).

### 1.5.1 Relational Data Model
- **Core Abstraction:** Data is organized into two-dimensional tables termed **Relations**. Each row is a **Tuple**, and each column is an **Attribute**.
- **Underlying Theory:** Grounded in First-Order Predicate Logic and Set Theory (developed by Dr. E.F. Codd in 1970).
- **Key Traits:** High physical data independence, declarative query processing via SQL, mathematical foundations in Relational Algebra and Relational Calculus.

### 1.5.2 Hierarchical Data Model
- **Core Abstraction:** Data is represented as a tree-structured collection of records connected by one-to-many ($1:N$) **Parent-Child Relationships (PCRs)**.
- **Pioneering Implementation:** IBM's IMS (Information Management System).
- **Structural Constraints:**
  - A tree has a single root record type.
  - Every child record can have **exactly one parent record**.
  - Efficient for strict hierarchies (e.g., `Company` $\to$ `Division` $\to$ `Department` $\to$ `Employee`).
- **Fatal Weaknesses:**
  - Cannot naturally model many-to-many ($M:N$) relationships (e.g., `Student` and `Course`). To simulate $M:N$, child records must be duplicated across multiple parent trees, creating massive data redundancy.
  - Deleting a parent node cascades to delete all child records (e.g., deleting a department automatically destroys all assigned employee records).
  - Navigation is entirely procedural (pointers like `GET UNIQUE`, `GET NEXT WITHIN PARENT`).

```
Hierarchical Tree:
                [ UNIVERSITY ]
                 /          \
       [ DEPARTMENT ]    [ ATHLETICS ]
          /        \
    [ PROFESSOR ] [ STUDENT ]
```

### 1.5.3 Network Data Model
- **Core Abstraction:** Data is organized as arbitrary graphs of records connected by **Set Types** (governed by the CODASYL DBTG standard).
- **Structural Concepts:**
  - A set type represents a $1:N$ relationship consisting of one **Owner** record type and one or more **Member** record types.
  - A member record can belong to multiple distinct set types (unlike the hierarchical model), allowing direct representation of directed graphs.
  - To model an $M:N$ relationship between `STUDENT` and `COURSE`, a dummy intermediary record type (termed an *Intersection Record* or *Junction Record*, e.g., `ENROLLMENT`) is created with two $1:N$ sets: `STUDENT-ENROLLMENT` and `COURSE-ENROLLMENT`.
- **Fatal Weaknesses:**
  - Querying requires low-level procedural pointer navigation (`FIND FIRST`, `FIND NEXT`).
  - Pointers (embedded linked lists or ring structures) are tightly bound to disk representations, destroying data independence.

```
Network Graph:
    [ STORE ] <===================> [ SUPPLIER ]
        \                                /
      (Set A)                         (Set B)
          \                             /
           v                           v
             [ PRODUCT_INVENTORY_LINK ]
```

### 1.5.4 Object-Oriented / Object-Relational Data Model
- **Core Abstraction:** Merges traditional database capabilities with object-oriented programming language paradigms (C++, Smalltalk, Java).
- **Core Concepts:**
  - **Object Identity (OID):** Every object has a system-generated, immutable, unique identifier independent of its attribute values.
  - **Encapsulation:** Objects encapsulate both state (attributes) and behavior (methods/functions).
  - **Complex Types:** Direct support for structured types (nested collections, arrays, multisets, lists) without forcing First Normal Form (1NF) atomicity.
  - **Inheritance:** Class hierarchies with attribute and method inheritance (polymorphism).
- **Object-Relational DBMS (ORDBMS):** Extends traditional relational engines with user-defined types (UDTs), table inheritance, and array columns (e.g., PostgreSQL, Oracle Database).

### 1.5.5 Comprehensive 4-Way Data Model Comparison Matrix

| Feature / Dimension | Relational Model | Hierarchical Model | Network Model | Object-Oriented Model |
| :--- | :--- | :--- | :--- | :--- |
| **Basic Data Structure** | 2D Tables (Relations) | Inverted Trees (Hierarchies) | Arbitrary Graphs (Sets) | Objects with Class Hierarchies |
| **Relationship Mechanism** | Foreign Keys (Value-based) | Physical Parent-Child Pointers | CODASYL Sets (Owner-Member links) | Object References (OIDs) |
| **M:N Relationship Support** | Natural (via Junction Table) | Difficult (Requires Duplication) | Supported (via Link Records) | Natural (via Object References) |
| **Query Mechanism** | Declarative (SQL, Relational Algebra) | Procedural (Tree Traversal) | Procedural (Pointer Navigation) | Object Query Language (OQL) / Method Calls |
| **Data Independence** | Very High | Low | Low | Moderate to High |
| **Mathematical Basis** | Relational Calculus & Set Theory | Graph/Tree Theory | Graph Theory | Object-Oriented Type Theory |
| **Industry Status** | Dominant standard (RDBMS/ORDBMS) | Legacy (Mainframe banking/IMS) | Legacy (CODASYL systems) | Niche/Specialized (CAD, Multimedia, GIS) |

---

## 1.6 Database Schemas, Instances, and Database State

### 1.6.1 Schema (Intension)
- The **Database Schema** is the overall structural design, description, and metadata of the database, declared during database design.
- It changes very infrequently.
- Corresponds to the *intension* in formal logic.
- *Analogy:* The variable type declaration in programming languages (e.g., `struct Student { int roll_no; char name[50]; };`).

### 1.6.2 Instance / State (Extension)
- The **Database Instance** (or **Database State**) is the actual collection of data populated in the database at a specific snapshot in time.
- It changes continuously as records are inserted, modified, or deleted.
- Corresponds to the *extension* in formal logic.
- *Analogy:* The runtime value stored in that struct at execution step $t_k$.

### 1.6.3 Valid State
A database state is considered **Valid** if and only if it satisfies all structural and semantic integrity constraints specified in the database schema (e.g., primary key uniqueness, foreign key validity, domain checks). The primary duty of the DBMS is to guarantee that the database transitions strictly from one valid state to another valid state.

---

## 1.7 Database Languages and Interfaces

A comprehensive DBMS provides specialized sub-languages to interact with different architectural layers.

```
+-----------------------------------------------------------------------------------+
|                            DATABASE LANGUAGES (SQL)                              |
+---------------------+---------------------+------------------+--------------------+
|         DDL         |         DML         |       DCL        |        TCL         |
|  (Data Definition)  |(Data Manipulation)  |  (Data Control)  |(Transaction Control)|
+---------------------+---------------------+------------------+--------------------+
| CREATE              | SELECT              | GRANT            | COMMIT             |
| ALTER               | INSERT              | REVOKE           | ROLLBACK           |
| DROP                | UPDATE              |                  | SAVEPOINT          |
| TRUNCATE            | DELETE              |                  | SET TRANSACTION    |
+---------------------+---------------------+------------------+--------------------+
```

### 1.7.1 Data Definition Language (DDL)
- Used by the DBA and database designers to specify the conceptual and external database schemas.
- The output of the DDL compiler is a set of internal system tables stored in the **System Catalog** (Metadata).
- Modern commercial systems also incorporate:
  - **Storage Definition Language (SDL):** Specifies the internal storage schema, block layout, and indexing parameters.
  - **View Definition Language (VDL):** Specifies user views and mappings to the conceptual schema. In SQL, DDL, SDL, and VDL are unified under a single syntax.

### 1.7.2 Data Manipulation Language (DML)
Used for data retrieval, insertion, deletion, and modification.
1. **High-Level / Non-Procedural (Declarative) DML:**
   - The user specifies *what* data is required without specifying *how* to retrieve it.
   - Example: SQL (`SELECT * FROM Student WHERE gpa > 3.5`).
   - The DBMS query optimizer determines the execution plan. Operates on sets of records (set-at-a-time).
2. **Low-Level / Procedural DML:**
   - The user specifies *what* data is required and *how* to navigate through the storage structures step-by-step.
   - Must be embedded in a general-purpose host programming language. Operates on individual records (record-at-a-time). Examples: CODASYL DML, IMS DL/1.

### 1.7.3 Data Control Language (DCL)
Manages user privileges, authorization tokens, and security enforcement:
- `GRANT`: Bestows specific permissions on database objects to users or roles.
- `REVOKE`: Withdraws previously assigned permissions.

### 1.7.4 Transaction Control Language (TCL)
Manages atomic transactions within the database engine:
- `COMMIT`: Permanently saves the current transaction's operations to disk.
- `ROLLBACK`: Discards the current transaction's uncommitted operations, restoring previous state.
- `SAVEPOINT`: Marks an intermediate checkpoint within a transaction for selective partial rollbacks.

### 1.7.5 DBMS User Interfaces
1. **Menu-Based Interfaces:** Geared towards naive end-users (e.g., bank tellers, web forms).
2. **Form-Based Interfaces:** Display structured forms for data entry, insertion, and querying.
3. **Graphical User Interfaces (GUIs):** Present schemas as diagrams allowing visual query construction (e.g., pgAdmin, MySQL Workbench).
4. **Natural Language Interfaces:** Accept queries in pseudo-English and map them onto SQL statements.
5. **DBA Interfaces:** Specialized privileged consoles for allocating tablespaces, tuning memory pools, managing transaction logs, and initiating online backups.

---

## 1.8 Overall Database System Structure (Architectural Blueprint)

The internal architecture of a modern relational DBMS is partitioned into two major functional divisions: the **Query Processor** and the **Storage Manager**, operating over **Physical Disk Storage**.

```
+---------------------------------------------------------------------------------------+
|                                    USER TAXONOMY                                      |
|  [ Naive Users ]     [ Application Programmers ]  [ Sophisticated Users ]   [ DBA ]   |
|   (Web Forms)           (Host Code / APIs)         (Ad-hoc SQL Analysts)  (Admin Tools)|
+-------+-------------------------+-------------------------+--------------------+------+
        |                         |                         |                    |
        v                         v                         v                    v
+---------------------------------------------------------------------------------------+
|                                    QUERY PROCESSOR                                    |
|                                                                                       |
|   +-----------------------+     +--------------------+     +---------------------+    |
|   |    DDL Interpreter    |     |    DML Compiler    |     | Embedded DML Pre-   |    |
|   | (Processes Schema DDL)|     |  (Parses & Types)  |     | compiler (Host APIs)|    |
|   +-----------+-----------+     +---------+----------+     +----------+----------+    |
|               |                           |                           |               |
|               v                           v                           v               |
|   +------------------------------------------------------------------------------+    |
|   |                              QUERY OPTIMIZER                                 |    |
|   |  - Generates Execution Plans                                                 |    |
|   |  - Cost-Based Evaluation (CPU cost, I/O cost, Index scans vs Table scans)    |    |
|   +---------------------------------------+--------------------------------------+    |
|                                           |                                           |
|                                           v                                           |
|   +------------------------------------------------------------------------------+    |
|   |                           QUERY EXECUTION ENGINE                             |    |
|   |  - Executes physical relational operators (Hash Join, Index Scan, Filter)   |    |
|   +---------------------------------------+--------------------------------------+    |
+-------------------------------------------|-------------------------------------------+
                                            | Evaluates Plan
                                            v
+---------------------------------------------------------------------------------------+
|                                    STORAGE MANAGER                                    |
|                                                                                       |
|   +-------------------------------------+   +-------------------------------------+   |
|   |  AUTHORIZATION & INTEGRITY MANAGER  |   |         TRANSACTION MANAGER         |   |
|   |  - Verifies user permissions        |   |  - Enforces ACID properties         |   |
|   |  - Validates integrity constraints  |   |  - Coordinates Commit / Rollback    |   |
|   +------------------+------------------+   +------------------+------------------+   |
|                      |                                         |                      |
|                      v                                         v                      |
|   +-------------------------------------+   +-------------------------------------+   |
|   |             FILE MANAGER            |   |            LOCK MANAGER             |   |
|   |  - Manages file allocation on disk  |   |  - Manages concurrency locks (S/X)  |   |
|   |  - Page structure & block layout    |   |  - Deadlock detection               |   |
|   +------------------+------------------+   +------------------+------------------+   |
|                      |                                         |                      |
|                      +--------------------+--------------------+                      |
|                                           |                                           |
|                                           v                                           |
|   +------------------------------------------------------------------------------+    |
|   |                                BUFFER MANAGER                                |    |
|   |  - Fetches disk blocks into memory frames (Buffer Pool)                      |    |
|   |  - Page replacement policies (LRU, Clock)                                    |    |
|   |  - Manages Dirty Pages & Write-Ahead Logging (WAL)                           |    |
|   +---------------------------------------+--------------------------------------+    |
+-------------------------------------------|-------------------------------------------+
                                            | Direct Disk I/O
                                            v
+---------------------------------------------------------------------------------------+
|                                 PHYSICAL DISK STORAGE                                 |
|                                                                                       |
|   +------------------+  +------------------+  +------------------+  +---------------+ |
|   |    Data Files    |  |  Data Dictionary |  |     Indices      |  | Recovery Logs | |
|   | (Raw Relations)  |  | (System Catalog) |  |   (B+ Trees,     |  | (WAL Redo/Undo| |
|   |                  |  |                  |  |    Hash Files)   |  |   Records)    | |
|   +------------------+  +------------------+  +------------------+  +---------------+ |
+---------------------------------------------------------------------------------------+
```

### 1.8.1 Deep Dive: Query Processor Components
1. **DDL Interpreter:** Parses DDL statements (`CREATE`, `ALTER`, `DROP`), executes them, and writes the resulting metadata directly into the system catalog.
2. **DML Compiler & Parser:** Analyzes SQL DML statements, performs syntactic validation, checks semantics against the data dictionary (verifying table names and column types), and converts the declarative SQL into an internal algebraic representation (Relational Algebra Tree).
3. **Query Optimizer:** Evaluates multiple algebraically equivalent execution plans for a given query. It estimates execution costs based on catalog statistics (e.g., number of tuples, block count, index selectivity) and outputs the lowest-cost physical execution plan.
4. **Query Execution Engine:** Interprets the execution plan, coordinating low-level requests to the Storage Manager to fetch, filter, sort, and join tuples.

### 1.8.2 Deep Dive: Storage Manager Components
1. **Authorization and Integrity Manager:** Verifies that the querying user has the requisite security privileges and ensures that incoming data modifications do not violate schema integrity rules.
2. **Transaction Manager:** Coordinates the execution of transactions, ensuring atomicity and durability via transaction state tracking.
3. **Lock Manager:** Implements concurrency control algorithms (such as Strict 2PL), granting, tracking, and releasing Shared ($S$) and Exclusive ($X$) locks on data items to prevent race conditions.
4. **Buffer Manager:** Controls the allocation of memory cache (the *Buffer Pool*). When a page is needed, the buffer manager checks if it resides in RAM; if not, it reads the page from disk, evicting an existing page using replacement policies (e.g., LRU - Least Recently Used). It manages *Dirty Pages* (pages modified in memory) and enforces the WAL rule before flushing blocks to disk.
5. **File Manager:** Manages the allocation of disk space for relations, allocating blocks and managing data structures used to represent files and records on disk.

---

## 1.9 Data Modeling Using the Entity-Relationship (ER) Model

The **Entity-Relationship (ER) Model** is a high-level conceptual data model developed by Dr. Peter Chen (1976). It allows database designers to conceptualize the structural requirements of the universe of discourse independently of any physical DBMS implementation.

### 1.9.1 Core Elements: Entities and Entity Sets
- **Entity:** An object that exists in the real world and is distinguishable from other objects (e.g., a specific student named *"Rahul Sharma"*, a specific car with VIN *"1HGCR2..."*).
- **Entity Set:** A collection of all entities of the same type that share the same attributes (e.g., the set of all students in a university).
- **Entity Type:** The schema or definition that describes the structure of entities in an entity set.

```
Chen ER Notation:
  +------------------+
  |      ENTITY      |     (Represented by a Rectangle)
  +------------------+
```

### 1.9.2 Strong vs. Weak Entity Sets
1. **Strong Entity Set:**
   - Possesses a **Primary Key** composed entirely of its own attributes.
   - Its existence does not depend on any other entity in the database.
   - Represented by a **Single Rectangle**.
2. **Weak Entity Set:**
   - Does not possess sufficient attributes to form a primary key of its own.
   - **Existence Dependent:** Cannot exist without an associated **Identifying (Owner) Entity Set**.
   - Identifies its tuples via a **Partial Key (Discriminator)** in combination with the primary key of its owner entity.
   - Connected to the owner via an **Identifying Relationship Set**.
   - Must have **Total Participation** in the identifying relationship.
   - Represented by a **Double Rectangle**, with its identifying relationship represented by a **Double Diamond**, and its partial key underlined with a **Dashed Line**.

*Concrete Weak Entity Example:*
A `DEPENDENT` entity set (tracking an employee's spouse and children for medical coverage) cannot exist without an `EMPLOYEE`. 
- Owner Entity: `EMPLOYEE(EmpID, Name, Salary)`
- Weak Entity: `DEPENDENT(DepName, Relationship, DOB)`
- Identifying Relationship: `HAS_DEPENDENT`
- Primary Key of Dependent: `{EMPLOYEE.EmpID, DEPENDENT.DepName}`.

```
+------------+               [ Identifying Rel ]               ||================||
|  EMPLOYEE  |---------------<  HAS_DEPENDENT  >===============||   DEPENDENT    ||
+------------+               [                 ]               ||================||
 (EmpID [PK])                                                    (DepName [PartKey])
```

### 1.9.3 Classification of Attributes
Attributes are the descriptive properties possessed by each entity in an entity set.

```
               +-------------------------------------------------+
               |              ATTRIBUTE CLASSIFICATIONS          |
               +-----------------------+-------------------------+
                                       |
    +----------------------------------+----------------------------------+
    |                                  |                                  |
    v                                  v                                  v
+-----------------------+   +-----------------------+   +-----------------------+
|  Simple vs Composite  |   | Single vs Multi-valued|   |   Stored vs Derived   |
+-----------------------+   +-----------------------+   +-----------------------+
| Simple: Atomic        |   | Single: One value     |   | Stored: Persisted     |
| (e.g., Age, RollNo)   |   | (e.g., SSN, Gender)   |   | (e.g., DateOfBirth)   |
| Composite: Hierarchical|  | Multi: Set of values  |   | Derived: Computed     |
| (e.g., Name -> F, M, L|   | (e.g., PhoneNumbers,  |   | (e.g., Age = NOW - DOB|
|  Address -> St, City) |   |  Degrees)             |   |  represented dashed)  |
+-----------------------+   +-----------------------+   +-----------------------+
```

1. **Simple (Atomic) vs. Composite:**
   - *Simple:* Cannot be divided into subparts (e.g., `Salary`, `RollNo`).
   - *Composite:* Can be divided into smaller subparts that represent basic independent attributes (e.g., `Name` divided into `FirstName`, `MiddleName`, `LastName`; `Address` divided into `StreetAddress`, `City`, `State`, `Pincode`).
2. **Single-Valued vs. Multi-Valued:**
   - *Single-Valued:* Holds exactly one value for a given entity instance (e.g., `DateOfBirth`, `SSN`).
   - *Multi-Valued:* Holds a set of values for a single entity instance (e.g., `CollegeDegree` for a professor who holds BSc, MSc, and PhD; `PhoneNumbers`). Represented by a **Double Oval**.
3. **Stored vs. Derived:**
   - *Stored:* Physically stored in the database files (e.g., `DateOfBirth`).
   - *Derived:* Computed dynamically on demand from stored attributes or system state (e.g., `Age` calculated as `CURRENT_DATE - DateOfBirth`; `TotalEmployees` in a department). Represented by a **Dashed Oval**.
4. **Null-Valued Attributes:**
   - Takes on a `NULL` value when an entity does not have a value for it (e.g., `ApartmentNumber` for a stand-alone house) or when the value is unknown/missing.

```
Chen ER Notation for Attributes:
       ( Attribute )             (( Multi-Valued ))            ((  Derived  ))
        Single Oval                 Double Oval                   Dashed Oval
```

### 1.9.4 Relationships, Relationship Sets, and Degree
- **Relationship:** An association among two or more distinct entities.
- **Relationship Set:** A set of relationships of the same type.
- **Degree of a Relationship:** The number of participating entity sets.
  1. **Unary (Recursive) Relationship (Degree 1):** The same entity set participates more than once in distinct roles.
     *Example:* An `EMPLOYEE` manages other `EMPLOYEE` entities (Roles: `Manager` and `Subordinate`).
  2. **Binary Relationship (Degree 2):** Connects two distinct entity sets (the most prevalent real-world form).
     *Example:* `STUDENT` enrolls in `COURSE`.
  3. **Ternary Relationship (Degree 3):** Simultaneously connects three distinct entity sets.
     *Example:* A `SUPPLIER` supplies a `PART` to a `PROJECT`. All three entities are simultaneously bound by the single transaction.
  4. **N-ary Relationship (Degree N):** Connects $N$ entity sets simultaneously.

```
Unary (Recursive):             Binary:                        Ternary:
  +------------+             +---------+     +--------+      +----------+   +------+
  |  EMPLOYEE  |             | STUDENT |<--->| COURSE |      | SUPPLIER |   | PART |
  +---+----+---+             +---------+     +--------+      +-----+----+   +---+--+
      |    |                      \             /                  \           /
[Manager] [Worker]                 \           /                    \         /
      \    /                    +-----------------+              +--------------+
     ( Manages )                |     ENROLLS     |              |   SUPPLIES   |
                                +-----------------+              +-------+------+
                                                                         |
                                                                   +-----+----+
                                                                   |  PROJECT |
                                                                   +----------+
```

### 1.9.5 Mapping Cardinalities (Cardinality Ratios)
Mapping cardinality defines the number of entity instances to which another entity instance can be associated via a relationship set. For a binary relationship between entity set $A$ and entity set $B$:

1. **One-to-One (1:1):**
   - An entity in $A$ is associated with at most one entity in $B$, and an entity in $B$ is associated with at most one entity in $A$.
   - *Example:* `DEPARTMENT` is managed by `HEAD_OF_DEPARTMENT`. Each department has one head, and a professor heads at most one department.

2. **One-to-Many (1:N):**
   - An entity in $A$ is associated with any number ($0, 1, \dots, N$) of entities in $B$. An entity in $B$ is associated with at most one entity in $A$.
   - *Example:* `DEPARTMENT` employs `EMPLOYEE`. A department employs multiple workers, but each worker belongs to exactly one department.

3. **Many-to-One (N:1):**
   - An entity in $A$ is associated with at most one entity in $B$. An entity in $B$ is associated with any number of entities in $A$.
   - *Example:* `STUDENT` belongs to `HOSTEL`. Many students live in one hostel, but a student resides in only one hostel.

4. **Many-to-Many (M:N):**
   - An entity in $A$ is associated with any number of entities in $B$, and an entity in $B$ is associated with any number of entities in $A$.
   - *Example:* `STUDENT` enrolls in `COURSE`. A student enrolls in many courses, and a course contains many students.

### 1.9.6 Participation Constraints: Total vs. Partial
- **Total Participation (Existence Dependency):**
  - Every entity in the entity set **must** participate in at least one relationship instance in the relationship set.
  - Represented by a **Double Line** connecting the entity set to the relationship diamond.
  - *Example:* Every `STUDENT` must be assigned to a `DEPARTMENT`. If a student exists, they cannot have a null department reference.
- **Partial Participation:**
  - Some entities in the entity set may not participate in the relationship.
  - Represented by a **Single Line**.
  - *Example:* Not every `EMPLOYEE` manages a `DEPARTMENT`. Most employees have no managerial association.

### 1.9.7 Min-Max Structural Constraints $(min, max)$
An alternative, mathematically rigorous notation replacing Chen's cardinalities and participation lines is the **$(min, max)$ Notation**.
A pair of integers $(min, max)$ is placed on the edge connecting entity $E$ to relationship $R$:
- $0 \le min \le max$ and $max \ge 1$.
- $min$ specifies the minimum number of relationship instances each entity in $E$ must participate in:
  - If $min = 0$: Participation is **Partial**.
  - If $min \ge 1$: Participation is **Total**.
- $max$ specifies the maximum number of relationship instances each entity in $E$ can participate in:
  - If $max = 1$: Entity can be bound to at most 1 partner.
  - If $max = N$ (or $\star$): Entity can be bound to unboundedly many partners.

*Example:*
$$\text{EMPLOYEE} \xrightarrow{(1, 1)} \text{WORKS\_FOR} \xleftarrow{(1, N)} \text{DEPARTMENT}$$
- An employee must participate in at least 1 and at most 1 `WORKS_FOR` relationship (total participation, single department).
- A department must have at least 1 employee and can have up to $N$ employees.

### 1.9.8 Comprehensive Taxonomy of Keys
A **Key** is an attribute or set of attributes that uniquely distinguishes individual entity instances within an entity set.

```
       +-------------------------------------------------------------+
       |                         SUPER KEY                           |
       |  Any set of attributes that uniquely identifies an entity   |
       |  (e.g., {SSN}, {SSN, Name}, {SSN, Email, Phone})            |
       |                                                             |
       |        +-------------------------------------------+        |
       |        |              CANDIDATE KEY                |        |
       |        |  Minimal Super Key (No proper subset is   |        |
       |        |  a super key)                             |        |
       |        |  (e.g., {SSN}, {Email})                   |        |
       |        |                                           |        |
       |        |      +-------------+  +-------------+     |        |
       |        |      | PRIMARY KEY |  |ALTERNATE KEY|     |        |
       |        |      |   {SSN}     |  |   {Email}   |     |        |
       |        |      +-------------+  +-------------+     |        |
       |        +-------------------------------------------+        |
       +-------------------------------------------------------------+
```

1. **Super Key:**
   - A set of one or more attributes whose combined values uniquely identify each entity in an entity set.
   - If $K$ is a super key, any superset $K \cup \{A\}$ is also a super key.
2. **Candidate Key:**
   - A **Minimal Super Key**. A candidate key $K$ has two properties:
     1. *Uniqueness:* No two distinct entities have identical values for $K$.
     2. *Minimality (Irreducibility):* If any attribute is removed from $K$, the remaining set ceases to be a super key.
3. **Primary Key:**
   - The candidate key selected by the database designer as the principal means of identifying entities within the entity set.
   - *Constraint:* **Must NEVER accept NULL values** (Entity Integrity Constraint) and must remain immutable over time.
4. **Alternate (Secondary) Key:**
   - Any candidate key that was not chosen as the primary key.
5. **Foreign Key:**
   - An attribute (or set of attributes) in one relation that references the primary key of another relation (or the same relation), enforcing **Referential Integrity**.

---

## 1.10 Extended / Enhanced ER (EER) Model Concepts

As database applications evolved into complex domains (CAD/CAM, GIS, software engineering), the standard ER model was extended with object-oriented abstractions.

### 1.10.1 Specialization and Generalization
- **Specialization (Top-Down Process):**
  - The process of defining a set of subclasses of an entity type (the superclass).
  - The superclass possesses common generalized attributes, while each subclass possesses specialized, distinguishing attributes and relationships.
  - *Example:* Superclass `EMPLOYEE` is specialized into subclasses `SECRETARY`, `ENGINEER`, and `TECHNICIAN`. `ENGINEER` has specialized attribute `EngineeringType`.
- **Generalization (Bottom-Up Process):**
  - The process of recognizing commonalities across multiple entity types and synthesizing them into a single, generalized superclass.
  - *Example:* Identifying common attributes between `CAR` and `TRUCK` (e.g., `VehicleID`, `Price`) and generalizing them into `VEHICLE`.

### 1.10.2 Constraints on Specialization and Generalization
Two independent dimensions of constraints govern any specialization hierarchy:

```
+---------------------------------------------------------------------------------------+
|                       SPECIALIZATION / GENERALIZATION CONSTRAINTS                     |
+-------------------------------------------+-------------------------------------------+
|         DISJOINTNESS CONSTRAINT           |          COMPLETENESS CONSTRAINT          |
|  (Can an entity belong to >1 subclass?)   | (Must a superclass belong to a subclass?) |
+-------------------------------------------+-------------------------------------------+
| Disjoint (d):                             | Total (Mandatory, Double Line):           |
| An entity can belong to AT MOST ONE       | Every entity in the superclass MUST belong|
| subclass.                                 | to at least one subclass.                 |
+-------------------------------------------+-------------------------------------------+
| Overlapping (o):                          | Partial (Optional, Single Line):          |
| An entity can belong to MULTIPLE          | An entity in the superclass DOES NOT have |
| subclasses simultaneously.                | to belong to any subclass.                |
+-------------------------------------------+-------------------------------------------+
```

This yields **Four Mutually Exclusive Structural Configurations**:
1. **Disjoint - Total ($d$, Total):** Every entity belongs to exactly one subclass.
   *Example:* An `ACCOUNT` must be either a `SAVINGS_ACCOUNT` or a `CHECKING_ACCOUNT`, and cannot be both.
2. **Disjoint - Partial ($d$, Partial):** An entity belongs to at most one subclass, or none at all.
   *Example:* An `EMPLOYEE` may be a `SALESPERSON` or an `ENGINEER`, but an administrator belongs to neither.
3. **Overlapping - Total ($o$, Total):** An entity must belong to at least one subclass and can belong to multiple.
   *Example:* A university `PERSON` must be either an `EMPLOYEE`, a `STUDENT`, or both.
4. **Overlapping - Partial ($o$, Partial):** An entity may belong to zero, one, or multiple subclasses.
   *Example:* A `PART` manufactured in a plant may be a `PURCHASED_PART`, a `MANUFACTURED_PART`, both, or neither.

### 1.10.3 Attribute and Relationship Inheritance
In a specialization hierarchy or lattice:
- A subclass inherits **all attributes** of its superclass.
- A subclass inherits **all relationship participations** of its superclass.
- In a **Specialization Lattice**, a subclass has more than one superclass (**Multiple Inheritance**).
  *Example:* `ENGINEERING_MANAGER` inherits attributes simultaneously from `ENGINEER` and `MANAGER`.

```
                  +--------------------------+
                  |         EMPLOYEE         |
                  |  (EmpID, Name, BaseSalary)
                  +--------------------------+
                               |
                               | (d, Total)
                               v
             +-----------------+-----------------+
             |                                   |
             v                                   v
  +----------------------+            +----------------------+
  |       ENGINEER       |            |       MANAGER        |
  |  (EngineeringDegree) |            |   (ManagementBonus)  |
  +----------------------+            +----------------------+
             \                                   /
              \                                 /
               v                               v
            +------------------------------------+
            |        ENGINEERING_MANAGER         |  <-- Multiple Inheritance (Lattice)
            |      (Specialized Projects)        |
            +------------------------------------+
```

### 1.10.4 Union Types / Category
- Standard specialization defines subclasses that share the *same* superclass.
- A **Category (or Union Type)** models a single subclass that represents a collection of objects that is a subset of the **UNION of distinct entity types**.
- *Example:* A vehicle `OWNER` can be a `PERSON`, a `BANK`, or a `COMPANY`.
  - Here, `OWNER` is a Category.
  - The superclasses (`PERSON`, `BANK`, `COMPANY`) have completely different primary keys and attribute structures.
  - A category can be **Total** (holds all entities from the union) or **Partial**.

### 1.10.5 Aggregation
- **Motivation:** In basic ER modeling, relationships cannot directly participate in other relationships; relationships only connect entities.
- **Aggregation** is an abstraction through which relationships are treated as higher-level entities.
- *Example:* A `DOCTOR` performs an `OPERATION` on a `PATIENT`. This ternary relationship forms an aggregated unit `TREATMENT`. Now, we want to record that a `NURSE` assists in this specific `TREATMENT`. Without aggregation, we would be forced into an unwieldy quaternary relationship. Aggregation wraps `(DOCTOR - OPERATION - PATIENT)` in a box and links it via a binary relationship `ASSISTS` to `NURSE`.

```
+----------------------------------------------------+
| AGGREGATION: TREATMENT                             |
|                                                    |
|  +--------+          +-----------+      +--------+ |
|  | DOCTOR |<-------->| OPERATION |<---->| PATIENT| |
|  +--------+          +-----------+      +--------+ |
+-------------------------+--------------------------+
                          ^
                          | (Assists)
                          v
                      +-------+
                      | NURSE |
                      +-------+
```

---

## 1.11 Reduction / Mapping of ER and EER Diagrams to Relational Tables

The formal transformation of an ER/EER conceptual model into a normalized Relational Database Schema follows a rigorous 10-step algorithm.

### Step 1: Mapping of Regular (Strong) Entity Sets
- For each strong entity set $E$ in the ER diagram, create a relation $R$ containing all the simple attributes of $E$.
- For composite attributes, flatten them by including only their simple component attributes.
- Choose one of the candidate keys of $E$ as the Primary Key of $R$: $\text{PK}(R) = \text{PK}(E)$.

### Step 2: Mapping of Weak Entity Sets
- For each weak entity set $W$ with owner entity set $E$, create a relation $R$.
- Include all simple attributes (and flattened components of composite attributes) of $W$.
- Include as a Foreign Key ($\text{FK}$) in $R$ the primary key attributes of the owner relation $E$.
- The Primary Key of $R$ is the composite combination of the owner primary key and the partial key (discriminator) of $W$:
  $$\text{PK}(R) = \{\text{PK}(E), \text{PartialKey}(W)\}$$

### Step 3: Mapping of Binary 1:1 Relationship Sets
For a binary 1:1 relationship $R$ connecting entity sets $S$ and $T$, choose one of three approaches:
1. **Foreign Key Approach (Preferred for Partial/Total asymmetries):**
   - Identify the entity that has **Total Participation** in $R$ (say $S$).
   - Include the primary key of $T$ as a Foreign Key in $S$: $\text{FK}(S) = \text{PK}(T)$.
   - Add any simple attributes of the relationship set $R$ directly into $S$.
   - *Why?* Placing the foreign key in the totally participating relation prevents unnecessary `NULL` values.
2. **Merged Relation Approach (Used when BOTH entities participate TOTALLY):**
   - If both $S$ and $T$ have total participation and do not participate in other relationships, merge $S$, $T$, and $R$ into a single unified relation.
3. **Cross-Reference (Relationship Table) Approach:**
   - Create a separate relation $R(\text{PK}_S, \text{PK}_T, \text{attributes})$.
   - Used when both participations are partial to avoid all nulls, though it incurs join overhead.

### Step 4: Mapping of Binary 1:N Relationship Sets
- For each binary 1:N relationship set $R$ connecting entity set $S$ (on the 1-side) and entity set $T$ (on the N-side):
  - Identify the relation $T$ representing the **N-side**.
  - Include the primary key of $S$ as a **Foreign Key** in $T$: $\text{FK}(T) = \text{PK}(S)$.
  - Include any attributes of the relationship set $R$ as attributes of $T$.
  - *Rule:* The foreign key **always migrates to the N-side**. Placing it on the 1-side violates First Normal Form by requiring a multi-valued array of foreign keys.

### Step 5: Mapping of Binary M:N Relationship Sets
- For each binary M:N relationship set $R$ connecting entity sets $S$ and $T$:
  - Create a **new relation** $R$ (a *Junction / Cross-Reference Table*).
  - Include the primary keys of both $S$ and $T$ as Foreign Keys in $R$.
  - The Primary Key of $R$ is the composite combination of both foreign keys:
    $$\text{PK}(R) = \{\text{PK}(S), \text{PK}(T)\}$$
  - Include any descriptive attributes of the relationship set $R$ in this new table.

### Step 6: Mapping of Multi-Valued Attributes
- For each multi-valued attribute $A$ of entity set $E$:
  - Create a **new relation** $R_A$.
  - Include attribute $A$ along with the primary key of $E$ as a Foreign Key referencing $E$.
  - The Primary Key of $R_A$ is the composite pair:
    $$\text{PK}(R_A) = \{\text{PK}(E), A\}$$

### Step 7: Mapping of N-ary Relationship Sets ($N > 2$)
- For each $N$-ary relationship set $R$ connecting entity sets $E_1, E_2, \dots, E_n$:
  - Create a new relation $R$.
  - Include the primary keys of all participating entity sets as foreign keys: $\text{FK}_1, \dots, \text{FK}_n$.
  - If the cardinality of all participating entities is many ($N$), the primary key is the composite combination of all foreign keys:
    $$\text{PK}(R) = \{\text{PK}(E_1), \text{PK}(E_2), \dots, \text{PK}(E_n)\}$$
  - If one entity participates with a maximum cardinality of 1, its foreign key alone forms the primary key.

### Step 8: Mapping of EER Specialization / Generalization
Four alternative strategies exist depending on constraints:
- **Option 8A: Multiple Relations for Superclass and Subclasses (Best for any constraint):**
  - Create a relation for the superclass $C$ with its attributes and $\text{PK}(C)$.
  - Create a relation for each subclass $S_i$ containing the specialized attributes of $S_i$ plus $\text{PK}(C)$ as both the **Primary Key and Foreign Key** referencing $C$.
- **Option 8B: Subclass Relations Only (Valid ONLY for Total Specialization and Disjoint subclasses):**
  - Create relations only for each subclass $S_i$, expanding them to include all superclass attributes. No superclass table is created.
  - *Flaw:* If an entity does not belong to any subclass (partial specialization), it cannot be stored. If overlapping, data is duplicated across subclass tables.
- **Option 8C: Single Relation with One Type Attribute (Valid ONLY for Disjoint subclasses):**
  - Create a single relation containing all superclass attributes, all subclass attributes, and an added discriminator attribute `Type`.
  - Attributes not applicable to a specific type are set to `NULL`.
- **Option 8D: Single Relation with Multiple Boolean Flags (Valid for Overlapping subclasses):**
  - Create a single relation with boolean columns (e.g., `is_engineer`, `is_manager`) to track memberships. Generates heavy null values if subclasses have many specialized attributes.

---

## 1.12 Comprehensive Case Study: Enterprise System ER-to-Relational Reduction

Consider a University Department System:
1. **Strong Entities:**
   - `PROFESSOR(ProfID, Name, Email, OfficeNo)`
   - `DEPARTMENT(DeptID, DeptName, Budget)`
   - `COURSE(CourseID, Title, Credits)`
   - `STUDENT(StudentID, FirstName, LastName, DateOfBirth)`
2. **Weak Entity:**
   - `DEPENDENT(DepName, Gender, Relationship)` linked to `PROFESSOR` via identifying relationship `HAS_DEP`.
3. **Relationships & Cardinalities:**
   - `CHAIRS`: 1:1 between `PROFESSOR` and `DEPARTMENT`. Total participation on `DEPARTMENT` (every department must have a chair).
   - `OFFERS`: 1:N between `DEPARTMENT` and `COURSE` (1 department offers $N$ courses).
   - `ENROLLS`: M:N between `STUDENT` and `COURSE` with attribute `Grade`.
   - `STUDENT` has multi-valued attribute `PhoneNumbers`.

```
                          ER DIAGRAM SCHEMA BLUEPRINT
                          ===========================

  (( PhoneNumbers ))
          ||
  +-------+-------+               +---------------+               +------------+
  |    STUDENT    |====( M )====< |    ENROLLS    | >====( N )====|   COURSE   |
  +---------------+               +-------+-------+               +-----+------+
   (StudentID [PK])                       | (Grade)                     ^
   (FirstName)                                                          | (N)
   (LastName)                                                           |
   (DateOfBirth)                                                   ( OFFERS )
                                                                        |
                                                                        | (1)
  +---------------+               +---------------+               +-----+------+
  |   PROFESSOR   |----( 1 )----< |    CHAIRS     | >====( 1 )====| DEPARTMENT |
  +-------+-------+               +---------------+               +------------+
   (ProfID [PK])                                                   (DeptID [PK])
          ||                                                       (DeptName)
          || (1)                                                   (Budget)
     [ Identifying ]
     <   HAS_DEP   >
     [             ]
          || (N)
  ||==============||
  ||  DEPENDENT   ||
  ||==============||
   (DepName [PartKey])
   (Gender, Relationship)
```

### Relational Schema Conversion Execution Trace

1. **Relation `PROFESSOR` (Step 1):**
   ```sql
   CREATE TABLE Professor (
       prof_id INT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       email VARCHAR(100) UNIQUE NOT NULL,
       office_no VARCHAR(20)
   );
   ```

2. **Relation `DEPARTMENT` with 1:1 `CHAIRS` (Step 1 & Step 3):**
   - Department has total participation in `CHAIRS`, so `prof_id` migrates into `Department`:
   ```sql
   CREATE TABLE Department (
       dept_id INT PRIMARY KEY,
       dept_name VARCHAR(100) NOT NULL,
       budget DECIMAL(12, 2) CHECK (budget >= 0),
       chair_prof_id INT NOT NULL UNIQUE,
       FOREIGN KEY (chair_prof_id) REFERENCES Professor(prof_id)
           ON DELETE RESTRICT ON UPDATE CASCADE
   );
   ```

3. **Relation `COURSE` with 1:N `OFFERS` (Step 1 & Step 4):**
   - `dept_id` migrates to the N-side (`Course`):
   ```sql
   CREATE TABLE Course (
       course_id VARCHAR(10) PRIMARY KEY,
       title VARCHAR(150) NOT NULL,
       credits INT CHECK (credits BETWEEN 1 AND 6),
       offering_dept_id INT NOT NULL,
       FOREIGN KEY (offering_dept_id) REFERENCES Department(dept_id)
           ON DELETE CASCADE ON UPDATE CASCADE
   );
   ```

4. **Relation `STUDENT` (Step 1 - Composite attribute flattened):**
   ```sql
   CREATE TABLE Student (
       student_id INT PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       date_of_birth DATE NOT NULL
   );
   ```

5. **Relation `STUDENT_PHONES` (Step 6 - Multi-valued attribute):**
   ```sql
   CREATE TABLE Student_Phones (
       student_id INT,
       phone_no VARCHAR(20),
       PRIMARY KEY (student_id, phone_no),
       FOREIGN KEY (student_id) REFERENCES Student(student_id)
           ON DELETE CASCADE ON UPDATE CASCADE
   );
   ```

6. **Relation `ENROLLS` (Step 5 - M:N relationship):**
   ```sql
   CREATE TABLE Enrolls (
       student_id INT,
       course_id VARCHAR(10),
       grade CHAR(2),
       PRIMARY KEY (student_id, course_id),
       FOREIGN KEY (student_id) REFERENCES Student(student_id)
           ON DELETE CASCADE ON UPDATE CASCADE,
       FOREIGN KEY (course_id) REFERENCES Course(course_id)
           ON DELETE CASCADE ON UPDATE CASCADE
   );
   ```

7. **Relation `DEPENDENT` (Step 2 - Weak Entity):**
   ```sql
   CREATE TABLE Dependent (
       prof_id INT,
       dep_name VARCHAR(50),
       gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
       relationship VARCHAR(30) NOT NULL,
       PRIMARY KEY (prof_id, dep_name),
       FOREIGN KEY (prof_id) REFERENCES Professor(prof_id)
           ON DELETE CASCADE ON UPDATE CASCADE
   );
   ```

---

## 1.13 High-Probability Exam Questions & Student Pitfalls

### High-Probability Exam Questions
1. **Explain the 3-Schema Architecture with a neat diagram. How does it facilitate Physical and Logical Data Independence?** (Must explain ANSI/SPARC, draw the 3 layers with mappings, and detail why logical independence is harder).
2. **Differentiate between File Systems and DBMS across at least eight parameters.** (Must present the comparative table covering redundancy, isolation, atomicity, concurrent access anomalies, etc.).
3. **Define Weak Entity Set. Explain how a weak entity set is converted into a relational table with an example.** (Must state the two conditions: existence dependency and lack of primary key, show partial key, double rectangle/diamond, and give composite primary key formula).
4. **Explain Disjointness and Completeness constraints in Extended ER (EER) modeling with real-world examples.** (Must define all four combinations: $d$-Total, $d$-Partial, $o$-Total, $o$-Partial).
5. **State the rules for reducing an ER diagram with 1:1, 1:N, and M:N relationships into relational schemas.** (Must highlight foreign key placement on the N-side for 1:N and separate junction table for M:N).

### Common Student Traps & Mistakes
- *Trap 1: Placing the Foreign Key on the 1-side in a 1:N relationship.*
  - **Error:** Placing `StudentID` in `Department`.
  - **Correction:** A single department has multiple students. Storing multiple IDs in one row violates 1NF atomicity. The foreign key **always** belongs on the N-side (`Student` holds `DeptID`).
- *Trap 2: Creating a separate junction table for a 1:N relationship.*
  - **Error:** Creating a table `Works_For(EmpID, DeptID)` for a 1:N relationship.
  - **Correction:** While mathematically permissible, it is an inefficient design that forces unnecessary `JOIN` operations. Simply place `DeptID` directly into `Employee`.
- *Trap 3: Confusing Candidate Key with Super Key.*
  - **Error:** Stating that `{SSN, Name}` is a candidate key.
  - **Correction:** It is a super key, but **not** a candidate key because `{SSN}` alone is sufficient. Candidate keys must be minimal.
- *Trap 4: Forgetting the Owner Primary Key in Weak Entity Tables.*
  - **Error:** Creating `Dependent(DepName [PK], Relationship)`.
  - **Correction:** `DepName` is only a partial discriminator. Two different professors can have dependents named "Aarav". The primary key **must** be `{ProfID, DepName}`.


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


# UNIT 4: Transaction Processing Concepts, Concurrency Control, and Recovery

---

## 4.1 Transaction Concepts & ACID Properties

A **Transaction** is a logical unit of database processing that includes one or more database access operations (such as `read`, `write`, `insert`, or `delete`). The boundaries of a transaction are explicitly delineated by statements such as `BEGIN TRANSACTION` and `COMMIT` or `ROLLBACK`.

### 4.1.1 The ACID Properties & Underlying Architectural Mechanisms
To preserve database consistency and integrity across multi-user execution and hardware crashes, every DBMS guarantees the four foundational **ACID** properties:

```
+---------------------------------------------------------------------------------------+
|                                  THE ACID PARADIGM                                    |
+---------------------+---------------------+---------------------+---------------------+
|    A - ATOMICITY    |   C - CONSISTENCY   |    I - ISOLATION    |   D - DURABILITY    |
+---------------------+---------------------+---------------------+---------------------+
| "All or Nothing"    | State Transition    | Transactions execute| Committed changes   |
| Either all ops      | preserves all       | as if running in    | survive any power or|
| succeed or all are  | integrity rules and | total isolation     | system failure      |
| rolled back.        | invariants.         | from each other.    | permanently.        |
+---------------------+---------------------+---------------------+---------------------+
| IMPLEMENTATION:     | IMPLEMENTATION:     | IMPLEMENTATION:     | IMPLEMENTATION:     |
| - Undo Log / WAL    | - Schema constraints| - Lock Manager (2PL)| - Redo Log / WAL    |
| - Shadow Paging     | - Transaction logic | - Timestamp Ordering| - Checkpointing     |
| - Rollback engine   | - Triggers / Checks | - MVCC Engine       | - Non-volatile disk |
+---------------------+---------------------+---------------------+---------------------+
```

1. **Atomicity ("All-or-Nothing Property"):**
   - A transaction is an indivisible unit of work; either all its operations are executed to completion and reflected in the database, or none of them are.
   - *Failure Scenario:* A funds transfer of $500 from Account $A$ to Account $B$ ($A = A - 500$; $B = B + 500$). If a system crash occurs after debiting $A$ but before crediting $B$, the transaction manager reads the Undo log and restores $A$'s balance to its pre-transaction value.
2. **Consistency ("Preservation of Invariants"):**
   - Execution of a transaction in isolation (without concurrent interference) preserves the consistency of the database, transitioning it from one valid state to another valid state.
   - *Responsibility:* Shared between the application programmer (ensuring business logic correctness, e.g., debit = credit) and the DBMS (enforcing schema integrity constraints such as `CHECK (balance >= 0)`).
3. **Isolation ("Serial Execution Illusion"):**
   - Although multiple transactions execute concurrently, the system guarantees that for every pair of transactions $T_i$ and $T_j$, it appears to $T_i$ that $T_j$ finished execution either before $T_i$ started or after $T_i$ completed. Intermediate, uncommitted state modifications of a transaction are invisible to concurrent transactions.
4. **Durability ("Permanence of Committed Updates"):**
   - After a transaction completes successfully and issues a `COMMIT`, the changes it has made to the database persist permanently in non-volatile storage and will never be lost, even if an operating system crash or physical power cut occurs immediately afterward.

---

## 4.2 Transaction State Diagram & Lifecycle

A transaction transitions through a finite set of discrete states during its execution:

```
                                  +-------------------+
                                  |      ACTIVE       |
                                  +---------+---------+
                                           / \
               Operation completes        /   \  Error occurs or abort signal
                                         /     \
                                        v       v
                   +------------------------+  +------------------------+
                   |  PARTIALLY COMMITTED   |  |         FAILED         |
                   +-----------+------------+  +-----------+------------+
                              / \                          |
         Log buffer flushed  /   \ Hardware failure        | Undo log operations
         to stable disk     /     \ during commit          | executed (Rollback)
                           v       v                       v
            +-------------------+  +------------------------------------+
            |     COMMITTED     |  |              ABORTED               |
            +-------------------+  +-------------------+----------------+
                                                       |
                                                       | Restart or Kill
                                                       v
                                           +-----------------------+
                                           |      TERMINATED       |
                                           +-----------------------+
```

### 4.2.1 State Descriptions
1. **Active:** The initial state; the transaction enters this state upon `BEGIN TRANSACTION` and remains here while executing read, write, and compute statements.
2. **Partially Committed:** Entered after the final statement has been executed in memory, but before the log records have been completely flushed to stable non-volatile storage.
3. **Committed:** Entered after all transaction log records have been successfully and durably flushed to stable disk (Write-Ahead Logging protocol). The transaction is now complete.
4. **Failed:** Entered when the transaction can no longer proceed due to normal execution errors (e.g., divide-by-zero, constraint violation) or hardware crashes.
5. **Aborted:** The transaction has been rolled back and the database has been restored to its pre-transaction state using Undo log records. The system can now either **Restart** the transaction (if failed due to concurrency deadlock) or **Kill** it (if failed due to internal application logic errors).
6. **Terminated:** The transaction record is removed from active memory tables.

---

## 4.3 Schedules & Serializability

A **Schedule (or History) $S$** of a set of concurrent transactions $\{T_1, T_2, \dots, T_n\}$ is an ordered sequence of the operations performed by those transactions, subject to the constraint that for each individual transaction $T_i$, the operations of $T_i$ in $S$ must appear in the same order as they occur within $T_i$ itself.

### 4.3.1 Classification of Schedules
- **Serial Schedule:** A schedule where the operations of each transaction are executed consecutively to completion without any interleaved operations from other transactions.
  *Properties:* Guaranteed to leave the database in a consistent state, but yields abysmal CPU/disk utilization and poor response times.
- **Non-Serial Schedule:** A schedule where operations of concurrent transactions are interleaved.
- **Serializable Schedule:** A non-serial schedule that is mathematically equivalent to some serial schedule of the same transactions.

### 4.3.2 Conflicting Operations
Two operations $O_i$ and $O_j$ in a schedule $S$ are in **Conflict** if and only if they satisfy all three of the following conditions:
1. They belong to **different transactions** ($T_i \neq T_j$).
2. They access the **same data item** ($Q$).
3. At least one of the two operations is a **Write operation** ($W$).

$$\begin{array}{|c|c|c|c|}
\hline
T_i \text{ Operation} & T_j \text{ Operation} & \text{Same Data Item?} & \text{Conflict Status} \\
\hline
\text{Read}(Q) & \text{Read}(Q) & \text{Yes} & \mathbf{No\ Conflict} \text{ (Read-Read is safe)} \\
\text{Read}(Q) & \text{Write}(Q) & \text{Yes} & \mathbf{CONFLICT} \text{ (Read-Write Conflict)} \\
\text{Write}(Q) & \text{Read}(Q) & \text{Yes} & \mathbf{CONFLICT} \text{ (Write-Read Conflict)} \\
\text{Write}(Q) & \text{Write}(Q) & \text{Yes} & \mathbf{CONFLICT} \text{ (Write-Write Conflict)} \\
\hline
\end{array}$$

---

### 4.3.3 Conflict Serializability

#### Definition: Conflict Equivalence
Two schedules $S$ and $S'$ over the same set of transactions are **Conflict Equivalent** if $S$ can be transformed into $S'$ by a series of swaps of non-conflicting adjacent operations.

#### Definition: Conflict Serializability
A schedule $S$ is **Conflict Serializable** if it is conflict equivalent to some serial schedule.

#### The Precedence Graph (Serialization Graph) Algorithm
Conflict serializability of any schedule $S$ can be tested in polynomial time ($O(|V| + |E|)$) using a directed graph $G = (V, E)$:
1. **Vertices ($V$):** Each active transaction $T_i$ in $S$ corresponds to a vertex in $V$.
2. **Directed Edges ($E$):** Construct a directed edge $T_i \to T_j$ if an operation of $T_i$ precedes and conflicts with an operation of $T_j$ in $S$. That is, add edge $T_i \to T_j$ if:
   - $T_i$ executes $W_i(Q)$ before $T_j$ executes $R_j(Q)$.
   - $T_i$ executes $R_i(Q)$ before $T_j$ executes $W_j(Q)$.
   - $T_i$ executes $W_i(Q)$ before $T_j$ executes $W_j(Q)$.

#### Serializability Theorem:
> **Theorem:** A schedule $S$ is **Conflict Serializable** if and only if its Precedence Graph $G(S)$ contains **NO DIRECTED CYCLES (is a Directed Acyclic Graph - DAG)**.

If the graph is acyclic, an equivalent serial schedule is obtained by performing a **Topological Sort** on the vertices of $G(S)$.

```
Acyclic Precedence Graph:                  Cyclic Precedence Graph:
       +-------+                                  +-------+
       |  T1   |                                  |  T1   |
       +---+---+                                  +---+---+
           |                                         / \
           |                                        /   \
           v                                       v     \
       +-------+                               +-------+  \
       |  T2   |                               |  T2   |  / (Edge T2 -> T1 creates cycle)
       +-------+                               +-------+ v
(Conflict Serializable: T1 -> T2)           (NOT Conflict Serializable: DEADLOCK/ANOMALY)
```

---

### 4.3.4 View Serializability

View serializability is a less restrictive form of serializability based on the data values read and written.

#### Definition: View Equivalence
Two schedules $S$ and $S'$ over the same transactions are **View Equivalent** if and only if they satisfy three conditions:
1. **Initial Read Condition:** For each data item $Q$, if transaction $T_i$ reads the initial value of $Q$ in $S$, then $T_i$ must also read the initial value of $Q$ in $S'$.
2. **Updated Read (Read-From) Condition:** For each data item $Q$, if transaction $T_i$ reads the value of $Q$ written by transaction $T_j$ in $S$, then $T_i$ must also read the value of $Q$ written by transaction $T_j$ in $S'$.
3. **Final Write Condition:** For each data item $Q$, if transaction $T_i$ executes the final write on $Q$ in $S$, then $T_i$ must also execute the final write on $Q$ in $S'$.

#### Definition: View Serializability
A schedule $S$ is **View Serializable** if it is view equivalent to some serial schedule.

#### Relationship Between Conflict & View Serializability:
- Every conflict-serializable schedule is **view-serializable**:
  $$\text{Conflict Serializable} \subset \text{View Serializable}$$
- A view-serializable schedule that is **NOT** conflict-serializable contains **Blind Writes** (operations where a transaction writes a data item $W(Q)$ without reading $R(Q)$ first).
- **Algorithmic Complexity Warning:**
  - Testing Conflict Serializability: **$O(V + E)$ (Polynomial time)** via cycle detection.
  - Testing View Serializability: **NP-Complete Problem**! Because testing view equivalence requires searching across all $n!$ permutations of transactions, commercial DBMS concurrency engines strictly enforce Conflict Serializability.

---

## 4.4 Recoverability of Schedules & Cascading Aborts

When concurrent transactions fail, the DBMS must be able to restore consistency without creating orphaned reads or phantom commitments.

```
       +-------------------------------------------------------------+
       |                    ALL POSSIBLE SCHEDULES                   |
       |                                                             |
       |        +-------------------------------------------+        |
       |        |           RECOVERABLE SCHEDULES           |        |
       |        |  (If Tj reads from Ti, Ci < Cj)           |        |
       |        |                                           |        |
       |        |      +-----------------------------+      |        |
       |        |      |    CASCADELESS SCHEDULES    |      |        |
       |        |      |  (If Tj reads from Ti,      |      |        |
       |        |      |   Ci < Rj(X))               |      |        |
       |        |      |                             |      |        |
       |        |      |      +---------------+      |      |        |
       |        |      |      |    STRICT     |      |      |        |
       |        |      |      |  Ci < Rj(X)   |      |      |        |
       |        |      |      |  & Ci < Wj(X) |      |      |        |
       |        |      |      +---------------+      |      |        |
       |        |      +-----------------------------+      |        |
       |        +-------------------------------------------+        |
       +-------------------------------------------------------------+
```

### 4.4.1 Unrecoverable Schedule (The Worst Concurrency Nightmare)
A schedule is **Unrecoverable** if transaction $T_j$ reads a value written by $T_i$, and $T_j$ **commits before** $T_i$ commits. If $T_i$ subsequently aborts, $T_j$ has committed a transaction based on data that "never existed". Because committed transactions cannot be aborted (Durability property), the database enters an unrecoverable, corrupted state.

*Unrecoverable Schedule Trace:*
$$S: W_1(A) \to R_2(A) \to W_2(A) \to C_2 \to \text{ABORT}_1$$
Here, $T_2$ read uncommitted data from $T_1$ and committed ($C_2$). When $T_1$ aborts, the system cannot rollback $T_2$ without violating Durability. **Unrecoverable schedules are strictly prohibited by all DBMSs.**

### 4.4.2 Recoverable Schedules
- **Formal Condition:** A schedule $S$ is **Recoverable** if, for every pair of transactions $T_i$ and $T_j$ such that $T_j$ reads a data item previously written by $T_i$, the commit operation of $T_i$ appears before the commit operation of $T_j$:
  $$C_i < C_j$$

### 4.4.3 Cascading Rollback & Cascadeless Schedules (ACA)
- **Cascading Rollback (Cascading Abort):** In a recoverable schedule, if $T_i$ aborts, all uncommitted transactions that read data modified by $T_i$ must also be recursively aborted and rolled back. This can trigger a catastrophic chain reaction aborting hundreds of transactions and wasting system work.
- **Cascadeless Schedule (Avoids Cascading Abort - ACA):**
  - **Formal Condition:** Every transaction reads only **committed data**. For every pair of transactions $T_i$ and $T_j$ such that $T_j$ reads an item written by $T_i$, the commit operation of $T_i$ must precede the read operation of $T_j$:
    $$C_i < R_j(X)$$

### 4.4.4 Strict Schedules
- **Formal Condition:** A schedule is **Strict** if transactions neither read nor write a data item until the previous transaction that wrote that data item has either committed or aborted:
  $$C_i < R_j(X) \quad \text{AND} \quad C_i < W_j(X)$$
- **Recovery Benefit:** In a strict schedule, restoring a data item upon a transaction abort requires only copying back its *Before-Image (BFIM)* from the log, with zero risk of overwriting uncommitted concurrent updates.

---

## 4.5 Concurrency Anomalies Without Control

When transactions execute without locking or concurrency control, four classic anomalies occur:

```
+-----------------------------------------------------------------------------------+
|                            CONCURRENCY ANOMALIES                                  |
+---------------------+---------------------+------------------+--------------------+
|  1. LOST UPDATE     |   2. DIRTY READ     | 3. UNREPEATABLE  | 4. PHANTOM READ    |
|   (Write-Write)     |    (Read-Write)     |   (Fuzzy Read)   |  (Dynamic Range)   |
+---------------------+---------------------+------------------+--------------------+
| Two transactions    | T2 reads data       | T1 reads item Q; | T1 queries range of|
| overwrite the same  | updated by T1 that  | T2 updates Q;    | rows; T2 inserts a |
| item concurrently;  | has not yet been    | T1 re-reads Q and| new row matching   |
| one update vanishes.| committed; T1 aborts| finds value has  | filter; T1 sees a  |
|                     |                     | changed!         | "phantom" record!  |
+---------------------+---------------------+------------------+--------------------+
```

### 4.5.1 Detailed Walkthrough of the Four Anomalies

1. **Lost Update Problem:**
   - $T_1$ and $T_2$ both read $A = 1000$.
   - $T_1$ writes $A = 1000 - 100 = 900$.
   - $T_2$ writes $A = 1000 + 200 = 1200$ (overwriting $T_1$'s modification).
   - $T_1$'s debit of $100$ is permanently lost.
2. **Dirty Read (Temporary Update) Problem:**
   - $T_1$ updates $A = 500 \to 1000$.
   - $T_2$ reads $A = 1000$ and calculates a tax report.
   - $T_1$ aborts and rolls back $A$ to $500$.
   - $T_2$ has acted on "dirty" fictitious data that never existed.
3. **Unrepeatable Read (Inconsistent Analysis):**
   - $T_1$ reads $A = 100$.
   - $T_2$ updates $A = 200$ and commits.
   - $T_1$ re-reads $A$ during the same transaction and finds $A = 200$.
   - $T_1$ reads two conflicting values for the identical data item within a single transaction.
4. **Phantom Read Problem:**
   - $T_1$ queries: `SELECT COUNT(*) FROM Employee WHERE dept_id = 10` (returns 5).
   - $T_2$ executes: `INSERT INTO Employee VALUES (..., dept_id = 10)` and commits.
   - $T_1$ runs the identical count query and receives 6.
   - A new "phantom" row appeared inside the range.

### 4.5.2 ANSI SQL Transaction Isolation Levels

| Isolation Level | Dirty Read Permitted? | Unrepeatable Read Permitted? | Phantom Read Permitted? |
| :--- | :--- | :--- | :--- |
| **Read Uncommitted** | **Yes** | **Yes** | **Yes** |
| **Read Committed** | **No** | **Yes** | **Yes** |
| **Repeatable Read** | **No** | **No** | **Yes** |
| **Serializable** | **No** | **No** | **No** |

---

## 4.6 Lock-Based Concurrency Control Protocols

### 4.6.1 Lock Modes and Compatibility
A **Lock** is a variable associated with a data item that describes the operations that can be performed on it.
- **Shared-Mode Lock ($S$):** Required for reading data ($R(Q)$). Multiple transactions can simultaneously hold shared locks on the same item.
- **Exclusive-Mode Lock ($X$):** Required for writing data ($W(Q)$). Only one transaction can hold an exclusive lock on an item at any time.

```
Lock Compatibility Matrix:
                  Requested Mode
             |   Shared (S)   | Exclusive (X) |
   ----------+----------------+---------------+
   Held  (S) |    COMPATIBLE  |  CONFLICT     |
   Mode  (X) |    CONFLICT    |  CONFLICT     |
```

---

### 4.6.2 The Two-Phase Locking (2PL) Protocol

The Two-Phase Locking protocol guarantees that transactions execute in a manner that yields strictly **Conflict Serializable** schedules.

```
       Lock Count Held
             ^
             |                 Lock Point (Max locks acquired)
             |                       *
             |                     *   *
             |                   *       *
             |                 *           *
             |   GROWING PHASE               SHRINKING PHASE
             |  (Acquiring Locks)           (Releasing Locks)
             |  [NO LOCKS RELEASED]         [NO LOCKS ACQUIRED]
             |
             +---------------------------------------------------> Time
```

#### The Fundamental Rules of 2PL:
1. **Growing (Expanding) Phase:** A transaction may acquire locks, but **cannot release any lock**.
2. **Shrinking (Contracting) Phase:** A transaction may release locks, but **cannot acquire any new locks**.
3. **Lock Point:** The exact instant when a transaction acquires its final lock.

#### Formal Proof: 2PL Guarantees Conflict Serializability
- **Proof by Contradiction:**
  1. Assume a schedule $S$ generated by a 2PL protocol is **NOT** conflict serializable.
  2. By the Serializability Theorem, the Precedence Graph $G(S)$ must contain a directed cycle:
     $$T_1 \to T_2 \to T_3 \to \dots \to T_n \to T_1$$
  3. A directed edge $T_i \to T_j$ means $T_i$ accessed a conflicting data item $Q$ before $T_j$.
  4. Under the rules of locking, $T_i$ cannot allow $T_j$ to access $Q$ until $T_i$ releases its lock on $Q$.
  5. Thus, $T_i$ must release a lock before $T_j$ acquires its lock on $Q$.
  6. Let $LP(T_k)$ denote the time of the **Lock Point** of transaction $T_k$.
  7. Because $T_i$ begins shrinking before $T_j$ finishes growing, we have:
     $$LP(T_i) < LP(T_j)$$
  8. Applying this strict inequality transitively along the entire cycle:
     $$LP(T_1) < LP(T_2) < LP(T_3) < \dots < LP(T_n) < LP(T_1)$$
  9. This implies:
     $$LP(T_1) < LP(T_1)$$
     which is a mathematical contradiction ($x < x$ is impossible)!
  10. Hence, no cycle can exist in $G(S)$. Therefore, every 2PL schedule is **guaranteed to be Conflict Serializable**. $\blacksquare$

---

### 4.6.3 Variations of Two-Phase Locking

```
+-----------------------------------------------------------------------------------+
|                                VARIATIONS OF 2PL                                  |
+---------------------+---------------------+------------------+--------------------+
|      BASIC 2PL      |     STRICT 2PL      |   RIGOROUS 2PL   |  CONSERVATIVE 2PL  |
+---------------------+---------------------+------------------+--------------------+
| - Releases locks    | - Holds all         | - Holds BOTH     | - Pre-declares and |
|   during shrinking  |   EXCLUSIVE (X)     |   Shared (S) and |   locks ALL data   |
|   phase.            |   locks until commit|   Exclusive (X)  |   items BEFORE     |
| - Prone to Cascading|   or abort.         |   locks until    |   execution.       |
|   Rollbacks!        | - Prevents cascading|   commit/abort.  | - DEADLOCK-FREE!   |
| - Can DEADLOCK.     |   aborts; Strict.   | - Serial order = | - Low concurrency. |
|                     | - Can DEADLOCK.     |   Commit order.  |                    |
+---------------------+---------------------+------------------+--------------------+
```

---

## 4.7 Deadlock Handling in Concurrency

A **Deadlock** is a state where two or more transactions are in a simultaneous circular wait, each waiting for a lock held by the other, such that none can proceed.

### 4.7.1 Deadlock Prevention Protocols (Timestamp-Based)
Each transaction $T_i$ is assigned a unique monotonically increasing timestamp $TS(T_i)$ when it begins. Older transactions have smaller timestamps ($TS(T_{old}) < TS(T_{young})$).

```
+-----------------------------------------------------------------------------------+
|                        DEADLOCK PREVENTION PROTOCOLS                              |
+-------------------------------------------+---------------------------------------+
|             WAIT-DIE SCHEME               |          WOUND-WAIT SCHEME            |
|             (Non-Preemptive)              |             (Preemptive)              |
+-------------------------------------------+---------------------------------------+
| - If Older requests lock held by Younger: | - If Older requests lock held by Young|
|   Older is allowed to WAIT.               |   Older WOUNDS (preempts/aborts) Young|
|                                           |   Younger rolls back!                 |
| - If Younger requests lock held by Older: | - If Younger requests lock held by Old|
|   Younger DIES (aborts & rolls back).     |   Younger is allowed to WAIT.         |
+-------------------------------------------+---------------------------------------+
```

*Starvation Prevention Rule:* When a transaction is aborted and restarted under either scheme, it is reassigned its **original timestamp** so that it progressively becomes the oldest transaction in the system, guaranteeing it will not starve.

### 4.7.2 Deadlock Detection: The Wait-For Graph (WFG)
The lock manager maintains a dynamic directed graph $G = (V, E)$:
- **Vertices ($V$):** Active transactions.
- **Edges ($E$):** Directed edge $T_i \to T_j$ indicates that $T_i$ is currently waiting for a lock held by $T_j$.
- **Detection Algorithm:** The system periodically invokes cycle detection (e.g., Tarjan's or Kosaraju's DFS algorithm). **A cycle in the Wait-For Graph indicates a Deadlock!**

```
Wait-For Graph Cycle (Deadlock):
       +-------+     Waiting for Lock A     +-------+
       |  T1   | ------------------------>  |  T2   |
       +-------+                            +-------+
           ^                                    |
           |                                    |
           +------------------------------------+
                    Waiting for Lock B
```

### 4.7.3 Deadlock Recovery (Three Steps)
1. **Victim Selection:** Choose the transaction whose rollback incurs the least cost based on:
   - How long the transaction has run.
   - Number of data items modified.
   - Number of locks held.
2. **Rollback:**
   - *Total Rollback:* Abort the transaction and undo all its changes.
   - *Partial Rollback:* Roll back the victim only as far as necessary to break the cycle (utilizing transaction `SAVEPOINT`s).
3. **Starvation Avoidance:** Ensure the same transaction is not continuously chosen as victim by tracking victim selection counts.

---

## 4.8 Timestamp-Based Protocols & Thomas' Write Rule

### 4.8.1 Timestamp Ordering (TO) Protocol
For each data item $Q$, the system maintains two timestamp values:
- **$W\text{-TS}(Q)$ (Write Timestamp):** The largest timestamp of any transaction that successfully executed $W(Q)$.
- **$R\text{-TS}(Q)$ (Read Timestamp):** The largest timestamp of any transaction that successfully executed $R(Q)$.

#### Protocol Rules:
1. **Transaction $T$ issues $R(Q)$:**
   - If $TS(T) < W\text{-TS}(Q)$: $T$ is attempting to read an obsolete, overwritten value. **Reject $R(Q)$ and abort $T$**.
   - If $TS(T) \ge W\text{-TS}(Q)$: Execute $R(Q)$, and update:
     $$R\text{-TS}(Q) := \max(R\text{-TS}(Q), TS(T))$$
2. **Transaction $T$ issues $W(Q)$:**
   - If $TS(T) < R\text{-TS}(Q)$: Another transaction that should have executed after $T$ has already read $Q$'s value. **Reject $W(Q)$ and abort $T$**.
   - If $TS(T) < W\text{-TS}(Q)$: $T$ is attempting to write an obsolete value. Under standard TO, **reject $W(Q)$ and abort $T$**.
   - Otherwise, execute $W(Q)$, and update:
     $$W\text{-TS}(Q) := TS(T)$$

### 4.8.2 Thomas' Write Rule
Thomas' Write Rule is an optimization of the timestamp ordering protocol for handling obsolete writes:
- If $TS(T) < W\text{-TS}(Q)$, rather than aborting $T$, **simply ignore (skip) the write operation and allow $T$ to continue!**
- *Rationale:* Since a newer transaction has already written $Q$, $T$'s write is obsolete and would be immediately overwritten anyway.
- **Theoretical Importance:** Thomas' Write Rule produces schedules that are **View Serializable** but are **NOT Conflict Serializable**!

---

## 4.9 Multiple Granularity Locking (MGL)

To balance concurrency with locking overhead, the DBMS organizes lockable data items into a **Granularity Hierarchy**:

```
                       +-------------------+
                       |     DATABASE      |
                       +---------+---------+
                                 |
                                 v
                       +-------------------+
                       |       FILE        |
                       +---------+---------+
                                 |
                                 v
                       +-------------------+
                       |       TABLE       |
                       +---------+---------+
                                 |
                                 v
                       +-------------------+
                       |    PAGE / BLOCK   |
                       +---------+---------+
                                 |
                                 v
                       +-------------------+
                       |   RECORD / ROW    |
                       +-------------------+
```

### 4.9.1 Intention Locks
To lock a fine-grained node (e.g., a single record), a transaction must first place **Intention Locks** on all its ancestor nodes (Table, File, Database), alerting other transactions not to lock the entire parent:
1. **Intention-Shared (IS):** Explicit locking will occur at a lower level with Shared locks.
2. **Intention-Exclusive (IX):** Explicit locking will occur at a lower level with Exclusive locks.
3. **Shared Intention-Exclusive (SIX):** The subtree rooted at this node is locked explicitly in Shared mode, but explicit Exclusive locking will occur at a lower level.

#### Complete 5x5 Compatibility Matrix for MGL:
$$\begin{array}{|c|c|c|c|c|c|}
\hline
\text{Held \ Requested} & \mathbf{IS} & \mathbf{IX} & \mathbf{S} & \mathbf{SIX} & \mathbf{X} \\
\hline
\mathbf{IS} & \text{Compatible} & \text{Compatible} & \text{Compatible} & \text{Compatible} & \text{Conflict} \\
\mathbf{IX} & \text{Compatible} & \text{Compatible} & \text{Conflict} & \text{Conflict} & \text{Conflict} \\
\mathbf{S}  & \text{Compatible} & \text{Conflict} & \text{Compatible} & \text{Conflict} & \text{Conflict} \\
\mathbf{SIX}& \text{Compatible} & \text{Conflict} & \text{Conflict} & \text{Conflict} & \text{Conflict} \\
\mathbf{X}  & \text{Conflict} & \text{Conflict} & \text{Conflict} & \text{Conflict} & \text{Conflict} \\
\hline
\end{array}$$

---

## 4.10 Database Recovery Techniques

Database recovery is the process of restoring the database to the most recent consistent state that existed immediately before a failure occurred.

### 4.10.1 Taxonomy of Failures
1. **Transaction Failure:** Logical error (bad input) or system error (deadlock victim).
2. **System Crash (Soft Failure):** Hardware failure, OS crash, or power interruption causing the contents of volatile main memory (Buffer Pool) to be lost.
3. **Disk / Media Failure (Hard Failure):** Disk head crash, bad sectors, or catastrophic drive failure destroying non-volatile blocks.

### 4.10.2 Storage Structure Hierarchy
- **Volatile Storage:** RAM cache/buffer pool; does not survive system crashes.
- **Non-Volatile Storage:** Magnetic disks, SSDs; survives crashes, but vulnerable to disk head failures.
- **Stable Storage:** Information is replicated across independent non-volatile media (RAID 1/5/6, geographical mirroring) such that data loss is virtually impossible.

### 4.10.3 The Write-Ahead Logging (WAL) Protocol
Every state modification is recorded in a **Log Record** residing on stable storage before modifying the physical database blocks on disk.
1. **The Undo Rule (WAL Principle 1):** The log record containing the before-image ($BFIM$) of an update must be flushed to stable storage **BEFORE** the modified database page is written to disk. (Guarantees Atomicity).
2. **The Redo Rule (WAL Principle 2):** All log records containing the after-images ($AFIM$) of a transaction must be flushed to stable storage **BEFORE** the transaction issues its commit acknowledgment. (Guarantees Durability).

```
Log Record Structure:
  <Ti, START>                    Transaction Ti began
  <Ti, X, Old_Val, New_Val>      Ti modified item X (Undo: Old_Val, Redo: New_Val)
  <Ti, COMMIT>                   Ti committed successfully
  <Ti, ABORT>                    Ti aborted
  <CHECKPOINT L>                 Active transactions list at checkpoint
```

---

### 4.10.4 Intermediate Update Recovery Strategies

#### 1. Deferred Database Modification (NO-UNDO / REDO Algorithm)
- Updates are kept in memory buffers and transaction log files; **no physical disk database pages are updated until AFTER the transaction successfully commits**.
- Because uncommitted data is never written to disk, **an abort never requires an UNDO operation!**
- If a system crash occurs:
  - Transactions with both `<T, START>` and `<T, COMMIT>` in the log are **REDO**-ed.
  - Transactions with only `<T, START>` are simply ignored (no changes ever touched disk).

#### 2. Immediate Database Modification (UNDO / REDO Algorithm)
- Database updates can be written to disk blocks even while the transaction is still active (before commit).
- If a system crash occurs:
  - Transactions that committed before the crash must be **REDO**-ed (their updates might still be lingering in volatile buffer pool memory).
  - Transactions that were active (uncommitted) at the time of the crash must be **UNDO**-ed (their dirty updates have already reached physical disk pages).

---

### 4.10.5 Shadow Paging Technique
- Alternative recovery method that does not require a log in single-user environments.
- Maintains two page tables during transaction execution:
  1. **Current Page Table:** Used to point to current database pages on disk.
  2. **Shadow Page Table:** Points to the original database pages prior to transaction execution.
- When an update occurs: A copy of the target page is written to a new free disk frame; the Current Page Table pointer is updated, while the Shadow Page Table remains unchanged.
- **Commit Operation:** An atomic disk write flips a single master pointer to make the Current Page Table the new Shadow Page Table.
- **Abort Operation:** Discard the Current Page Table; the Shadow Page Table immediately restores the original state without undoing data pages.
- **Disadvantages:** High disk fragmentation, loss of data page clustering, and expensive page table copying overhead.

```
Shadow Paging Architecture:
   Current Page Table                 Shadow Page Table
   +----+----------+                  +----+----------+
   |Page| Frame No |                  |Page| Frame No |
   +----+----------+                  +----+----------+
   | 0  | Frame 5  |                  | 0  | Frame 5  |
   | 1  | Frame 12*| (Updated Page 1) | 1  | Frame 8  | (Original Page 1)
   | 2  | Frame 20 |                  | 2  | Frame 20 |
   +----+----------+                  +----+----------+
```

---

### 4.10.6 Checkpointing & Log Recovery Algorithm

#### Motivation
Scanning the transaction log from the beginning of time is computationally infeasible for high-throughput production systems. **Checkpointing** flushes dirty database pages and log buffers to disk periodically, establishing a boundary before which all operations are guaranteed to be durable.

#### The Checkpoint Algorithm:
1. Stop accepting new transactions temporarily.
2. Flush all modified log records currently in main memory to stable storage.
3. Flush all dirty database buffer blocks to disk.
4. Write a log record `<CHECKPOINT L>`, where $L$ is the list of transactions currently active at the moment of the checkpoint.
5. Flush the log buffer containing the checkpoint record to stable storage.

#### Recovery Procedure Following a Crash:
1. Initialize two lists:
   - **UNDO List:** Transactions that were active when the crash occurred and must be rolled back.
   - **REDO List:** Transactions that committed before the crash but whose pages may not have reached disk.
2. Scan the log **backward** from the end to find the most recent `<CHECKPOINT L>` record.
3. Set $\text{UNDO} := L$, and $\text{REDO} := \emptyset$.
4. Scan the log **forward** from the checkpoint record to the end of the log:
   - If a `<T, COMMIT>` is found: Remove $T$ from $\text{UNDO}$ and add $T$ to $\text{REDO}$.
   - If a `<T, START>` is found: Add $T$ to $\text{UNDO}$.
5. **Execute REDO Phase:** Scan forward from the earliest uncommitted operation of any transaction in $\text{REDO}$, reapplying new values: $X := New\_Val$.
6. **Execute UNDO Phase:** Scan backward from the end of the log, reversing all updates made by transactions in the $\text{UNDO}$ list: $X := Old\_Val$.

---

### 4.10.7 Comprehensive Worked Log Trace Problem

**Problem Scenario:**
A database system uses Immediate Database Modification with Checkpointing. The following log records appear on stable disk storage:

```
[Log Position]   [Log Record Content]
1.               <T1, START>
2.               <T1, A, 50, 60>
3.               <T2, START>
4.               <T2, B, 100, 150>
5.               <T1, COMMIT>
6.               <CHECKPOINT {T2}>
7.               <T3, START>
8.               <T3, C, 200, 250>
9.               <T2, B, 150, 300>
10.              <T2, COMMIT>
11.              <T4, START>
12.              <T4, D, 400, 450>
                 *** SYSTEM CRASH OCCURS HERE ***
```

**Step-by-Step Recovery Walkthrough:**
1. **Identify the Checkpoint:**
   At Log Position 6: `<CHECKPOINT {T2}>`.
   Transactions active at checkpoint: $\{T_2\}$.
2. **Initialize Lists:**
   $\text{UNDO} = \{T_2\}$, $\text{REDO} = \emptyset$.
3. **Scan Forward from Checkpoint (Log Positions 7 to 12):**
   - Position 7: `<T3, START>` $\implies \text{UNDO} = \{T_2, T_3\}$.
   - Position 10: `<T2, COMMIT>` $\implies$ Move $T_2$ to REDO:
     $$\text{UNDO} = \{T_3\}, \quad \text{REDO} = \{T_2\}$$
   - Position 11: `<T4, START>` $\implies \text{UNDO} = \{T_3, T_4\}$.
   - Crash encountered!
4. **Final Transaction Classification:**
   - **$\mathbf{REDO\ List} = \{T_2\}$** (Committed after checkpoint).
   - **$\mathbf{UNDO\ List} = \{T_3, T_4\}$** (Active at crash; never committed).
   - *Note on $T_1$:* $T_1$ committed before the checkpoint, so all its updates were flushed to disk during checkpoint step 3. $T_1$ requires neither undo nor redo!
5. **Execution of Recovery:**
   - **REDO Phase (Roll-Forward):**
     Reapply $T_2$'s updates:
     - Set $B := 300$ (from Log Position 9).
   - **UNDO Phase (Roll-Backward):**
     Reverse $T_4$ and $T_3$'s uncommitted updates:
     - Undo $T_4$: Set $D := 400$ (from Log Position 12).
     - Undo $T_3$: Set $C := 200$ (from Log Position 8).
6. **Recovery Complete:** System writes `<T4, ABORT>` and `<T3, ABORT>` to log and resumes normal processing.

---

## 4.11 High-Probability Exam Questions & Student Pitfalls

### High-Probability Exam Questions
1. **Explain the ACID properties and describe the specific DBMS subsystems responsible for enforcing each.**
2. **State and prove the Serializability Theorem using Precedence Graphs. Perform topological sorting on an acyclic graph.**
3. **Differentiate between Conflict Serializability and View Serializability. Why is conflict serializability preferred in commercial systems?**
4. **Explain Two-Phase Locking (2PL). Prove formally that 2PL guarantees conflict serializability. Differentiate between Strict 2PL and Rigorous 2PL.**
5. **Differentiate between Wait-Die and Wound-Wait deadlock prevention schemes with concrete examples.**
6. **Describe the checkpointing algorithm. Given a transaction log trace, construct the UNDO and REDO lists and trace recovery step-by-step.**

### Common Student Traps & Mistakes
- *Trap 1: Confusing 2PL with Deadlock Prevention.*
  - **Mistake:** Assuming that standard Two-Phase Locking prevents deadlocks.
  - **Correction:** 2PL guarantees **serializability**, but it can and does suffer from deadlocks! (Only Conservative 2PL prevents deadlocks).
- *Trap 2: Believing Read-Read operations conflict.*
  - **Mistake:** Drawing an edge in the precedence graph for $R_1(A)$ followed by $R_2(A)$.
  - **Correction:** Two reads **never conflict**. Only $R-W, W-R,$ and $W-W$ operations conflict.
- *Trap 3: Reversing the roles in Wait-Die vs Wound-Wait.*
  - **Mistake:** Thinking older transactions die in Wait-Die.
  - **Correction:** In Wait-Die, the **older waits** while the **younger dies**. Older transactions never die in Wait-Die.


# UNIT 5: Client/Server Databases, Security, and Repositories

---

## 5.1 Client/Server Concepts and Architectures

In centralized database architectures (the mainframe era), a single monolithic computer executed both application logic and database processing while users connected via passive, non-programmable dummy terminals. 
The advent of personal computers and local area networks (LANs) led to **Client/Server Architectures**, which partition workload between client machines (requesting services) and server machines (providing specialized services).

```
===================================================================================
                        TWO-TIER CLIENT/SERVER ARCHITECTURE
   +-----------------------------------------------------------------------------+
   |                             CLIENT TIER                                     |
   |   User Interface + Application Business Logic (Thick / Fat Client)          |
   |   [ C++ / Java / Python Desktop App ]                                       |
   +-----------------------------------------------------------------------------+
                                         ^
                                         | Network Protocol (ODBC / JDBC / Net8)
                                         v
   +-----------------------------------------------------------------------------+
   |                             SERVER TIER                                     |
   |   DBMS Query Engine + Transaction Processing + Storage Management           |
   |   [ Oracle / PostgreSQL / MySQL Server ]                                    |
   +-----------------------------------------------------------------------------+

===================================================================================
                       THREE-TIER CLIENT/SERVER ARCHITECTURE
   +-----------------------------------------------------------------------------+
   |                        PRESENTATION TIER (Tier 1)                           |
   |   Graphical User Interface (Thin Client: Web Browser / Mobile App)          |
   |   [ React / Angular / HTML5 / iOS / Android UI ]                            |
   +-----------------------------------------------------------------------------+
                                         ^
                                         | HTTPS / REST / GraphQL / JSON
                                         v
   +-----------------------------------------------------------------------------+
   |                      APPLICATION / BUSINESS TIER (Tier 2)                   |
   |   Business Rules, Workflows, Validation, Security Logic, Connection Pooling |
   |   [ Spring Boot / Node.js / Django / ASP.NET Application Server ]           |
   +-----------------------------------------------------------------------------+
                                         ^
                                         | JDBC / Native Database Driver
                                         v
   +-----------------------------------------------------------------------------+
   |                          DATABASE TIER (Tier 3)                             |
   |   DBMS Engine, Relational Catalog, Physical Tablespaces, ACID Storage       |
   |   [ PostgreSQL / Oracle / SQL Server Database Cluster ]                     |
   +-----------------------------------------------------------------------------+
```

### 5.1.1 Two-Tier Architecture ("Fat Client")
- **Structure:** The client workstation hosts both the User Interface (UI) and the application business logic. The client connects directly to the database server via specialized database network protocols (e.g., Oracle Net8, MySQL Wire Protocol) using client APIs like ODBC or JDBC.
- **Deficiencies of Two-Tier Architecture:**
  1. **Deployment and Maintenance Overhead:** Updating a single business rule requires recompiling and deploying new client software binaries to thousands of user desktops.
  2. **Security Vulnerability:** Because clients connect directly to the database, database connection strings, credentials, and schema details must be stored locally on client machines, creating attack surfaces.
  3. **High Network Traffic:** Intermediate filtering is performed on the client, requiring large volumes of raw data to traverse corporate LANs.
  4. **Poor Scalability:** Each client establishes and maintains its own dedicated, persistent database connection, rapidly exhausting server connection limits.

### 5.1.2 Three-Tier Architecture ("Thin Client")
- **Structure:** Partitions responsibilities into three distinct physical and logical layers:
  1. **Presentation Tier (Client):** Executes on the user's device (web browser, mobile application). It handles display formatting and input collection without containing business or database access code ("Thin Client").
  2. **Application / Business Logic Tier (Middle Tier):** Executes on centralized application servers. It processes complex business rules, enforces domain validations, handles user authentication, and orchestrates transactions.
  3. **Database Tier (Data Tier):** Dedicated exclusively to relational storage, query execution, indexing, concurrency control, and crash recovery.
- **Advantages of Three-Tier Architecture:**
  1. **Zero Client-Side Maintenance:** Updates to business rules are deployed solely to the application server cluster.
  2. **Connection Pooling:** Application servers maintain a shared pool of open database connections, multiplexing thousands of concurrent user web sessions over a small set of database connections.
  3. **Enhanced Security:** Direct client access to the database server is completely blocked by firewalls; clients can only invoke authenticated API endpoints exposed by the middle tier.
  4. **Horizontal Scalability:** The application and database tiers can be independently scaled, load-balanced, and replicated.

### 5.1.3 Comprehensive Comparison: Two-Tier vs. Three-Tier

| Architectural Dimension | Two-Tier Client/Server | Three-Tier Client/Server |
| :--- | :--- | :--- |
| **Client Type** | Fat / Thick Client (UI + Logic) | Thin Client (UI Presentation only) |
| **Middle Tier** | Absent; direct client-to-DB link | Present (Application / Web Server) |
| **Connection Pooling** | No; each client opens a persistent DB socket | Yes; middle-tier pools and reuses connections |
| **Software Maintenance** | Costly; updating requires updating every client | Simple; updates deployed centrally to middle tier |
| **System Security** | Vulnerable; DB exposed directly to clients | High; DB completely shielded behind middle tier |
| **Scalability** | Low; max 100s of direct DB connections | Very High; millions of users via web clusters |
| **Performance over WAN** | Poor; high network chatter | Excellent; light JSON payloads over HTTP/HTTPS |

### 5.1.4 Client-Server Communication Protocols
- **Remote Procedure Call (RPC):** Enables a client program to execute a procedural subroutine located on a remote server as if it were a local function call.
- **Socket-Level Communication:** Direct, low-level bidirectional communication channels over TCP/IP ports connecting client runtime libraries to the DBMS listener process.
- **Message Queuing Systems:** Asynchronous, decoupled communication protocols (e.g., AMQP, Kafka, RabbitMQ) buffering database update messages during peak loads.

---

## 5.2 Application Programming Interfaces (APIs): ODBC & JDBC

To eliminate vendor lock-in and enable client programs written in general-purpose languages to interact with disparate DBMS backends, standardized database connectivity APIs were established.

```
+-----------------------------------------------------------------------------------+
|                           DATABASE CONNECTIVITY APIS                              |
+-------------------------------------------+---------------------------------------+
|                    ODBC                   |                 JDBC                  |
|       (Open Database Connectivity)        |      (Java Database Connectivity)     |
+-------------------------------------------+---------------------------------------+
| - Industry standard developed by Microsoft| - Standard Java API created by Sun/   |
|   and the SQL Access Group (1992).        |   Oracle Corporation.                 |
| - Based on C/C++ procedural call interface| - Object-oriented Java interface      |
|   (CLI standard).                         |   (`java.sql` and `javax.sql`).       |
| - Platform & language neutral, but widely | - Platform-independent ("Write Once,  |
|   used in Windows/C/C++ environments.     |   Run Anywhere").                     |
+-------------------------------------------+---------------------------------------+
```

### 5.2.1 Architecture of ODBC
1. **Application:** Invokes standard ODBC functions (e.g., `SQLConnect`, `SQLExecDirect`).
2. **Driver Manager:** Loads the appropriate DBMS-specific driver based on the Data Source Name (DSN) and routes API calls.
3. **Database Driver:** A dynamically linked library (DLL) that translates standard ODBC function calls into the proprietary wire protocol of the target DBMS.
4. **Data Source:** The target database server and its physical storage files.

---

### 5.2.2 Architecture of JDBC & The Four Driver Types
The JDBC framework consists of two layers: the **JDBC API** (used by Java programmers) and the **JDBC Driver API** (implemented by database vendors).

```
       +---------------------------------------------------------------+
       |                       JAVA APPLICATION                        |
       +-------------------------------+-------------------------------+
                                       |
                                       v
       +---------------------------------------------------------------+
       |                      JDBC DRIVER MANAGER                      |
       +-------+---------------+---------------+---------------+-------+
               |               |               |               |
               v               v               v               v
       +---------------+---------------+---------------+---------------+
       |    TYPE 1     |    TYPE 2     |    TYPE 3     |    TYPE 4     |
       |  JDBC-ODBC    |  Native-API   |    Network    |  Direct Pure  |
       |    Bridge     |  Partly-Java  |   Protocol    |  Java (Thin)  |
       +---------------+---------------+---------------+---------------+
               |               |               |               |
               v               v               v               v
       [ Local ODBC ]   [ Vendor Client] [ Middleware ] [ Direct TCP/IP]
       [   Driver   ]   [  C/C++ Libs  ] [   Server   ] [  DBMS Wire   ]
               |               |               |               |
               v               v               v               v
       +---------------+---------------+---------------+---------------+
       |                          TARGET DBMS                          |
       +---------------------------------------------------------------+
```

#### Detailed Breakdown of the Four JDBC Driver Types:

1. **Type 1: JDBC-ODBC Bridge Driver:**
   - Translates all JDBC calls into equivalent ODBC function calls. Requires the local machine to have both the Microsoft ODBC Driver Manager and DBMS-specific ODBC drivers installed.
   - *Status:* Completely deprecated and removed from modern Java (Java 8+). High latency and zero platform independence.
2. **Type 2: Native-API / Partly-Java Driver:**
   - Converts JDBC calls directly into native C/C++ client API calls of the target database (e.g., Oracle OCI client libraries).
   - *Weakness:* Requires proprietary vendor C/C++ native client software to be manually installed on every client machine. Breaks platform portability.
3. **Type 3: Network-Protocol / All-Java Middleware Driver:**
   - Translates JDBC calls into an independent, DBMS-neutral network protocol that is routed over sockets to an intermediate Application/Middleware Server. The middleware server then connects to the actual database.
   - Highly flexible for multi-database environments, but adds network latency.
4. **Type 4: Direct-to-Database Pure Java Driver (Thin Driver):**
   - The absolute gold standard of commercial database connectivity.
   - Written 100% in pure Java. Converts JDBC calls directly into the native wire protocol of the database engine over TCP/IP sockets (e.g., port 1521 for Oracle, 5432 for PostgreSQL, 3306 for MySQL).
   - Requires zero client-side installation or native vendor libraries. "Zero-deployment".

#### Comparison Matrix: The 4 JDBC Driver Types

| Dimension | Type 1 (Bridge) | Type 2 (Native API) | Type 3 (Network) | Type 4 (Thin Driver) |
| :--- | :--- | :--- | :--- | :--- |
| **Implementation Language** | Mixed Java / C | Mixed Java / Native C | 100% Pure Java | 100% Pure Java |
| **Client Configuration** | Heavy (ODBC + Vendor) | Heavy (Vendor client libs) | Zero (Pure Java) | **Zero (Single JAR file)** |
| **Execution Speed** | Very Slow | Fast | Moderate | **Fastest** |
| **Portability** | Low (OS dependent) | Low (Architecture dependent)| High | **Highest (Any JVM)** |
| **Current Industry Status** | Obsolete / Deprecated | Rare (Legacy systems) | Moderate (Enterprise) | **Dominant Standard (>95%)** |

---

### 5.2.3 Complete JDBC Lifecycle & Fully Annotated Java Implementation

A robust, enterprise-grade JDBC transaction adheres to a six-stage lifecycle:
1. Register and Load the Driver.
2. Establish Database Connection.
3. Create `PreparedStatement` (neutralizing SQL injection).
4. Execute Query and Retrieve `ResultSet`.
5. Process ResultSet rows iteratively.
6. Cleanly release resources via `try-with-resources`.

```java
package com.university.dbms;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * Fully annotated enterprise JDBC implementation demonstrating:
 * 1. Type 4 Thin Driver connection.
 * 2. Parameterized PreparedStatement execution.
 * 3. Atomic transaction handling with explicit COMMIT and ROLLBACK.
 * 4. Automatic resource closure (AutoCloseable).
 */
public class DatabaseManager {

    private static final String DB_URL  = "jdbc:postgresql://localhost:5432/university_db";
    private static final String USER    = "admin_user";
    private static final String PASS    = "SecurePassword#2026";

    public static void transferFunds(int fromAccount, int toAccount, double amount) {
        String debitSQL  = "UPDATE Account SET balance = balance - ? WHERE account_no = ?";
        String creditSQL = "UPDATE Account SET balance = balance + ? WHERE account_no = ?";

        // Establish connection inside try-with-resources for guaranteed socket cleanup
        try (Connection conn = DriverManager.getConnection(DB_URL, USER, PASS)) {
            
            // Step 1: Disable Auto-Commit to initiate an atomic transaction block
            conn.setAutoCommit(false);

            try (PreparedStatement debitStmt  = conn.prepareStatement(debitSQL);
                 PreparedStatement creditStmt = conn.prepareStatement(creditSQL)) {

                // Step 2: Bind parameters for debit operation
                debitStmt.setDouble(1, amount);
                debitStmt.setInt(2, fromAccount);
                int rowsDebited = debitStmt.executeUpdate();

                // Step 3: Bind parameters for credit operation
                creditStmt.setDouble(1, amount);
                creditStmt.setInt(2, toAccount);
                int rowsCredited = creditStmt.executeUpdate();

                // Step 4: Validate business constraints
                if (rowsDebited == 1 && rowsCredited == 1) {
                    // Atomically make updates permanent
                    conn.commit();
                    System.out.println("Transaction Committed Successfully: Transferred $" + amount);
                } else {
                    // Abort and rollback if any account was not found
                    conn.rollback();
                    System.err.println("Transaction Aborted: Invalid Account IDs. Rolled back.");
                }

            } catch (SQLException e) {
                // Step 5: Rollback on any SQL failure (e.g., negative balance check violation)
                conn.rollback();
                System.err.println("SQL Execution Exception: " + e.getMessage() + ". Rollback executed.");
            } finally {
                // Restore default auto-commit state
                conn.setAutoCommit(true);
            }

        } catch (SQLException e) {
            System.err.println("Database Connection Failure: " + e.getMessage());
        }
    }
}
```

---

## 5.3 Database Integrity & Declarative Repositories

Database integrity guarantees that data entered into the database is accurate, valid, and consistent across operations.

### 5.3.1 Non-Procedural vs. Procedural Integrity Constraints
1. **Non-Procedural (Declarative) Integrity Constraints:**
   - Declared directly within the schema definition using DDL.
   - Enforced automatically by the DBMS engine without requiring procedural code.
   - *Mechanisms:* `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`.
2. **Procedural Integrity Constraints:**
   - Enforced by active rules and stored procedural code (**Triggers** and **Stored Procedures**).
   - Used when constraints require multi-table queries, conditional branches, or external audits.

### 5.3.2 SQL ASSERTIONS
An **Assertion** is a declarative schema-level integrity constraint that can check predicates across **multiple tables simultaneously**. Unlike column or table-level `CHECK` constraints (which are evaluated only when the specific table is modified), an `ASSERTION` is evaluated by the DBMS whenever *any* table participating in the assertion query is modified.

```sql
-- Create an assertion ensuring that the total salary of a department 
-- never exceeds the department's authorized budget:
CREATE ASSERTION Check_Dept_Budget_Limit
CHECK (
    NOT EXISTS (
        SELECT D.dept_id
        FROM Department D
        WHERE D.budget < (
            SELECT SUM(E.salary)
            FROM Employee E
            WHERE E.dept_id = D.dept_id
        )
    )
);
```

*Commercial Reality Note:* Because evaluating assertions requires executing expensive subqueries across multiple tables on every `INSERT`, `UPDATE`, and `DELETE` across the entire database, virtually **no commercial relational DBMS (Oracle, MySQL, PostgreSQL, SQL Server) implements the standard SQL `CREATE ASSERTION` statement**. In practice, architects enforce cross-table constraints using **Triggers** or middle-tier application validations.

---

## 5.4 Database Security Mechanisms

Database security protects data against accidental disclosure, unauthorized tampering, and malicious deletion, preserving the **CIA Triad** (Confidentiality, Integrity, Availability).

```
+-----------------------------------------------------------------------------------+
|                        DATABASE ACCESS CONTROL MODELS                             |
+---------------------+---------------------+---------------------------------------+
|  DISCRETIONARY (DAC)|   MANDATORY (MAC)   |       ROLE-BASED (RBAC)               |
+---------------------+---------------------+---------------------------------------+
| - Owner-controlled  | - Central authority | - Privileges assigned to ROLES.       |
| - User grants/      | - Strict clearance  | - Users assigned to roles based on    |
|   revokes rights via|   levels & security |   job function.                       |
|   GRANT / REVOKE.   |   labels (Bell-     | - Enforces Principle of Least         |
| - Fine-grained SQL  |   LaPadula Model).  |   Privilege.                          |
+---------------------+---------------------+---------------------------------------+
```

### 5.4.1 Discretionary Access Control (DAC)
In DAC, the creator (owner) of a database object is granted full privileges on that object and can selectively bestow (grant) or withdraw (revoke) those privileges to other users.

#### Privilege Types in SQL:
- `SELECT`: Read tuples.
- `INSERT`: Add new tuples.
- `UPDATE`: Modify existing tuples (can be restricted to specific columns).
- `DELETE`: Remove tuples.
- `REFERENCES`: Right to create a foreign key referencing the table's primary key.

#### The `GRANT` Statement & `WITH GRANT OPTION`:
```sql
-- Granting read and salary-update privileges to user 'Amit':
GRANT SELECT, UPDATE (salary) ON Employee TO Amit;

-- Bestowing the right to propagate privileges to other users:
GRANT SELECT ON Employee TO Priya WITH GRANT OPTION;
```

#### The `REVOKE` Statement & Cascading Revocation:
When a grantor revokes a privilege previously bestowed `WITH GRANT OPTION`, the DBMS must determine how to handle dependent privileges:
- **`CASCADE`:** Recursively revokes the privilege from the user AND from all other users who received the privilege from that user (traversing the **Privilege Dependency Graph**).
- **`RESTRICT`:** Aborts the revoke operation if any dependent privileges exist.

```sql
-- Cascading revocation:
REVOKE SELECT ON Employee FROM Priya CASCADE;
```

---

### 5.4.2 Mandatory Access Control (MAC) & The Bell-LaPadula Model
Used in high-security military, intelligence, and government systems where data classification cannot be left to individual discretionary user decisions.

#### Security Classifications and Clearance Levels:
The system defines a strict hierarchical security scale:
$$\text{Top Secret (TS)} > \text{Secret (S)} > \text{Confidential (C)} > \text{Unclassified (U)}$$
- Every **Subject** (user, program) is assigned a **Clearance Level**: $Class(S)$.
- Every **Object** (table, tuple, attribute) is assigned a **Security Classification**: $Class(O)$.

#### The Bell-LaPadula Model Formal Axioms:

```
                  SECURITY LEVEL HIERARCHY:
                  +-----------------------+
                  |    TOP SECRET (TS)    |
                  +-----------+-----------+
                              |
                              v
                  +-----------------------+
                  |       SECRET (S)      |
                  +-----------+-----------+
                              |
                              v
                  +-----------------------+
                  |    CONFIDENTIAL (C)   |
                  +-----------+-----------+
                              |
                              v
                  +-----------------------+
                  |    UNCLASSIFIED (U)   |
                  +-----------------------+

  RULE 1: Simple Security Property (NO READ-UP)
  - Subject at Level S CANNOT read Top Secret data!
  - Class(S) >= Class(O) to READ.

  RULE 2: Star-Property / Confinement Property (NO WRITE-DOWN)
  - Subject at Level S CANNOT write/leak data down to Unclassified!
  - Class(S) <= Class(O) to WRITE.
```

1. **Simple Security Property ("No Read-Up"):**
   A subject $S$ is allowed read access to an object $O$ if and only if the clearance level of $S$ is greater than or equal to the classification of $O$:
   $$\mathbf{Class(S) \ge Class(O)}$$
   *Interpretation:* A user with "Secret" clearance can read Secret and Unclassified records, but is blocked from reading "Top Secret" documents.
2. **$\star$-Property (Star / Confinement Property) ("No Write-Down"):**
   A subject $S$ is allowed write access to an object $O$ if and only if the clearance level of $S$ is less than or equal to the classification of $O$:
   $$\mathbf{Class(S) \le Class(O)}$$
   *Interpretation:* A user with "Top Secret" clearance is strictly prohibited from writing data into an "Unclassified" table. This prevents malicious Trojan horses from copying classified data into low-security files accessible to unauthorized users (eliminating **Covert Channels**).

---

### 5.4.3 Role-Based Access Control (RBAC)
RBAC decouples users from privileges by introducing the concept of a **Role** (representing a job function or responsibility). Privileges are assigned to roles, and roles are assigned to users.

```sql
-- Step 1: Create organizational roles
CREATE ROLE BillingClerk;
CREATE ROLE MedicalOfficer;

-- Step 2: Assign granular privileges to roles
GRANT SELECT, INSERT ON PatientBilling TO BillingClerk;
GRANT SELECT, UPDATE ON PatientMedicalRecord TO MedicalOfficer;

-- Step 3: Assign roles to users
GRANT BillingClerk TO Rahul;
GRANT MedicalOfficer TO DrAarav;
```

---

### 5.4.4 SQL Injection (SQLi) Attacks and Defense In-Depth

#### The Attack Mechanism:
SQL Injection occurs when untrusted user input is directly concatenated into a dynamic SQL command string without sanitization, altering the logical syntactic structure of the query executed by the database parser.

```
VULNERABLE DYNAMIC SQL CONSTRUCTION:
  String sql = "SELECT * FROM Users WHERE username = '" + userInput + "' AND password = '" + passInput + "'";

ATTACKER INPUT:
  userInput:  admin' --
  passInput:  irrelevant

RESULTING QUERY PARSED BY DBMS:
  SELECT * FROM Users WHERE username = 'admin' --' AND password = '...';
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  The double dash (--) converts the remainder of the query into a comment!
  The password check is completely bypassed, granting instant admin access!
```

#### Taxonomy of SQL Injection Attacks:
1. **In-Band (Classic) SQLi:**
   - **Tautology / Authentication Bypass:** `' OR '1'='1`
   - **UNION-Based SQLi:** Appends a `UNION SELECT column1, column2 FROM CreditCards--` query to leak sensitive tables in the HTTP response.
2. **Inferential (Blind) SQLi:**
   - The application displays generic error pages. The attacker reconstructs data character-by-character by observing server behavior:
   - *Boolean Blind:* Injecting `AND (SUBSTRING((SELECT password FROM Users WHERE id=1), 1, 1) = 'a')`.
   - *Time-Based Blind:* Injecting `'; IF (SELECT user) = 'sa' WAITFOR DELAY '0:0:5'--`.
3. **Out-of-Band SQLi:** Exploits database DNS or HTTP resolution features to trigger external network callbacks.

#### Architectural Defenses: Why Parameterized Queries Fix SQLi
The absolute, non-negotiable defense against SQL injection is the use of **Parameterized Queries (Prepared Statements)**:

```
  +----------------------+      +----------------------+      +----------------------+
  | 1. SQL Query Template| ---> |  2. Query Parser &   | ---> | 3. Immutable Query   |
  | with Placeholders (?) |      |     Optimizer Engine |      |    Execution Plan    |
  +----------------------+      +----------------------+      +----------+-----------+
                                                                         |
                                                                         v
                                +----------------------+      +----------------------+
                                | 4. Untrusted Input   | ---> | 5. Evaluated PURELY  |
                                |    Bound as Literal  |      |    as Data Literal!  |
                                +----------------------+      +----------------------+
```

- When a `PreparedStatement` is created, the SQL text structure is sent to the DBMS Query Processor **first**, where it is parsed, compiled, and turned into an execution plan **before any user input is provided**.
- When parameters are subsequently bound via `.setString(1, userInput)`, the database engine treats that input strictly as a **scalar literal value**, never as executable SQL code. Even if the user submits `' OR '1'='1`, the DBMS literally searches for an employee whose username string is exactly the 10 characters `"admin' OR '1'='1"`.

---

### 5.4.5 Audit Trails & Database Encryption

### 1. Audit Trails (Database Auditing)
An **Audit Trail** is a tamper-resistant historical log that automatically records all operations performed on the database. It captures:
- **Who:** The authenticated database user and IP address.
- **When:** Exact timestamp.
- **What:** The exact SQL statement executed and data modified (before and after values).
- **Success/Failure:** Whether the authorization was granted or denied.

### 2. Database Encryption
- **Data in Transit:** Enforced using TLS/SSL cryptographic tunnels encrypting all network packets between client applications and database socket listeners.
- **Data at Rest (Transparent Data Encryption - TDE):** Automatically encrypts physical database files, tablespaces, and transaction log files on disk using AES-256. Prevents data theft if physical hard disks or backup tapes are stolen.
- **Cryptographic Hashing for Credentials:** Passwords must **never** be stored in plaintext. They are hashed using slow, salted cryptographic hashing functions (such as `Argon2id` or `bcrypt`) to defeat precomputed dictionary and rainbow table attacks.

---

## 5.5 High-Probability Exam Questions & Student Pitfalls

### High-Probability Exam Questions
1. **Compare Two-Tier and Three-Tier Client-Server Architectures across at least six architectural dimensions.**
2. **Explain the Four JDBC Driver Types with neat diagrams. Compare them in terms of performance, portability, and configuration overhead.**
3. **Write a complete, robust Java program demonstrating the JDBC lifecycle using `PreparedStatement` with transaction `commit` and `rollback`.**
4. **Explain Discretionary Access Control (DAC) vs. Mandatory Access Control (MAC). Formulate the two rules of the Bell-LaPadula Model (No Read-Up, No Write-Down).**
5. **What is SQL Injection? Explain how an authentication bypass attack operates and prove why Prepared Statements neutralize SQL injection.**
6. **Explain the concept of SQL Assertions. Why are assertions rarely implemented in commercial RDBMS engines?**

### Common Student Traps & Mistakes
- *Trap 1: Believing Type 4 JDBC Drivers require vendor client software.*
  - **Mistake:** Assuming Type 4 drivers need Oracle/PostgreSQL client binaries installed.
  - **Correction:** Type 4 drivers are **100% pure Java**. They talk directly to the database wire protocol via TCP/IP; no client installation is needed.
- *Trap 2: Confusing the No Write-Down rule in Bell-LaPadula.*
  - **Mistake:** Assuming higher-clearance users can write anywhere.
  - **Correction:** The Star Property strictly forbids high-clearance users from writing to lower classifications (No Write-Down) to prevent classified data leaks.
- *Trap 3: Believing client-side input validation is sufficient to prevent SQL injection.*
  - **Mistake:** Relying on JavaScript regex validation in HTML forms.
  - **Correction:** Attackers easily bypass browser validation using tools like Postman or `curl`. Only server-side **Parameterized Prepared Statements** guarantee protection.


