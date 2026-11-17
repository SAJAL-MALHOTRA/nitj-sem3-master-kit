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
