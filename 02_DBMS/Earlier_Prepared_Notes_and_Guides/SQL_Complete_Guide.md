# SQL Complete Guide — Zero to Advanced
### (Based on Unit 2 syllabus: Relational Model + SQL, and Lab 1–4)

> Sample tables used throughout this guide (same as your lab sheets), so you can run every query mentally against real-looking data.

**Table: `salesman`**

| salesman_id | name | city | commission |
|---|---|---|---|
| 5001 | James Hoog | New York | 0.15 |
| 5002 | Nail Knite | Paris | 0.13 |
| 5003 | Lauson Hen | San Jose | 0.12 |
| 5005 | Pit Alex | London | 0.11 |
| 5006 | Mc Lyon | Paris | 0.14 |
| 5007 | Paul Adam | Rome | 0.13 |

**Table: `customer`**

| customer_id | cust_name | city | grade | salesman_id |
|---|---|---|---|---|
| 3002 | Nick Rimando | New York | 100 | 5001 |
| 3007 | Brad Davis | New York | 200 | 5001 |
| 3005 | Graham Zusi | California | 200 | 5002 |
| 3008 | Julian Green | London | 300 | 5002 |
| 3004 | Fabian Johnson | Paris | 300 | 5006 |
| 3009 | Geoff Cameron | Berlin | 100 | 5003 |
| 3003 | Jozy Altidor | Moscow | 200 | 5007 |
| 3001 | Brad Guzan | London | NULL | 5005 |

**Table: `orders`**

| ord_no | purch_amt | ord_date | customer_id | salesman_id |
|---|---|---|---|---|
| 70001 | 150.5 | 2012-10-05 | 3005 | 5002 |
| 70009 | 270.65 | 2012-09-10 | 3001 | 5005 |
| 70002 | 65.26 | 2012-10-05 | 3002 | 5001 |
| 70004 | 110.5 | 2012-08-17 | 3009 | 5003 |
| 70007 | 948.5 | 2012-09-10 | 3005 | 5002 |
| 70005 | 2400.6 | 2012-07-27 | 3007 | 5001 |
| 70008 | 5760 | 2012-09-10 | 3002 | 5001 |
| 70010 | 1983.43 | 2012-10-10 | 3004 | 5006 |

---

## Table of Contents

1. [What is a Database & DBMS](#1-what-is-a-database--dbms)
2. [Relational Data Model](#2-relational-data-model)
3. [Keys](#3-keys)
4. [Integrity & Domain Constraints](#4-integrity--domain-constraints)
5. [Relational Algebra](#5-relational-algebra)
6. [Introduction to SQL](#6-introduction-to-sql)
7. [SQL Data Types](#7-sql-data-types)
8. [Types of SQL Commands](#8-types-of-sql-commands)
9. [Creating & Modifying Tables (DDL)](#9-creating--modifying-tables-ddl)
10. [Inserting, Updating, Deleting Data (DML)](#10-inserting-updating-deleting-data-dml)
11. [The SELECT Statement & WHERE Clause](#11-the-select-statement--where-clause)
12. [Operators in SQL](#12-operators-in-sql)
13. [Pattern Matching — LIKE & Wildcards](#13-pattern-matching--like--wildcards)
14. [Sorting & NULL handling](#14-sorting--null-handling)
15. [Aggregate Functions](#15-aggregate-functions)
16. [GROUP BY and HAVING](#16-group-by-and-having)
17. [Subqueries](#17-subqueries)
18. [Joins](#18-joins)
19. [Set Operations — UNION, INTERSECT, MINUS](#19-set-operations--union-intersect-minus)
20. [Aliases](#20-aliases)
21. [Views](#21-views)
22. [Indexes](#22-indexes)
23. [Stored Procedures](#23-stored-procedures)
24. [CASE Statement](#24-case-statement)
25. [AUTO_INCREMENT](#25-auto_increment)
26. [Cursors](#26-cursors)
27. [Comments in SQL](#27-comments-in-sql)
28. [Practice Problems — Worked Solutions](#28-practice-problems--worked-solutions)
29. [Viva Questions Bank](#29-viva-questions-bank)

---

## 1. What is a Database & DBMS

A **database** is an organized collection of related data stored electronically so it can be easily accessed, managed, and updated.

A **DBMS (Database Management System)** is software that lets you create, read, update, and delete data in a database, while handling concurrency, security, and integrity. Examples: MySQL, PostgreSQL, Oracle, SQL Server, SQLite.

**Why not just use files (like Excel/CSV)?**
- Files have data redundancy and inconsistency.
- Files can't easily enforce rules (e.g., "age must be ≥ 18").
- Files don't handle multiple users writing at the same time safely.
- Files make relationships between data (customer ↔ orders) hard to manage.

A DBMS solves all of this.

---

## 2. Relational Data Model

Proposed by E.F. Codd (1970). Data is organized into **relations (tables)**, where:

- Each **table** = a relation (e.g., `customer`).
- Each **row** = a tuple (one record — one customer).
- Each **column** = an attribute (e.g., `cust_name`, `city`).
- The set of allowed values for a column = its **domain** (e.g., `grade` can only be an integer, `city` only text).
- **Degree** = number of attributes (columns) in a relation.
- **Cardinality** = number of tuples (rows) in a relation.

Think of a table like an Excel sheet: columns are fields, rows are records — but with strict rules attached (constraints) that Excel doesn't enforce.

**Relation Schema vs Relation Instance**
- Schema = the structure/blueprint: `customer(customer_id, cust_name, city, grade, salesman_id)`
- Instance = the actual data sitting in the table right now (changes every time you insert/delete).

---

## 3. Keys

Keys are how you uniquely identify rows and link tables together.

| Key | Meaning |
|---|---|
| **Super Key** | Any column (or set of columns) that can uniquely identify a row. (Can have extra, unnecessary columns.) |
| **Candidate Key** | A *minimal* super key — no extra columns; removing any column breaks uniqueness. A table can have multiple candidate keys. |
| **Primary Key** | The candidate key chosen to uniquely identify rows. Cannot be NULL, cannot repeat. Only one per table. |
| **Alternate Key** | Candidate keys that were *not* chosen as the primary key. |
| **Foreign Key** | A column in one table that refers to the Primary Key of another table. Used to link tables (this is how relationships work). |
| **Composite Key** | A primary key made of *two or more* columns together (neither alone is unique). |

**Example from our tables:**
- `customer_id` is the **Primary Key** of `customer`.
- `salesman_id` in the `customer` table is a **Foreign Key** referencing `salesman_id` in the `salesman` table — this is how we know which salesman handles which customer.
- In `orders`, `customer_id` and `salesman_id` are both foreign keys.

```sql
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```

---

## 4. Integrity & Domain Constraints

Constraints are **rules enforced on data** so the database never ends up in a bad/inconsistent state.

| Constraint | Meaning |
|---|---|
| `NOT NULL` | Column can't be empty |
| `UNIQUE` | All values in the column must be different |
| `PRIMARY KEY` | `NOT NULL` + `UNIQUE`, uniquely identifies a row |
| `FOREIGN KEY` | Value must exist in the referenced table's primary key (prevents orphan records) |
| `CHECK` | Value must satisfy a condition, e.g. `CHECK (Age >= 18)` |
| `DEFAULT` | Sets a default value when none is given |

**Types of integrity:**
- **Domain constraint** — every attribute value must come from its declared domain/type (e.g., `grade` must be a valid integer, not "abc").
- **Entity integrity** — no primary key value can be NULL (every row must be uniquely identifiable).
- **Referential integrity** — a foreign key value must either be NULL or match an existing primary key value in the parent table (you can't have an order for a `customer_id` that doesn't exist).

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age >= 18)
);
```

---

## 5. Relational Algebra

Relational algebra is the **theoretical foundation** SQL is built on — a set of operations that take relations (tables) as input and produce a relation as output.

| Operation | Symbol | SQL equivalent | What it does |
|---|---|---|---|
| Select | σ (sigma) | `WHERE` | Filters **rows** based on a condition. `σ city='Paris'(salesman)` |
| Project | π (pi) | `SELECT column1, column2` | Filters **columns**, drops the rest |
| Union | ∪ | `UNION` | Combines rows of two *union-compatible* relations, removes duplicates |
| Set Difference | − | `MINUS` / `EXCEPT` | Rows in relation A that are NOT in relation B |
| Intersection | ∩ | `INTERSECT` | Rows common to both relations |
| Cartesian Product | × | Comma join / `CROSS JOIN` | Every row of A paired with every row of B |
| Join | ⋈ | `JOIN` | Combines rows from two tables based on a related column (essentially a filtered Cartesian product) |
| Rename | ρ (rho) | `AS` (alias) | Renames a relation or attribute |

**Example:** "Find names and cities of salesmen who commission > 0.13"

Relational algebra:
```
π name, city (σ commission > 0.13 (salesman))
```
Equivalent SQL:
```sql
SELECT name, city FROM salesman WHERE commission > 0.13;
```
This mapping (σ → WHERE, π → SELECT columns) is the key insight: **SQL is just a practical syntax for relational algebra.**

---

## 6. Introduction to SQL

**SQL (Structured Query Language)** is the standard language to communicate with a relational database.

**Characteristics of SQL:**
- Declarative — you say *what* you want, not *how* to get it (the DBMS figures out the "how").
- Non-procedural for the most part (unlike C/Java where you write step-by-step logic).
- Works on **sets** of rows at once, not one row at a time (that's what makes it powerful).
- Standardized (ANSI/ISO SQL), but every vendor (MySQL, Oracle, SQL Server, PostgreSQL) has small syntax differences.

**Advantages of SQL:**
- No coding needed for basic data operations — simple English-like syntax.
- Handles large amounts of data efficiently.
- Standardized across most database systems.
- Portable — runs on PCs, servers, laptops, even mobile devices.
- Interfaces with programming languages (Python, Java, etc.) via connectors/drivers.
- Provides different views of the same data to different users (via Views).

---

## 7. SQL Data Types

| Category | Types | Notes |
|---|---|---|
| **String** | `CHAR(size)` | Fixed length, 0–255 chars, padded with spaces |
| | `VARCHAR(size)` | Variable length, up to 65535 chars — most commonly used |
| | `TEXT(size)`, `TINYTEXT`, `BLOB` | For large text/binary data |
| **Numeric** | `INT` / `INTEGER` | Whole numbers, range ≈ ±2.1 billion |
| | `BIGINT` | Very large whole numbers |
| | `FLOAT(size, d)` / `DOUBLE(size, d)` | Decimal numbers; `d` = digits after decimal point |
| | `DECIMAL(size, d)` | Exact decimal — preferred for money |
| **Date/Time** | `DATE` | Format `YYYY-MM-DD` |
| | `DATETIME` | Format `YYYY-MM-DD hh:mm:ss` |
| | `TIMESTAMP` | Like DATETIME but stored relative to Unix epoch, auto-updatable |
| | `TIME` | `hh:mm:ss` |
| | `YEAR` | 4-digit year |

**Literals** are the actual constant values you write in SQL:
- Numeric: `10`, `65.26`, `-5`
- String/character: `'New York'`, `'James Hoog'` (single quotes)
- Date: `'2012-10-05'`

---

## 8. Types of SQL Commands

SQL commands are grouped into 5 categories:

| Category | Full form | Commands | Purpose |
|---|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Defines/changes structure of DB objects (tables, views) |
| **DML** | Data Manipulation Language | `INSERT`, `UPDATE`, `DELETE`, `SELECT`* | Manipulates the actual data |
| **DQL** | Data Query Language | `SELECT` | Retrieving data (some texts fold this into DML) |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | Controls access/permissions |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Manages transactions |

> **Viva tip:** DDL commands are *auto-committed* (permanent instantly). DML commands can be rolled back until committed.

---

## 9. Creating & Modifying Tables (DDL)

**Create a database:**
```sql
CREATE DATABASE testDB;
DROP DATABASE testDB;
```

**Create a table:**
```sql
CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    city VARCHAR(50),
    commission DECIMAL(4,2)
);
```

**Alter a table (add a column):**
```sql
ALTER TABLE salesman ADD phone VARCHAR(15);
```

**Drop a table entirely:**
```sql
DROP TABLE salesman;
```

**Backup a database:**
```sql
BACKUP DATABASE testDB TO DISK = 'filepath';
```

**Full example with constraints:**
```sql
CREATE TABLE Orders (
    OrderID INT NOT NULL,
    OrderNumber INT NOT NULL,
    OrderDate DATE DEFAULT GETDATE(),
    PersonID INT,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```

---

## 10. Inserting, Updating, Deleting Data (DML)

**INSERT — add a new row:**
```sql
-- specifying columns (safer, recommended)
INSERT INTO salesman (salesman_id, name, city, commission)
VALUES (5008, 'Ravi Kumar', 'Delhi', 0.16);

-- without specifying columns (must match table's column order exactly)
INSERT INTO salesman VALUES (5008, 'Ravi Kumar', 'Delhi', 0.16);
```

**UPDATE — modify existing rows:**
```sql
UPDATE salesman
SET commission = 0.18
WHERE salesman_id = 5008;
```
⚠️ **Always use WHERE with UPDATE**, or every row in the table gets updated!

**DELETE — remove rows:**
```sql
DELETE FROM salesman WHERE salesman_id = 5008;
```
⚠️ Same warning applies — `DELETE FROM salesman;` with no WHERE wipes the *entire table*.

---

## 11. The SELECT Statement & WHERE Clause

**Basic SELECT:**
```sql
SELECT * FROM salesman;                      -- all columns
SELECT name, commission FROM salesman;       -- specific columns
```

**DISTINCT — remove duplicate rows:**
```sql
SELECT DISTINCT salesman_id FROM orders;
```
> This answers a classic lab question: *"retrieve salesman_id of all salesmen getting orders, without repeats."*

**WHERE — filter rows:**
```sql
SELECT name, city FROM salesman WHERE city = 'Paris';
```

**Displaying a literal string or computed expression (no table needed):**
```sql
SELECT 'This is SQL Exercise, Practice and Solution';
SELECT 10, 15, 25;                 -- three numbers in three columns
SELECT 10 + 15 AS Sum;             -- sum of two numbers
SELECT (25 * 4) - 10 AS Result;    -- arithmetic expression
```

---

## 12. Operators in SQL

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `<>` or `!=` | Not equal |
| `BETWEEN` | Within a range (inclusive) |
| `IN` | Matches any value in a list |
| `LIKE` | Pattern matching (see next section) |
| `AND` | Both conditions must be true |
| `OR` | At least one condition true |
| `NOT` | Negates a condition |
| `IS NULL` / `IS NOT NULL` | Checks for missing values |
| `ANY` / `ALL` | Compares a value to a set returned by a subquery |
| `EXISTS` | True if a subquery returns at least one row |

**Examples:**
```sql
-- BETWEEN: orders with amount between 500 and 2000
SELECT * FROM orders WHERE purch_amt BETWEEN 500 AND 2000;

-- IN: customers with a specific set of grades
SELECT * FROM customer WHERE grade IN (100, 300);

-- AND / OR / NOT
SELECT * FROM customer WHERE city = 'London' AND grade = 300;
SELECT * FROM customer WHERE city = 'London' OR city = 'Paris';
SELECT * FROM customer WHERE NOT city = 'London';

-- ANY / ALL: customers whose grade is greater than ANY salesman's... (conceptual)
SELECT name FROM salesman
WHERE commission > ANY (SELECT commission FROM salesman WHERE city = 'Paris');

-- EXISTS: salesmen who have at least one customer
SELECT name FROM salesman s
WHERE EXISTS (SELECT 1 FROM customer c WHERE c.salesman_id = s.salesman_id);
```

---

## 13. Pattern Matching — LIKE & Wildcards

```sql
SELECT column1, column2 FROM table_name WHERE columnN LIKE pattern;
```

| Wildcard | Meaning | Example |
|---|---|---|
| `%` | Zero, one, or many characters | `'a%'` → starts with "a" |
| `_` | Exactly one character | `'_r%'` → "r" is the 2nd character |
| `[ ]` | Any single character within brackets (SQL Server) | `h[oa]t` → "hot" or "hat" |
| `[^ ]` | Any character NOT in brackets | `h[^oa]t` → "hit" but not "hot"/"hat" |
| `-` | Range of characters inside `[ ]` | `c[a-b]t` → "cat" or "cbt" |

**Examples:**
```sql
WHERE CustomerName LIKE 'a%'      -- starts with "a"
WHERE CustomerName LIKE '%a'      -- ends with "a"
WHERE CustomerName LIKE '%or%'    -- contains "or" anywhere
WHERE CustomerName LIKE '_r%'     -- "r" in the 2nd position
WHERE CustomerName LIKE 'a_%'     -- starts with "a", at least 2 chars long
WHERE CustomerName LIKE 'a__%'    -- starts with "a", at least 3 chars long
WHERE ContactName LIKE 'a%o'      -- starts with "a" AND ends with "o"
```

---

## 14. Sorting & NULL handling

**ORDER BY:**
```sql
SELECT * FROM customer ORDER BY grade DESC;                  -- descending
SELECT * FROM customer ORDER BY city ASC, grade DESC;        -- multi-column sort
```
Default sort order is `ASC` if not specified.

**NULL checks** — you can NEVER use `= NULL`, you must use `IS NULL`:
```sql
SELECT * FROM customer WHERE grade IS NULL;      -- Brad Guzan has no grade
SELECT * FROM customer WHERE grade IS NOT NULL;
```

**LIMIT / TOP** — restrict number of rows returned:
```sql
SELECT * FROM orders ORDER BY purch_amt DESC LIMIT 5;    -- MySQL/Postgres style
-- SQL Server style: SELECT TOP 5 * FROM orders ORDER BY purch_amt DESC;
```

---

## 15. Aggregate Functions

Aggregate functions operate on a **set of rows** and return a **single value**.

| Function | Purpose |
|---|---|
| `COUNT()` | Number of rows |
| `SUM()` | Total of a numeric column |
| `AVG()` | Average of a numeric column |
| `MIN()` | Smallest value |
| `MAX()` | Largest value |

```sql
SELECT COUNT(*) FROM orders;                       -- total number of orders
SELECT SUM(purch_amt) FROM orders;                  -- total purchase amount
SELECT AVG(purch_amt) FROM orders;                  -- average purchase amount
SELECT MAX(purch_amt) FROM orders;                  -- biggest order
SELECT MIN(purch_amt) FROM orders;                  -- smallest order
SELECT COUNT(DISTINCT salesman_id) FROM orders;     -- number of unique salesmen with orders
```

> **Important rule:** Aggregate functions ignore NULL values (except `COUNT(*)`, which counts rows regardless of NULLs).

---

## 16. GROUP BY and HAVING

`GROUP BY` splits rows into groups so an aggregate function runs **per group** instead of on the whole table. `HAVING` filters those *groups* (unlike `WHERE`, which filters individual rows *before* grouping).

```sql
SELECT customer_id, MAX(purch_amt) AS highest
FROM orders
GROUP BY customer_id;
-- "highest purchase amount ordered by each customer, with their ID"

SELECT customer_id, ord_date, MAX(purch_amt) AS highest
FROM orders
GROUP BY customer_id, ord_date;
-- highest purchase per customer PER DATE

SELECT salesman_id, COUNT(*) AS num_customers
FROM customer
GROUP BY salesman_id
HAVING COUNT(*) > 1;
-- salesmen who have more than one customer
```

**Order of execution (very important, common viva question):**
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

**WHERE vs HAVING:**

| | WHERE | HAVING |
|---|---|---|
| Filters | Individual rows | Groups (after aggregation) |
| Can use aggregate functions? | ❌ No | ✅ Yes |
| Runs | Before GROUP BY | After GROUP BY |

---

## 17. Subqueries

A **subquery** (inner query / nested query) is a query inside another query. It runs first, and its result is used by the outer query.

**Types:**
- **Single-row subquery** — returns one value, use with `=`, `>`, `<` etc.
- **Multi-row subquery** — returns multiple values, use with `IN`, `ANY`, `ALL`.
- **Correlated subquery** — inner query references a column from the outer query, so it re-runs once per outer row.

```sql
-- Single-row: customers with grade greater than the average grade
SELECT cust_name FROM customer
WHERE grade > (SELECT AVG(grade) FROM customer);

-- Multi-row IN: customers who have placed an order
SELECT cust_name FROM customer
WHERE customer_id IN (SELECT customer_id FROM orders);

-- Subquery in WHERE with EXISTS
SELECT name FROM salesman s
WHERE EXISTS (SELECT * FROM customer c WHERE c.salesman_id = s.salesman_id);

-- Subquery in FROM (must alias it)
SELECT city, avg_grade FROM
  (SELECT city, AVG(grade) AS avg_grade FROM customer GROUP BY city) AS city_avg
WHERE avg_grade > 150;
```

---

## 18. Joins

Joins combine rows from two or more tables based on a related column, most commonly a foreign key ↔ primary key relationship.

### INNER JOIN
Returns only rows where there's a match in **both** tables.
```sql
SELECT c.cust_name, s.name AS salesman_name
FROM customer c
INNER JOIN salesman s ON c.salesman_id = s.salesman_id;
```

### LEFT (OUTER) JOIN
All rows from the left table, plus matched rows from the right (unmatched → NULL).
```sql
SELECT c.cust_name, o.ord_no
FROM customer c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
-- shows customers even if they've placed NO orders
```

### RIGHT (OUTER) JOIN
All rows from the right table, plus matched rows from the left.
```sql
SELECT c.cust_name, o.ord_no
FROM orders o
RIGHT JOIN customer c ON o.customer_id = c.customer_id;
```

### FULL OUTER JOIN
All rows from both tables; unmatched sides get NULLs.
```sql
SELECT c.cust_name, o.ord_no
FROM customer c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;
```
*(MySQL has no native FULL OUTER JOIN — simulate with `LEFT JOIN UNION RIGHT JOIN`.)*

### SELF JOIN
A table joined with itself — useful for comparing rows within the same table.
```sql
SELECT a.name AS salesman1, b.name AS salesman2, a.city
FROM salesman a, salesman b
WHERE a.city = b.city AND a.salesman_id <> b.salesman_id;
-- pairs of salesmen who work in the same city
```

### CROSS JOIN (Cartesian Product)
Every row of table A paired with every row of table B (no ON condition).
```sql
SELECT s.name, c.cust_name
FROM salesman s
CROSS JOIN customer c;
-- if salesman has 6 rows and customer has 8 rows → 48 rows result
```

**Visual summary:**
```
INNER JOIN     → only the overlap
LEFT JOIN      → everything on the left + overlap
RIGHT JOIN     → everything on the right + overlap
FULL OUTER     → everything from both sides
CROSS JOIN     → every combination (no condition)
```

---

## 19. Set Operations — UNION, INTERSECT, MINUS

These combine the **results of two SELECT queries**. Rules: same number of columns, compatible data types, column order matters.

```sql
-- UNION: combines rows, removes duplicates
SELECT name FROM salesman
UNION
SELECT cust_name FROM customer;

-- UNION ALL: combines rows, KEEPS duplicates (faster, no dedup step)
SELECT name FROM salesman
UNION ALL
SELECT cust_name FROM customer;

-- INTERSECT: rows common to both queries
SELECT city FROM salesman
INTERSECT
SELECT city FROM customer;

-- MINUS (Oracle) / EXCEPT (SQL Server, Postgres): rows in first query NOT in second
SELECT city FROM customer
MINUS
SELECT city FROM salesman;
```

> MySQL doesn't support `INTERSECT`/`MINUS` natively (added INTERSECT/EXCEPT from v8.0.31) — older MySQL simulates them with `IN` / `NOT IN` / joins.

---

## 20. Aliases

Temporary names given to a table or column, useful for readability and required for self-joins/subqueries.
```sql
SELECT cust_name AS Customer, city AS Location FROM customer;
SELECT * FROM customer AS c WHERE c.grade = 200;
```

---

## 21. Views

A **view** is a virtual table based on the result of a saved SELECT query. It doesn't store data itself — it re-runs the underlying query every time you use it.

```sql
CREATE VIEW ny_salesmen AS
SELECT salesman_id, name, city
FROM salesman
WHERE city = 'New York';

SELECT * FROM ny_salesmen;    -- use it just like a table

CREATE OR REPLACE VIEW ny_salesmen AS
SELECT salesman_id, name FROM salesman WHERE city = 'New York';

DROP VIEW ny_salesmen;
```

**Why use views?**
- Simplify complex/repeated joins into a single reusable object.
- Restrict access — show only certain columns/rows to certain users (security).
- Present a consistent interface even if underlying tables change.

---

## 22. Indexes

An **index** speeds up data retrieval (like a book's index) at the cost of extra storage and slightly slower writes (INSERT/UPDATE/DELETE need to update the index too).

```sql
CREATE INDEX idx_city ON customer (city);
CREATE UNIQUE INDEX idx_custname ON customer (cust_name);
ALTER TABLE customer DROP INDEX idx_city;
```
Users never "see" an index directly — it just makes `WHERE`/`JOIN`/`ORDER BY` on that column faster. Primary keys get an index automatically.

---

## 23. Stored Procedures

A **stored procedure** is precompiled SQL code saved in the database, so it can be executed repeatedly without rewriting it.

```sql
CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;

EXEC SelectAllCustomers;

-- with a parameter
CREATE PROCEDURE SelectCustomersByCity @City nvarchar(30)
AS
SELECT * FROM Customers WHERE City = @City
GO;

EXEC SelectCustomersByCity @City = 'Hamirpur';

-- with multiple parameters
CREATE PROCEDURE SelectCustomersByCityAndPostal
    @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
```
**Benefits:** reusability, better performance (precompiled), reduced network traffic, centralized business logic, improved security (users can be given EXEC rights without direct table access).

---

## 24. CASE Statement

SQL's version of if-else logic, used inside a SELECT.
```sql
SELECT ord_no, purch_amt,
CASE
    WHEN purch_amt > 1000 THEN 'High Value'
    WHEN purch_amt = 1000 THEN 'Exactly 1000'
    ELSE 'Low Value'
END AS OrderCategory
FROM orders;
```

---

## 25. AUTO_INCREMENT

Automatically generates a unique number for a column whenever a new row is inserted — commonly used for primary keys.
```sql
CREATE TABLE Persons (
    PersonId INT AUTO_INCREMENT PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    Age INT
);
-- start at 10, increment by 5 each time (MySQL syntax varies):
ALTER TABLE Persons AUTO_INCREMENT = 10;
```

---

## 26. Cursors

A **cursor** is a database object used to retrieve and process query results **row by row**, instead of all at once as SQL normally does. Used inside stored procedures / PL-SQL when you need row-level procedural logic that plain SQL can't express.

```sql
DECLARE cust_cursor CURSOR FOR
    SELECT cust_name FROM customer WHERE grade = 200;

OPEN cust_cursor;
FETCH NEXT FROM cust_cursor INTO @name;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @name;
    FETCH NEXT FROM cust_cursor INTO @name;
END;

CLOSE cust_cursor;
DEALLOCATE cust_cursor;
```
**Downside:** cursors are slow (row-by-row) compared to set-based SQL — use only when a set-based query genuinely can't do the job.

---

## 27. Comments in SQL

```sql
-- This is a single-line comment
SELECT * FROM Customers;

/* This is a
   multi-line comment */
SELECT * FROM Customers;
```

---

## 28. Practice Problems — Worked Solutions

*(A worked sample from each lab, showing you the thought process — try the rest of your lab sheet yourself using these as a template.)*

**Q: Total and average purchase amount of all orders.**
```sql
SELECT SUM(purch_amt) AS total, AVG(purch_amt) AS average FROM orders;
```

**Q: Highest purchase amount for each customer, with ID and date.**
```sql
SELECT customer_id, ord_date, MAX(purch_amt) AS highest
FROM orders
GROUP BY customer_id, ord_date;
```

**Q: Customers whose highest order in a day is within {2000, 3000, 5760, 6000}.**
```sql
SELECT customer_id, MAX(purch_amt) AS highest
FROM orders
GROUP BY customer_id
HAVING MAX(purch_amt) IN (2000, 3000, 5760, 6000);
```

**Q: Salesman name, customer name, and city where salesman & customer are from the same city.**
```sql
SELECT s.name AS salesman_name, c.cust_name, c.city
FROM salesman s
INNER JOIN customer c ON s.city = c.city;
```

**Q: View for salesmen from New York.**
```sql
CREATE VIEW ny_salesmen_view AS
SELECT salesman_id, name, city FROM salesman WHERE city = 'New York';
```

**Q: List salesmen who work for more than one customer.**
```sql
SELECT s.name, COUNT(c.customer_id) AS num_customers
FROM salesman s
JOIN customer c ON s.salesman_id = c.salesman_id
GROUP BY s.name
HAVING COUNT(c.customer_id) > 1;
```

**Q: Cartesian product between salesman and customer.**
```sql
SELECT s.name, c.cust_name FROM salesman s, customer c;
-- equivalent to: SELECT s.name, c.cust_name FROM salesman s CROSS JOIN customer c;
```

**Q: Salesman and customer who does NOT live in the same city, and commission > 12%.**
```sql
SELECT s.name, c.cust_name, s.city AS salesman_city, c.city AS customer_city
FROM salesman s
JOIN customer c ON s.salesman_id = c.salesman_id
WHERE s.city <> c.city AND s.commission > 0.12;
```

---

## 29. Viva Questions Bank

### A. Basics / Relational Model
1. What is a database vs a DBMS?
2. What is a relation, tuple, attribute, domain, degree, and cardinality?
3. What's the difference between a relation schema and a relation instance?
4. Why is the relational model called "relational"?
5. What is data redundancy, and how does the relational model reduce it?

### B. Keys
6. Differentiate between primary key, candidate key, and super key.
7. Can a table have more than one candidate key? Can it have more than one primary key?
8. What is a composite key? Give an example.
9. What is a foreign key, and what problem does it solve?
10. Can a foreign key value be NULL? Can a primary key value be NULL?
11. What is a self-referencing foreign key?

### C. Constraints
12. What is the difference between entity integrity and referential integrity?
13. What does the `CHECK` constraint do? Give an example.
14. What happens if you try to insert a duplicate value into a `UNIQUE` column?
15. What is a `DEFAULT` constraint used for?
16. What is domain constraint, with an example?

### D. Relational Algebra
17. What are the fundamental operations of relational algebra?
18. Map SELECT (σ) and PROJECT (π) to their SQL equivalents.
19. What is the difference between a Cartesian Product and a Join in relational algebra?
20. Is relational algebra procedural or non-procedural? How does that compare to SQL?

### E. SQL Basics & Commands
21. What are the categories of SQL commands (DDL, DML, DCL, TCL)? Give one example command in each.
22. Is `SELECT` a DDL, DML, or DQL command?
23. Difference between `DELETE`, `TRUNCATE`, and `DROP`.
24. Why can `DROP`/`TRUNCATE` not usually be rolled back, but `DELETE` can?
25. What is the difference between `CHAR` and `VARCHAR`?
26. When would you use `DECIMAL` instead of `FLOAT`?
27. What's the difference between `DATE`, `DATETIME`, and `TIMESTAMP`?

### F. Queries, WHERE, Operators
28. What does `SELECT DISTINCT` do, and how is it different from plain `SELECT`?
29. Difference between `WHERE` and `HAVING`.
30. What's the difference between `IN` and `BETWEEN`?
31. Why can't you write `WHERE grade = NULL`? What's the correct syntax?
32. What is the difference between `=` and `LIKE`?
33. Explain the `%` and `_` wildcards with an example each.
34. What do `ANY` and `ALL` operators do? How are they different?
35. What does the `EXISTS` operator return, and when would you use it over `IN`?

### G. Aggregate Functions & Grouping
36. Name the 5 standard aggregate functions.
37. Does `COUNT(*)` count NULLs? Does `COUNT(column_name)`?
38. What is the purpose of `GROUP BY`?
39. Why can't you filter on an aggregate function using `WHERE`? What must you use instead?
40. What is the logical order of execution of a SQL query (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)?
41. Can you `GROUP BY` more than one column? What does that do?

### H. Subqueries
42. What is a subquery? Where can subqueries appear in a SQL statement (WHERE, FROM, SELECT)?
43. What is a correlated subquery, and how is it different from a regular (non-correlated) subquery?
44. When would you use a subquery vs a JOIN to solve the same problem?
45. Can a subquery return more than one column? More than one row?

### I. Joins
46. What is the difference between INNER JOIN and OUTER JOIN?
47. Explain LEFT JOIN with an example — what happens to unmatched rows?
48. What is a self-join, and why would you need table aliases for it?
49. What is a Cartesian product / CROSS JOIN, and when might it happen accidentally?
50. If table A has 5 rows and table B has 3 rows, how many rows can a CROSS JOIN produce?
51. Difference between `NATURAL JOIN` and `INNER JOIN ... ON`.

### J. Set Operations
52. What are the requirements for using `UNION` on two SELECT queries?
53. Difference between `UNION` and `UNION ALL`.
54. What does `INTERSECT` return? What does `MINUS`/`EXCEPT` return?
55. Does `UNION` allow duplicate rows in the result? Does `UNION ALL`?

### K. Views, Indexes, Procedures
56. What is a view, and does it store data physically?
57. Give two reasons you would use a view.
58. What is an index, and what's the trade-off of creating too many indexes?
59. What is a stored procedure, and what are its advantages over sending raw SQL each time?
60. Can a stored procedure accept parameters? Give a syntax example.

### L. Miscellaneous / Advanced
61. What is a cursor, and why is it generally slower than a set-based SQL query?
62. What does `AUTO_INCREMENT` do?
63. Explain the `CASE` statement with a short example.
64. What is the difference between a clustered and non-clustered index? *(bonus/advanced)*
65. What is normalization, and why is it related to good relational design? *(bonus/advanced)*
66. What is ACID in the context of transactions? *(bonus/advanced)*

---

### How to use this file to actually learn
1. Read sections 1–8 first (theory) — don't skip, viva questions come heavily from here.
2. Then open a free online SQL sandbox (e.g., SQLite/MySQL playground) and type out every query in sections 9–19 yourself using the sample tables above.
3. Do your Lab 1–4 questions one by one — you now have the syntax pattern for every single one of them in this file.
4. Test yourself with Section 29 (viva bank) out loud, without looking, before your viva.

Good luck — SQL is 90% pattern recognition once you've typed enough queries by hand.
