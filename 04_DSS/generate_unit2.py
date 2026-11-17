# generate_unit2.py
# Generates Unit 2: Set Theory, Relations, Functions, Posets, Lattices, Counting, Number Theory, Probability, Recurrence

def get_unit2_text():
    return r"""# UNIT 2: SET THEORY, RELATIONS, FUNCTIONS, POSETS, LATTICES, COUNTING & DISCRETE STRUCTURES

---

## 2.1 SET THEORY FOUNDATIONS & ALGEBRA OF SETS

### 2.1.1 Definitions and Fundamental Notation
A **set** is a well-defined, unordered collection of distinct mathematical objects called **elements** or **members**.
- **Well-defined**: For any candidate object $x$ and set $S$, the proposition $x \in S$ has an unambiguous truth value ($T$ or $F$).
- **Roster (Tabular) Form**: Explicit enumeration, e.g., $S = \{2, 3, 5, 7, 11\}$.
- **Set-Builder Form**: Predicative specification, e.g., $S = \{x \in \mathbb{Z} \mid x \ge 0 \land x \text{ is prime} \land x \le 11\}$.
- **Cardinality ($|S|$)**: The number of distinct elements in $S$. For an empty set $\emptyset = \{\}$, $|\emptyset| = 0$.

### 2.1.2 Set Operations & Set-Theoretic Identities
Let $U$ be the universal set, and $A, B \subseteq U$:

1. **Union ($A \cup B$)**:
   $$A \cup B = \{x \in U \mid x \in A \lor x \in B\}$$
2. **Intersection ($A \cap B$)**:
   $$A \cap B = \{x \in U \mid x \in A \land x \in B\}$$
   - If $A \cap B = \emptyset$, $A$ and $B$ are **mutually disjoint**.
3. **Set Difference / Relative Complement ($A \setminus B$ or $A - B$)**:
   $$A \setminus B = \{x \in U \mid x \in A \land x \notin B\} = A \cap \overline{B}$$
4. **Symmetric Difference ($A \Delta B$ or $A \oplus B$)**:
   $$A \Delta B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B) = \{x \in U \mid x \in A \oplus x \in B\}$$
5. **Absolute Complement ($\overline{A}$ or $A^c$ or $A'$)**:
   $$\overline{A} = U \setminus A = \{x \in U \mid x \notin A\}$$

```
     UNION (A ∪ B)               INTERSECTION (A ∩ B)           DIFFERENCE (A \ B)
  ┌─────────────────┐             ┌─────────────────┐             ┌─────────────────┐
  │ ┌────┐   ┌────┐ │             │ ┌────┐   ┌────┐ │             │ ┌────┐   ┌────┐ │
  │ │░░░░┼───┼░░░░│ │             │ │    │░░░│    │ │             │ │░░░░│   │    │ │
  │ │░░░░│░░░│░░░░│ │             │ │    │░░░│    │ │             │ │░░░░│   │    │ │
  │ └────┼───┼────┘ │             │ └────┼───┼────┘ │             │ └────┼───┼────┘ │
  │   A  └───┘  B   │             │   A  └───┘  B   │             │   A  └───┘  B   │
  └─────────────────┘             └─────────────────┘             └─────────────────┘
   All shaded regions               Only overlap region             Only A excluding B

 SYMMETRIC DIFF (A Δ B)          COMPLEMENT (A')
  ┌─────────────────┐             ┌─────────────────┐
  │ ┌────┐   ┌────┐ │             │░░░░░░░░░░░░░░░░░│
  │ │░░░░│   │░░░░│ │             │░┌────┐░░░░░░░░░░│
  │ │░░░░│   │░░░░│ │             │░│ A  │░░░░░░░░░░│
  │ └────┼───┼────┘ │             │░└────┘░░░░░░░░░░│
  │   A  └───┘  B   │             │░░░░░░░░░░░░░░░░░│
  └─────────────────┘             └─────────────────┘
    In A or B, NOT both             Everything outside A
```

### 2.1.3 Master Table: Isomorphism Between Set Algebra and Logic

| Law Name | Propositional Logic | Set Theory |
|:---|:---|:---|
| **Identity** | $p \land \top \equiv p$, $p \lor \bot \equiv p$ | $A \cap U = A$, $A \cup \emptyset = A$ |
| **Domination** | $p \lor \top \equiv \top$, $p \land \bot \equiv \bot$ | $A \cup U = U$, $A \cap \emptyset = \emptyset$ |
| **Idempotent** | $p \lor p \equiv p$, $p \land p \equiv p$ | $A \cup A = A$, $A \cap A = A$ |
| **Complementation** | $\neg(\neg p) \equiv p$ | $\overline{\overline{A}} = A$ |
| **Commutative** | $p \lor q \equiv q \lor p$ | $A \cup B = B \cup A$, $A \cap B = B \cap A$ |
| **Associative** | $(p \lor q) \lor r \equiv p \lor (q \lor r)$ | $(A \cup B) \cup C = A \cup (B \cup C)$ |
| **Distributive** | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ <br> $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| **De Morgan's** | $\neg(p \land q) \equiv \neg p \lor \neg q$ | $\overline{A \cap B} = \overline{A} \cup \overline{B}$ <br> $\overline{A \cup B} = \overline{A} \cap \overline{B}$ |
| **Absorption** | $p \lor (p \land q) \equiv p$ | $A \cup (A \cap B) = A$, $A \cap (A \cup B) = A$ |
| **Complement Laws** | $p \lor \neg p \equiv \top$, $p \land \neg p \equiv \bot$ | $A \cup \overline{A} = U$, $A \cap \overline{A} = \emptyset$ |

---

### 2.1.4 Power Set and Cartesian Product
- **Power Set ($\mathcal{P}(A)$ or $2^A$)**: The set of all subsets of $A$:
  $$\mathcal{P}(A) = \{S \mid S \subseteq A\}$$
  - Cardinality Theorem: If $|A| = n$, then $|\mathcal{P}(A)| = 2^n$.
  - *Proof by Combinatorics*: Every element $x_i \in A$ has exactly 2 independent choices regarding its inclusion in a subset $S$ (either $x_i \in S$ or $x_i \notin S$). By the product rule: $2 \times 2 \times \dots \times 2 = 2^n$.
  - Example: If $A = \{1, 2\}$, then $\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$. $|\mathcal{P}(A)| = 2^2 = 4$.
- **Cartesian Product ($A \times B$)**:
  $$A \times B = \{(a, b) \mid a \in A \land b \in B\}$$
  - Cardinality: $|A \times B| = |A| \times |B|$.
  - Non-commutative: $A \times B \neq B \times A$ unless $A = B$ or $A = \emptyset$ or $B = \emptyset$.

### 2.1.5 Methods of Proof for Sets: Double Inclusion
To prove $A = B$, we must prove two directional subset inclusions:
1. Show $A \subseteq B$: Choose an arbitrary element $x \in A$, and deduce $x \in B$.
2. Show $B \subseteq A$: Choose an arbitrary element $y \in B$, and deduce $y \in A$.

#### Rigorous Proof: $\overline{A \cup B} = \overline{A} \cap \overline{B}$ (De Morgan's Set Law)
- **Part 1 ($\subseteq$)**:
  - Let $x \in \overline{A \cup B}$.
  - By definition of complement, $x \notin (A \cup B)$.
  - This means $\neg(x \in A \lor x \in B) \equiv (x \notin A) \land (x \notin B)$.
  - Since $x \notin A$, $x \in \overline{A}$. Since $x \notin B$, $x \in \overline{B}$.
  - Thus $x \in (\overline{A} \cap \overline{B})$.
  - Therefore, $\overline{A \cup B} \subseteq \overline{A} \cap \overline{B}$.
- **Part 2 ($\supseteq$)**:
  - Let $y \in (\overline{A} \cap \overline{B})$.
  - Then $y \in \overline{A} \land y \in \overline{B} \implies (y \notin A) \land (y \notin B)$.
  - By De Morgan's logic law, this is equivalent to $\neg(y \in A \lor y \in B) \implies y \notin (A \cup B)$.
  - Thus $y \in \overline{A \cup B}$.
  - Therefore, $\overline{A} \cap \overline{B} \subseteq \overline{A \cup B}$.
- Combining Part 1 and Part 2, $\overline{A \cup B} = \overline{A} \cap \overline{B}$. $\blacksquare$

---

## 2.2 RELATIONS AND THEIR ALGEBRAIC PROPERTIES

### 2.2.1 Definitions and Representations
A **binary relation** $R$ from set $A$ to set $B$ is a subset of the Cartesian product $A \times B$:
$$R \subseteq A \times B$$
If $A = B$, $R$ is called a **binary relation on $A$**. If $(a, b) \in R$, we write $a R b$.

#### Representations of Relations:
1. **Set of Ordered Pairs**: $R = \{(1, 1), (1, 2), (2, 3), (3, 1)\}$.
2. **0-1 Adjacency Matrix ($M_R$)**: For finite set $A = \{a_1, a_2, \dots, a_n\}$, the $n \times n$ matrix $M_R$ is defined by:
   $$M_R[i][j] = \begin{cases} 1 & \text{if } (a_i, a_j) \in R \\ 0 & \text{if } (a_i, a_j) \notin R \end{cases}$$
3. **Directed Graph (Digraph)**: Vertices represent elements of $A$; a directed edge $(a_i \to a_j)$ exists iff $(a_i, a_j) \in R$. Self-loops represent $(a_i, a_i) \in R$.

---

### 2.2.2 Fundamental Properties of Relations on a Set $A$

Let $R$ be a binary relation on set $A$ where $|A| = n$:

#### 1. Reflexive Relation
- **Definition**: Every element is related to itself:
  $$\forall x \in A, \, (x, x) \in R$$
- **Matrix Characterization**: All main diagonal entries are $1$ ($M_R[i][i] = 1$ for all $i$).
- **Digraph Characterization**: Every vertex has a self-loop.

#### 2. Irreflexive Relation (Strict Anti-reflexive)
- **Definition**: No element is related to itself:
  $$\forall x \in A, \, (x, x) \notin R$$
- **Matrix Characterization**: All main diagonal entries are $0$ ($M_R[i][i] = 0$ for all $i$).
- **Digraph Characterization**: The digraph contains zero self-loops.
- **Trap**: Irreflexive is NOT the opposite of reflexive! A relation can be **neither reflexive nor irreflexive** (some diagonal elements are 1, others are 0).

#### 3. Symmetric Relation
- **Definition**: If an element is related to another, the reverse is also true:
  $$\forall x, y \in A, \, (x, y) \in R \implies (y, x) \in R$$
- **Matrix Characterization**: The matrix is symmetric: $M_R = M_R^T$ ($M_R[i][j] = M_R[j][i]$).
- **Digraph Characterization**: Every directed edge is accompanied by an antiparallel edge in the opposite direction (or represented as an undirected edge).

#### 4. Antisymmetric Relation
- **Definition**: If two distinct elements are related, they cannot be related in the reverse direction:
  $$\forall x, y \in A, \, \big( (x, y) \in R \land (y, x) \in R \big) \implies x = y$$
  - Equivalently (contrapositive): If $x \neq y$, then $(x, y) \in R \implies (y, x) \notin R$.
- **Matrix Characterization**: If $i \neq j$ and $M_R[i][j] = 1$, then $M_R[j][i]$ must be $0$. Diagonal elements can be either 0 or 1.

#### 5. Asymmetric Relation
- **Definition**: If $(x, y) \in R$, then $(y, x) \notin R$ under ALL circumstances (even when $x = y$):
  $$\forall x, y \in A, \, (x, y) \in R \implies (y, x) \notin R$$
- **Fundamental Equivalence**:
  $$\text{Asymmetric} \iff \text{Antisymmetric} \land \text{Irreflexive}$$
  - *Proof*: If $R$ is asymmetric, then for any $x$, if $(x, x) \in R \implies (x, x) \notin R$, a contradiction. Thus $(x, x) \notin R$ for all $x$, proving $R$ is irreflexive. Furthermore, for $x \neq y$, if $(x, y) \in R$, then $(y, x) \notin R$, satisfying antisymmetry. $\blacksquare$

#### 6. Transitive Relation
- **Definition**:
  $$\forall x, y, z \in A, \, \big( (x, y) \in R \land (y, z) \in R \big) \implies (x, z) \in R$$
- **Matrix Characterization**: If $M_R^{[2]}[i][j] > 0$, then $M_R[i][j] = 1$ (where $M^{[2]}$ is Boolean matrix product).

---

### 2.2.3 Master Derivation: Counting Formulas for Binary Relations
Let $|A| = n$. The total number of pairs in $A \times A$ is $n^2$.
The $n \times n$ matrix contains:
- **$n$ diagonal pairs**: $(a_i, a_i)$ for $i = 1, \dots, n$.
- **$\frac{n(n-1)}{2}$ symmetric off-diagonal pairs**: $\{(a_i, a_j), (a_j, a_i)\}$ with $i < j$.

```
                        n x n RELATION MATRIX STRUCTURE
                                     j --->
                     1       2       3      ...      n
                 ┌───────┬───────┬───────┬───────┬───────┐
             1   │ (1,1) │ (1,2) │ (1,3) │  ...  │ (1,n) │
                 ├───────┼───────┼───────┼───────┼───────┤
             2   │ (2,1) │ (2,2) │ (2,3) │  ...  │ (2,n) │   Total pairs = n²
     i           ├───────┼───────┼───────┼───────┼───────┤
     │       3   │ (3,1) │ (3,2) │ (3,3) │  ...  │ (3,n) │   Diagonal pairs = n
     ▼           ├───────┼───────┼───────┼───────┼───────┤
            ...  │  ...  │  ...  │  ...  │ (i,i) │  ...  │   Off-diagonal pairs = n² - n
                 ├───────┼───────┼───────┼───────┼───────┤   Unordered off-diagonal pairs
             n   │ (n,1) │ (n,2) │ (n,3) │  ...  │ (n,n) │     = n(n-1) / 2
                 └───────┴───────┴───────┴───────┴───────┘
```

#### Step-by-Step Derivations:

1. **Total Number of Binary Relations**:
   Since a relation is any subset of $A \times A$, there are:
   $$N_{\text{total}} = 2^{n^2}$$

2. **Total Reflexive Relations**:
   All $n$ diagonal pairs MUST be present (1 choice each). The remaining $n^2 - n = n(n-1)$ off-diagonal pairs can be either present or absent (2 choices each).
   $$N_{\text{reflexive}} = 1^n \times 2^{n(n-1)} = 2^{n(n-1)}$$

3. **Total Irreflexive Relations**:
   All $n$ diagonal pairs MUST be absent (1 choice each). The $n(n-1)$ off-diagonal pairs can be either present or absent.
   $$N_{\text{irreflexive}} = 1^n \times 2^{n(n-1)} = 2^{n(n-1)}$$

4. **Relations Neither Reflexive Nor Irreflexive**:
   The diagonal elements can neither be ALL 1s (reflexive) nor ALL 0s (irreflexive).
   - Diagonal configurations: $2^n - 2$ valid choices.
   - Off-diagonal configurations: $2^{n(n-1)}$ choices.
   $$N_{\text{neither ref nor irref}} = (2^n - 2) \cdot 2^{n(n-1)}$$

5. **Total Symmetric Relations**:
   - Diagonal elements: $n$ elements, 2 choices each ($0$ or $1$) $\implies 2^n$.
   - Off-diagonal pairs: For each pair $\{(a_i, a_j), (a_j, a_i)\}$, both must be 0 or both must be 1 (2 choices per pair). Number of pairs is $\frac{n(n-1)}{2}$.
   $$N_{\text{symmetric}} = 2^n \times 2^{\frac{n(n-1)}{2}} = 2^{n + \frac{n(n-1)}{2}} = 2^{\frac{n(n+1)}{2}}$$

6. **Total Antisymmetric Relations**:
   - Diagonal elements: $n$ elements, 2 choices each ($0$ or $1$) $\implies 2^n$.
   - Off-diagonal pairs: For each pair $\{(a_i, a_j), (a_j, a_i)\}$, we cannot have both equal to 1.
     - Choice 1: Neither is in $R$ ($(0, 0)$).
     - Choice 2: Only $(a_i, a_j) \in R$ ($(1, 0)$).
     - Choice 3: Only $(a_j, a_i) \in R$ ($(0, 1)$).
     - Exactly **3 valid choices** for each of the $\frac{n(n-1)}{2}$ pairs!
   $$N_{\text{antisymmetric}} = 2^n \times 3^{\frac{n(n-1)}{2}}$$

7. **Total Asymmetric Relations**:
   - Diagonal elements: Must all be $0$ (1 choice: irreflexivity condition) $\implies 1^n = 1$.
   - Off-diagonal pairs: Exactly the same 3 choices as antisymmetric ($(0,0), (1,0), (0,1)$).
   $$N_{\text{asymmetric}} = 1^n \times 3^{\frac{n(n-1)}{2}} = 3^{\frac{n(n-1)}{2}}$$

---

### 2.2.4 Venn Diagram Analysis: Asymmetric vs Antisymmetric (NIT Jalandhar PYQ Solved)

```
        ┌──────────────────────────────────────────────────────────┐
        │                  ANTISYMMETRIC RELATIONS                 │
        │               Total = 2ⁿ · 3^(n(n-1)/2)                  │
        │                                                          │
        │       ┌──────────────────────────────┐                   │
        │       │     ASYMMETRIC RELATIONS     │                   │
        │       │    (Irreflexive Diagonal)    │  (Has at least    │
        │       │                              │   one diagonal    │
        │       │   Total = 3^(n(n-1)/2)       │   element = 1)    │
        │       │                              │                   │
        │       └──────────────────────────────┘                   │
        │                                                          │
        └──────────────────────────────────────────────────────────┘
```

Since every asymmetric relation is antisymmetric (Asym $\subset$ Antisym):
1. **$k(\text{Asym} \cup \text{Antisym})$**:
   Since $\text{Asym} \subset \text{Antisym}$:
   $$k(\text{Asym} \cup \text{Antisym}) = k(\text{Antisym}) = 2^n \cdot 3^{\frac{n(n-1)}{2}}$$
2. **$k\big(\overline{\text{Asym} \cup \text{Antisym}}\big)$**:
   Total relations minus antisymmetric relations:
   $$k\big(\overline{\text{Asym} \cup \text{Antisym}}\big) = 2^{n^2} - 2^n \cdot 3^{\frac{n(n-1)}{2}}$$
3. **$k(\text{Asym} - \text{Antisym})$**:
   Since Asym is a strict subset of Antisym:
   $$k(\text{Asym} - \text{Antisym}) = 0$$
4. **$k(\text{Antisym} - \text{Asym})$**:
   Antisymmetric relations that have at least one diagonal element equal to 1:
   $$k(\text{Antisym} - \text{Asym}) = k(\text{Antisym}) - k(\text{Asym}) = (2^n - 1) \cdot 3^{\frac{n(n-1)}{2}}$$

---

### 2.2.5 Equivalence Relations, Equivalence Classes & Partitions

A relation $R$ on a set $A$ is an **equivalence relation** if and only if it satisfies three axioms simultaneously:
1. **Reflexivity**: $\forall x \in A, \, (x, x) \in R$.
2. **Symmetry**: $\forall x, y \in A, \, (x, y) \in R \implies (y, x) \in R$.
3. **Transitivity**: $\forall x, y, z \in A, \, ((x, y) \in R \land (y, z) \in R) \implies (x, z) \in R$.

#### Equivalence Classes
For $a \in A$, the **equivalence class of $a$**, denoted $[a]$ or $a/R$, is the set of all elements in $A$ related to $a$:
$$[a] = \{x \in A \mid (a, x) \in R\}$$

#### Fundamental Properties of Equivalence Classes:
1. $\forall a \in A, \, a \in [a]$ (by reflexivity, no class is empty).
2. $[a] = [b] \iff (a, b) \in R$.
3. Either $[a] = [b]$ or $[a] \cap [b] = \emptyset$ (Classes are pairwise disjoint).
4. $\bigcup_{a \in A} [a] = A$.

#### Fundamental Theorem of Equivalence Relations:
> **Theorem**: Every equivalence relation on a set $A$ partitions $A$ into mutually disjoint, non-empty subsets whose union is $A$. Conversely, every partition of $A$ uniquely induces an equivalence relation on $A$.

- **Counting Partitions**: The number of partitions of an $n$-element set is given by the **Bell Number $B_n$**, where:
  $$B_n = \sum_{k=1}^n S(n, k)$$
  where $S(n, k) = \frac{1}{k!} \sum_{j=0}^k (-1)^{k-j} \binom{k}{j} j^n$ is the Stirling number of the second kind.
  - $B_1 = 1$, $B_2 = 2$, $B_3 = 5$, $B_4 = 15$, $B_5 = 52$.

---

## 2.3 PARTIAL ORDERS (POSETS) & LATTICES

### 2.3.1 Partially Ordered Sets (Posets)
A relation $R$ on a set $S$ is a **partial ordering relation** if and only if it is:
1. **Reflexive**: $\forall x \in S, \, x \le x$.
2. **Antisymmetric**: $\forall x, y \in S, \, (x \le y \land y \le x) \implies x = y$.
3. **Transitive**: $\forall x, y, z \in S, \, (x \le y \land y \le z) \implies x \le z$.

The pair $(S, \le)$ is called a **Poset (Partially Ordered Set)**.

#### Chains and Antichains:
- Two elements $a, b \in S$ are **comparable** if $a \le b$ or $b \le a$; otherwise they are **incomparable** ($a \parallel b$).
- A subset $C \subseteq S$ is a **chain** (totally ordered set) if every pair of elements in $C$ is comparable.
- A subset $A \subseteq S$ is an **antichain** if every pair of distinct elements in $A$ is incomparable.

---

### 2.3.2 Hasse Diagrams: Construction Rules
A **Hasse diagram** is a simplified graphical representation of a finite poset:
1. **Rule 1 (Remove Reflexive Loops)**: Do not draw self-loops at any vertex (reflexivity is implicit).
2. **Rule 2 (Remove Transitive Edges)**: If $x < y$ and $y < z$, do NOT draw an edge from $x$ to $z$ (transitivity is implicit).
3. **Rule 3 (Upward Orientation)**: If $x < y$, place vertex $y$ higher than vertex $x$ on the page and connect them with an undirected straight segment. Arrowheads are omitted because direction is strictly upwards.

```
          Step 1: Digraph (with loops & transitivity)
                     (30)
                    ↗  ▲  ↖
                  (6) (10)(15)
                 ↗ ↖ ↗  ↖ ↗ ↖
                (2)   (3)   (5)
                 ↖     ▲     ↗
                   ＼  │   ／
                      (1)
            [Loops at every node omitted for clarity]

          Step 2: HASSE DIAGRAM of (D₃₀, |)
                          30
                       ／ │  ＼
                     ／   │    ＼
                   10     6      15
                  │ ╲   ／ ╲    ／│
                  │   ╳     ╳   │
                  │ ／   ＼ ／   ＼│
                  2       3       5
                   ＼     │     ／
                     ＼   │   ／
                          1
```

---

### 2.3.3 Extremal Elements in Posets
For a poset $(S, \le)$:
- **Maximal Element**: An element $m \in S$ is maximal if there is no $x \in S$ such that $m < x$ (nothing sits above it). A poset can have multiple maximal elements.
- **Minimal Element**: An element $m \in S$ is minimal if there is no $x \in S$ such that $x < m$ (nothing sits below it). A poset can have multiple minimal elements.
- **Greatest Element (Maximum / Top / 1)**: An element $g \in S$ such that $\forall x \in S, x \le g$. If it exists, it is **strictly UNIQUE**.
- **Least Element (Minimum / Bottom / 0)**: An element $l \in S$ such that $\forall x \in S, l \le x$. If it exists, it is **strictly UNIQUE**.

#### Upper Bounds, Lower Bounds, LUB, and GLB:
For a subset $A \subseteq S$:
- **Upper Bound**: $u \in S$ is an upper bound of $A$ if $\forall a \in A, a \le u$.
- **Lower Bound**: $l \in S$ is a lower bound of $A$ if $\forall a \in A, l \le a$.
- **Least Upper Bound (LUB / Supremum / Join $\lor$)**: The least element among all upper bounds of $A$.
- **Greatest Lower Bound (GLB / Infimum / Meet $\land$)**: The greatest element among all lower bounds of $A$.

---

### 2.3.4 Lattices: Algebraic and Relational Definitions
A poset $(L, \le)$ is a **Lattice** if for every pair of elements $a, b \in L$, both the **Least Upper Bound (Join: $a \lor b = \text{LUB}(a, b)$)** and the **Greatest Lower Bound (Meet: $a \land b = \text{GLB}(a, b)$)** exist in $L$.

#### Fundamental Properties of Lattice Operations:
1. **Idempotent**: $a \lor a = a$, $a \land a = a$.
2. **Commutative**: $a \lor b = b \lor a$, $a \land b = b \land a$.
3. **Associative**: $(a \lor b) \lor c = a \lor (b \lor c)$, $(a \land b) \land c = a \land (b \land c)$.
4. **Absorption**: $a \lor (a \land b) = a$, $a \land (a \lor b) = a$.

#### Specialized Classes of Lattices:
1. **Bounded Lattice**: A lattice $(L, \lor, \land, 0, 1)$ with a global least element $0$ and greatest element $1$.
   $$a \lor 0 = a, \quad a \land 0 = 0, \quad a \lor 1 = 1, \quad a \land 1 = a$$
2. **Distributive Lattice**: A lattice satisfying the distributive laws:
   $$a \land (b \lor c) = (a \land b) \lor (a \land c)$$
   $$a \lor (b \land c) = (a \lor b) \land (a \lor c)$$
   - **Birkhoff's Characterization Theorem**: A lattice is distributive **if and only if it contains no sublattice isomorphic to $M_3$ (Diamond lattice) or $N_5$ (Pentagon lattice)**.

```
       M₃ (Diamond Lattice)              N₅ (Pentagon Lattice)
                 1                                1
              ／ │ ＼                          ／   │
            ／   │   ＼                       ／     │
           a     b     c                     c       b
            ＼   │   ／                       │       │
              ＼ │ ／                         │       a
                 0                            ＼     │
                                                ＼   │
                                                  0
     a ∧ (b ∨ c) = a ∧ 1 = a          a ∨ (b ∧ c) = a ∨ 0 = a
     (a ∧ b) ∨ (a ∧ c) = 0 ∨ 0 = 0    (a ∨ b) ∧ (a ∨ c) = b ∧ 1 = b
     [a ≠ 0 => FAILS DISTRIBUTIVITY]  [a ≠ b => FAILS DISTRIBUTIVITY]
```

3. **Complemented Lattice**: In a bounded lattice $(L, \lor, \land, 0, 1)$, an element $b$ is a **complement** of $a$ if:
   $$a \lor b = 1 \quad \text{and} \quad a \land b = 0$$
   A lattice is **complemented** if every element has at least one complement.
4. **Boolean Algebra**: A lattice that is **both distributive and complemented**. In any Boolean algebra, complements are strictly unique.

---

### 2.3.5 Comprehensive Divisor Lattice Analysis ($D_{30}$) (NIT Jalandhar PYQ Solved)
Consider the poset of divisors of 30, $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$ under divisibility ($a \mid b$).
- **Least Element (0)**: $1$ (since $1 \mid x$ for all $x$).
- **Greatest Element (1)**: $30$ (since $x \mid 30$ for all $x$).
- **Operations**:
  - $a \lor b = \text{lcm}(a, b)$
  - $a \land b = \gcd(a, b)$
- **Is $D_{30}$ Complemented?**
  - For each element $x$, we require $x' \in D_{30}$ such that $\gcd(x, x') = 1$ and $\text{lcm}(x, x') = 30$.
  - Complements:
    - Complement of $1$ is $30$ ($\gcd(1,30)=1, \text{lcm}(1,30)=30$).
    - Complement of $2$ is $15$ ($\gcd(2,15)=1, \text{lcm}(2,15)=30$).
    - Complement of $3$ is $10$ ($\gcd(3,10)=1, \text{lcm}(3,10)=30$).
    - Complement of $5$ is $6$ ($\gcd(5,6)=1, \text{lcm}(5,6)=30$).
  - Every element possesses a valid complement $\implies$ **$D_{30}$ is a Complemented Lattice**.
- **Is $D_{30}$ Distributive?**
  - In general, any divisor lattice $D_n$ where $a \lor b = \text{lcm}(a, b)$ and $a \land b = \gcd(a, b)$ satisfies the distributive law because $\gcd(a, \text{lcm}(b, c)) = \text{lcm}(\gcd(a, b), \gcd(a, c))$.
  - $\implies$ **$D_{30}$ is a Distributive Lattice**.
  - Since $D_{30}$ is distributive and complemented, **$D_{30}$ is isomorphic to the Boolean Algebra $B_3$ ($\mathcal{P}(\{p_1, p_2, p_3\})$)** where $30 = 2 \times 3 \times 5$ is a product of 3 distinct primes (square-free).
  - *Square-Free Divisor Rule*: $D_n$ is complemented **if and only if $n$ is square-free** (no prime factor appears with exponent $\ge 2$). For example, $D_{12}$ ($12 = 2^2 \times 3$) is NOT complemented because the element $2$ has no complement ($\gcd(2, x)=1 \implies x \in \{1, 3\}$, but $\text{lcm}(2, 1)=2 \neq 12, \text{lcm}(2, 3)=6 \neq 12$).

---

### 2.3.6 Total Orders & Linear Extensions of a Partial Order (NIT Jalandhar PYQ Solved)
**Problem**: Let $P$ be the partial order defined on $\{1, 2, 3, 4\}$:
$$P = \{(x, x) \mid x \in \{1, 2, 3, 4\}\} \cup \{(1, 2), (3, 2), (3, 4)\}$$
Determine the number of total orders (topological sorts / linear extensions) that contain $P$.

**Step-by-Step Derivation**:
- The non-trivial strict ordering constraints given are:
  1. $1 < 2$
  2. $3 < 2$
  3. $3 < 4$
- Notice:
  - Element $3$ must precede both $2$ and $4$ ($3 < 2$ and $3 < 4$).
  - Element $1$ must precede $2$ ($1 < 2$).
  - Element $2$ has no elements after it. Elements $2$ and $4$ are maximal candidates.
  - Minimal candidates: $1$ and $3$ have no predecessors.
- A total order is a permutation $(x_1, x_2, x_3, x_4)$ of $\{1, 2, 3, 4\}$ compatible with all three constraints.
- Total permutations of 4 elements = $4! = 24$.
- Let's determine valid position assignments:
  - Constraint 1: $1$ appears before $2$.
  - Constraint 2: $3$ appears before $2$.
  - Constraint 3: $3$ appears before $4$.
- Let's test the positions of $3$:
  - $3$ must appear before $2$ and before $4$, so $3$ can be in position 1 or position 2 (1-indexed).
  - **Case A: $3$ is in position 1**: $(3, \_, \_, \_)$
    - Remaining elements $\{1, 2, 4\}$.
    - Constraint $3 < 2$ and $3 < 4$ are automatically satisfied.
    - We only need $1$ before $2$ among $\{1, 2, 4\}$.
    - Total permutations of $\{1, 2, 4\}$ is $3! = 6$.
    - In exactly half of them ($\frac{6}{2} = 3$), $1$ appears before $2$:
      1. $(3, 1, 2, 4)$
      2. $(3, 1, 4, 2)$
      3. $(3, 4, 1, 2)$
    - All 3 satisfy all constraints!
  - **Case B: $3$ is in position 2**: $(\_, 3, \_, \_)$
    - What can be in position 1?
    - Neither $2$ nor $4$ can be before $3$ (since $3 < 2$ and $3 < 4$).
    - Therefore, **position 1 MUST be $1$**: $(1, 3, \_, \_)$.
    - Then remaining positions 3 and 4 are filled by $\{2, 4\}$.
    - Both permutations:
      4. $(1, 3, 2, 4)$
      5. $(1, 3, 4, 2)$
    - Both satisfy $1 < 2$, $3 < 2$, and $3 < 4$!
  - **Case C: Can $3$ be in position 3 or 4?**
    - If $3$ is in position 3, only 1 element remains after it. But $3$ must precede TWO elements ($2$ and $4$). Impossible!
- **Total number of linear extensions = $3 + 2 = 5$**.

---

## 2.4 FUNCTIONS AND BIJECTIONS

### 2.4.1 Formal Definition & Terminology
A **function** $f: A \to B$ is a special relation from $A$ to $B$ such that every element $a \in A$ is associated with **exactly one element** $b \in B$:
$$\forall x \in A, \, \exists! y \in B \text{ such that } (x, y) \in f$$
- $A$: **Domain** of $f$.
- $B$: **Codomain** of $f$.
- **Range / Image**: $f(A) = \{f(x) \mid x \in A\} \subseteq B$.

### 2.4.2 Classification of Functions

```
       INJECTIVE (1-to-1)           SURJECTIVE (Onto)             BIJECTIVE (1-to-1 & Onto)
     A               B             A               B             A               B
   ┌───┐           ┌───┐         ┌───┐           ┌───┐         ┌───┐           ┌───┐
   │ 1 ├───┐   ┌──>│ a │         │ 1 ├───┐       │ a │         │ 1 ├──────────>│ a │
   │ 2 ├───┼───┘   │ b │         │ 2 ├───┼──────>│ b │         │ 2 ├──────────>│ b │
   │ 3 ├───┼──────>│ c │         │ 3 ├───┴──────>│   │         │ 3 ├──────────>│ c │
   └───┘   │       │ d │         └───┘           └───┘         └───┘           └───┘
           └──────>│   │        [Range = Codomain]            [Perfect 1-to-1 matching;
   [Distinct inputs =>           Every target hit              |A| = |B|; Invertible]
    distinct outputs]
```

1. **Injective (One-to-One)**:
   $$\forall x_1, x_2 \in A, \, f(x_1) = f(x_2) \implies x_1 = x_2$$
   - Cardinality condition: $|A| \le |B|$.
2. **Surjective (Onto)**:
   $$\forall y \in B, \, \exists x \in A \text{ such that } f(x) = y \quad (f(A) = B)$$
   - Cardinality condition: $|A| \ge |B|$.
3. **Bijective (One-to-One Correspondence)**:
   - $f$ is both Injective and Surjective.
   - Cardinality condition: $|A| = |B|$.
   - A function is **invertible ($f^{-1}$ exists)** if and only if it is **bijective**.

### 2.4.3 Advanced Bijection Construction (NIT Jalandhar PYQ Solved)
**Problem**: Find an explicit bijection $f: (0, 1] \to [0, \infty)$.

**Mathematical Construction**:
1. *Analysis*: We are mapping a bounded semi-closed interval $(0, 1]$ onto an unbounded semi-closed interval $[0, \infty)$. Both sets have the cardinality of the continuum ($\mathfrak{c} = 2^{\aleph_0}$).
2. *Strategy*: Use a two-stage composition or Hilbert's Hotel shift:
   - **Step 1: Map $(0, 1]$ to $[1, \infty)$**:
     The function $g(x) = \frac{1}{x}$ maps $(0, 1]$ bijectively onto $[1, \infty)$.
     - *Check*: For $x \in (0, 1]$, as $x \to 0^+$, $\frac{1}{x} \to \infty$. When $x = 1$, $\frac{1}{1} = 1$.
     - Strictly decreasing and continuous, hence a bijection from $(0, 1] \to [1, \infty)$.
   - **Step 2: Map $[1, \infty)$ to $[0, \infty)$**:
     We need to shift the interval $[1, \infty)$ down by $1$ to start at $0$:
     $$h(y) = y - 1$$
     - *Check*: $h(1) = 0$, and as $y \to \infty$, $h(y) \to \infty$. Clearly bijective.
3. *Composite Function*:
   $$f(x) = (h \circ g)(x) = h(g(x)) = \frac{1}{x} - 1 = \frac{1 - x}{x}$$
4. *Rigorous Verification of Bijection*:
   - **Domain**: For any $x \in (0, 1]$, $0 < x \le 1 \implies 0 \le 1 - x < 1$. Thus $f(x) = \frac{1-x}{x} \ge 0$. Codomain $[0, \infty)$ is satisfied.
   - **Injectivity**:
     $$\frac{1 - x_1}{x_1} = \frac{1 - x_2}{x_2} \implies \frac{1}{x_1} - 1 = \frac{1}{x_2} - 1 \implies \frac{1}{x_1} = \frac{1}{x_2} \implies x_1 = x_2 \quad \text{[Injective]}$$
   - **Surjectivity**:
     For any $y \in [0, \infty)$, solve $y = \frac{1 - x}{x}$:
     $$yx = 1 - x \implies x(y + 1) = 1 \implies x = \frac{1}{y + 1}$$
     Since $y \ge 0$, $y + 1 \ge 1 \implies 0 < \frac{1}{y + 1} \le 1$, so $x \in (0, 1]$.
     Thus every $y \in [0, \infty)$ has a unique preimage $x = \frac{1}{y + 1} \in (0, 1]$.
   - Hence, $f(x) = \frac{1 - x}{x}$ is a **provably valid bijection**. $\blacksquare$

---

## 2.5 ADVANCED COUNTING PRINCIPLES & COMBINATORICS

### 2.5.1 Sum Rule and Product Rule
- **Sum Rule (Disjoint Tasks)**: If task 1 can be done in $n_1$ ways, and task 2 in $n_2$ ways, and the tasks cannot be done simultaneously, then doing either task can be done in $n_1 + n_2$ ways.
- **Product Rule (Sequential Tasks)**: If a procedure breaks into independent sequential stages with $n_1, n_2, \dots, n_k$ choices respectively, the entire procedure can be executed in $\prod_{i=1}^k n_i$ ways.

### 2.5.2 Pigeonhole Principle (PHP) & Generalized PHP
- **Basic PHP**: If $k + 1$ or more pigeons are placed into $k$ pigeonholes, then at least one pigeonhole must contain two or more pigeons.
- **Generalized PHP**: If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least:
  $$\left\lceil \frac{N}{k} \right\rceil \text{ objects}$$
  - *Proof by Contradiction*: Assume every box contains at most $\lceil N/k \rceil - 1$ objects.
  - Total objects $\le k \left( \lceil N/k \rceil - 1 \right) < k \left( (N/k + 1) - 1 \right) = N$, a direct contradiction! $\blacksquare$

#### Exam Problem: Generalized PHP Walkthrough
*Question*: How many cards must be selected from a standard deck of 52 cards to guarantee that at least 3 cards of the same suit are chosen?
- Number of boxes (suits) $k = 4$ ($\spadesuit, \heartsuit, \diamondsuit, \clubsuit$).
- We require $\lceil N/4 \rceil = 3$.
- Worst-case distribution before guarantee: 2 cards of each suit = $4 \times 2 = 8$ cards.
- Adding 1 more card forces one suit to reach 3.
- Answer: $N = 4 \times (3 - 1) + 1 = 9$ cards.

---

### 2.5.3 Principle of Inclusion-Exclusion (PIE)
For finite sets $A, B, C$:
1. **Two Sets**:
   $$|A \cup B| = |A| + |B| - |A \cap B|$$
2. **Three Sets**:
   $$|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$$
3. **General Formulation ($n$ Sets)**:
   $$\left| \bigcup_{i=1}^n A_i \right| = \sum_{i=1}^n |A_i| - \sum_{1 \le i < j \le n} |A_i \cap A_j| + \sum_{1 \le i < j < k \le n} |A_i \cap A_j \cap A_k| - \dots + (-1)^{n-1} \left| \bigcap_{i=1}^n A_i \right|$$

#### Application: Derangements ($D_n$)
A **derangement** is a permutation of $\{1, 2, \dots, n\}$ such that no element appears in its original position ($\pi(i) \neq i$ for all $i$).
Using PIE:
$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!} = n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + \frac{(-1)^n}{n!} \right)$$
- $D_1 = 0$, $D_2 = 1$, $D_3 = 2$, $D_4 = 9$, $D_5 = 44$.
- As $n \to \infty$, $\frac{D_n}{n!} \to \frac{1}{e} \approx 0.3678$.

---

## 2.6 NUMBER THEORY & MODULAR ARITHMETIC

### 2.6.1 Division Algorithm & Divisibility Properties
- **Division Algorithm Theorem**: Let $a$ be an integer and $d$ a positive integer. Then there exist unique integers $q$ (quotient) and $r$ (remainder) such that:
  $$a = dq + r, \quad 0 \le r < d$$
  - $q = \lfloor a/d \rfloor$, $r = a \bmod d$.
- **Divisibility**: $d \mid a$ ("$d$ divides $a$") iff $\exists k \in \mathbb{Z}$ such that $a = dk$.

### 2.6.2 Euclidean Algorithm & Extended Euclidean Algorithm
The Euclidean algorithm computes the **Greatest Common Divisor ($\gcd(a, b)$)** based on the identity:
$$\gcd(a, b) = \gcd(b, a \bmod b)$$

#### Extended Euclidean Algorithm (Bézout's Identity)
For any non-zero integers $a$ and $b$, there exist integers $x, y \in \mathbb{Z}$ such that:
$$ax + by = \gcd(a, b)$$

#### Complete Worked Computation: Find $\gcd(252, 105)$ and express as $252x + 105y$:
1. **Forward Euclidean Divisions**:
   $$\begin{aligned}
   252 &= 2 \times 105 + 42 && \implies 42 = 252 - 2(105) \\
   105 &= 2 \times 42 + 21 && \implies 21 = 105 - 2(42) \\
   42 &= 2 \times 21 + 0 && \implies \gcd(252, 105) = 21
   \end{aligned}$$
2. **Backward Substitution for Bézout Coefficients**:
   $$\begin{aligned}
   21 &= 105 - 2(42) \\
   &= 105 - 2\big( 252 - 2(105) \big) \\
   &= 105 - 2(252) + 4(105) \\
   &= 5(105) - 2(252) \\
   &= 252(-2) + 105(5)
   \end{aligned}$$
   - Bézout coefficients: $x = -2, y = 5$.
   - Verification: $252(-2) + 105(5) = -504 + 525 = 21$. $\blacksquare$

---

## 2.7 ELEMENTS OF PROBABILITY & BAYES' THEOREM

### 2.7.1 Sample Space, Events, and Axioms
- **Sample Space ($S$)**: The set of all possible outcomes of a random experiment.
- **Event ($E$)**: Any subset $E \subseteq S$.
- **Kolmogorov's Axioms**:
  1. $0 \le P(E) \le 1$ for any event $E$.
  2. $P(S) = 1$.
  3. For mutually exclusive events $E_1, E_2, \dots$ ($E_i \cap E_j = \emptyset$ for $i \neq j$):
     $$P\left( \bigcup_{i=1}^\infty E_i \right) = \sum_{i=1}^\infty P(E_i)$$

### 2.7.2 Conditional Probability and Bayes' Theorem
- **Conditional Probability**:
  $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad \text{provided } P(B) > 0$$
- **Law of Total Probability**: If $B_1, B_2, \dots, B_k$ partition sample space $S$:
  $$P(A) = \sum_{i=1}^k P(A \mid B_i) P(B_i)$$
- **Bayes' Theorem**:
  $$P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^k P(A \mid B_i) P(B_i)}$$

---

## 2.8 RECURRENCE RELATIONS

A recurrence relation defines a sequence $\{a_n\}$ in terms of one or more of its preceding terms.

### 2.8.1 Linear Homogeneous Recurrence Relations with Constant Coefficients (LHRR-CC)
A relation of the form:
$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k}$$
where $c_i$ are constants and $c_k \neq 0$.

#### Solving via the Characteristic Equation:
Substitute $a_n = r^n$:
$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \dots - c_k = 0$$

- **Case 1: Distinct Real Roots ($r_1, r_2, \dots, r_k$)**:
  $$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + \dots + \alpha_k r_k^n$$
- **Case 2: Repeated Roots**: If root $r_1$ occurs with multiplicity $m$:
  $$a_n = (\alpha_{1,0} + \alpha_{1,1} n + \alpha_{1,2} n^2 + \dots + \alpha_{1,m-1} n^{m-1}) r_1^n$$

#### Fully Worked Numerical Problem:
**Solve**: $a_n = 5a_{n-1} - 6a_{n-2}$ with initial conditions $a_0 = 1, a_1 = 4$.
1. **Characteristic Equation**:
   $$r^2 - 5r + 6 = 0 \implies (r - 2)(r - 3) = 0 \implies r_1 = 2, r_2 = 3$$
2. **General Solution**:
   $$a_n = \alpha_1 2^n + \alpha_2 3^n$$
3. **Apply Initial Conditions**:
   - For $n = 0$: $a_0 = \alpha_1 + \alpha_2 = 1 \implies \alpha_2 = 1 - \alpha_1$.
   - For $n = 1$: $a_1 = 2\alpha_1 + 3\alpha_2 = 4$.
   - Substitute $\alpha_2$: $2\alpha_1 + 3(1 - \alpha_1) = 4 \implies -\alpha_1 + 3 = 4 \implies \alpha_1 = -1$.
   - Then $\alpha_2 = 1 - (-1) = 2$.
4. **Final Closed-Form Solution**:
   $$a_n = -2^n + 2 \cdot 3^n = 2 \cdot 3^n - 2^n \quad \blacksquare$$

---
"""

if __name__ == "__main__":
    print(f"Unit 2 generated: {len(get_unit2_text())} characters")
