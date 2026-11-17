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
