# generate_unit5.py
# Generates Unit 5: Basics of Structures (Algebraic Structures)

def get_unit5_text():
    return r"""# UNIT 5: ALGEBRAIC STRUCTURES & MATHEMATICAL INDUCTION

---

## 5.1 MATHEMATICAL INDUCTION

### 5.1.1 The Well-Ordering Principle
The **Well-Ordering Principle** states that every non-empty set of non-negative integers contains a **least element**:
$$\forall S \subseteq \mathbb{Z}_{\ge 0}, \, S \neq \emptyset \implies \exists m \in S \text{ such that } \forall s \in S, m \le s$$
This foundational axiom provides the axiomatic justification for both weak and strong mathematical induction.

---

### 5.1.2 Principle of Mathematical Induction (Weak Induction)
To prove that a proposition $P(n)$ is true for all integers $n \ge n_0$:
1. **Basis Step**: Verify that $P(n_0)$ is True.
2. **Inductive Hypothesis**: Assume $P(k)$ is True for an arbitrary integer $k \ge n_0$.
3. **Inductive Step**: Prove that $P(k + 1)$ must be True based on the truth of $P(k)$.
4. **Conclusion**: By the Principle of Mathematical Induction, $P(n)$ is true for all $n \ge n_0$.

$$\Big( P(n_0) \land \forall k \ge n_0 \big( P(k) \to P(k+1) \big) \Big) \implies \forall n \ge n_0 P(n)$$

#### Rigorous Worked Proof: Sum of First $n$ Squares
Prove that for all integers $n \ge 1$:
$$\sum_{i=1}^n i^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

- **Basis Step ($n = 1$)**:
  $$\text{LHS} = 1^2 = 1$$
  $$\text{RHS} = \frac{1(1+1)(2(1)+1)}{6} = \frac{1(2)(3)}{6} = 1$$
  $\text{LHS} = \text{RHS}$. The basis step holds.
- **Inductive Hypothesis**:
  Assume the statement holds for an arbitrary integer $k \ge 1$:
  $$1^2 + 2^2 + \dots + k^2 = \frac{k(k+1)(2k+1)}{6}$$
- **Inductive Step ($n = k + 1$)**:
  We must prove:
  $$\sum_{i=1}^{k+1} i^2 = \frac{(k+1)((k+1)+1)(2(k+1)+1)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}$$
  Starting from the LHS:
  $$\begin{aligned}
  \sum_{i=1}^{k+1} i^2 &= \left( \sum_{i=1}^k i^2 \right) + (k+1)^2 \\
  &= \frac{k(k+1)(2k+1)}{6} + (k+1)^2 && \text{[By Inductive Hypothesis]} \\
  &= (k+1) \left[ \frac{k(2k+1)}{6} + (k+1) \right] \\
  &= (k+1) \left[ \frac{2k^2 + k + 6k + 6}{6} \right] \\
  &= (k+1) \left[ \frac{2k^2 + 7k + 6}{6} \right]
  \end{aligned}$$
  Factoring the quadratic numerator: $2k^2 + 7k + 6 = (k+2)(2k+3)$.
  $$\sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2k+3)}{6} = \text{RHS}$$
- The inductive step is proven. By mathematical induction, the identity holds for all $n \ge 1$. $\blacksquare$

---

### 5.1.3 Strong Mathematical Induction
In **Strong Induction**, the inductive hypothesis assumes that the proposition holds for **all values from the base case up to $k$**:
$$\Big( P(n_0) \land \forall k \ge n_0 \big( [P(n_0) \land P(n_0+1) \land \dots \land P(k)] \to P(k+1) \big) \Big) \implies \forall n \ge n_0 P(n)$$

#### Classic Worked Proof: Fundamental Theorem of Arithmetic (Existence Part)
Prove that every integer $n \ge 2$ can be factored into a product of one or more prime numbers.
- **Basis Step ($n = 2$)**:
  $2$ is itself a prime number (product of a single prime). Holds.
- **Inductive Hypothesis**:
  Assume that every integer $j$ with $2 \le j \le k$ can be written as a product of primes.
- **Inductive Step ($n = k + 1$)**:
  - *Case 1*: If $k + 1$ is prime, then it is trivially a product of primes.
  - *Case 2*: If $k + 1$ is composite, then by definition there exist integers $a$ and $b$ such that:
    $$k + 1 = a \cdot b, \quad \text{where } 2 \le a \le k \text{ and } 2 \le b \le k$$
  - Since both $a$ and $b$ fall within the range $[2, k]$, by our **Strong Inductive Hypothesis**, both $a$ and $b$ can be written as products of primes:
    $$a = p_1 p_2 \dots p_r \quad \text{and} \quad b = q_1 q_2 \dots q_s$$
    where all $p_i, q_j$ are primes.
  - Therefore:
    $$k + 1 = a \cdot b = (p_1 p_2 \dots p_r)(q_1 q_2 \dots q_s)$$
  - Thus, $k + 1$ is expressed as a product of primes.
- By strong induction, every integer $n \ge 2$ can be written as a product of primes. $\blacksquare$

---

## 5.2 BINARY OPERATIONS & THEIR ALGEBRAIC PROPERTIES

A **binary operation** $*$ on a non-empty set $S$ is a function that maps every ordered pair of elements in $S \times S$ to a unique element in $S$:
$$*: S \times S \to S, \quad *(a, b) = a * b \in S$$

### 5.2.1 Core Axiomatic Properties of Binary Operations
Let $(S, *)$ be a set equipped with a binary operation:
1. **Closure**:
   $$\forall a, b \in S, \, a * b \in S$$
2. **Associativity**:
   $$\forall a, b, c \in S, \, (a * b) * c = a * (b * c)$$
   - *Significance*: Associativity allows omitting parentheses ($a * b * c$).
3. **Commutativity**:
   $$\forall a, b \in S, \, a * b = b * a$$
4. **Identity Element ($e$)**:
   $$\exists e \in S \text{ such that } \forall a \in S, \, a * e = e * a = a$$
   - **Theorem: Uniqueness of Identity Element**:
     *Proof*: Suppose $e_1$ and $e_2$ are both identity elements in $(S, *)$.
     Since $e_1$ is an identity: $e_2 * e_1 = e_2$.
     Since $e_2$ is an identity: $e_1 * e_2 = e_1$.
     Furthermore, $e_1 * e_2 = e_2 * e_1$ (evaluating the pair $(e_1, e_2)$ under both identity definitions).
     Therefore: $e_1 = e_1 * e_2 = e_2 \implies e_1 = e_2$. The identity is strictly unique. $\blacksquare$
5. **Inverse Element ($a^{-1}$)**:
   For an algebraic structure with identity $e$, an element $b \in S$ is the inverse of $a \in S$ if:
   $$a * b = b * a = e$$
   - **Theorem: Uniqueness of Inverses in Associative Structures**:
     *Proof*: Suppose $b_1$ and $b_2$ are both inverses of $a$ in an associative structure $(S, *)$.
     $$b_1 = b_1 * e = b_1 * (a * b_2) = (b_1 * a) * b_2 = e * b_2 = b_2$$
     Therefore, $b_1 = b_2$. Inverses are strictly unique. $\blacksquare$

---

## 5.3 HIERARCHY OF ALGEBRAIC STRUCTURES

```
       ┌────────────────────────────────────────────────────────────┐
       │                   ALGEBRAIC STRUCTURES                     │
       ├───────────────────┬────────────────────────────────────────┤
       │ Structure         │ Axioms Satisfied                       │
       ├───────────────────┼────────────────────────────────────────┤
       │ 1. Groupoid       │ Closure                                │
       │ 2. Semi-group     │ Closure + Associativity                │
       │ 3. Monoid         │ Closure + Associativity + Identity     │
       │ 4. Group          │ Monoid + Inverse for EVERY element     │
       │ 5. Abelian Group  │ Group + Commutativity                  │
       └───────────────────┴────────────────────────────────────────┘
```

### 5.3.1 Detailed Structural Definitions
1. **Semi-group**: $(S, *)$ is a semi-group if $*$ is **closed** and **associative**.
   - Example: $(\mathbb{N}, +)$ where $\mathbb{N} = \{1, 2, 3, \dots\}$. Closed under addition and associative, but has no identity ($0 \notin \mathbb{N}$).
2. **Monoid**: $(M, *, e)$ is a monoid if it is a semi-group with an **identity element** $e \in M$.
   - Example: $(\mathbb{N}_0, +, 0)$ (natural numbers with zero). Identity is 0. But elements have no additive inverses in $\mathbb{N}_0$ (except 0).
3. **Group**: $(G, *)$ is a group if it is a monoid where **every element $a \in G$ possesses an inverse $a^{-1} \in G$**.
   - Example: $(\mathbb{Z}, +, 0)$ where inverse of $a$ is $-a$.
4. **Abelian (Commutative) Group**: A group $(G, *)$ where the operation is also **commutative** ($a * b = b * a$ for all $a, b \in G$).

---

### 5.3.2 Real-World Computer Science Connection: Distributed Systems & Rollback (NIT Jalandhar PYQ Solved)
**Problem Statement**:
In distributed transaction systems, state transitions are modeled by sequential composition of tasks. If the system is modeled as a monoid $(M, \circ)$ rather than a group $(G, \circ)$, there are irreversible operations. Explain the impact on system rollback capabilities.

**Analytical Technical Explanation**:
1. **Monoids vs Groups in State Transitions**:
   - In a transaction log, state transitions are composed sequentially: $S_{\text{new}} = S_{\text{init}} \circ T_1 \circ T_2 \circ \dots \circ T_k$.
   - The identity element $e$ corresponds to the **No-Op (Identity Transaction)** ($S \circ e = S$).
   - Composition is associative: $(T_1 \circ T_2) \circ T_3 = T_1 \circ (T_2 \circ T_3)$.
   - Thus, transaction processing naturally forms a **Monoid**.
2. **The Non-Invertible Element**:
   - In a group, every element $g$ possesses an inverse $g^{-1}$ such that $g \circ g^{-1} = e$. This allows exact mathematical rollback: $S \circ g \circ g^{-1} = S$.
   - However, in a general monoid, elements **do not necessarily have inverses**.
   - *Concrete Example*: Consider the operation $\text{Overwrite}(x, 0)$ or $\text{DeleteRecord}(ID)$.
     $$\text{DeleteRecord}(ID): \text{Database} \to \text{Database}$$
     Once the record is deleted and discarded from disk, the state transition has no mathematical inverse within the operation set; information entropy is lost.
   - Another example: An external irreversible action, such as $\text{SendEmail}(to, text)$ or $\text{DispenseCash}(amount)$.
3. **Impact on System Rollback Capabilities**:
   - Because $(M, \circ)$ lacks inverses, **automatic state restoration via inverse operations is impossible**.
   - *Architectural Solutions*: Distributed databases cannot rely on mathematical group inverses; instead, they must introduce:
     1. **Write-Ahead Logging (WAL)**: Preserving the previous state explicitly before executing the non-invertible monoid transition.
     2. **Saga Orchestration & Compensating Transactions**: Executing semantic compensation (e.g., issuing a refund transaction to compensate for a non-reversible payment) rather than a true algebraic inverse.

---

### 5.3.3 Analysis of Modular Additive Groups: $M_n = (\mathbb{Z}_n, +_n)$
Consider the group $M_n = \{0, 1, 2, \dots, n - 1\}$ under addition modulo $n$:
$$a +_n b = (a + b) \bmod n$$
- Identity element: $e = 0$.
- Inverse of $a$: $a^{-1} = (n - a) \bmod n$. (Inverse of $0$ is $0$).

#### Self-Inverse Elements in $M_3$ and $M_4$ (NIT Jalandhar PYQ Solved):
An element $a$ is its **own inverse** (self-inverse) if and only if:
$$a +_n a = 0 \iff (2a) \equiv 0 \pmod n$$

1. **For $M_3 = \{0, 1, 2\}$ ($n = 3$)**:
   - Solve $2a \equiv 0 \pmod 3$:
     - $a = 0: 2(0) = 0 \equiv 0 \pmod 3$ $\implies$ **Self-inverse**.
     - $a = 1: 2(1) = 2 \not\equiv 0 \pmod 3$ (Inverse of 1 is 2).
     - $a = 2: 2(2) = 4 \equiv 1 \not\equiv 0 \pmod 3$ (Inverse of 2 is 1).
   - **Result for $M_3$**: Exactly **$1$ self-inverse element** (only $0$).
2. **For $M_4 = \{0, 1, 2, 3\}$ ($n = 4$)**:
   - Solve $2a \equiv 0 \pmod 4$:
     - $a = 0: 2(0) = 0 \equiv 0 \pmod 4$ $\implies$ **Self-inverse**.
     - $a = 1: 2(1) = 2 \not\equiv 0 \pmod 4$ (Inverse of 1 is 3).
     - $a = 2: 2(2) = 4 \equiv 0 \pmod 4$ $\implies$ **Self-inverse**.
     - $a = 3: 2(3) = 6 \equiv 2 \not\equiv 0 \pmod 4$ (Inverse of 3 is 1).
   - **Result for $M_4$**: Exactly **$2$ self-inverse elements** ($0$ and $2$).
   - *(General Rule: In $M_n$, if $n$ is odd, only $0$ is self-inverse (1 element). If $n$ is even, $0$ and $n/2$ are self-inverses (2 elements).)*

---

## 5.4 SUBGROUPS & SUBGROUP TESTS

A subset $H$ of a group $(G, *)$ is a **subgroup** (denoted $H \le G$) if $H$ itself forms a group under the operation $*$ inherited from $G$.
- Every group $G$ has at least two trivial subgroups: $\{e\}$ and $G$ itself. Any other subgroup is a **proper, non-trivial subgroup**.

### 5.4.1 Subgroup Criterion Theorems (Subgroup Tests)

#### 1. Two-Step Subgroup Test
A non-empty subset $H \subseteq G$ is a subgroup of $G$ if and only if:
1. $\forall a, b \in H, \, a * b \in H$ (Closure under operation).
2. $\forall a \in H, \, a^{-1} \in H$ (Closure under inverses).

#### 2. One-Step Subgroup Test (Standard Exam Proof)
> **Theorem**: A non-empty subset $H \subseteq G$ is a subgroup of $G$ **if and only if**:
> $$\forall a, b \in H, \, a * b^{-1} \in H$$

##### Formal Mathematical Proof:
- **$(\implies)$ Direction (Necessary condition)**:
  - If $H \le G$, then $H$ is a group.
  - Let $a, b \in H$. Since $H$ contains inverses, $b^{-1} \in H$.
  - Since $H$ is closed under the group operation, $a * b^{-1} \in H$. Holds.
- **$(\impliedby)$ Direction (Sufficient condition)**:
  - Assume $H \neq \emptyset$ and $\forall a, b \in H, a * b^{-1} \in H$.
  - We must prove that $H$ satisfies all group axioms:
    1. **Identity**: Since $H \neq \emptyset$, choose any element $x \in H$. Setting $a = x$ and $b = x$, we have:
       $$e = x * x^{-1} \in H$$
       Thus, the identity element $e$ is in $H$.
    2. **Inverses**: Let $y \in H$. Setting $a = e \in H$ and $b = y \in H$, we have:
       $$y^{-1} = e * y^{-1} \in H$$
       Thus, every element has its inverse in $H$.
    3. **Closure**: Let $u, v \in H$. Since $v \in H$, its inverse $v^{-1} \in H$. Setting $a = u$ and $b = v^{-1}$, we have:
       $$u * (v^{-1})^{-1} = u * v \in H$$
       Thus, $H$ is closed under $*$.
    4. **Associativity**: Associativity holds automatically because $H \subseteq G$ and the operation $*$ is associative on all elements of $G$.
  - Therefore, $H$ is a subgroup of $G$. $\blacksquare$

#### 3. Finite Subgroup Test
> **Theorem**: Let $H$ be a non-empty **finite** subset of a group $G$. If $H$ is closed under the group operation ($a, b \in H \implies ab \in H$), then $H$ is a subgroup of $G$.
- *Proof*: In a finite set closed under multiplication, the sequence $a, a^2, a^3, \dots$ must eventually repeat by the Pigeonhole Principle ($a^i = a^j$ for $i > j$). Thus $a^{i-j} = e \in H$, and $a^{-1} = a^{i-j-1} \in H$. $\blacksquare$

---

### 5.4.2 Identifying All Subgroups of $\mathbb{Z}_9$ (NIT Jalandhar PYQ Solved)
Consider the group $\mathbb{Z}_9 = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}$ under addition modulo 9.
- Order of the group: $|\mathbb{Z}_9| = 9$.
- By **Lagrange's Theorem**, the order of any subgroup $H$ must divide $|\mathbb{Z}_9| = 9$.
- The divisors of 9 are: $1, 3, 9$.
- Therefore, any subgroup of $\mathbb{Z}_9$ must have order 1, 3, or 9:
  1. **Subgroup of order 1**:
     The trivial subgroup containing only the identity:
     $$H_1 = \{0\} = \langle 0 \rangle$$
  2. **Subgroup of order 3**:
     Generated by an element of order 3.
     In $\mathbb{Z}_9$, elements with order 3 satisfy $3x \equiv 0 \pmod 9 \implies x \in \{3, 6\}$.
     $$H_2 = \langle 3 \rangle = \langle 6 \rangle = \{0, 3, 6\}$$
     - *Check*: Closed under addition mod 9: $3+3=6, 3+6=0, 6+6=3$. Inverses: $3^{-1}=6, 6^{-1}=3, 0^{-1}=0$. Valid subgroup!
  3. **Subgroup of order 9**:
     The entire group itself:
     $$H_3 = \mathbb{Z}_9 = \langle 1 \rangle = \langle 2 \rangle = \langle 4 \rangle = \langle 5 \rangle = \langle 7 \rangle = \langle 8 \rangle$$
- **Conclusion**: $\mathbb{Z}_9$ has **exactly 3 subgroups**:
  $$\{0\}, \quad \{0, 3, 6\}, \quad \text{and} \quad \mathbb{Z}_9$$

---

## 5.5 CYCLIC GROUPS & NUMBER OF GENERATORS

A group $(G, *)$ is **cyclic** if there exists an element $g \in G$ such that every element of $G$ is a power (or multiple in additive notation) of $g$:
$$G = \langle g \rangle = \{g^k \mid k \in \mathbb{Z}\}$$
The element $g$ is called a **generator** of $G$.

### 5.5.1 Fundamental Properties of Cyclic Groups
1. **Every cyclic group is Abelian**:
   *Proof*: Let $x, y \in G$. Since $G = \langle g \rangle$, $x = g^r$ and $y = g^s$ for some integers $r, s$.
   $$x * y = g^r * g^s = g^{r+s} = g^{s+r} = g^s * g^r = y * x \quad \blacksquare$$
2. **Every subgroup of a cyclic group is cyclic**:
   *Proof*: Let $H \le G = \langle g \rangle$. If $H = \{e\}$, it is trivially cyclic. If $H \neq \{e\}$, let $m$ be the smallest positive integer such that $g^m \in H$. By the Division Algorithm, every element $g^k \in H$ satisfies $k = mq + r$ ($0 \le r < m$). Then $g^r = g^{k - mq} = g^k (g^m)^{-q} \in H$. Since $m$ was minimal, $r = 0$, so $k = mq$. Thus $H = \langle g^m \rangle$. $\blacksquare$

---

### 5.5.2 Generators of a Finite Cyclic Group & Euler's Totient Function
> **Theorem**: Let $G = \langle g \rangle$ be a cyclic group of order $n$. An element $g^k$ is a generator of $G$ **if and only if $\gcd(k, n) = 1$**.
- Consequently, the **total number of generators** of a finite cyclic group of order $n$ is given by **Euler's Totient Function $\phi(n)$**:
  $$\text{Number of Generators} = \phi(n)$$

#### Calculation of Euler's Totient Function:
If the prime factorization of $n$ is $n = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$, then:
$$\phi(n) = n \left( 1 - \frac{1}{p_1} \right) \left( 1 - \frac{1}{p_2} \right) \dots \left( 1 - \frac{1}{p_k} \right)$$

---

### 5.5.3 Cryptographic Generator Problem (NIT Jalandhar PYQ Solved)
**Problem Statement**:
A cryptographic system relies on a cyclic group $G$ of order $187$. To ensure system robustness, a generator $g$ must be chosen. How many elements in $G$ can serve as a generator? Show complete steps.

**Complete Mathematical Solution**:
1. **Identify the Order of the Group**:
   $$|G| = n = 187$$
2. **Prime Factorization of $n = 187$**:
   Testing small primes: $187$ is not divisible by 2, 3, 5, 7.
   Testing 11:
   $$\frac{187}{11} = 17$$
   Both $11$ and $17$ are prime numbers!
   Therefore:
   $$187 = 11 \times 17$$
3. **Apply the Generator Counting Theorem**:
   For any finite cyclic group of order $n$, the number of generators is $\phi(n)$.
4. **Compute $\phi(187)$**:
   Using the Euler totient product formula for distinct primes:
   $$\begin{aligned}
   \phi(187) &= \phi(11 \times 17) \\
   &= \phi(11) \times \phi(17) && \text{[Since } \gcd(11, 17) = 1\text{]} \\
   &= (11 - 1) \times (17 - 1) && \text{[Since } \phi(p) = p - 1 \text{ for prime } p\text{]} \\
   &= 10 \times 16 \\
   &= \mathbf{160}
   \end{aligned}$$
5. **Alternative Formula Verification**:
   $$\phi(187) = 187 \left( 1 - \frac{1}{11} \right) \left( 1 - \frac{1}{17} \right) = 187 \times \frac{10}{11} \times \frac{16}{17} = 17 \times 10 \times \frac{16}{17} = 10 \times 16 = 160$$
6. **Final Conclusion**:
   Exactly **$160$ elements** in $G$ can serve as valid generators for the cryptographic system.

---

## 5.6 COSETS & LAGRANGE'S THEOREM

### 5.6.1 Left Cosets and Right Cosets
Let $H$ be a subgroup of $(G, *)$. For any $a \in G$:
- The **left coset of $H$ containing $a$** is:
  $$aH = \{a * h \mid h \in H\}$$
- The **right coset of $H$ containing $a$** is:
  $$Ha = \{h * a \mid h \in H\}$$
- If $G$ is Abelian, $aH = Ha$ for all $a \in G$.

#### Fundamental Properties of Cosets:
1. $a \in aH$ (since $e \in H \implies a = ae \in aH$).
2. $aH = H \iff a \in H$.
3. $aH = bH \iff a^{-1}b \in H$.
4. **Coset Disjointness**: Either $aH = bH$ or $aH \cap bH = \emptyset$.
5. **Equal Cardinality**: Every coset $aH$ has the exact same cardinality as $H$:
   $$|aH| = |H|$$
   - *Proof*: The map $f: H \to aH$ defined by $f(h) = ah$ is a bijection.
     - Injective: $ah_1 = ah_2 \implies h_1 = h_2$ (left cancellation in $G$).
     - Surjective: Any element in $aH$ is of the form $ah$ by definition.
6. The family of left cosets forms a **partition of $G$**.

---

### 5.6.2 Lagrange's Theorem: Formal Statement and Full Proof
> **Theorem (Lagrange)**: If $G$ is a finite group and $H$ is a subgroup of $G$, then the order of $H$ divides the order of $G$:
> $$|H| \text{ divides } |G|$$
> Furthermore, the ratio $\frac{|G|}{|H|}$ equals the number of distinct left cosets of $H$ in $G$, termed the **index of $H$ in $G$** (denoted $[G : H]$):
> $$|G| = [G : H] \cdot |H|$$

```
                         THE GROUP G PARTITIONED BY COSETS
             ┌─────────────────────────────────────────────────────────┐
             │       G = a₁H  ∪  a₂H  ∪  a₃H  ∪  ...  ∪  a_k H         │
             ├─────────────┬─────────────┬─────────────┬───────────────┤
             │     a₁H     │     a₂H     │     a₃H     │     a_k H     │
             │   (= H)     │             │             │               │
             │  |H| items  │  |H| items  │  |H| items  │   |H| items   │
             └─────────────┴─────────────┴─────────────┴───────────────┘
                       Total elements in G = k · |H|
                       Therefore, |H| divides |G| evenly!
```

#### Complete Step-by-Step Mathematical Proof:
1. Let $G$ be a finite group of order $n = |G|$, and let $H$ be a subgroup of $G$ with $|H| = m$.
2. Consider the collection of all left cosets of $H$ in $G$:
   $$\{aH \mid a \in G\}$$
3. By the fundamental coset properties established above:
   - Every element $x \in G$ belongs to at least one coset (specifically $x \in xH$). Therefore:
     $$G = \bigcup_{a \in G} aH$$
   - Any two left cosets are either **strictly identical or completely disjoint**:
     $$\text{If } aH \neq bH \implies aH \cap bH = \emptyset$$
4. Since $G$ is finite, there can only be a finite number of distinct left cosets. Let this number be $k = [G : H]$.
5. Let $\{a_1 H, a_2 H, \dots, a_k H\}$ be the complete list of distinct, pairwise disjoint left cosets.
6. Therefore, the union is a disjoint union:
   $$G = a_1 H \cup a_2 H \cup \dots \cup a_k H, \quad \text{where } a_i H \cap a_j H = \emptyset \text{ for } i \neq j$$
7. Taking the cardinality of both sides:
   $$|G| = |a_1 H| + |a_2 H| + \dots + |a_k H|$$
8. Since every coset has cardinality equal to $|H| = m$:
   $$|a_i H| = m \quad \text{for all } i = 1, 2, \dots, k$$
9. Substituting this into the sum:
   $$|G| = \underbrace{m + m + \dots + m}_{k \text{ times}} = k \cdot m = k \cdot |H|$$
10. Rearranging:
    $$k = \frac{|G|}{|H|} \implies |H| \text{ divides } |G| \text{ evenly}$$
This completes the formal proof of Lagrange's Theorem. $\blacksquare$

---

### 5.6.3 Corollaries of Lagrange's Theorem

#### Corollary 1: Order of an Element Divides Group Order
> **Theorem**: In any finite group $G$, the order of every element $a \in G$ divides $|G|$.
- *Proof*: The cyclic subgroup generated by $a$ is $H = \langle a \rangle$.
- By definition of element order, $|H| = |a|$.
- By Lagrange's Theorem, $|H|$ divides $|G| \implies |a|$ divides $|G|$. $\blacksquare$
- Direct consequence: For any $a \in G$, $a^{|G|} = e$.

#### Corollary 2: Groups of Prime Order are Strictly Cyclic
> **Theorem**: Every group $G$ of prime order $p$ is cyclic, and any non-identity element generates $G$.
- *Proof*: Let $|G| = p$ where $p$ is prime.
- Choose any element $a \in G$ such that $a \neq e$.
- Consider the subgroup $H = \langle a \rangle$. Since $a \neq e$, $|H| \ge 2$.
- By Lagrange's Theorem, $|H|$ must divide $|G| = p$.
- Since $p$ is prime, its only positive divisors are $1$ and $p$.
- Since $|H| \ge 2$, $|H| = p = |G|$.
- Therefore, $H = \langle a \rangle = G$, proving that $G$ is cyclic and generated by $a$. $\blacksquare$

#### Corollary 3: Fermat's Little Theorem and Euler's Totient Theorem
- **Euler's Totient Theorem**: For any integer $a$ coprime to $n$ ($\gcd(a, n) = 1$):
  $$a^{\phi(n)} \equiv 1 \pmod n$$
  - *Proof*: The group of units $U(n) = (\mathbb{Z}_n^*, \cdot)$ has order $\phi(n)$. By Corollary 1, $a^{\phi(n)} = e = 1$. $\blacksquare$
- **Fermat's Little Theorem**: If $p$ is prime and $p \nmid a$:
  $$a^{p-1} \equiv 1 \pmod p \implies a^p \equiv a \pmod p$$

---

## 5.7 RINGS, INTEGRAL DOMAINS, AND FIELDS

### 5.7.1 Ring $(R, +, \cdot)$
An algebraic structure $(R, +, \cdot)$ equipped with two binary operations (Addition $+$ and Multiplication $\cdot$) is a **Ring** if it satisfies 8 axioms:
1. **$(R, +)$ is an Abelian Group**:
   - Closure: $a + b \in R$.
   - Associativity: $(a + b) + c = a + (b + c)$.
   - Additive Identity ($0$): $a + 0 = a$.
   - Additive Inverse ($-a$): $a + (-a) = 0$.
   - Commutativity: $a + b = b + a$.
2. **$(R, \cdot)$ is a Semi-group**:
   - Multiplicative Closure: $a \cdot b \in R$.
   - Multiplicative Associativity: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
3. **Multiplication Distributes over Addition**:
   - Left Distributive: $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$.
   - Right Distributive: $(b + c) \cdot a = (b \cdot a) + (c \cdot a)$.

#### Specialized Ring Terminology:
- **Commutative Ring**: A ring where multiplication is commutative ($a \cdot b = b \cdot a$).
- **Ring with Unity (Identity)**: A ring containing a multiplicative identity $1_R$ such that $a \cdot 1_R = 1_R \cdot a = a$ for all $a \in R$.

---

### 5.7.2 Zero Divisors & Integral Domains
- **Zero Divisors**: In a ring $R$, a non-zero element $a \neq 0$ is a zero divisor if there exists a non-zero element $b \neq 0$ such that:
  $$a \cdot b = 0 \quad \text{or} \quad b \cdot a = 0$$
  - Example: In $(\mathbb{Z}_6, +, \cdot)$, $2 \neq 0$ and $3 \neq 0$, but $2 \cdot 3 = 6 \equiv 0 \pmod 6$. Thus, $2$ and $3$ are zero divisors.
- **Integral Domain**: A **commutative ring with unity** $(1 \neq 0)$ that contains **NO zero divisors**:
  $$a \cdot b = 0 \implies a = 0 \lor b = 0$$
  - **Cancellation Law**: In an integral domain, if $a \neq 0$ and $a \cdot b = a \cdot c$, then $b = c$.

---

### 5.7.3 Field $(F, +, \cdot)$
A **Field** is a commutative ring with unity $(1 \neq 0)$ in which **every non-zero element possesses a multiplicative inverse**:
$$\forall a \in F \setminus \{0\}, \, \exists a^{-1} \in F \text{ such that } a \cdot a^{-1} = 1$$
Equivalently:
- $(F, +)$ is an Abelian group (identity 0).
- $(F \setminus \{0\}, \cdot)$ is an Abelian group (identity 1).
- Multiplication distributes over addition.

#### Fundamental Theorems on Domains and Fields:
1. **Theorem**: Every Field is an Integral Domain.
   - *Proof*: Let $a, b \in F$ with $a \cdot b = 0$. If $a \neq 0$, then $a^{-1}$ exists. Multiply both sides by $a^{-1}$:
     $$a^{-1}(ab) = a^{-1}(0) \implies (a^{-1}a)b = 0 \implies 1 \cdot b = 0 \implies b = 0$$
     Thus, $F$ has no zero divisors and is an integral domain. $\blacksquare$
2. **Theorem (Wedderburn's Lemma)**: Every **finite integral domain is a field**.
   - *Proof*: Let $D = \{0, x_1, x_2, \dots, x_n\}$ be a finite integral domain.
   - Choose any non-zero element $a \in D$. Consider the products $a x_1, a x_2, \dots, a x_n$.
   - All these $n$ products are non-zero (since $D$ has no zero divisors).
   - All these products are distinct: if $a x_i = a x_j$, by cancellation $x_i = x_j$.
   - Since $D$ has only $n$ non-zero elements, the set $\{a x_1, \dots, a x_n\}$ must be the entire set of non-zero elements of $D$.
   - In particular, the unity $1$ must be one of these products: $a x_k = 1$ for some $k$.
   - Thus, $x_k$ is the multiplicative inverse of $a$. Every non-zero element has an inverse! $\blacksquare$

---

### 5.7.4 Master Comparison Matrix: Algebraic Structures

| Algebraic Structure | Set & Operations | Addition $(+)$ Properties | Multiplication $(\cdot)$ Properties | Zero Divisors Allowed? | Multiplicative Inverses Required? | Canonical Examples |
|:---|:---|:---|:---|:---:|:---:|:---|
| **Semigroup** | $(S, *)$ | N/A | Closed, Associative | N/A | No | $(\mathbb{N}, +)$, Strings under concatenation |
| **Monoid** | $(M, *, e)$ | N/A | Closed, Associative, Identity | N/A | No | $(\mathbb{N}_0, +, 0)$, $(\Sigma^*, \cdot, \epsilon)$ |
| **Group** | $(G, *)$ | N/A | Closed, Assoc, Identity, Inverses | N/A | Yes | $(\mathbb{Z}, +)$, $GL(n, \mathbb{R})$ under matrix mult |
| **Abelian Group** | $(G, *)$ | N/A | Closed, Assoc, Identity, Inverses, **Commutative** | N/A | Yes | $(\mathbb{Z}, +)$, $(\mathbb{Z}_n, +_n)$ |
| **Ring** | $(R, +, \cdot)$ | Abelian Group | Semigroup, Distributive over $+$ | Yes | No | $(\mathbb{Z}, +, \cdot)$, $M_{n \times n}(\mathbb{R})$ |
| **Commutative Ring** | $(R, +, \cdot)$ | Abelian Group | Commutative Semigroup, Distributive | Yes | No | $(\mathbb{Z}_6, +, \cdot)$ |
| **Integral Domain** | $(D, +, \cdot)$ | Abelian Group | Commutative Monoid with Unity $1$, Distributive | **NO** | No | $(\mathbb{Z}, +, \cdot)$, Polynomial ring $\mathbb{R}[x]$ |
| **Field** | $(F, +, \cdot)$ | Abelian Group | Non-zero elements form **Abelian Group** under $\cdot$ | **NO** | **YES (all $x \neq 0$)** | $(\mathbb{Q}, +, \cdot)$, $(\mathbb{R}, +, \cdot)$, $(\mathbb{Z}_p, +, \cdot)$ for prime $p$ |

---
"""

if __name__ == "__main__":
    print(f"Unit 5 generated: {len(get_unit5_text())} characters")
