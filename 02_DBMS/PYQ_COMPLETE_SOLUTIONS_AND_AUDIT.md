# DATABASE MANAGEMENT SYSTEMS (ITDC0207)
## NIT JALANDHAR PYQ MASTER SOLUTION COMPENDIUM & COVERAGE AUDIT
### Fully Solved Examination Papers: Dec 2025 (End-Sem), Sept 2026 (Mid-Sem), Sept 2025 (Mid-Sem)

---

# SECTION 1: 100% SYLLABUS & THEORY COVERAGE AUDIT

| Exam Paper | Q# | Topic / Concept Tested | Covered in Theory Notes |
| :--- | :---: | :--- | :--- |
| **Sept 2026 Mid-Sem** | Q1(a) | Complete Enterprise ER Diagram (NITJ Research & Academic System) | Unit 1 (§1.5 ER Modeling, Cardinalities, Weak Entities, Roles) |
| **Sept 2026 Mid-Sem** | Q1(b) | ER-to-Relational Schema Conversion Rules | Unit 1 (§1.6 Relational Reduction Rules for 1:1, 1:N, M:N) |
| **Sept 2026 Mid-Sem** | Q1(c) | Identification & Justification of 4 Critical Integrity Constraints | Unit 2 (§2.1 Domain, Entity, Referential & Check Constraints) |
| **Sept 2026 Mid-Sem** | Q2(a)–(e) | Complex Queries in Relational Algebra, TRC, and DRC | Unit 2 (§2.2 Relational Algebra, §2.3 TRC, §2.4 DRC) |
| **Sept 2025 Mid-Sem** | Q1 | Notown Records Conceptual Schema, ERD, SQL DDL, Uncapturable Constraints | Unit 1 (§1.5 ER Design), Unit 2 (§2.5 SQL DDL Constraints) |
| **Sept 2025 Mid-Sem** | Q2(a)–(e) | Student/Course/Enroll/Professor Queries in RA, TRC, DRC | Unit 2 (§2.2, §2.3, §2.4 Formal Query Languages) |
| **Dec 2025 End-Sem** | Q1(a)–(e) | Suppliers/Parts/Catalog Queries in Relational Algebra & TRC | Unit 2 (§2.2 Relational Division, §2.3 Tuple Calculus) |
| **Dec 2025 End-Sem** | Q2(a)–(e) | Disk Physics (Sector, Track, Surface, Capacity, Cylinder, Block size, Latency, Transfer rate) | Unit 5 (§5.1 Physical Database Storage Architecture) |
| **Dec 2025 End-Sem** | Q3(a)–(c) | Concurrency Schedules Venn Diagram (2PL, Strict 2PL, Conservative, Timestamp, MVCC) | Unit 4 (§4.2 Serializability, §4.3 Concurrency Control Protocols) |
| **Dec 2025 End-Sem** | Q4(a),(b) | Strongest Normal Form Determination & BCNF Decomposition (5 Subrelations) | Unit 3 (§3.2 FDs & Closures, §3.3 Normal Forms 1NF to BCNF) |
| **Dec 2025 End-Sem** | Q5(a),(b) | ARIES Recovery Architecture: Analysis, Redo, Undo phases & Crash Trace Walkthrough | Unit 4 (§4.5 Database Recovery, ARIES Algorithm & Log Traces) |

---

# SECTION 2: COMPLETE MATHEMATICAL & RELATIONAL QUERY MASTER SOLUTIONS

### 1. Dec 2025 End-Sem Q1: Suppliers-Parts-Catalog Queries
**Schema**:
* `Suppliers(sid: integer, sname: string, address: string)`
* `Parts(pid: integer, pname: string, color: string)`
* `Catalog(sid: integer, pid: integer, cost: real)`

#### Query (a): Find the sids of suppliers who supply every red part or supply every green part.
* **Relational Algebra**:
  $$\text{RedParts} \leftarrow \pi_{pid}(\sigma_{color='red'}(Parts))$$
  $$\text{GreenParts} \leftarrow \pi_{pid}(\sigma_{color='green'}(Parts))$$
  $$\text{SuppliersRed} \leftarrow \pi_{sid, pid}(Catalog) / \text{RedParts}$$
  $$\text{SuppliersGreen} \leftarrow \pi_{sid, pid}(Catalog) / \text{GreenParts}$$
  $$\mathbf{Result} = \text{SuppliersRed} \cup \text{SuppliersGreen}$$
* **Tuple Relational Calculus (TRC)**:
  $$\{ s | \exists c \in Catalog (s[sid] = c[sid]) \land [ (\forall p \in Parts (p[color]='red' \implies \exists c1 \in Catalog (c1[sid]=s[sid] \land c1[pid]=p[pid]))) \lor (\forall p \in Parts (p[color]='green' \implies \exists c2 \in Catalog (c2[sid]=s[sid] \land c2[pid]=p[pid]))) ] \}$$

#### Query (b): Find pairs of sids such that the supplier with the first sid charges more for some part than the supplier with the second sid.
* **Relational Algebra**:
  $$\mathbf{Result} = \pi_{C1.sid, C2.sid} (\sigma_{C1.pid = C2.pid \land C1.cost > C2.cost} (\rho_{C1}(Catalog) \times \rho_{C2}(Catalog)))$$
* **TRC**:
  $$\{ t | \exists c1 \in Catalog \exists c2 \in Catalog (c1[pid] = c2[pid] \land c1[cost] > c2[cost] \land t[sid1] = c1[sid] \land t[sid2] = c2[sid]) \}$$

#### Query (c): Find the pids of parts supplied by at least two different suppliers.
* **Relational Algebra**:
  $$\mathbf{Result} = \pi_{C1.pid} (\sigma_{C1.pid = C2.pid \land C1.sid \ne C2.sid} (\rho_{C1}(Catalog) \times \rho_{C2}(Catalog)))$$
* **TRC**:
  $$\{ t | \exists c1 \in Catalog \exists c2 \in Catalog (c1[pid] = c2[pid] \land c1[sid] \ne c2[sid] \land t[pid] = c1[pid]) \}$$

#### Query (d): Find the pids of the most expensive parts supplied by suppliers named Yosemite Sham.
* **Relational Algebra**:
  $$YS\_Catalog \leftarrow \pi_{pid, cost}(Catalog \bowtie \sigma_{sname='Yosemite\ Sham'}(Suppliers))$$
  $$Lower\_Parts \leftarrow \pi_{Y1.pid}(\sigma_{Y1.cost < Y2.cost}(\rho_{Y1}(YS\_Catalog) \times \rho_{Y2}(YS\_Catalog)))$$
  $$\mathbf{Result} = \pi_{pid}(YS\_Catalog) - Lower\_Parts$$

#### Query (e): Find the pids of parts supplied by every supplier at less than $200.
* **Relational Algebra**:
  $$AllSuppliers \leftarrow \pi_{sid}(Suppliers)$$
  $$Under200 \leftarrow \pi_{sid, pid}(\sigma_{cost < 200}(Catalog))$$
  $$\mathbf{Result} = Under200 / AllSuppliers$$

---

### 2. Dec 2025 End-Sem Q2: Hard Disk Physical Organization
**Given**:
* Sector size $= 512$ bytes
* Tracks per surface $= 2,000$ tracks
* Sectors per track $= 50$ sectors
* Platters $= 5$ double-sided platters $\implies$ Surfaces $= 5 \times 2 = \mathbf{10\text{ surfaces}}$
* Rotational speed $= 5,400$ RPM
* Average seek time $= 10$ ms

#### Solutions:
* **a) Capacities**:
  - **Track Capacity**: $50\text{ sectors} \times 512\text{ bytes} = 25,600\text{ bytes} = \mathbf{25\text{ KiB}}$
  - **Surface Capacity**: $2,000\text{ tracks} \times 25,600\text{ bytes} = 51,200,000\text{ bytes} = \mathbf{51.2\text{ MB}}$
  - **Disk Capacity**: $10\text{ surfaces} \times 51.2\text{ MB} = 512,000,000\text{ bytes} = \mathbf{512\text{ MB}}$
* **b) Number of Cylinders**:
  - A cylinder consists of tracks at the same radial position across all surfaces.
  - $\mathbf{\text{Cylinders}} = \text{Tracks per surface} = \mathbf{2,000\text{ cylinders}}$.
* **c) Block Size Validity**:
  - In file systems, a block must be a contiguous integer multiple of the physical sector size ($512$ bytes).
  - **256 bytes**: **INVALID** (smaller than minimum sector size; sub-sector allocation is physically unsupported).
  - **2,048 bytes**: **VALID** ($4 \times 512$ bytes $= 4$ sectors).
  - **51,200 bytes**: **VALID** ($100 \times 512$ bytes $= 2$ full tracks).
* **d) Maximum Rotational Delay**:
  - At $5,400$ RPM, time for one full revolution:
    $$T_{rev} = \frac{60\text{ s}}{5400} = \frac{1}{90}\text{ s} \approx 0.01111\text{ s} = \mathbf{11.11\text{ ms}}$$
  - **Maximum Rotational Delay** $= T_{rev} = \mathbf{11.11\text{ ms}}$ (when read head just misses the target sector).
* **e) Transfer Rate**:
  - One track ($25,600$ bytes) is transferred in one revolution ($0.01111$ s):
    $$\text{Transfer Rate} = \frac{25,600\text{ bytes}}{0.011111\text{ s}} = 2,304,000\text{ B/s} \approx \mathbf{2.304\text{ MB/s}}$$

---

### 3. Dec 2025 End-Sem Q4: Normal Forms & BCNF Decomposition

#### Subrelation I: $R1(A, C, B, D, E)$ with $A \to B, C \to D$
* **Candidate Key**: Closure $(ACE)^+ = ACEBD = R1 \implies$ Candidate Key is **$ACE$**.
* **Analysis**:
  - $A \to B$: $A$ is a proper subset of candidate key $ACE$, and $B$ is a non-prime attribute $\implies$ **Partial Dependency** exists! Violates 2NF.
* **Strongest Normal Form**: **1NF**.
* **BCNF Decomposition**:
  1. For $A \to B$: Decompose into $R_{11}(A, B)$ (Key: $A$) and $R'(A, C, D, E)$.
  2. In $R'$, $C \to D$: Decompose into $R_{12}(C, D)$ (Key: $C$) and $R_{13}(A, C, E)$ (Key: $ACE$).
  - **Final BCNF Relations**: **$R_{11}(A, B), R_{12}(C, D), R_{13}(A, C, E)$**.

#### Subrelation II: $R2(A, B, F)$ with $AC \to E, B \to F$
* **Candidate Key**: $(AB)^+ = ABF \implies$ Candidate Key is **$AB$**.
* **Analysis**:
  - $B \to F$: $B$ is a proper subset of candidate key $AB$, and $F$ is non-prime $\implies$ **Partial Dependency** exists!
* **Strongest Normal Form**: **1NF** (Violates 2NF due to partial dependency).
* **BCNF Decomposition**:
  - Decompose using $B \to F$: **$R_{21}(B, F)$** (Key: $B$) and **$R_{22}(A, B)$** (Key: $AB$).

#### Subrelation III: $R3(A, D)$ with global FDs $D \to G, G \to H$
* Attributes $G$ and $H$ do not appear in $R3$.
* Projection of FDs on $R3$: Only trivial FDs hold.
* **Candidate Key**: **$AD$**.
* **Strongest Normal Form**: **BCNF** (Since only trivial FDs hold on $R3$).

#### Subrelation IV: $R4(D, C, H, G)$ with global FDs $A \to I, I \to A$
* None of $A$ or $I$ belong to $R4$.
* Projection of FDs on $R4$: No non-trivial FDs.
* **Candidate Key**: **$DCHG$**.
* **Strongest Normal Form**: **BCNF**.

#### Subrelation V: $R5(A, I, C, E)$ with $A \to I, I \to A$
* **Candidate Keys**:
  - $(ACE)^+ = ACEI \implies ACE$ is a candidate key.
  - $(ICE)^+ = ICEA \implies ICE$ is a candidate key.
* Prime attributes: $\{A, I, C, E\}$ (All attributes are prime!).
* In $A \to I$: $A$ is not a superkey, but $I$ is prime $\implies$ satisfies 3NF, but violates BCNF ($A$ is not a superkey).
* **Strongest Normal Form**: **3NF**.
* **BCNF Decomposition**:
  - Decompose using $A \to I$: **$R_{51}(A, I)$** (Key: $A$) and **$R_{52}(A, C, E)$** (Key: $ACE$).

---

### 4. Dec 2025 End-Sem Q5: ARIES Recovery Architecture
* **(a) Roles of ARIES Phases**:
  1. **Analysis Phase**: Scans log **forward** from the last checkpoint to identify:
     - Dirty pages in buffer pool at crash time $\implies$ rebuilds **Dirty Page Table (DPT)**.
     - Active transactions at crash time $\implies$ rebuilds **Transaction Table (TT)** to determine the **Undo list (Losers)**.
  2. **Redo Phase**: Scans log **forward** from the smallest `recLSN` across all pages in the DPT up to the crash point. **Repeats history** (reapplying both committed and uncommitted changes) to restore database buffer state to the exact moment of crash.
  3. **Undo Phase**: Scans log **backward** from the crash point, reversing all actions of transactions in the Undo list (Losers) and writing Compensation Log Records (CLRs) to ensure idempotence during repeated crashes.
* **(b) Figure 1 Crash Execution Analysis**:
  - **I. Analysis Phase**: Begins at `begin_checkpoint` (**LSN 00**) and scans forward to crash point (**LSN 70**).
    - At LSN 40, T2 commits; at LSN 50, T2 ends $\implies$ T2 removed from TT.
    - At LSN 70, T1 has an abort record but has not finished rolling back $\implies$ T1 is active (Loser).
    - T3 wrote P3 at LSN 60 and never committed $\implies$ T3 is active (Loser).
    - **Final Transaction Table**: $TT = \{ T1: \text{status}=\text{aborted}, T3: \text{status}=\text{active} \}$.
    - **Loser Transactions (Undo List)**: **$\{ T1, T3 \}$**.
    - **Dirty Page Table**: $DPT = \{ P5: \text{recLSN}=20, P3: \text{recLSN}=30 \}$.
  - **II. Redo Phase**: Begins at the **smallest `recLSN` in DPT = LSN 20** (update T1 writes P5) and ends at the end of the log (**LSN 70**).
  - **III. Undo Phase**: Begins at the latest log record of the loser transactions (**LSN 70**) and scans backward, undoing actions of T3 and T1 until all their log records are undone down to LSN 20.
