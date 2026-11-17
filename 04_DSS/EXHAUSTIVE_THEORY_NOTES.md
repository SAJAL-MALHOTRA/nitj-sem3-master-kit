# DISCRETE STRUCTURES (COURSE CODE: ITDC0211 / ITPC-309)
## ULTIMATE END-SEMESTER EXAMINATION THEORY MASTER BOOK
### Dr B R Ambedkar National Institute of Technology, Jalandhar (NIT Jalandhar)
#### Department of Information Technology | B.Tech Semester 3 / 5

---

> ### 📘 ACADEMIC PREFACE & PEDAGOGICAL OBJECTIVE
> This volume constitutes the definitive, exhaustive, and mathematically rigorous Theory Master Guide for **Discrete Structures (ITDC0211 / ITPC-309)**.
> Engineered specifically for end-semester academic examinations, this guide covers every concept from the foundational syllabus with zero omissions, zero high-level handwaving, and complete analytical proofs.
> 
> **Every unit integrates**:
> - Formal mathematical axioms, definitions, and domain constraints.
> - Step-by-step analytical derivations and formal logic truth tables.
> - ASCII architectural diagrams, Hasse lattices, state machines, and digraphs.
> - Full mathematical proofs (Handshaking Lemma, Euler's Planar Formula $V - E + F = 2$, Lagrange's Subgroup Theorem, Tree Edge-Vertex Theorem, Bipartite Cycle Characterization).
> - Fully worked step-by-step numerical problems and execution traces (Warshall, Dijkstra, Prim, Kruskal, Huffman, Extended Euclidean Algorithm).
> - Annotated C++ implementations for core discrete algorithms.
> - Complete, fully verified solutions to the actual NIT Jalandhar Mid-Semester and End-Semester examination questions.
> - Student Exam Traps, Common Pitfalls, and Scoring Strategies.

---

## MASTER TABLE OF CONTENTS

1. [UNIT 1: INTRODUCTION TO PRELIMINARIES AND PREDICATE CALCULUS](#unit-1-introduction-to-preliminaries-and-predicate-calculus)
   - 1.1 Foundations of Mathematical Logic & Discrete Mathematics
   - 1.2 Logical Connectives & Full Truth Tables
   - 1.3 Compound Propositions & Propositional Classification
   - 1.4 Laws of Logical Equivalence (Algebra of Propositions)
   - 1.5 Predicates and Quantifiers (First-Order Logic)
   - 1.6 Rules of Inference & Formal Deductive Proofs
   - 1.7 Normal Forms (DNF, CNF, PDNF, PCNF)
   - 1.8 Methods of Mathematical Proof
   - 1.9 High-Probability Exam Questions & Student Traps
2. [UNIT 2: SET THEORY, RELATIONS, FUNCTIONS, POSETS, LATTICES, COUNTING & DISCRETE STRUCTURES](#unit-2-set-theory-relations-functions-posets-lattices-counting--discrete-structures)
   - 2.1 Set Theory Foundations & Algebra of Sets
   - 2.2 Relations and Their Algebraic Properties
   - 2.3 Partial Orders (Posets) & Lattices
   - 2.4 Functions and Bijections
   - 2.5 Advanced Counting Principles & Combinatorics
   - 2.6 Number Theory & Modular Arithmetic
   - 2.7 Elements of Probability & Bayes' Theorem
   - 2.8 Recurrence Relations
3. [UNIT 3: GRAPH THEORY & NETWORK ARCHITECTURES](#unit-3-graph-theory--network-architectures)
   - 3.1 Fundamental Concepts & Classification of Graphs
   - 3.2 Special Families of Graphs & Topological Metrics
   - 3.3 Connectivity, Matrix Representations & Warshall's Algorithm
   - 3.4 Eulerian and Hamiltonian Graphs
   - 3.5 Planar Graphs & Graph Coloring
   - 3.6 Graph Isomorphism
4. [UNIT 4: BINARY TREES, TREE ALGORITHMS & DATA STRUCTURES](#unit-4-binary-trees-tree-algorithms--data-structures)
   - 4.1 Tree Architectures & Mathematical Foundations
   - 4.2 Binary Tree Traversals
   - 4.3 Binary Search Trees (BST)
   - 4.4 Spanning Trees & Minimum Spanning Trees (MST)
   - 4.5 Heaps: Min-Heap & Max-Heap
   - 4.6 Huffman's Data Compression Algorithm
5. [UNIT 5: ALGEBRAIC STRUCTURES & MATHEMATICAL INDUCTION](#unit-5-algebraic-structures--mathematical-induction)
   - 5.1 Mathematical Induction
   - 5.2 Binary Operations & Their Algebraic Properties
   - 5.3 Hierarchy of Algebraic Structures
   - 5.4 Subgroups & Subgroup Tests
   - 5.5 Cyclic Groups & Number of Generators
   - 5.6 Cosets & Lagrange's Theorem
   - 5.7 Rings, Integral Domains, and Fields
6. [APPENDICES: CODE IMPLEMENTATIONS, PYQ SOLUTIONS & EXAM CHEAT SHEET](#appendices-code-implementations-pyq-solutions--exam-cheat-sheet)
   - Appendix A: Master Formula & Theorem Quick Reference Cheat Sheet
   - Appendix B: Annotated C++ Implementations for Core Discrete Algorithms
   - Appendix C: NIT Jalandhar Comprehensive Examination Solutions (Midsem & Endsem)

---



# UNIT 1: INTRODUCTION TO PRELIMINARIES AND PREDICATE CALCULUS

---

## 1.1 FOUNDATIONS OF MATHEMATICAL LOGIC & DISCRETE MATHEMATICS

### 1.1.1 What is Discrete Mathematics?
Discrete Mathematics is the mathematical foundation of computer science. Unlike continuous mathematics (calculus, differential equations), which deals with smoothly varying real numbers, discrete mathematics deals with distinct, separated, countable mathematical structures. In computing, where data is represented digitally as finite sequences of discrete bits ($0$ and $1$), memory addresses are discrete, algorithms execute in discrete time steps, and data structures (trees, graphs, networks) consist of discrete interconnected entities, discrete mathematics provides the fundamental language of abstraction, specification, verification, and analysis.

### 1.1.2 Propositions and Truth Values
A **proposition** (or statement) is a declarative sentence that is either **strictly True ($T$ or $1$)** or **strictly False ($F$ or $0$)**, but **never both simultaneously**. The truth or falsity of a proposition is termed its **truth value**.

#### Formal Mathematical Criteria for Propositions:
1. **Declarative Syntax**: It must make an assertive factual claim about reality or a mathematical universe.
2. **Determinable Truth Value**: Given unambiguous definitions, its truth value must be uniquely decidable (even if computationally difficult to evaluate or unknown to current human knowledge).
3. **Law of the Excluded Middle**: Every proposition $p$ must be either $T$ or $F$ ($p \lor \neg p \equiv \top$).
4. **Law of Non-Contradiction**: A proposition cannot be both $T$ and $F$ simultaneously ($p \land \neg p \equiv \bot$).

```
                    ┌────────────────────────────────────────┐
                    │               SENTENCE                 │
                    └───────────────────┬────────────────────┘
                                        │
                         Is it a declarative statement?
                                        │
                        ┌───────────────┴───────────────┐
                       YES                              NO
                        │                               │
        Does it have a definite, single         [NON-PROPOSITION]
             truth value (T or F)?               - Interrogative: "What is n?"
                        │                        - Imperative: "Sort this array!"
                ┌───────┴───────┐                - Exclamatory: "Wow, fast code!"
               YES              NO               - Subjective: "Python is best."
                │               │
          [PROPOSITION]     [PARADOX / ILL-DEFINED]
      - "7 is a prime" (T)   - "This statement is false." (Liar Paradox)
      - "2 + 2 = 5" (F)      - "The set of all sets that do not contain
      - "For all n, n²>=0" (T) themselves." (Russell's Paradox)
```

#### Examples of Propositions:
- $p_1$: "$\pi$ is an irrational number." (Truth value: **True**)
- $p_2$: "$2^{10} = 1024$." (Truth value: **True**)
- $p_3$: "For every integer $n$, $n^2 \ge 0$." (Truth value: **True**)
- $p_4$: "$15$ is divisible by $4$." (Truth value: **False**)
- $p_5$: "Goldbach's Conjecture is true." (Even though unproven, it has an objective truth value: **Proposition**)

#### Non-Propositions (Sentences that FAIL the definition):
1. **Imperative commands**: "Run the quicksort algorithm immediately!" (No truth value)
2. **Interrogative sentences**: "Is $P = NP$?" (A question is neither true nor false)
3. **Exclamations**: "What a beautiful binary tree!" (Subjective evaluation)
4. **Sentences with free unbound variables**: "$x + 5 = 12$" (Truth depends on $x$; without a quantifier or value assignment, it is a *predicate*, not a proposition)
5. **Self-Referential Paradoxes**: "This statement is false." 
   - If assumed True $\implies$ the statement is False (Contradiction).
   - If assumed False $\implies$ the statement is True (Contradiction).
   - Thus, it violates the fundamental axiom of logic and is not a proposition.

---

## 1.2 LOGICAL CONNECTIVES & FULL TRUTH TABLES

Propositional logic builds complex statements from atomic propositions using **logical connectives** (operators).

### 1.2.1 Negation ($\neg$ or $\sim$)
The **negation** of proposition $p$, denoted $\neg p$ (read "NOT $p$"), is the proposition whose truth value is the exact opposite of $p$.
- **Formal definition**: $\neg p$ is True if $p$ is False; $\neg p$ is False if $p$ is True.
- **Hardware Equivalent**: Inverter / NOT Gate.

### 1.2.2 Conjunction ($\land$)
The **conjunction** of propositions $p$ and $q$, denoted $p \land q$ (read "$p$ AND $q$"), is the compound proposition that is True **if and only if both $p$ and $q$ are True**.
- **Formal definition**: $v(p \land q) = \min(v(p), v(q))$ where $v: \text{Prop} \to \{0, 1\}$.
- **Hardware Equivalent**: AND Gate.

### 1.2.3 Disjunction ($\lor$) - Inclusive OR
The **disjunction** of propositions $p$ and $q$, denoted $p \lor q$ (read "$p$ OR $q$"), is the compound proposition that is True **if at least one of $p$ or $q$ is True**, and False only when both are False.
- **Formal definition**: $v(p \lor q) = \max(v(p), v(q))$.
- **Hardware Equivalent**: OR Gate.

### 1.2.4 Exclusive OR ($\oplus$ or $\text{XOR}$)
The **exclusive disjunction** of propositions $p$ and $q$, denoted $p \oplus q$ (read "$p$ XOR $q$"), is True **if exactly one of $p$ or $q$ is True, but not both**.
- **Formal definition**: $p \oplus q \equiv (p \land \neg q) \lor (\neg p \land q) \equiv (p \lor q) \land \neg(p \land q)$.
- **Parity Property**: In digital circuits, XOR is an odd-parity checker: $x_1 \oplus x_2 \oplus \dots \oplus x_n$ is $1$ iff the number of $1$s is odd.
- **Hardware Equivalent**: XOR Gate.

### 1.2.5 Conditional Statement / Implication ($\to$ or $\implies$)
The **conditional proposition** $p \to q$ (read "if $p$, then $q$") asserts that whenever the **hypothesis / antecedent** $p$ is True, the **conclusion / consequent** $q$ must also be True.
- **Formal definition**: $p \to q$ is **False ONLY when $p$ is True and $q$ is False**. In all other cases, $p \to q$ is **True**.
- **Equivalent Logical Form**: $p \to q \equiv \neg p \lor q$.

#### The Concept of Vacuous Truth (Crucial Exam Concept)
When the hypothesis $p$ is False ($p = F$), the conditional statement $p \to q$ evaluates to **True**, regardless of whether $q$ is True or False.
- *Why?* A conditional statement makes a promise: "If $p$ happens, I promise $q$ will happen." If $p$ never occurs, the promise was never broken. Therefore, the statement cannot be declared False.
- *Mathematical Example*: "If $0 = 1$, then I am the King of England." Hypothesis $0=1$ is False, so the statement is **vacuously True**.

#### Natural Language Variants of $p \to q$:
- "If $p$, then $q$"
- "$p$ implies $q$"
- "$p$ is sufficient for $q$" (If $p$ holds, it is enough to guarantee $q$)
- "$q$ is necessary for $p$" (Without $q$, $p$ cannot hold: $\neg q \to \neg p$)
- "$q$ whenever $p$"
- "$p$ only if $q$" (Warning: "$p$ only if $q$" means $p \to q$, NOT $q \to p$)
- "$q$ unless $\neg p$" ($\neg p$ is the condition that frees $q$, meaning $\neg(\neg p) \to q \implies p \to q$)

#### Related Conditionals: Converse, Inverse, and Contrapositive
For a given conditional statement $p \to q$:
1. **Converse**: $q \to p$ (Swaps hypothesis and conclusion).
2. **Inverse**: $\neg p \to \neg q$ (Negates both hypothesis and conclusion).
3. **Contrapositive**: $\neg q \to \neg p$ (Swaps and negates both).

```
                      p ─── Conditional (p → q) ───> q
                      │                              │
           Negate     │                              │ Negate
                      ▼                              ▼
                   ¬p ───      Inverse       ───> ¬q
                      │                              │
                      │                              │
                      ▲                              ▲
                      │      Converse (q → p)        │
                      └──────────────────────────────┘
               Contrapositive of (p → q) is (¬q → ¬p)
```

**Fundamental Theorem of Conditional Equivalence**:
- A conditional statement is **logically equivalent to its contrapositive**:
  $$p \to q \equiv \neg q \to \neg p$$
- The converse is **logically equivalent to the inverse**:
  $$q \to p \equiv \neg p \to \neg q$$
- A conditional statement is **NOT** logically equivalent to its converse or inverse:
  $$(p \to q) \not\equiv (q \to p)$$

### 1.2.6 Biconditional Statement ($\leftrightarrow$ or $\iff$)
The **biconditional proposition** $p \leftrightarrow q$ (read "$p$ if and only if $q$", abbreviated "$p$ iff $q$") asserts that $p$ and $q$ have identical truth values.
- **Formal definition**: $p \leftrightarrow q$ is True when both $p$ and $q$ are True, or both are False.
- **Decomposition**: $p \leftrightarrow q \equiv (p \to q) \land (q \to p) \equiv (p \land q) \lor (\neg p \land \neg q)$.
- **Relation to XOR**: $p \leftrightarrow q \equiv \neg(p \oplus q)$ (Equivalence is XNOR).

---

### 1.2.7 Master Consolidated Truth Table
The following master table specifies the exact truth values for all binary connectives across all possible assignments of $p$ and $q$:

| $p$ | $q$ | $\neg p$ | $p \land q$ (AND) | $p \lor q$ (OR) | $p \oplus q$ (XOR) | $p \to q$ (Implies) | $q \to p$ (Converse) | $\neg p \to \neg q$ (Inverse) | $\neg q \to \neg p$ (Contrapositive) | $p \leftrightarrow q$ (XNOR / Iff) |
|:---:|:---:|:--------:|:-----------------:|:---------------:|:------------------:|:-------------------:|:--------------------:|:-----------------------------:|:------------------------------------:|:----------------------------------:|
|  T  |  T  |    F     |         T         |        T        |         F          |          T          |          T           |               T               |                  T                   |                 T                  |
|  T  |  F  |    F     |         F         |        T        |         T          |          F          |          T           |               T               |                  F                   |                 F                  |
|  F  |  T  |    T     |         F         |        T        |         T          |          T          |          F           |               F               |                  T                   |                 F                  |
|  F  |  F  |    T     |         F         |        F        |         F          |          T          |          T           |               T               |                  T                   |                 T                  |

> **Notice**: Column 7 ($p \to q$) is identical to Column 10 ($\neg q \to \neg p$). Column 8 ($q \to p$) is identical to Column 9 ($\neg p \to \neg q$).

---

## 1.3 COMPOUND PROPOSITIONS & CLASSIFICATION

A compound proposition is classified into one of three categories based on its truth table evaluation across all possible truth assignments of its constituent variables:

1. **Tautology**: A compound proposition that is **True under all possible truth assignments**.
   - Denoted by $\top$ or $\mathbf{1}$.
   - Example: $p \lor \neg p$ (Law of the Excluded Middle), $p \to p$, $(p \land (p \to q)) \to q$ (Modus Ponens).
2. **Contradiction (or Absurdity / Fallacy)**: A compound proposition that is **False under all possible truth assignments**.
   - Denoted by $\bot$ or $\mathbf{0}$.
   - Example: $p \land \neg p$ (Principle of Non-Contradiction), $p \leftrightarrow \neg p$.
3. **Contingency**: A compound proposition that is **neither a tautology nor a contradiction**; its truth value depends on the assignments given to its constituent variables (has at least one True and at least one False in its truth table).
   - Example: $p \land q$, $p \to q$, $p \oplus q$.

```
                            COMPOUND PROPOSITIONS
                                      │
                     ┌────────────────┴────────────────┐
                     │                                 │
           Truth value constant?             Truth value varies?
                     │                                 │
             ┌───────┴───────┐                         │
            YES              YES                       │
             │                │                        │
       Always TRUE      Always FALSE           TRUE for some,
             │                │                FALSE for others
             ▼                ▼                        ▼
        [TAUTOLOGY]    [CONTRADICTION]           [CONTINGENCY]
        (p ∨ ¬p ≡ ⊤)     (p ∧ ¬p ≡ ⊥)             (p ∧ q, p → q)
```

---

## 1.4 LAWS OF LOGICAL EQUIVALENCE (ALGEBRA OF PROPOSITIONS)

Two compound propositions $A$ and $B$ are **logically equivalent**, denoted $A \equiv B$ or $A \iff B$, if $A \leftrightarrow B$ is a tautology (i.e., they possess identical truth values for every possible valuation of their variables).

### 1.4.1 Comprehensive Catalog of Logical Equivalence Laws

| Law Name | Algebraic Identities |
|:---|:---|
| **Identity Laws** | $p \land \top \equiv p$ <br> $p \lor \bot \equiv p$ |
| **Domination (Null) Laws** | $p \lor \top \equiv \top$ <br> $p \land \bot \equiv \bot$ |
| **Idempotent Laws** | $p \lor p \equiv p$ <br> $p \land p \equiv p$ |
| **Double Negation Law** | $\neg(\neg p) \equiv p$ |
| **Commutative Laws** | $p \lor q \equiv q \lor p$ <br> $p \land q \equiv q \land p$ |
| **Associative Laws** | $(p \lor q) \lor r \equiv p \lor (q \lor r)$ <br> $(p \land q) \land r \equiv p \land (q \land r)$ |
| **Distributive Laws** | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ <br> $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ |
| **De Morgan's Laws** | $\neg(p \land q) \equiv \neg p \lor \neg q$ <br> $\neg(p \lor q) \equiv \neg p \land \neg q$ |
| **Absorption Laws** | $p \lor (p \land q) \equiv p$ <br> $p \land (p \lor q) \equiv p$ |
| **Negation (Complement) Laws** | $p \lor \neg p \equiv \top$ <br> $p \land \neg p \equiv \bot$ |
| **Conditional (Implication) Equivalences** | $p \to q \equiv \neg p \lor q$ <br> $p \to q \equiv \neg q \to \neg p$ (Contrapositive) <br> $p \lor q \equiv \neg p \to q$ <br> $p \land q \equiv \neg(p \to \neg q)$ <br> $\neg(p \to q) \equiv p \land \neg q$ |
| **Exportation / Importation Law** | $(p \land q) \to r \equiv p \to (q \to r)$ |
| **Biconditional Equivalences** | $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$ <br> $p \leftrightarrow q \equiv (\neg p \lor q) \land (\neg q \lor p)$ <br> $p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)$ <br> $\neg(p \leftrightarrow q) \equiv p \leftrightarrow \neg q \equiv p \oplus q$ |

---

### 1.4.2 Mathematical Derivations & Proofs of Fundamental Laws

#### Proof 1: Rigorous Derivation of Absorption Law $p \lor (p \land q) \equiv p$
$$\begin{aligned}
p \lor (p \land q) &\equiv (p \land \top) \lor (p \land q) && \text{[Identity Law: } p \equiv p \land \top\text{]} \\
&\equiv p \land (\top \lor q) && \text{[Distributive Law]} \\
&\equiv p \land (q \lor \top) && \text{[Commutative Law]} \\
&\equiv p \land \top && \text{[Domination Law: } q \lor \top \equiv \top\text{]} \\
&\equiv p && \text{[Identity Law: } p \land \top \equiv p\text{]} \quad \blacksquare
\end{aligned}$$

#### Proof 2: Step-by-Step Truth Table Verification of De Morgan's Law $\neg(p \land q) \equiv \neg p \lor \neg q$

| $p$ | $q$ | $p \land q$ | $\neg(p \land q)$ [Col A] | $\neg p$ | $\neg q$ | $\neg p \lor \neg q$ [Col B] | Col A $\leftrightarrow$ Col B |
|:---:|:---:|:-----------:|:-------------------------:|:--------:|:--------:|:----------------------------:|:------------------------------:|
|  T  |  T  |      T      |             F             |    F     |    F     |              F               |               T                |
|  T  |  F  |      F      |             T             |    F     |    T     |              T               |               T                |
|  F  |  T  |      F      |             T             |    T     |    F     |              T               |               T                |
|  F  |  F  |      F      |             T             |    T     |    T     |              T               |               T                |

Since Col A and Col B match for all possible valuations, $\neg(p \land q) \equiv \neg p \lor \neg q$. $\blacksquare$

#### Proof 3: Proving $(p \to (q \to r)) \equiv ((p \land q) \to r)$ (Exportation Law)
$$\begin{aligned}
p \to (q \to r) &\equiv \neg p \lor (q \to r) && \text{[Conditional Law]} \\
&\equiv \neg p \lor (\neg q \lor r) && \text{[Conditional Law]} \\
&\equiv (\neg p \lor \neg q) \lor r && \text{[Associative Law]} \\
&\equiv \neg(p \land q) \lor r && \text{[De Morgan's Law]} \\
&\equiv (p \land q) \to r && \text{[Conditional Law]} \quad \blacksquare
\end{aligned}$$

---

## 1.5 PREDICATES AND QUANTIFIERS (FIRST-ORDER LOGIC)

Propositional logic cannot express relationships within statements like "Every prime greater than 2 is odd" or "There exists a computer program that halts on all inputs." Predicate logic (First-Order Logic) extends propositional logic by introducing variables, predicates, domains, and quantifiers.

### 1.5.1 Predicates and Universe of Discourse
A **predicate** (or propositional function) is an expression containing variables that becomes a proposition when concrete values from a specified **Domain (Universe of Discourse $U$)** are assigned to the variables.
- Notation: $P(x)$, $Q(x, y)$, $S(x_1, \dots, x_n)$.
- $P(x)$: "$x > 3$". If $U = \mathbb{Z}$:
  - $P(4)$ is True.
  - $P(2)$ is False.

### 1.5.2 Universal Quantifier ($\forall$)
The **universal quantification** of $P(x)$, denoted $\forall x P(x)$ (read "for all $x, P(x)$" or "for every $x, P(x)$"), asserts that $P(x)$ is True for **every element $x$ in the domain $U$**.
- **Truth Condition**: $\forall x P(x)$ is **True** iff $P(x)$ is True for all $x \in U$.
- **Falsity Condition**: $\forall x P(x)$ is **False** iff there exists at least one element $c \in U$ such that $P(c)$ is False. Such an element $c$ is termed a **counterexample**.
- **Finite Domain Expansion**: If $U = \{x_1, x_2, \dots, x_n\}$, then:
  $$\forall x P(x) \equiv P(x_1) \land P(x_2) \land \dots \land P(x_n)$$

### 1.5.3 Existential Quantifier ($\exists$)
The **existential quantification** of $P(x)$, denoted $\exists x P(x)$ (read "there exists an $x$ such that $P(x)$" or "for at least one $x, P(x)$"), asserts that $P(x)$ is True for **at least one element $x$ in the domain $U$**.
- **Truth Condition**: $\exists x P(x)$ is **True** iff there exists at least one $c \in U$ for which $P(c)$ is True.
- **Falsity Condition**: $\exists x P(x)$ is **False** iff for every $x \in U$, $P(x)$ is False.
- **Finite Domain Expansion**: If $U = \{x_1, x_2, \dots, x_n\}$, then:
  $$\exists x P(x) \equiv P(x_1) \lor P(x_2) \lor \dots \lor P(x_n)$$

### 1.5.4 Uniqueness Quantifier ($\exists!$ or $\exists_1$)
$\exists! x P(x)$ means "there exists a unique $x$ such that $P(x)$" (exactly one element in $U$ satisfies $P(x)$).
- **Formal First-Order Representation**:
  $$\exists! x P(x) \equiv \exists x \Big( P(x) \land \forall y \big( P(y) \to y = x \big) \Big)$$

---

### 1.5.5 Negating Quantified Statements (De Morgan's Laws for Quantifiers)
To negate a quantified statement, change the quantifier to its dual and negate the predicate:

$$\neg \forall x P(x) \equiv \exists x \neg P(x)$$
$$\neg \exists x P(x) \equiv \forall x \neg P(x)$$

#### Formal Proof using Finite Domain Expansion:
Let $U = \{x_1, x_2, \dots, x_n\}$.
$$\begin{aligned}
\neg \forall x P(x) &\equiv \neg \big( P(x_1) \land P(x_2) \land \dots \land P(x_n) \big) \\
&\equiv \neg P(x_1) \lor \neg P(x_2) \lor \dots \lor \neg P(x_n) && \text{[By De Morgan's Law for } \land \text{]} \\
&\equiv \exists x \neg P(x) \quad \blacksquare
\end{aligned}$$

---

### 1.5.6 Nested Quantifiers & Scope Order Dependency
When multiple quantifiers appear, the **order of quantifiers is critical** unless they are of the same type.

| Expression | Meaning | Truth Condition |
|:---|:---|:---|
| $\forall x \forall y P(x, y)$ | For all $x$ and for all $y$, $P(x, y)$ | $P(x, y)$ is True for every pair $(x, y)$. |
| $\forall x \exists y P(x, y)$ | For every $x$, there is a $y$ such that $P(x, y)$ | For each given $x$, we can find at least one $y$ (possibly dependent on $x$). |
| $\exists y \forall x P(x, y)$ | There exists a $y$ such that for all $x$, $P(x, y)$ | A single uniform $y$ works simultaneously for all $x$. |
| $\exists x \exists y P(x, y)$ | There exists a pair $(x, y)$ satisfying $P(x, y)$ | At least one pair $(x, y)$ satisfies the predicate. |

> **CRITICAL THEOREM**: $\exists y \forall x P(x, y) \implies \forall x \exists y P(x, y)$, but the converse IS FALSE!
> 
> *Concrete Counterexample*:
> Let $U = \mathbb{R}$ and $P(x, y)$ be "$x + y = 0$".
> - Statement 1: $\forall x \exists y (x + y = 0)$ is **True** (Given any $x$, choose $y = -x$).
> - Statement 2: $\exists y \forall x (x + y = 0)$ is **False** (There is no single constant $y$ that when added to all real numbers yields 0).

---

### 1.5.7 Translation of Natural Language into Predicate Logic

#### Exam Problem: System State Specifications
Translate the following system specifications where $S(x, y)$ is "$x$ is in state $y$", with domains $x \in \text{Systems}, y \in \text{States}$:
1. $\exists x S(x, \text{open})$: "There exists at least one system that is in the open state."
2. $\forall x (S(x, \text{malfunctioning}) \lor S(x, \text{diagnostic}))$: "Every system is either malfunctioning or in diagnostic mode (or both)."
3. $\exists x S(x, \text{open}) \lor \exists x S(x, \text{diagnostic})$: "At least one system is open, or at least one system is in diagnostic mode."
4. $\exists x \neg S(x, \text{available})$: "There exists a system that is not available."
5. $\forall x \neg S(x, \text{working})$: "No system is working" (or "Every system is not working").

#### Exam Problem: Complex Relational Translation
Express: "If a person is female and is a parent, then this person is someone's mother."
- Universe $U$: All people.
- Predicates: $F(x)$ = "$x$ is female", $P(x)$ = "$x$ is a parent", $M(x, y)$ = "$x$ is the mother of $y$".
- Formal Logic:
  $$\forall x \Big( \big( F(x) \land P(x) \big) \to \exists y M(x, y) \Big)$$

---

## 1.6 RULES OF INFERENCE & FORMAL DEDUCTIVE PROOFS

An **argument** is a sequence of propositions ending with a conclusion. An argument is **valid** if the truth of all premises forces the conclusion to be True.
$$\text{Premise}_1 \land \text{Premise}_2 \land \dots \land \text{Premise}_k \implies \text{Conclusion}$$

### 1.6.1 Master Table: Rules of Inference for Propositional Logic

| Rule of Inference | Name | Tautological Form | Description |
|:---|:---|:---|:---|
| $\begin{aligned} &p \\ &p \to q \\ \hline \therefore &q \end{aligned}$ | **Modus Ponens** (Rule of Detachment) | $(p \land (p \to q)) \to q$ | If hypothesis holds, conclusion must hold. |
| $\begin{aligned} &\neg q \\ &p \to q \\ \hline \therefore &\neg p \end{aligned}$ | **Modus Tollens** (Denying the Consequent) | $(\neg q \land (p \to q)) \to \neg p$ | If conclusion fails, hypothesis must fail. |
| $\begin{aligned} &p \to q \\ &q \to r \\ \hline \therefore &p \to r \end{aligned}$ | **Hypothetical Syllogism** (Chain Rule) | $((p \to q) \land (q \to r)) \to (p \to r)$ | Transitivity of logical implication. |
| $\begin{aligned} &p \lor q \\ &\neg p \\ \hline \therefore &q \end{aligned}$ | **Disjunctive Syllogism** | $((p \lor q) \land \neg p) \to q$ | Eliminating one branch forces the other. |
| $\begin{aligned} &p \\ \hline \therefore &p \lor q \end{aligned}$ | **Addition** | $p \to (p \lor q)$ | If $p$ is True, $p$ OR anything is True. |
| $\begin{aligned} &p \land q \\ \hline \therefore &p \end{aligned}$ | **Simplification** | $(p \land q) \to p$ | If both hold, each component holds individually. |
| $\begin{aligned} &p \\ &q \\ \hline \therefore &p \land q \end{aligned}$ | **Conjunction** | $((p) \land (q)) \to (p \land q)$ | Combining independent truths. |
| $\begin{aligned} &p \lor q \\ &\neg p \lor r \\ \hline \therefore &q \lor r \end{aligned}$ | **Resolution** | $((p \lor q) \land (\neg p \lor r)) \to (q \lor r)$ | Core engine of automated theorem provers. |

---

### 1.6.2 Logical Fallacies (Invalid Reasoning)

1. **Fallacy of Affirming the Consequent**:
   $$\begin{aligned} &p \to q \\ &q \\ \hline \therefore &p \quad \text{[INVALID]} \end{aligned}$$
   - *Error*: Finding $q$ True does NOT guarantee $p$ was the cause ($p$ could be False while $q$ is True).
   - *Example*: "If it rains, the grass is wet. The grass is wet. Therefore, it rained." (Someone could have used a sprinkler!)
2. **Fallacy of Denying the Antecedent**:
   $$\begin{aligned} &p \to q \\ &\neg p \\ \hline \therefore &\neg q \quad \text{[INVALID]} \end{aligned}$$
   - *Error*: Even if $p$ did not happen, $q$ could still happen through other causes.

---

### 1.6.3 Rules of Inference for Quantified Statements

| Rule | Name | Condition / Restriction |
|:---|:---|:---|
| $\begin{aligned} &\forall x P(x) \\ \hline \therefore &P(c) \end{aligned}$ | **Universal Instantiation (UI)** | $c$ is an arbitrary or specific member of domain $U$. |
| $\begin{aligned} &P(c) \text{ for an arbitrary } c \\ \hline \therefore &\forall x P(x) \end{aligned}$ | **Universal Generalization (UG)** | $c$ must be strictly arbitrary (no special assumptions made on $c$). |
| $\begin{aligned} &\exists x P(x) \\ \hline \therefore &P(c) \text{ for some element } c \end{aligned}$ | **Existential Instantiation (EI)** | $c$ must be a fresh constant not previously used in the proof. |
| $\begin{aligned} &P(c) \text{ for some known } c \\ \hline \therefore &\exists x P(x) \end{aligned}$ | **Existential Generalization (EG)** | $c$ is a valid member of domain $U$. |

---

### 1.6.4 Fully Worked Formal Deductive Proof
**Problem**: Prove the conclusion $r$ from the following premises:
1. $p \to q$
2. $\neg r \to \neg q$
3. $p$

**Two-Column Step-by-Step Proof**:

| Step | Statement | Justification |
|:---:|:---|:---|
| 1 | $p$ | Premise 3 |
| 2 | $p \to q$ | Premise 1 |
| 3 | $q$ | Modus Ponens on steps (1) and (2) |
| 4 | $\neg r \to \neg q$ | Premise 2 |
| 5 | $q \to r$ | Contrapositive of step (4) |
| 6 | $r$ | Modus Ponens on steps (3) and (5) $\blacksquare$ |

---

## 1.7 NORMAL FORMS (DNF, CNF, PDNF, PCNF)

Normal forms provide canonical structural representations for Boolean and propositional formulas, vital for hardware logic synthesis, circuit optimization, and SAT-solvers.

### 1.7.1 Definitions & Distinctions
- **Literal**: A propositional variable ($p$) or its negation ($\neg p$).
- **Fundamental Conjunction (Minterm)**: A conjunction ($\land$) of literals where every variable appears exactly once (either complemented or uncomplemented).
  - A minterm evaluates to **1 (True) for exactly ONE truth assignment**.
  - For $n$ variables, there are $2^n$ unique minterms, denoted $m_0, m_1, \dots, m_{2^n-1}$.
- **Fundamental Disjunction (Maxterm)**: A disjunction ($\lor$) of literals where every variable appears exactly once.
  - A maxterm evaluates to **0 (False) for exactly ONE truth assignment**.
  - For $n$ variables, there are $2^n$ unique maxterms, denoted $M_0, M_1, \dots, M_{2^n-1}$.
- **Disjunctive Normal Form (DNF)**: A disjunction of conjunctions (Sum of Products, SOP):
  $$(L_{1,1} \land \dots \land L_{1,k}) \lor (L_{2,1} \land \dots \land L_{2,m}) \lor \dots$$
- **Conjunctive Normal Form (CNF)**: A conjunction of disjunctions (Product of Sums, POS):
  $$(L_{1,1} \lor \dots \lor L_{1,k}) \land (L_{2,1} \lor \dots \lor L_{2,m}) \land \dots$$
- **Principal Disjunctive Normal Form (PDNF / Canonical SOP)**: A DNF where **every conjunction is a minterm** containing all variables of the formula.
- **Principal Conjunctive Normal Form (PCNF / Canonical POS)**: A CNF where **every disjunction is a maxterm** containing all variables of the formula.

```
       Minterms (AND of all vars)  ──(OR together)──>  PDNF (Canonical SOP)
       [Evaluates to 1 for unique row]                 [Collect rows where formula = 1]

       Maxterms (OR of all vars)   ──(AND together)─>  PCNF (Canonical POS)
       [Evaluates to 0 for unique row]                 [Collect rows where formula = 0]
```

---

### 1.7.2 Step-by-Step Conversion Algorithms

#### Method 1: Truth Table Construction (Guaranteed & Systematic)
1. Construct the complete truth table for formula $F(p_1, \dots, p_n)$ containing all $2^n$ rows.
2. **For PDNF**:
   - Locate every row where $F = 1$ (True).
   - For each such row, construct a minterm: variable $p_i$ is taken as $p_i$ if its value is $T$, and $\neg p_i$ if its value is $F$.
   - Form the disjunction ($\lor$) of all these minterms: $\text{PDNF} = \bigvee_{F(\mathbf{v})=1} m_i = \sum m(\dots)$.
3. **For PCNF**:
   - Locate every row where $F = 0$ (False).
   - For each such row, construct a maxterm: variable $p_i$ is taken as $\neg p_i$ if its value is $T$, and $p_i$ if its value is $F$.
   - Form the conjunction ($\land$) of all these maxterms: $\text{PCNF} = \bigwedge_{F(\mathbf{v})=0} M_i = \prod M(\dots)$.

#### Method 2: Algebraic Expansion
- **To obtain PDNF algebraically**:
  1. Eliminate $\to$ and $\leftrightarrow$ using conditional laws.
  2. Push negations inward using De Morgan's laws.
  3. Apply Distributive laws to get DNF.
  4. If a term lacks variable $x$, introduce it by ANDing with $(x \lor \neg x)$:
     $$T \equiv T \land (x \lor \neg x) \equiv (T \land x) \lor (T \land \neg x)$$
  5. Remove duplicate terms using Idempotent laws ($A \lor A \equiv A$).
- **To obtain PCNF algebraically**:
  1. In a disjunction lacking variable $x$, introduce it by ORing with $(x \land \neg x)$:
     $$D \equiv D \lor (x \land \neg x) \equiv (D \lor x) \land (D \lor \neg x)$$

---

### 1.7.3 Fully Worked Example: PDNF and PCNF Calculation
**Problem**: Obtain the PDNF and PCNF of $F(p, q, r) = (p \land q) \lor (\neg p \land r)$.

**Step 1: Construct Truth Table**:

| Row | $p$ | $q$ | $r$ | $p \land q$ | $\neg p$ | $\neg p \land r$ | $F = (p \land q) \lor (\neg p \land r)$ | Minterm / Maxterm Label |
|:---:|:---:|:---:|:---:|:-----------:|:--------:|:----------------:|:---------------------------------------:|:-----------------------:|
|  0  |  0  |  0  |  0  |      0      |    1     |        0         |                    0                    |     Maxterm $M_0 = p \lor q \lor r$ |
|  1  |  0  |  0  |  1  |      0      |    1     |        1         |                    1                    | Minterm $m_1 = \neg p \land \neg q \land r$ |
|  2  |  0  |  1  |  0  |      0      |    1     |        0         |                    0                    |  Maxterm $M_2 = p \lor \neg q \lor r$ |
|  3  |  0  |  1  |  1  |      0      |    1     |        1         |                    1                    | Minterm $m_3 = \neg p \land q \land r$ |
|  4  |  1  |  0  |  0  |      0      |    0     |        0         |                    0                    |  Maxterm $M_4 = \neg p \lor q \lor r$ |
|  5  |  1  |  0  |  1  |      0      |    0     |        0         |                    0                    | Maxterm $M_5 = \neg p \lor q \lor \neg r$ |
|  6  |  1  |  1  |  0  |      1      |    0     |        0         |                    1                    |  Minterm $m_6 = p \land q \land \neg r$ |
|  7  |  1  |  1  |  1  |      1      |    0     |        0         |                    1                    |   Minterm $m_7 = p \land q \land r$ |

**Step 2: Collect Minterms for PDNF ($F = 1$)**:
Rows where $F = 1$ are: $\{1, 3, 6, 7\}$.
$$\text{PDNF} = m_1 \lor m_3 \lor m_6 \lor m_7$$
$$\text{PDNF} = (\neg p \land \neg q \land r) \lor (\neg p \land q \land r) \lor (p \land q \land \neg r) \lor (p \land q \land r)$$

**Step 3: Collect Maxterms for PCNF ($F = 0$)**:
Rows where $F = 0$ are: $\{0, 2, 4, 5\}$.
$$\text{PCNF} = M_0 \land M_2 \land M_4 \land M_5$$
$$\text{PCNF} = (p \lor q \lor r) \land (p \lor \neg q \lor r) \land (\neg p \lor q \lor r) \land (\neg p \lor q \lor \neg r)$$

> **CRITICAL EXAM THEOREM**:
> 1. $\text{PDNF} \cup \text{PCNF}$ partition all $2^n$ minterm/maxterm indices.
> 2. A formula is a **Tautology** iff its PDNF contains all $2^n$ minterms (and its PCNF is empty / $\top$).
> 3. A formula is a **Contradiction** iff its PCNF contains all $2^n$ maxterms (and its PDNF is empty / $\bot$).

---

## 1.8 METHODS OF MATHEMATICAL PROOF

### 1.8.1 Direct Proof ($p \implies q$)
- **Mechanism**: Assume hypothesis $p$ is True. Apply definitions, axioms, algebraic properties, and established theorems in a sequential chain to deduce that conclusion $q$ must be True.
- **Worked Problem**: Prove that if $n$ is an odd integer, then $n^2$ is odd.
  - *Proof*: By definition of an odd integer, $n = 2k + 1$ for some integer $k$.
  - Squaring both sides:
    $$n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
  - Let $m = 2k^2 + 2k$. Since $k \in \mathbb{Z}$, $m \in \mathbb{Z}$.
  - Thus $n^2 = 2m + 1$, which by definition means $n^2$ is odd. $\blacksquare$

### 1.8.2 Proof by Contraposition ($\neg q \implies \neg p$)
- **Mechanism**: Used when direct proof is cumbersome (e.g., hypothesis is complicated or conclusion involves a product). We prove the logically equivalent contrapositive: Assume $\neg q$ is True, and prove $\neg p$ is True.
- **Worked Problem**: Prove that for any integer $n$, if $3n + 2$ is odd, then $n$ is odd.
  - *Proof by Contraposition*: The statement is $P(n) \to Q(n)$ where $P(n)$: "$3n+2$ is odd", $Q(n)$: "$n$ is odd".
  - Contrapositive: $\neg Q(n) \to \neg P(n)$ ("If $n$ is even, then $3n + 2$ is even").
  - Assume $n$ is even $\implies n = 2k$ for some $k \in \mathbb{Z}$.
  - Then:
    $$3n + 2 = 3(2k) + 2 = 6k + 2 = 2(3k + 1)$$
  - Let $m = 3k + 1 \in \mathbb{Z}$. Then $3n + 2 = 2m$, which is even.
  - Having proven $\neg Q(n) \implies \neg P(n)$, the original claim $P(n) \implies Q(n)$ is true. $\blacksquare$

### 1.8.3 Proof by Contradiction (Reductio ad Absurdum)
- **Mechanism**: To prove proposition $p$, assume $\neg p$ is True. Deduce a logical contradiction ($\neg p \to \bot \equiv \top$). This forces $\neg p$ to be False, meaning $p$ must be True.
- **Worked Problem**: Prove that $\sqrt{2}$ is irrational.
  - *Proof*: Assume for contradiction that $\sqrt{2}$ is rational.
  - Then $\sqrt{2} = \frac{a}{b}$ where $a, b \in \mathbb{Z}, b \neq 0$, and $\gcd(a, b) = 1$ (the fraction is in lowest terms).
  - Squaring both sides: $2 = \frac{a^2}{b^2} \implies a^2 = 2b^2$.
  - This implies $a^2$ is even, which forces $a$ to be even (since square of odd is odd).
  - Therefore, $a = 2k$ for some $k \in \mathbb{Z}$.
  - Substitute $a = 2k$ into $a^2 = 2b^2$:
    $$(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2$$
  - This implies $b^2$ is even, which forces $b$ to be even.
  - Since both $a$ and $b$ are even, $2$ divides both $a$ and $b$, so $\gcd(a, b) \ge 2$.
  - This directly contradicts the premise that $\gcd(a, b) = 1$.
  - Thus, the assumption that $\sqrt{2}$ is rational must be false. $\sqrt{2}$ is irrational. $\blacksquare$

### 1.8.4 Proof by Cases (Exhaustion)
- **Mechanism**: To prove $p \to q$ where $p \equiv p_1 \lor p_2 \lor \dots \lor p_k$, prove each individual case $p_i \to q$ separately.
- **Worked Problem**: Prove that for all real numbers $x, y$, $|xy| = |x| \cdot |y|$.
  - *Case 1*: $x \ge 0, y \ge 0$. Then $|x| = x, |y| = y, xy \ge 0 \implies |xy| = xy = |x||y|$.
  - *Case 2*: $x \ge 0, y < 0$. Then $|x| = x, |y| = -y, xy \le 0 \implies |xy| = -(xy) = x(-y) = |x||y|$.
  - *Case 3*: $x < 0, y \ge 0$. Symmetric to Case 2.
  - *Case 4*: $x < 0, y < 0$. Then $|x| = -x, |y| = -y, xy > 0 \implies |xy| = xy = (-x)(-y) = |x||y|$.
  - Since all cases exhaust $\mathbb{R} \times \mathbb{R}$, $|xy| = |x||y|$ holds for all $x, y$. $\blacksquare$

### 1.8.5 Disproof by Counterexample
- **Mechanism**: To disprove a universal claim $\forall x P(x)$, find a **single element $c$** in the domain such that $P(c)$ is False ($\exists x \neg P(x)$).
- **Worked Example**: Claim: "For every prime number $p$, $2^p - 1$ is prime."
  - *Counterexample*: Let $p = 11$ (which is prime).
  - $2^{11} - 1 = 2048 - 1 = 2047$.
  - Note that $2047 = 23 \times 89$. Both $23$ and $89$ are integers $> 1$.
  - Therefore, $2^{11}-1$ is composite. The universal claim is FALSE. $\blacksquare$

---

## 1.9 HIGH-PROBABILITY EXAM QUESTIONS & STUDENT TRAPS

### 1.9.1 The Logic Protocol Alignment Problem (NIT Jalandhar PYQ Analysis)
**Problem Statement**:
An encrypted system specification reads: "If the absence of Condition $P$ guarantees the absence of Condition $Q$, determine how this relates to defined system protocols."
Formally given: $(\neg P) \to (\neg Q)$.
Analyze how this condition aligns with the following protocols:
- **Protocol I**: $P \to Q$
- **Protocol II**: $Q \to P$
- **Protocol III**: $(\neg Q) \lor P$
- **Protocol IV**: $(\neg P) \lor Q$

**Exhaustive Analytical Solution**:
1. **Simplification of the Given Condition**:
   $$\text{Given Condition: } (\neg P) \to (\neg Q)$$
   By the Conditional Law ($A \to B \equiv \neg A \lor B$):
   $$\neg(\neg P) \lor (\neg Q) \equiv P \lor \neg Q \equiv \neg Q \lor P$$
   By the Law of Contraposition ($A \to B \equiv \neg B \to \neg A$):
   $$(\neg P) \to (\neg Q) \equiv \neg(\neg Q) \to \neg(\neg P) \equiv Q \to P$$
2. **Alignment Analysis for Each Protocol**:
   - **Protocol I ($P \to Q$)**:
     - Truth tables differ when $P=T, Q=F$ and $P=F, Q=T$.
     - In fact, $P \to Q$ is the inverse of $(\neg P \to \neg Q)$. An implication is NOT equivalent to its inverse.
     - **Result: DOES NOT ALIGN.**
   - **Protocol II ($Q \to P$)**:
     - This is the exact contrapositive of the given condition:
       $$(\neg P \to \neg Q) \equiv (Q \to P)$$
     - **Result: PERFECTLY ALIGNS (Logically Equivalent).**
   - **Protocol III ($(\neg Q) \lor P$)**:
     - Expanding Protocol II using the conditional equivalence gives:
       $$Q \to P \equiv \neg Q \lor P$$
     - This is identical to Protocol III.
     - **Result: PERFECTLY ALIGNS (Logically Equivalent).**
   - **Protocol IV ($(\neg P) \lor Q$)**:
     - This is the disjunctive form of Protocol I ($P \to Q \equiv \neg P \lor Q$).
     - As demonstrated above, $P \to Q$ is not equivalent to the given condition.
     - **Result: DOES NOT ALIGN.**
3. **Conclusion**:
   The encrypted condition aligns identically with **Protocol II** and **Protocol III**, while Protocol I and Protocol IV represent the converse/inverse relation.

---

### 1.9.2 Common Student Traps & Pitfalls in Unit 1

| Trap Number | Common Error | Correct Mathematical Fact | Explanation / Why it Fails |
|:---:|:---|:---|:---|
| **Trap 1** | Negating $p \to q$ as $p \to \neg q$ or $\neg p \to \neg q$. | $\neg(p \to q) \equiv p \land \neg q$ | The negation of "If you study, you pass" is "You studied AND you did not pass", NOT "If you study, you fail". |
| **Trap 2** | Assuming $p \to q$ is logically equivalent to $q \to p$. | $(p \to q) \not\equiv (q \to p)$ | Confusing implication with converse is the Fallacy of Affirming the Consequent. |
| **Trap 3** | Distributing $\forall$ over $\lor$: $\forall x (P(x) \lor Q(x)) \equiv \forall x P(x) \lor \forall x Q(x)$. | $\forall x (P(x) \lor Q(x)) \not\equiv \forall x P(x) \lor \forall x Q(x)$ | Example: Every integer is either even or odd (True). But it is FALSE that all integers are even OR all integers are odd! |
| **Trap 4** | Swapping nested quantifiers: $\forall x \exists y P(x, y) \equiv \exists y \forall x P(x, y)$. | Order cannot be swapped when quantifiers differ. | $\forall x \exists y$ allows $y$ to depend on $x$. $\exists y \forall x$ demands a single constant $y$ across all $x$. |
| **Trap 5** | Applying Universal Generalization to an arbitrary constant that had prior assumptions. | $c$ must be strictly generic. | If properties of $c$ were assumed during instantiation, generalization to all $x$ is logically invalid. |

---


# UNIT 2: SET THEORY, RELATIONS, FUNCTIONS, POSETS, LATTICES, COUNTING & DISCRETE STRUCTURES

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


# UNIT 3: GRAPH THEORY & NETWORK ARCHITECTURES

---

## 3.1 FUNDAMENTAL CONCEPTS & CLASSIFICATION OF GRAPHS

### 3.1.1 Formal Mathematical Definition
A **graph** $G$ is an ordered pair $G = (V, E)$ consisting of:
1. $V = V(G)$: A non-empty set of **vertices** (or nodes).
2. $E = E(G)$: A set of **edges** (or arcs), where each edge $e \in E$ is associated with an unordered pair $\{u, v\}$ (for undirected graphs) or an ordered pair $(u, v)$ (for directed graphs) of vertices in $V$.

### 3.1.2 Taxonomy of Graphs

| Graph Type | Edges Directed? | Multiple Edges Allowed? | Self-Loops Allowed? | Mathematical Description |
|:---|:---:|:---:|:---:|:---|
| **Simple Graph** | No | No | No | Undirected edges are distinct 2-element subsets $\{u, v\}$. |
| **Multigraph** | No | Yes | No | Multiple edges between the same pair of distinct vertices. |
| **Pseudograph** | No | Yes | Yes | Loops (edge connecting a vertex to itself) and multiple edges. |
| **Simple Directed Graph** | Yes | No | No | Edges are distinct ordered pairs $(u, v)$ with $u \neq v$. |
| **Directed Multigraph** | Yes | Yes | Yes | Multiple directed edges $(u, v)$ and directed self-loops $(u, u)$. |
| **Weighted Graph** | Either | Either | Either | A weight function $w: E \to \mathbb{R}$ assigns numerical costs to edges. |

```
    SIMPLE GRAPH              MULTIGRAPH                  PSEUDOGRAPH
       (A)───(B)                 (A)═════(B)                 (A)═════(B)↺ (loop)
        │     │                   │       │                   │       │
        │     │                   │       │                   │       │
       (C)───(D)                 (C)─────(D)                 (C)─────(D)
  No loops, no parallels    Multiple edges between A-B     Contains loops & parallels
```

---

### 3.1.3 Vertex Degrees and the Handshaking Lemma

- **Degree of a Vertex ($\deg(v)$)**: In an undirected graph, the degree of vertex $v$ is the number of edges incident with $v$. Each self-loop contributes **$2$ to the degree** of that vertex.
- **Isolated Vertex**: A vertex with degree $0$ ($\deg(v) = 0$).
- **Pendant (Leaf) Vertex**: A vertex with degree $1$ ($\deg(v) = 1$).
- **Directed Graph Degrees**:
  - **In-degree ($\deg^-(v)$)**: Number of edges terminating at $v$ (incoming edges).
  - **Out-degree ($\deg^+(v)$)**: Number of edges originating at $v$ (outgoing edges).
  - Total degree: $\deg(v) = \deg^-(v) + \deg^+(v)$.

---

### 3.1.4 The Handshaking Lemma: Formal Proof and Corollaries

#### Theorem: The Handshaking Lemma
Let $G = (V, E)$ be an undirected graph with $V = \{v_1, v_2, \dots, v_n\}$ and $|E| = m$. Then:
$$\sum_{v \in V} \deg(v) = 2|E|$$

#### Rigorous Mathematical Proof (Incidence Counting):
1. Consider the incidence relationship between vertices and edges: each edge $e \in E$ has exactly two endpoints (or one endpoint counted twice in the case of a self-loop).
2. Let $I(v, e)$ be an indicator function defined as:
   $$I(v, e) = \begin{cases} 1 & \text{if edge } e \text{ is incident with vertex } v \text{ (not a loop)} \\ 2 & \text{if edge } e \text{ is a self-loop on vertex } v \\ 0 & \text{otherwise} \end{cases}$$
3. Summing $I(v, e)$ over all vertices $v \in V$ for a fixed edge $e$:
   $$\sum_{v \in V} I(v, e) = 2 \quad \text{(since every edge has exactly 2 ends)}$$
4. Now sum over all edges $e \in E$:
   $$\sum_{e \in E} \left( \sum_{v \in V} I(v, e) \right) = \sum_{e \in E} 2 = 2|E|$$
5. By Fubini's principle of double counting (exchanging the order of summation):
   $$\sum_{v \in V} \left( \sum_{e \in E} I(v, e) \right) = \sum_{v \in V} \deg(v)$$
6. Therefore:
   $$\sum_{v \in V} \deg(v) = 2|E| \quad \blacksquare$$

---

#### Corollary 1: The Number of Odd-Degree Vertices is Even
> **Theorem**: In any undirected graph, the number of vertices that have an odd degree is even.

#### Formal Proof:
1. Let $V$ be partitioned into two disjoint subsets:
   - $V_{\text{even}} = \{v \in V \mid \deg(v) \text{ is even}\}$
   - $V_{\text{odd}} = \{v \in V \mid \deg(v) \text{ is odd}\}$
2. By the Handshaking Lemma:
   $$\sum_{v \in V} \deg(v) = \sum_{v \in V_{\text{even}}} \deg(v) + \sum_{v \in V_{\text{odd}}} \deg(v) = 2|E|$$
3. Notice that $2|E|$ is an even integer.
4. The sum $\sum_{v \in V_{\text{even}}} \deg(v)$ is a sum of even integers, so it is strictly **even**.
5. Rearranging the equation:
   $$\sum_{v \in V_{\text{odd}}} \deg(v) = 2|E| - \sum_{v \in V_{\text{even}}} \deg(v) = \text{Even} - \text{Even} = \text{Even}$$
6. A sum of odd integers is even **if and only if the number of terms in the sum is even**.
7. Therefore, $|V_{\text{odd}}|$ must be an **even number**. $\blacksquare$

---

#### Corollary 2: Directed Handshaking Lemma
For any directed graph $G = (V, E)$:
$$\sum_{v \in V} \deg^-(v) = \sum_{v \in V} \deg^+(v) = |E|$$
- *Proof*: Every directed edge $(u, v)$ contributes exactly $1$ to the out-degree of its source vertex $u$ and exactly $1$ to the in-degree of its target vertex $v$. Summing across all edges yields the total edge count $|E|$. $\blacksquare$

---

## 3.2 SPECIAL FAMILIES OF GRAPHS & TOPOLOGICAL METRICS

### 3.2.1 Standard Graph Families

1. **Complete Graph ($K_n$)**:
   - A simple graph containing an edge between every pair of distinct vertices.
   - Vertices: $n$.
   - Edges: $|E| = \binom{n}{2} = \frac{n(n-1)}{2}$.
   - Degree of every vertex: $\deg(v) = n - 1$ ($(n-1)$-regular).
2. **Cycle Graph ($C_n$, $n \ge 3$)**:
   - A single closed cycle of $n$ vertices and $n$ edges.
   - 2-regular: $\deg(v) = 2$ for all $v$.
3. **Wheel Graph ($W_n = C_n * K_1$, $n \ge 3$)**:
   - Formed by taking a cycle $C_n$ and adding an additional central vertex (the "hub") connected to all $n$ cycle vertices (the "spokes").
   - Vertices: $n + 1$.
   - Edges: $2n$ ($n$ rim edges $+ n$ spoke edges).
4. **Bipartite Graph**:
   - A graph whose vertex set $V$ can be partitioned into two disjoint subsets $V_1$ and $V_2$ ($V = V_1 \cup V_2, V_1 \cap V_2 = \emptyset$) such that every edge in $E$ connects a vertex in $V_1$ to a vertex in $V_2$. No edge connects two vertices in the same partition.
5. **Complete Bipartite Graph ($K_{m, n}$)**:
   - A bipartite graph where every vertex in $V_1$ ($|V_1| = m$) is connected to every vertex in $V_2$ ($|V_2| = n$).
   - Vertices: $m + n$.
   - Edges: $m \times n$.
6. **Hypercube Graph ($Q_n$, $n$-cube)**:
   - Vertices represent all $2^n$ bitstrings of length $n$.
   - Two vertices are adjacent iff their bitstrings differ in **exactly one bit position** (Hamming distance $d_H(u, v) = 1$).
   - Vertices: $2^n$.
   - Edges: $n \cdot 2^{n-1}$.
   - $n$-regular bipartite graph.

```
       K₄ (Complete)               C₄ (Cycle)                W₄ (Wheel)
          (1)─────(2)              (1)─────(2)              (1)─────(2)
           │ ╲   ╱ │                │       │                │ ╲   ╱ │
           │   ╳   │                │       │                │  (H)  │
           │ ╱   ╲ │                │       │                │ ╱   ╲ │
          (3)─────(4)              (3)─────(4)              (3)─────(4)
          E = 4(3)/2 = 6            E = 4, 2-regular         E = 8 (4 rim + 4 spokes)

       K₂,₃ (Complete Bipartite)                 Q₃ (Hypercube / 3-Cube)
           V₁: (1)   (2)                                011───────111
               │ ╲   │ ╲                                 │ ╲       │ ╲
               │  ╲  │  ╲                                │  001────┼──101
               │   ╲ │   ╲                               │   │     │   │
           V₂: (a)  (b)  (c)                            010──┼────110  │
           Edges = 2 x 3 = 6                             ╲   │     ╲   │
                                                          ╲  000─────╲100
```

---

### 3.2.2 Characterization Theorem of Bipartite Graphs
> **Fundamental Theorem (Kőnig, 1936)**: A graph $G$ is bipartite **if and only if it contains no cycles of odd length**.

#### Formal Proof ($\implies$):
1. Assume $G$ is bipartite with partition sets $V_1$ and $V_2$.
2. Let $C = (v_0, v_1, v_2, \dots, v_k = v_0)$ be any cycle in $G$.
3. Without loss of generality, assume $v_0 \in V_1$.
4. Since every edge connects $V_1$ to $V_2$, the sequence of vertices alternates partitions:
   $$v_0 \in V_1 \implies v_1 \in V_2 \implies v_2 \in V_1 \implies v_3 \in V_2 \implies \dots$$
5. In general, $v_i \in V_1$ if $i$ is even, and $v_i \in V_2$ if $i$ is odd.
6. Since $C$ is a closed cycle, the final vertex $v_k = v_0 \in V_1$.
7. This forces the index $k$ to be **even**.
8. Therefore, the length of the cycle $k$ is even. An odd cycle cannot exist in a bipartite graph. $\blacksquare$

---

### 3.2.3 Maximum Edges in a Bipartite Graph (NIT Jalandhar PYQ Solved)
**Problem**: In a bipartite graph with $n$ vertices partitioned into $U$ and $V$ ($|U| + |V| = n$), what is the maximum number of edges that can exist? Show steps.

**Mathematical Derivation**:
1. Let $|U| = k$. Since $|U| + |V| = n$, $|V| = n - k$.
2. In a simple bipartite graph, edges can only exist between $U$ and $V$.
3. The maximum number of edges for a fixed partition size $k$ occurs in the complete bipartite graph $K_{k, n-k}$:
   $$E(k) = k(n - k) = n k - k^2$$
4. To maximize $E(k)$ over continuous values of $k$, take the first derivative with respect to $k$:
   $$\frac{dE}{dk} = n - 2k = 0 \implies k = \frac{n}{2}$$
5. The second derivative $\frac{d^2E}{dk^2} = -2 < 0$, confirming that $k = n/2$ yields the global maximum.
6. For discrete integer values of $k$:
   - **If $n$ is even**: $k = n/2$, so $|U| = n/2$ and $|V| = n/2$.
     $$E_{\max} = \left(\frac{n}{2}\right)\left(\frac{n}{2}\right) = \frac{n^2}{4}$$
   - **If $n$ is odd**: Choose $k = \frac{n-1}{2}$ and $n - k = \frac{n+1}{2}$.
     $$E_{\max} = \left(\frac{n-1}{2}\right)\left(\frac{n+1}{2}\right) = \frac{n^2 - 1}{4} = \left\lfloor \frac{n^2}{4} \right\rfloor$$
7. **Unified General Formula**:
   $$E_{\max} = \left\lfloor \frac{n^2}{4} \right\rfloor \quad \blacksquare$$

---

### 3.2.4 Topological Graph Metrics: Radius, Diameter, and Eccentricity (NIT Jalandhar PYQ Solved)

#### Formal Definitions:
1. **Distance $d(u, v)$**: The length (number of edges) of the shortest path connecting vertices $u$ and $v$. If no path exists, $d(u, v) = \infty$.
2. **Eccentricity $e(v)$**: The maximum distance from vertex $v$ to any other vertex in the graph:
   $$e(v) = \max_{u \in V} d(v, u)$$
3. **Radius ($\text{rad}(G)$)**: The minimum eccentricity among all vertices:
   $$\text{rad}(G) = \min_{v \in V} e(v)$$
4. **Diameter ($\text{diam}(G)$)**: The maximum eccentricity among all vertices (the longest shortest-path in the graph):
   $$\text{diam}(G) = \max_{v \in V} e(v)$$
   - General Inequality: $\text{rad}(G) \le \text{diam}(G) \le 2 \cdot \text{rad}(G)$.
5. **Center of a Graph**: The set of all vertices $v$ whose eccentricity equals the radius: $C(G) = \{v \in V \mid e(v) = \text{rad}(G)\}$.

---

#### Exhaustive Topological Analysis of $K_6$, $K_{4,5}$, and $Q_3$:

##### 1. Complete Graph $K_6$:
- *Structure*: 6 vertices, each connected directly to all other 5 vertices.
- For any distinct vertices $u, v$: $d(u, v) = 1$.
- Eccentricity for every vertex: $e(v) = \max_{u \neq v} d(v, u) = 1$.
- **Radius**: $\text{rad}(K_6) = \min_{v} e(v) = 1$.
- **Diameter**: $\text{diam}(K_6) = \max_{v} e(v) = 1$.

##### 2. Complete Bipartite Graph $K_{4, 5}$:
- *Structure*: Partitioned into $U$ with $|U|=4$ and $V$ with $|V|=5$.
- Distance between vertices in different partitions: $u \in U, v \in V \implies d(u, v) = 1$ (direct edge).
- Distance between distinct vertices in the same partition:
  - If $u_1, u_2 \in U$, there is no direct edge between them. But choosing any $v \in V$, the path $u_1 - v - u_2$ has length 2. Thus $d(u_1, u_2) = 2$.
  - Similarly, for $v_1, v_2 \in V$, choosing any $u \in U$, the path $v_1 - u - v_2$ has length 2. Thus $d(v_1, v_2) = 2$.
- For any vertex $x \in K_{4, 5}$, its maximum distance to another vertex is $2$.
- Eccentricity for every vertex: $e(x) = 2$.
- **Radius**: $\text{rad}(K_{4, 5}) = 2$.
- **Diameter**: $\text{diam}(K_{4, 5}) = 2$.
- *(General rule for complete bipartite graphs $K_{m,n}$ with $m, n \ge 2$: $\text{rad} = \text{diam} = 2$.)*

##### 3. Hypercube Graph $Q_3$:
- *Structure*: 8 vertices representing 3-bit binary strings $\{000, \dots, 111\}$.
- Distance between any two vertices $u$ and $v$ is their **Hamming distance** $d_H(u, v)$ (the number of bit flips needed):
  $$d(u, v) = d_H(u, v)$$
- For any vertex $v$, its unique antipodal (furthest) vertex is its bitwise complement $\overline{v}$ (e.g., $000 \to 111$).
  $$d(v, \overline{v}) = 3$$
- Eccentricity for every vertex: $e(v) = 3$.
- **Radius**: $\text{rad}(Q_3) = 3$.
- **Diameter**: $\text{diam}(Q_3) = 3$.
- *(General rule for hypercube $Q_n$: $\text{rad}(Q_n) = \text{diam}(Q_n) = n$.)*

#### Summary Comparison Table:
| Graph Configuration | Number of Vertices $|V|$ | Number of Edges $|E|$ | Eccentricity $e(v)$ | Radius | Diameter |
|:---|:---:|:---:|:---:|:---:|:---:|
| **$K_6$** | 6 | 15 | 1 for all $v$ | **1** | **1** |
| **$K_{4, 5}$** | 9 | 20 | 2 for all $v$ | **2** | **2** |
| **$Q_3$** | 8 | 12 | 3 for all $v$ | **3** | **3** |

---

## 3.3 CONNECTIVITY, MATRIX REPRESENTATIONS & WARSHALL'S ALGORITHM

### 3.3.1 Walks, Trails, Paths, Circuits, and Cycles

| Term | Edge Repetition Allowed? | Vertex Repetition Allowed? | Open / Closed |
|:---|:---:|:---:|:---:|
| **Walk** | Yes | Yes | Either |
| **Trail** | **No** (All edges distinct) | Yes | Open ($u \neq v$) |
| **Path (Simple Path)** | **No** | **No** (All vertices distinct) | Open ($u \neq v$) |
| **Circuit** | **No** | Yes | **Closed** ($u = v$) |
| **Cycle (Simple Circuit)** | **No** | **No** (Only first = last) | **Closed** ($u = v$) |

### 3.3.2 Cut-Vertices (Articulation Points) and Bridges (Cut-Edges)
- **Cut-Vertex**: A vertex $v \in V$ whose removal (along with its incident edges) increases the number of connected components:
  $$\omega(G - v) > \omega(G)$$
- **Cut-Edge (Bridge)**: An edge $e \in E$ whose removal increases the number of connected components:
  $$\omega(G - e) > \omega(G)$$
  - *Fundamental Theorem*: An edge $e$ is a bridge **if and only if $e$ does not belong to any cycle in $G$**.

---

### 3.3.3 Matrix Representations & Walk Counting Theorem

1. **Adjacency Matrix ($A$)**:
   For a graph with vertices $\{v_1, \dots, v_n\}$, $A$ is an $n \times n$ matrix where:
   $$A[i][j] = \text{number of edges between } v_i \text{ and } v_j$$
   - For undirected graphs, $A$ is **strictly symmetric** ($A = A^T$).
2. **Incidence Matrix ($M$)**:
   An $n \times m$ matrix (vertices $\times$ edges) where:
   $$M[i][j] = \begin{cases} 1 & \text{if vertex } v_i \text{ is incident with edge } e_j \\ 0 & \text{otherwise} \end{cases}$$
   - For an undirected graph without loops, every column has **exactly two 1s**.
3. **Walk Counting Theorem**:
   > **Theorem**: Let $A$ be the adjacency matrix of a graph $G$. The $(i, j)$-th entry of the matrix power $A^k$, denoted $(A^k)_{ij}$, equals the **exact number of distinct walks of length $k$** from vertex $v_i$ to vertex $v_j$.
   - *Proof by Induction on $k$*:
     - Base step ($k = 1$): $A^1 = A$. By definition, $A_{ij}$ is the number of edges (walks of length 1) from $v_i$ to $v_j$.
     - Inductive hypothesis: Assume $(A^{k-1})_{im}$ equals the number of walks of length $k-1$ from $v_i$ to $v_m$.
     - Inductive step: Any walk of length $k$ from $v_i$ to $v_j$ consists of a walk of length $k-1$ from $v_i$ to some intermediate vertex $v_m$, followed by a single edge from $v_m$ to $v_j$.
     - By the sum rule and matrix multiplication:
       $$(A^k)_{ij} = \sum_{m=1}^n (A^{k-1})_{im} \cdot A_{mj}$$
     - This completes the inductive step. $\blacksquare$

---

### 3.3.4 Warshall's Algorithm for Transitive Closure

Warshall's algorithm calculates the **transitive closure / reachability matrix** $W$ of a directed graph with $n$ vertices in $O(n^3)$ time, constructing a sequence of Boolean matrices $W^{(0)}, W^{(1)}, \dots, W^{(n)}$.

- **Semantics of $W^{(k)}[i][j]$**: $W^{(k)}[i][j] = 1$ if there exists a directed path from $v_i$ to $v_j$ whose intermediate vertices all belong to the subset $\{v_1, v_2, \dots, v_k\}$.
- **Recurrence Relation**:
  $$W^{(k)}[i][j] = W^{(k-1)}[i][j] \lor \Big( W^{(k-1)}[i][k] \land W^{(k-1)}[k][j] \Big)$$

```
     PATH VIA INTERMEDIATE VERTEX k:
     v_i ───────────────> v_k ───────────────> v_j
          Path using               Path using
          {v₁,...,vₖ₋₁}            {v₁,...,vₖ₋₁}
     ──────────────────────────────────────────────>
                 Path using {v₁,...,vₖ}
```

#### Step-by-Step Worked Example:
Consider directed graph $G$ with 4 vertices $\{1, 2, 3, 4\}$ and edges: $1 \to 2$, $2 \to 3$, $3 \to 4$, $4 \to 1$.

1. **Initial Matrix $W^{(0)}$ (Adjacency Matrix)**:
   $$W^{(0)} = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \end{bmatrix}$$
2. **Iteration $k = 1$ (Intermediate Vertex 1)**:
   - Examine Column 1 and Row 1 of $W^{(0)}$:
     - Column 1 has a $1$ at Row 4 ($W^{(0)}[4][1] = 1$).
     - Row 1 has a $1$ at Column 2 ($W^{(0)}[1][2] = 1$).
     - Path created: $4 \to 1 \to 2 \implies W^{(1)}[4][2] = 1$.
   $$W^{(1)} = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & \mathbf{1} & 0 & 0 \end{bmatrix}$$
3. **Iteration $k = 2$ (Intermediate Vertex 2)**:
   - Column 2 has $1$s at Row 1 and Row 4.
   - Row 2 has a $1$ at Column 3.
   - Paths created: $1 \to 2 \to 3 \implies W^{(2)}[1][3] = 1$ and $4 \to 2 \to 3 \implies W^{(2)}[4][3] = 1$.
   $$W^{(2)} = \begin{bmatrix} 0 & 1 & \mathbf{1} & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 1 & \mathbf{1} & 0 \end{bmatrix}$$
4. **Iteration $k = 3$ (Intermediate Vertex 3)**:
   - Column 3 has $1$s at Rows 1, 2, 4.
   - Row 3 has a $1$ at Column 4.
   - New paths: $1 \to 3 \to 4$, $2 \to 3 \to 4$, $4 \to 3 \to 4$.
   $$W^{(3)} = \begin{bmatrix} 0 & 1 & 1 & \mathbf{1} \\ 0 & 0 & 1 & \mathbf{1} \\ 0 & 0 & 0 & 1 \\ 1 & 1 & 1 & \mathbf{1} \end{bmatrix}$$
5. **Iteration $k = 4$ (Intermediate Vertex 4)**:
   - Column 4 has $1$s at Rows 1, 2, 3, 4.
   - Row 4 has $1$s at Columns 1, 2, 3, 4.
   - Cross products fill ALL remaining entries with 1s!
   $$W^{(4)} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix}$$
   The resulting reachability matrix confirms that $G$ is **strongly connected**.

---

### 3.3.5 Shortest Path: Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest path from a single source vertex $s$ to all other vertices in a weighted graph with **non-negative edge weights** ($w(e) \ge 0$).

#### Algorithm Mechanism:
1. Maintain distance array $\text{dist}[v]$, initialized to $\infty$, with $\text{dist}[s] = 0$.
2. Maintain priority queue of unvisited vertices.
3. In each iteration, extract vertex $u$ with minimum $\text{dist}[u]$.
4. For each neighbor $v$ of $u$, perform **relaxation**:
   $$\text{if } \text{dist}[u] + w(u, v) < \text{dist}[v] \implies \text{dist}[v] = \text{dist}[u] + w(u, v)$$
5. **Complexity**: $O((V + E) \log V)$ with binary heap.
6. **Critical Constraint**: Fails on negative edge weights (requires Bellman-Ford algorithm).

---

## 3.4 EULERIAN AND HAMILTONIAN GRAPHS

```
              ┌────────────────────────────────────────────────────────┐
              │           EULERIAN VS HAMILTONIAN TRAVERSALS           │
              ├──────────────────────────┬─────────────────────────────┤
              │     EULERIAN GRAPH       │      HAMILTONIAN GRAPH      │
              ├──────────────────────────┼─────────────────────────────┤
              │ Traverses EVERY EDGE     │ Visits EVERY VERTEX         │
              │ exactly ONCE.            │ exactly ONCE.               │
              ├──────────────────────────┼─────────────────────────────┤
              │ Decidable in O(V + E)    │ NP-Complete to decide       │
              │ polynomial time.         │ (no known polynomial time). │
              ├──────────────────────────┼─────────────────────────────┤
              │ Exact Necessary &        │ Only SUFFICIENT conditions  │
              │ Sufficient condition     │ known (Dirac, Ore).         │
              │ (Vertex degree parity).  │ No simple characterization. │
              └──────────────────────────┴─────────────────────────────┘
```

### 3.4.1 Eulerian Graphs
- **Eulerian Trail (Path)**: An open trail that visits every edge of $G$ exactly once.
- **Eulerian Circuit**: A closed circuit that visits every edge of $G$ exactly once.
- **Eulerian Graph**: A graph containing an Eulerian circuit.

#### Theorem: Euler's Characterization Theorem (Euler-Hierholzer)
Let $G = (V, E)$ be a connected graph (ignoring isolated vertices):
1. $G$ contains an **Eulerian circuit** $\iff$ **Every vertex has an EVEN degree**.
2. $G$ contains an **Eulerian trail** (open) $\iff$ **Exactly TWO vertices have ODD degree** (the trail must start at one odd vertex and terminate at the other).

#### Formal Proof of the Even Degree Condition ($\implies$):
1. Assume $G$ has an Euler circuit $C$.
2. As $C$ traverses the graph, whenever it visits a vertex $v$, it must enter via an edge and leave via a different edge.
3. Each such entrance and exit contributes exactly $2$ to the degree of $v$.
4. Since every edge in $E$ is used exactly once, the total degree of every vertex must be a multiple of $2$ (even). $\blacksquare$

#### Fleury's Algorithm for Constructing an Euler Circuit:
1. Verify all vertex degrees are even.
2. Start at any vertex $v_0$.
3. At any step, traverse an edge $e = (u, v)$ following the **Golden Rule of Fleury**:
   > **Never traverse a bridge (cut-edge) of the remaining subgraph unless there is no other alternative!**
4. Remove the traversed edge from the graph.
5. Repeat until all edges are traversed.

---

### 3.4.2 Hamiltonian Graphs
- **Hamiltonian Path**: A simple path that visits every vertex in $V$ exactly once.
- **Hamiltonian Cycle**: A closed cycle that visits every vertex in $V$ exactly once.
- **Hamiltonian Graph**: A graph containing a Hamiltonian cycle.

#### Sufficient Conditions for Hamiltonicity:
1. **Dirac's Theorem (1952)**:
   Let $G$ be a simple graph with $n \ge 3$ vertices. If:
   $$\deg(v) \ge \frac{n}{2} \quad \text{for every vertex } v \in V$$
   then $G$ is **Hamiltonian**.
2. **Ore's Theorem (1960)**:
   Let $G$ be a simple graph with $n \ge 3$ vertices. If for every pair of non-adjacent vertices $u$ and $v$:
   $$\deg(u) + \deg(v) \ge n$$
   then $G$ is **Hamiltonian**.
   - Note: Dirac's Theorem is a direct corollary of Ore's Theorem (since $\deg(u) \ge n/2$ and $\deg(v) \ge n/2 \implies \deg(u) + \deg(v) \ge n$).

---

## 3.5 PLANAR GRAPHS & GRAPH COLORING

### 3.5.1 Planarity and Euler's Planar Formula
A graph $G$ is **planar** if it can be drawn in the Euclidean plane $\mathbb{R}^2$ such that its edges intersect only at their common endpoints (no edge crossings). Such a drawing is a **planar embedding**.
- A planar embedding divides the plane into connected topological regions called **faces** (or regions $F$ or $R$), including exactly **one unbounded outer face**.

---

### 3.5.2 Formal Proof of Euler's Formula: $V - E + F = 2$
> **Theorem (Euler, 1752)**: For any connected planar graph with $V$ vertices, $E$ edges, and $F$ faces:
> $$V - E + F = 2$$

#### Complete Step-by-Step Mathematical Induction Proof:
- **Proof Strategy**: Induction on the number of edges $E$.
- **Base Step ($E = V - 1$)**:
  - The minimum number of edges for a connected graph with $V$ vertices is $V - 1$, which occurs when $G$ is a **tree** ($T$).
  - A tree has no cycles, so it cannot enclose any bounded region.
  - Therefore, a tree has only $1$ face (the unbounded exterior face): $F = 1$.
  - Substitute into Euler's formula:
    $$V - E + F = V - (V - 1) + 1 = V - V + 1 + 1 = 2$$
  - The base step holds with mathematical precision.
- **Inductive Hypothesis**:
  - Assume Euler's formula $V' - E' + F' = 2$ holds for all connected planar graphs with $k$ edges ($E' = k \ge V - 1$).
- **Inductive Step**:
  - Let $G$ be a connected planar graph with $E = k + 1$ edges.
  - Since $E > V - 1$, $G$ is not a tree and must contain at least one simple cycle $C$.
  - Choose an edge $e$ that lies on cycle $C$.
  - Consider the subgraph $G' = G - e$ obtained by removing edge $e$.
  - Properties of $G'$:
    1. $G'$ is still connected (removing an edge from a cycle cannot disconnect the graph).
    2. Vertices: $V' = V$ (no vertices were removed).
    3. Edges: $E' = E - 1 = (k + 1) - 1 = k$.
    4. Faces: Since edge $e$ lay on cycle $C$, it was shared by two distinct adjacent faces in $G$. Removing $e$ merges those two faces into a single combined face. Thus, $F' = F - 1$.
  - By our Inductive Hypothesis, Euler's formula holds for $G'$:
    $$V' - E' + F' = 2$$
  - Substituting $V' = V$, $E' = E - 1$, and $F' = F - 1$:
    $$V - (E - 1) + (F - 1) = 2 \implies V - E + 1 + F - 1 = 2 \implies V - E + F = 2$$
  - The formula holds for $k + 1$ edges.
- By the Principle of Mathematical Induction, $V - E + F = 2$ holds for all connected planar graphs. $\blacksquare$

---

### 3.5.3 Planar Inequality Derivations
Let $G$ be a connected simple planar graph with $V \ge 3$ vertices:
1. Every face is bounded by at least 3 edges (a polygon requires $\ge 3$ sides):
   $$\sum_{f \in \text{Faces}} \text{degree}(f) \ge 3F$$
2. Since each edge borders at most 2 faces:
   $$\sum_{f \in \text{Faces}} \text{degree}(f) = 2E \implies 2E \ge 3F \implies F \le \frac{2}{3}E$$
3. Substitute $F \le \frac{2}{3}E$ into Euler's formula:
   $$2 = V - E + F \le V - E + \frac{2}{3}E = V - \frac{1}{3}E$$
   $$2 \le V - \frac{1}{3}E \implies \frac{1}{3}E \le V - 2 \implies \mathbf{E \le 3V - 6}$$

#### Corollary for Triangle-Free Planar Graphs (Girth $\ge 4$):
If $G$ contains no triangles (cycles of length 3), such as in bipartite graphs, every face is bounded by at least 4 edges:
$$2E \ge 4F \implies F \le \frac{E}{2}$$
Substituting into Euler's formula:
$$2 = V - E + F \le V - E + \frac{E}{2} = V - \frac{E}{2} \implies \mathbf{E \le 2V - 4}$$

---

### 3.5.4 Non-Planarity Proofs for $K_5$ and $K_{3,3}$

#### Proof 1: Non-Planarity of $K_5$ (Complete Graph on 5 Vertices)
1. For $K_5$: $V = 5$, and $|E| = \binom{5}{2} = \frac{5 \times 4}{2} = 10$.
2. If $K_5$ were planar, it must satisfy the planar inequality $E \le 3V - 6$.
3. Substitute $V = 5$:
   $$3V - 6 = 3(5) - 6 = 15 - 6 = 9$$
4. But $K_5$ has $E = 10$ edges.
5. This requires $10 \le 9$, which is a **blatant mathematical contradiction**.
6. Therefore, $K_5$ **cannot be planar**. $\blacksquare$

#### Proof 2: Non-Planarity of $K_{3,3}$ (Utility Graph)
1. $K_{3,3}$ is a complete bipartite graph with partitions of size 3.
   - Vertices: $V = 3 + 3 = 6$.
   - Edges: $E = 3 \times 3 = 9$.
2. Since $K_{3,3}$ is bipartite, by Kőnig's Theorem it contains **no odd cycles**. In particular, it contains **no triangles** (cycles of length 3).
3. Therefore, its girth is $\ge 4$.
4. If $K_{3,3}$ were planar, it must satisfy the triangle-free planar inequality $E \le 2V - 4$.
5. Substitute $V = 6$:
   $$2V - 4 = 2(6) - 4 = 12 - 4 = 8$$
6. But $K_{3,3}$ has $E = 9$ edges.
7. This requires $9 \le 8$, which is a **blatant mathematical contradiction**.
8. Therefore, $K_{3,3}$ **cannot be planar**. $\blacksquare$

---

### 3.5.5 Kuratowski's Theorem
> **Theorem (Kuratowski, 1930)**: A graph $G$ is planar **if and only if it contains no subgraph that is homeomorphic to (or contains an elementary subdivision of) $K_5$ or $K_{3,3}$**.
- **Elementary Subdivision**: Inserting a vertex of degree 2 into an edge ($u \frac{\quad}{v} \implies u \frac{\quad}{w} \frac{\quad}{v}$).
- Two graphs are **homeomorphic** if both can be obtained from the same graph by a sequence of elementary subdivisions.

---

### 3.5.6 Graph Coloring & Chromatic Number
- A **proper vertex coloring** is an assignment of colors to vertices such that no two adjacent vertices share the same color:
  $$(u, v) \in E \implies c(u) \neq c(v)$$
- **Chromatic Number ($\chi(G)$)**: The minimum number of colors needed to properly color $G$.

#### Chromatic Numbers for Standard Graphs:
- Complete Graph: $\chi(K_n) = n$.
- Bipartite Graph ($K_{m,n}$): $\chi(G) = 2$ (color partition 1 with color A, partition 2 with color B).
- Trees / Forests: $\chi(T) = 2$ (bipartite).
- Cycle Graph $C_n$:
  $$\chi(C_n) = \begin{cases} 2 & \text{if } n \text{ is even} \\ 3 & \text{if } n \text{ is odd} \end{cases}$$
- **The Four Color Theorem (Appel & Haken, 1976)**:
  The chromatic number of every planar graph is at most 4:
  $$\chi(G) \le 4 \quad \text{for any planar graph } G$$

---

## 3.6 GRAPH ISOMORPHISM

Two simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** ($G_1 \cong G_2$) if there exists a bijection $f: V_1 \to V_2$ such that:
$$(u, v) \in E_1 \iff (f(u), f(v)) \in E_2 \quad \text{for all } u, v \in V_1$$

### Graph Invariants (Necessary Conditions for Isomorphism):
If $G_1 \cong G_2$, they MUST share all graph invariants:
1. Equal number of vertices: $|V_1| = |V_2|$.
2. Equal number of edges: $|E_1| = |E_2|$.
3. Identical **degree sequence** (sorted list of vertex degrees).
4. Identical number of cycles of each length $k$.
5. Identical connectivity and diameter.

> **Warning**: Invariants are **necessary but NOT sufficient**! Two non-isomorphic graphs can have identical degree sequences. To prove isomorphism, one must construct an explicit bijection $f$ preserving all edges.

---


# UNIT 4: BINARY TREES, TREE ALGORITHMS & DATA STRUCTURES

---

## 4.1 TREE ARCHITECTURES & MATHEMATICAL FOUNDATIONS

### 4.1.1 Formal Definition of a Tree
A **tree** $T = (V, E)$ is an undirected, simple, connected acyclic graph.
- A collection of disjoint trees is termed a **forest**.
- Adding any edge between non-adjacent vertices creates **exactly one simple cycle**.
- Removing any edge disconnects the tree (every edge is a **bridge**).

### 4.1.2 The Master Characterization Theorem of Trees
> **Theorem**: Let $G = (V, E)$ be an undirected graph with $|V| = n$ vertices. The following statements are mathematically equivalent:
> 1. $G$ is a tree (connected and acyclic).
> 2. There exists a **unique simple path** between every pair of vertices in $G$.
> 3. $G$ is connected and has exactly $n - 1$ edges ($|E| = n - 1$).
> 4. $G$ is acyclic and has exactly $n - 1$ edges ($|E| = n - 1$).
> 5. $G$ is acyclic, and adding any edge creates exactly one cycle.
> 6. $G$ is connected, and removing any edge disconnects $G$.

---

### 4.1.3 Mathematical Proof: A Tree with $n$ Vertices Has $n - 1$ Edges
> **Theorem**: Every tree $T = (V, E)$ with $n \ge 1$ vertices has exactly $n - 1$ edges:
> $$|E| = |V| - 1$$

#### Rigorous Mathematical Induction Proof:
- **Basis Step ($n = 1$)**:
  - A tree with $n = 1$ vertex has no cycles and cannot have edges (simple graph).
  - $|V| = 1$, $|E| = 0$.
  - Formula: $|E| = 1 - 1 = 0$. The base step holds.
- **Inductive Hypothesis**:
  - Assume every tree with $k$ vertices ($1 \le k \le m$) has exactly $k - 1$ edges.
- **Inductive Step ($n = m + 1$)**:
  - Let $T = (V, E)$ be a tree with $m + 1$ vertices.
  - Choose any edge $e = (u, v) \in E$.
  - Since $T$ is acyclic, $e$ is not part of any cycle. Therefore, $e$ is a bridge.
  - Removing $e$ disconnects $T$ into **exactly two connected components**, $T_1 = (V_1, E_1)$ and $T_2 = (V_2, E_2)$.
  - Neither $T_1$ nor $T_2$ contains cycles (subgraphs of an acyclic graph are acyclic).
  - Therefore, both $T_1$ and $T_2$ are trees!
  - Let $|V_1| = n_1$ and $|V_2| = n_2$. Since $V_1$ and $V_2$ partition $V$:
    $$n_1 + n_2 = m + 1$$
    Since each component has at least one vertex, $1 \le n_1 \le m$ and $1 \le n_2 \le m$.
  - By our Inductive Hypothesis:
    $$|E_1| = n_1 - 1 \quad \text{and} \quad |E_2| = n_2 - 1$$
  - The total number of edges in $T$ is the sum of edges in $T_1$, $T_2$, plus the removed bridge $e$:
    $$\begin{aligned}
    |E| &= |E_1| + |E_2| + 1 \\
    &= (n_1 - 1) + (n_2 - 1) + 1 \\
    &= n_1 + n_2 - 1 \\
    &= (m + 1) - 1 = m
    \end{aligned}$$
  - The formula holds for $n = m + 1$.
- By mathematical induction, every tree with $n$ vertices has $n - 1$ edges. $\blacksquare$

---

### 4.1.4 Rooted Trees & Hierarchical Nomenclature
A **rooted tree** is a tree in which one vertex is designated as the **root**, and every edge is directed away from the root.

```
                         (A)  <── Root (Level 0, Depth 0)
                       ／   ＼
                     ／       ＼
                   (B)         (C)  <── Level 1
                  ／ ＼          ＼
                (D)   (E)        (F)  <── Level 2
                      │
                     (G)  <── Level 3 (Height = 3)
```

- **Parent**: The unique immediate predecessor of a vertex. (Root has no parent).
- **Child**: An immediate successor of a vertex.
- **Siblings**: Vertices sharing the identical parent.
- **Ancestors**: All vertices along the unique path from the root to the node.
- **Descendants**: All vertices reachable from the node moving away from the root.
- **Leaf (External Vertex)**: A vertex with no children ($\deg^+(v) = 0$).
- **Internal Vertex**: A vertex with at least one child.
- **Depth / Level**: Length of path from root to node (Root depth = 0).
- **Height of Tree**: Maximum depth of any node in the tree.

---

### 4.1.5 Taxonomy of Binary Trees

```
   FULL BINARY TREE           COMPLETE BINARY TREE         EXTENDED BINARY TREE
    (Every node has            (All levels filled except      (Null pointers replaced
     0 or 2 children)           last, filled Left-to-Right)    with external square nodes)
          (A)                         (A)                             (A)
        ／   ＼                     ／   ＼                         ／   ＼
      (B)     (C)                 (B)     (C)                     (B)     (C)
     ／ ＼                       ／ ＼    ／                     ／ ＼    ／ ＼
   (D)   (E)                   (D)  (E) (F)                    (D)  [□] [□]  (E)
                                                              ／ ＼         ／ ＼
                                                            [□]  [□]       [□]  [□]
```

1. **Full (Strict / Proper) Binary Tree**:
   - Every node has **either 0 or 2 children** (no node has exactly 1 child).
   - If a full binary tree has $I$ internal nodes, it has:
     $$L = I + 1 \text{ leaves}, \quad N = 2I + 1 \text{ total nodes}$$
2. **Complete Binary Tree**:
   - Every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
   - For height $h$, number of nodes satisfies:
     $$2^h \le N \le 2^{h+1} - 1 \implies h = \lfloor \log_2 N \rfloor$$
3. **Perfect (Saturated) Binary Tree**:
   - All internal nodes have 2 children, and all leaves are at the exact same depth.
   - Total nodes: $N = 2^{h+1} - 1$. Leaves: $2^h$.
4. **Extended Binary Tree (2-Tree)**:
   - Formed by replacing every empty/null pointer of a binary tree with a special **external node** (represented as square boxes $\Box$).
   - If the original tree has $N$ internal nodes, the extended tree has **$N + 1$ external nodes**.
   - Path Length Relation: $E = I + 2N$ where $E$ is external path length and $I$ is internal path length.

---

## 4.2 BINARY TREE TRAVERSALS

Traversal is the systematic process of visiting every vertex in a tree exactly once.

### 4.2.1 The Three Classical Depth-First Traversals
Consider a binary tree node with root $R$, left subtree $T_L$, and right subtree $T_R$:

1. **Preorder Traversal (N-L-R)**:
   $$\text{Visit Root } R \implies \text{Traverse } T_L \text{ in Preorder} \implies \text{Traverse } T_R \text{ in Preorder}$$
2. **Inorder Traversal (L-N-R)**:
   $$\text{Traverse } T_L \text{ in Inorder} \implies \text{Visit Root } R \implies \text{Traverse } T_R \text{ in Inorder}$$
   - *Crucial Property*: In a Binary Search Tree (BST), Inorder traversal visits nodes in **strictly ascending sorted order**!
3. **Postorder Traversal (L-R-N)**:
   $$\text{Traverse } T_L \text{ in Postorder} \implies \text{Traverse } T_R \text{ in Postorder} \implies \text{Visit Root } R$$

```
                           Tree for Traversal:
                                   (A)
                                 ／   ＼
                               (B)     (C)
                              ／ ＼      ＼
                            (D)   (E)    (F)

  PREORDER  (Root-Left-Right):  A ──> B ──> D ──> E ──> C ──> F
  INORDER   (Left-Root-Right):  D ──> B ──> E ──> A ──> C ──> F
  POSTORDER (Left-Right-Root):  D ──> E ──> B ──> F ──> C ──> A
```

---

### 4.2.2 Reconstruction of a Unique Binary Tree from Traversals
> **Theorem**: A binary tree can be **uniquely reconstructed** from:
> 1. Inorder + Preorder Traversals.
> 2. Inorder + Postorder Traversals.
> 
> *A tree CANNOT be uniquely reconstructed from Preorder + Postorder alone!*

#### Step-by-Step Tree Reconstruction Algorithm (Inorder + Preorder):
**Given**:
- $\text{Preorder} = [A, B, D, E, C, F]$
- $\text{Inorder} = [D, B, E, A, C, F]$

**Execution Trace**:
1. First element of Preorder is the **Root**: $\text{Root} = A$.
2. Locate $A$ in Inorder:
   $$\underbrace{D, B, E}_{\text{Left Subtree } T_L} \quad \mathbf{A} \quad \underbrace{C, F}_{\text{Right Subtree } T_R}$$
3. Subtree sizes: $|T_L| = 3$, $|T_R| = 2$.
4. Split Preorder:
   - Root: $A$
   - Preorder for $T_L$: $[B, D, E]$
   - Preorder for $T_R$: $[C, F]$
5. Recursively build $T_L$:
   - Root of $T_L$ is first element of $[B, D, E] \implies B$.
   - In Inorder $[D, B, E]$, $D$ is to the left of $B$ (left child), $E$ is to the right (right child).
6. Recursively build $T_R$:
   - Root of $T_R$ is first element of $[C, F] \implies C$.
   - In Inorder $[C, F]$, left is empty, $F$ is to the right (right child).
7. Reconstructed tree matches our diagram above. $\blacksquare$

---

## 4.3 BINARY SEARCH TREES (BST)

A **Binary Search Tree (BST)** is a binary tree where each node stores a key such that for any node $x$:
- All keys in the left subtree of $x$ are **strictly less than** key($x$):
  $$\forall y \in T_{\text{left}}(x), \, \text{key}(y) < \text{key}(x)$$
- All keys in the right subtree of $x$ are **strictly greater than** key($x$):
  $$\forall z \in T_{\text{right}}(x), \, \text{key}(z) > \text{key}(x)$$

```
                               BST Example:
                                   (50)
                                 ／    ＼
                              (30)      (70)
                             ／  ＼    ／  ＼
                           (20)  (40)(60)  (80)

         Inorder: 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 (Sorted!)
```

### 4.3.1 BST Operations & Complexities

1. **Search**: Recursively compare search key with root. If equal, return node. If smaller, recurse left; if larger, recurse right.
2. **Insertion**: Traverse down to find appropriate null position and attach new leaf node.
3. **Deletion**: Three distinct cases:
   - **Case 1 (Leaf Node, 0 children)**: Simply delete node and set parent pointer to null.
   - **Case 2 (1 child)**: Bypass node: connect parent directly to the single child.
   - **Case 3 (2 children)**: Replace node's key with its **Inorder Successor** (minimum element in right subtree) or **Inorder Predecessor** (maximum in left subtree), then recursively delete that successor/predecessor node (which is guaranteed to have at most 1 child).

#### Time Complexity:
- Average Case (Random Balanced Tree): $O(\log n)$.
- Worst Case (Skewed Tree): $O(n)$.

---

## 4.4 SPANNING TREES & MINIMUM SPANNING TREES (MST)

### 4.4.1 Spanning Trees: Definition & Traversal-Based Construction
A **spanning tree** $T$ of an undirected connected graph $G = (V, E)$ is a subgraph that is a tree and includes **all vertices of $G$**:
$$V(T) = V(G) \quad \text{and} \quad |E(T)| = |V| - 1$$

- **DFS Spanning Tree**:
  - Traversal partitions edges into:
    1. **Tree Edges**: Edges included in the DFS tree.
    2. **Back Edges**: Edges connecting a vertex to one of its ancestors in the DFS tree (indicates presence of cycles).
- **BFS Spanning Tree**:
  - Partitions edges into:
    1. **Tree Edges**.
    2. **Cross Edges**: Edges connecting vertices on the same level or adjacent levels (no back edges).
- **Cayley's Formula (1889)**:
  The number of distinct labeled trees on $n$ vertices is:
  $$T_n = n^{n-2}$$

---

### 4.4.2 Minimum Spanning Tree (MST)
For a connected weighted graph $G = (V, E, w)$, the **Minimum Spanning Tree (MST)** is a spanning tree whose total edge weight is minimized:
$$w(T) = \sum_{e \in E(T)} w(e) \quad \text{is minimized}$$

#### The Cut Property (Core Proof of Correctness for Greedy MST):
> **Theorem (Cut Property)**: Let $S \subset V$ be any proper subset of vertices, defining a cut $(S, V \setminus S)$. If $e = (u, v)$ is an edge with minimum weight crossing the cut ($u \in S, v \in V \setminus S$), then this edge $e$ belongs to **every MST of $G$** (assuming distinct edge weights).

---

### 4.4.3 Kruskal's vs Prim's Algorithms

```
  KRUSKAL'S ALGORITHM (Edge-Centric)         PRIM'S ALGORITHM (Vertex-Centric)
  - Sort ALL edges by weight.               - Start from an arbitrary root vertex.
  - Add next smallest edge that             - Greedily add cheapest edge connecting
    DOES NOT create a cycle.                  the growing tree to an outside vertex.
  - Uses Disjoint Set Union (DSU).          - Uses Priority Queue (Min-Heap).
  - Time: O(E log E) = O(E log V).          - Time: O(E log V) with binary heap.
  - Better for SPARSE graphs.               - Better for DENSE graphs.
```

#### Step-by-Step Worked MST Problem:
Consider the following 5-vertex weighted graph:
- Vertices: $\{A, B, C, D, E\}$
- Edges:
  $(A, B): 1$, $(A, C): 7$, $(B, C): 5$, $(B, D): 4$, $(B, E): 3$, $(C, E): 6$, $(D, E): 2$.

```
              (A)─── 1 ───(B)─── 4 ───(D)
               │         ／ │         ／
               │       ／   │       ／
               7     5      3     2
               │   ／       │   ／
               │ ／         │ ／
              (C)─── 6 ───(E)
```

#### 1. Kruskal's Algorithm Execution:
- **Sorted Edges**:
  1. $(A, B) = 1$
  2. $(D, E) = 2$
  3. $(B, E) = 3$
  4. $(B, D) = 4$
  5. $(B, C) = 5$
  6. $(C, E) = 6$
  7. $(A, C) = 7$
- **Selection Process**:
  - Pick $(A, B)$ [Weight 1]: No cycle. Add to MST. (Components: $\{A, B\}, \{C\}, \{D\}, \{E\}$)
  - Pick $(D, E)$ [Weight 2]: No cycle. Add to MST. (Components: $\{A, B\}, \{D, E\}, \{C\}$)
  - Pick $(B, E)$ [Weight 3]: Connects $\{A, B\}$ to $\{D, E\}$. No cycle. Add to MST. (Components: $\{A, B, D, E\}, \{C\}$)
  - Pick $(B, D)$ [Weight 4]: $B$ and $D$ already belong to same component $\{A, B, D, E\}$. **REJECT (Forms cycle $B-E-D-B$)**.
  - Pick $(B, C)$ [Weight 5]: Connects $\{A, B, D, E\}$ to $\{C\}$. No cycle. Add to MST. (Components: $\{A, B, C, D, E\}$)
  - Total edges selected = $4 = |V| - 1$. Algorithm terminates!
- **MST Edges**: $\{(A, B), (D, E), (B, E), (B, C)\}$.
- **Total Minimum Weight**: $1 + 2 + 3 + 5 = \mathbf{11}$.

---

## 4.5 HEAPS: MIN-HEAP & MAX-HEAP

A **binary heap** is a complete binary tree stored compactly in an array that satisfies the **Heap Order Property**.

### 4.5.1 Heap Classifications
1. **Min-Heap**: The value of each node is $\ge$ the value of its parent:
   $$\text{A}[\text{parent}(i)] \le \text{A}[i]$$
   The minimum element resides permanently at the root ($\text{A}[1]$).
2. **Max-Heap**: The value of each node is $\le$ the value of its parent:
   $$\text{A}[\text{parent}(i)] \ge \text{A}[i]$$
   The maximum element resides permanently at the root ($\text{A}[1]$).

```
          MAX-HEAP (Tree)                    MAX-HEAP (1-Indexed Array)
                (90)                       Index:  1   2   3   4   5   6   7
              ／    ＼                    ┌───┬───┬───┬───┬───┬───┬───┐
           (80)      (70)                 │ 90│ 80│ 70│ 40│ 30│ 60│ 50│
          ／  ＼    ／  ＼                └───┴───┴───┴───┴───┴───┴───┘
        (40)  (30)(60)  (50)              Parent(i) = ⌊i/2⌋
                                          LeftChild(i) = 2i
                                          RightChild(i) = 2i + 1
```

### 4.5.2 Array Index Mapping (1-Indexed)
For any element at index $i$:
- $\text{Parent}(i) = \lfloor i / 2 \rfloor$
- $\text{Left Child}(i) = 2i$
- $\text{Right Child}(i) = 2i + 1$

### 4.5.3 Core Heap Operations:
1. **Insert (`sift_up`)**: Place new element at end of array (maintaining complete tree shape), then bubble up by repeatedly swapping with parent until heap property is restored. Time: $O(\log n)$.
2. **Extract-Max / Extract-Min (`sift_down`)**: Replace root with last element of array, decrement heap size, then push root down by repeatedly swapping with its larger child (for max-heap). Time: $O(\log n)$.
3. **Build Heap**: Bottom-up heapification starting from the last internal node $\lfloor n/2 \rfloor$ down to $1$.
   $$\text{Time Complexity} = \sum_{h=0}^{\lfloor \log n \rfloor} \frac{n}{2^{h+1}} O(h) = O(n)$$

---

## 4.6 HUFFMAN'S DATA COMPRESSION ALGORITHM

Huffman's algorithm creates **optimal variable-length prefix codes** for lossless data compression based on character frequencies.
- **Prefix Code Property**: No codeword is a prefix of any other codeword (enables instantaneous, unambiguous decoding without delimiters).

### 4.6.1 Huffman Algorithm Mechanism
1. Compute frequency of each character.
2. Initialize a min-priority queue where each character is a single-node tree with weight equal to its frequency.
3. While queue contains more than one tree:
   - Extract the two trees $T_1$ and $T_2$ with lowest frequencies.
   - Create a new internal node with weight $= w(T_1) + w(T_2)$.
   - Make $T_1$ its left child (assign bit `0`) and $T_2$ its right child (assign bit `1`).
   - Insert new merged tree back into priority queue.
4. The remaining single tree is the **Huffman Code Tree**.

---

### 4.6.2 Fully Worked Numerical Huffman Problem

**Input Data**:
| Character | A | B | C | D | E |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Frequency** | 35 | 25 | 15 | 15 | 10 |

Total characters = $35 + 25 + 15 + 15 + 10 = 100$.

#### Step-by-Step Construction Trace:
- **Initial Min-Heap**: $[(E:10), (C:15), (D:15), (B:25), (A:35)]$
- **Iteration 1**:
  - Extract two smallest: $E(10)$ and $C(15)$ (or $D$).
  - Merge into new node $N_1$ with weight $10 + 15 = 25$.
  - Left: $E(10)$, Right: $C(15)$.
  - Queue now: $[(D:15), (B:25), (N_1:25), (A:35)]$.
- **Iteration 2**:
  - Extract two smallest: $D(15)$ and $B(25)$ (or $N_1$).
  - Merge into new node $N_2$ with weight $15 + 25 = 40$.
  - Left: $D(15)$, Right: $B(25)$.
  - Queue now: $[(N_1:25), (A:35), (N_2:40)]$.
- **Iteration 3**:
  - Extract two smallest: $N_1(25)$ and $A(35)$.
  - Merge into new node $N_3$ with weight $25 + 35 = 60$.
  - Left: $N_1(25)$, Right: $A(35)$.
  - Queue now: $[(N_2:40), (N_3:60)]$.
- **Iteration 4**:
  - Extract the remaining two: $N_2(40)$ and $N_3(60)$.
  - Merge into root node $R$ with weight $40 + 60 = 100$.
  - Left: $N_2(40)$, Right: $N_3(60)$.

```
                      HUFFMAN CODING TREE
                             (100)
                          0／     ＼1
                         ／         ＼
                     (40)             (60)
                   0／  ＼1         0／  ＼1
                   ／    ＼         ／    ＼
                 D(15)   B(25)   (25)     A(35)
                               0／  ＼1
                               ／    ＼
                             E(10)   C(15)
```

#### Codeword Assignment Table:
| Character | Frequency ($f_i$) | Codeword (Path from Root) | Bit Length ($l_i$) | Total Bits ($f_i \times l_i$) |
|:---:|:---:|:---:|:---:|:---:|
| **A** | 35 | `11` | 2 | $35 \times 2 = 70$ |
| **B** | 25 | `01` | 2 | $25 \times 2 = 50$ |
| **C** | 15 | `101` | 3 | $15 \times 3 = 45$ |
| **D** | 15 | `00` | 2 | $15 \times 2 = 30$ |
| **E** | 10 | `100` | 3 | $10 \times 3 = 30$ |
| **Total** | **100** | — | — | **225 bits** |

#### Performance & Compression Ratio Calculation:
1. **Average Bits Per Character ($L_{\text{avg}}$)**:
   $$L_{\text{avg}} = \sum_{i=1}^n \frac{f_i}{N} \cdot l_i = \frac{225}{100} = \mathbf{2.25 \text{ bits/char}}$$
2. **Fixed-Length Encoding Comparison**:
   With 5 unique characters, fixed-length requires $\lceil \log_2 5 \rceil = 3$ bits per character.
   $$\text{Total Fixed Bits} = 100 \times 3 = \mathbf{300 \text{ bits}}$$
3. **Compression Ratio**:
   $$\text{Compression Ratio} = \frac{300 - 225}{300} \times 100\% = \frac{75}{300} \times 100\% = \mathbf{25\% \text{ reduction}}$$

---


# UNIT 5: ALGEBRAIC STRUCTURES & MATHEMATICAL INDUCTION

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


# APPENDICES: CODE IMPLEMENTATIONS, PYQ SOLUTIONS & EXAM CHEAT SHEET

---

## APPENDIX A: MASTER FORMULA & THEOREM QUICK REFERENCE CHEAT SHEET

### A.1 Propositional & Predicate Logic
- **Implication**: $p \to q \equiv \neg p \lor q \equiv \neg q \to \neg p$ (Contrapositive).
- **Negation of Implication**: $\neg(p \to q) \equiv p \land \neg q$.
- **Quantifier Negations**:
  $$\neg \forall x P(x) \equiv \exists x \neg P(x), \quad \neg \exists x P(x) \equiv \forall x \neg P(x)$$
- **Canonical Forms**:
  - PDNF: $\bigvee_{f(\mathbf{v})=1} m_i$ (Sum of Minterms).
  - PCNF: $\bigwedge_{f(\mathbf{v})=0} M_i$ (Product of Maxterms).

### A.2 Set Theory, Relations & Functions
- **Total Relations on $n$-element set**: $2^{n^2}$.
- **Reflexive Relations**: $2^{n(n-1)}$.
- **Irreflexive Relations**: $2^{n(n-1)}$.
- **Neither Reflexive nor Irreflexive Relations**: $(2^n - 2) \cdot 2^{n(n-1)}$.
- **Symmetric Relations**: $2^{n(n+1)/2}$.
- **Antisymmetric Relations**: $2^n \cdot 3^{n(n-1)/2}$.
- **Asymmetric Relations**: $3^{n(n-1)/2}$.
- **Symmetric and Antisymmetric Relations**: $2^n$.
- **Equivalence Classes & Partitions**: Bell Number $B_n = \sum_{k=1}^n S(n, k)$.
- **Number of Functions $A \to B$**: $|B|^{|A|}$.
- **Number of Injections $A \to B$ ($|A| \le |B|$)**: $P(|B|, |A|) = \frac{|B|!}{(|B|-|A|)!}$.
- **Number of Bijections ($|A| = |B| = n$)**: $n!$.
- **Derangements ($D_n$)**: $n! \sum_{k=0}^n \frac{(-1)^k}{k!} \approx \frac{n!}{e}$.

### A.3 Graph Theory Metrics & Inequalities
- **Handshaking Lemma**: $\sum_{v \in V} \deg(v) = 2|E|$.
- **Complete Graph $K_n$**: $|E| = \frac{n(n-1)}{2}$, $\text{rad} = \text{diam} = 1$.
- **Complete Bipartite Graph $K_{m,n}$**: $|E| = m \cdot n$, $\text{rad} = \text{diam} = 2$ ($m, n \ge 2$).
- **Maximum Edges in Bipartite Graph of $n$ Vertices**: $\lfloor \frac{n^2}{4} \rfloor$.
- **Hypercube Graph $Q_n$**: $|V| = 2^n$, $|E| = n 2^{n-1}$, $\text{rad} = \text{diam} = n$.
- **Eulerian Circuit Criterion**: Connected + Every vertex has **even degree**.
- **Eulerian Trail Criterion**: Connected + Exactly **two vertices have odd degree**.
- **Euler's Planar Formula**: $V - E + F = 2$.
- **Planar Inequalities**:
  - Simple Planar ($V \ge 3$): $E \le 3V - 6$.
  - Triangle-Free Planar / Bipartite ($V \ge 3$): $E \le 2V - 4$.
- **Labeled Trees on $n$ Vertices (Cayley's Formula)**: $n^{n-2}$.

### A.4 Algebraic Structures & Number Theory
- **Lagrange's Theorem**: $|H|$ divides $|G|$; $[G : H] = \frac{|G|}{|H|}$.
- **Order of an Element**: $|a|$ divides $|G|$; $a^{|G|} = e$.
- **Euler's Totient Function $\phi(n)$**:
  $$\phi(n) = n \prod_{p \mid n} \left( 1 - \frac{1}{p} \right)$$
- **Generators of Cyclic Group of Order $n$**: Exactly $\phi(n)$ generators.
- **Divisor Lattice $D_n$**: Complemented $\iff n$ is **square-free**.

---

## APPENDIX B: ANNOTATED C++ IMPLEMENTATIONS FOR CORE DISCRETE ALGORITHMS

### B.1 Warshall's Algorithm (Transitive Closure / Reachability)
```cpp
#include <iostream>
#include <vector>

using namespace std;

// Computes the transitive closure of a directed graph using Warshall's algorithm.
// Time Complexity: O(V^3)
// Space Complexity: O(V^2)
void warshallTransitiveClosure(vector<vector<int>>& W, int V) {
    // Iterate through all possible intermediate vertices k
    for (int k = 0; k < V; ++k) {
        // Iterate through all source vertices i
        for (int i = 0; i < V; ++i) {
            // Iterate through all destination vertices j
            for (int j = 0; j < V; ++j) {
                // If vertex j is reachable from i directly or through {0, ..., k}
                W[i][j] = W[i][j] || (W[i][k] && W[k][j]);
            }
        }
    }
}

int main() {
    int V = 4;
    // Initial adjacency matrix W^(0)
    vector<vector<int>> W = {
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {0, 0, 0, 1},
        {1, 0, 0, 0}
    };

    warshallTransitiveClosure(W, V);

    cout << "Transitive Closure Matrix (Reachability):\n";
    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            cout << W[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
```

---

### B.2 Dijkstra's Single-Source Shortest Path Algorithm
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 1e9;

// Structure to represent a weighted directed/undirected edge
struct Edge {
    int to;
    int weight;
};

// Dijkstra's Algorithm using Min-Priority Queue
// Time Complexity: O((V + E) log V)
// Space Complexity: O(V + E)
void dijkstra(int src, int V, const vector<vector<Edge>>& adj, vector<int>& dist) {
    dist.assign(V, INF);
    dist[src] = 0;

    // Min-heap storing pairs: (distance, vertex)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue; // Stale queue entry

        for (const auto& edge : adj[u]) {
            int v = edge.to;
            int w = edge.weight;

            // Relaxation step
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
}
```

---

### B.3 Kruskal's Algorithm with Disjoint Set Union (DSU / Union-Find)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Disjoint Set Union structure with Path Compression & Union by Rank
struct DSU {
    vector<int> parent, rank;
    DSU(int n) {
        parent.resize(n);
        rank.assign(n, 0);
        for (int i = 0; i < n; ++i) parent[i] = i;
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]); // Path compression
    }

    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i == root_j) return false; // Cycle detected

        // Union by rank
        if (rank[root_i] < rank[root_j])
            parent[root_i] = root_j;
        else if (rank[root_i] > rank[root_j])
            parent[root_j] = root_i;
        else {
            parent[root_j] = root_i;
            rank[root_i]++;
        }
        return true;
    }
};

struct Edge {
    int u, v, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight; // For greedy sorting
    }
};

// Kruskal's MST Algorithm
// Time Complexity: O(E log E)
int kruskalMST(int V, vector<Edge>& edges, vector<Edge>& mstEdges) {
    sort(edges.begin(), edges.end());
    DSU dsu(V);
    int totalWeight = 0;

    for (const auto& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            mstEdges.push_back(edge);
            totalWeight += edge.weight;
            if (mstEdges.size() == V - 1) break;
        }
    }
    return totalWeight;
}
```

---

## APPENDIX C: NIT JALANDHAR COMPREHENSIVE EXAMINATION SOLUTIONS

### C.1 Solution to Mid-Semester Examination 2024 (Full Solutions)

#### Problem 2(a): Function & Relation Counting
*Question*: There are 6561 functions $f: X \to Y$ and $|Y| = 3$. If $X$ is the power set of $A$, then how many binary relations on $A$ are possible which are neither reflexive nor irreflexive? Show steps.

**Solution**:
1. **Find $|X|$**:
   The total number of functions from $X$ to $Y$ is given by $|Y|^{|X|}$.
   $$|Y|^{|X|} = 3^{|X|} = 6561$$
   Express 6561 as a power of 3:
   $$3^1 = 3, 3^2 = 9, 3^3 = 27, 3^4 = 81, 3^5 = 243, 3^6 = 729, 3^7 = 2187, 3^8 = 6561$$
   Therefore:
   $$|X| = 8$$
2. **Find $|A|$**:
   We are given that $X = \mathcal{P}(A)$ (the power set of $A$).
   $$|X| = |\mathcal{P}(A)| = 2^{|A|} = 8 = 2^3 \implies |A| = n = 3$$
3. **Count Binary Relations on $A$ Neither Reflexive Nor Irreflexive**:
   A relation $R$ on $A$ ($n = 3$) has $n = 3$ diagonal elements and $n(n - 1) = 3(2) = 6$ off-diagonal elements.
   - For a relation to be neither reflexive nor irreflexive, the diagonal elements can neither be ALL 1s (which would be reflexive) nor ALL 0s (which would be irreflexive).
   - Valid diagonal configurations = $2^n - 2 = 2^3 - 2 = 8 - 2 = 6$.
   - The 6 off-diagonal elements have no restrictions: $2^{n(n-1)} = 2^{3(2)} = 2^6 = 64$ choices.
   - By the Product Rule:
     $$N = (2^n - 2) \cdot 2^{n(n-1)} = 6 \times 64 = \mathbf{384}$$
4. **Answer**: Exactly **$384$ binary relations** are possible.

---

#### Problem 2(b): Social Network Matrix & Asymmetric Relations
*Question*: In an $n \times n$ matrix $R$ representing an asymmetric relation on $n = 100$ users:
I. Express mathematically the condition for the relation to be asymmetric.
II. What is the maximum number of 1's that can appear in $R$?

**Solution**:
1. **Mathematical Condition**:
   $$\forall i, j \in \{1, 2, \dots, n\}, \, (R[i][j] = 1) \implies (R[j][i] = 0)$$
   Equivalently: $R[i][j] + R[j][i] \le 1$ for $i \neq j$, and $R[i][i] = 0$ for all $i$.
2. **Maximum Number of 1's**:
   - Because asymmetry requires irreflexivity, all $n = 100$ diagonal entries MUST be $0$ ($R[i][i] = 0$).
   - For each of the $\frac{n(n-1)}{2}$ unordered pairs of distinct users $\{i, j\}$, at most one directed edge can exist (either $R[i][j]=1$ or $R[j][i]=1$, but not both).
   - To maximize 1's, we choose exactly one edge for every pair.
   - Maximum number of 1's:
     $$M_{\max} = \frac{n(n-1)}{2} = \frac{100 \times 99}{2} = 50 \times 99 = \mathbf{4950}$$

---

#### Problem 3(a): Probability of Reflexive Relation
*Question*: Let $\mathcal{R}$ be the set of all binary relations on $\{1, 2, 3\}$. A relation is chosen at random. What is the probability that it is reflexive?

**Solution**:
1. Cardinality of set $A$: $n = 3$.
2. Total number of binary relations on $A$:
   $$|\mathcal{R}| = 2^{n^2} = 2^{3^2} = 2^9 = 512$$
3. Total number of reflexive binary relations on $A$:
   $$N_{\text{reflexive}} = 2^{n(n-1)} = 2^{3(2)} = 2^6 = 64$$
4. Probability of choosing a reflexive relation:
   $$P(\text{Reflexive}) = \frac{N_{\text{reflexive}}}{|\mathcal{R}|} = \frac{64}{512} = \frac{1}{8} = \mathbf{0.125} \quad (12.5\%)$$

---

#### Problem 5(a): Properties of Relation $R = \{(x, y) \in \mathbb{N}^2 \mid \exists n \in \mathbb{N}, x^n = y\}$
*Question*: Analyze Reflexive, Symmetric, and Anti-symmetric properties on $\mathbb{N} = \{1, 2, 3, \dots\}$.

**Solution**:
1. **Reflexive**:
   - Condition: $\forall x \in \mathbb{N}, (x, x) \in R \iff \exists n \in \mathbb{N}, x^n = x$.
   - For any $x \in \mathbb{N}$, choosing $n = 1 \in \mathbb{N}$, we have $x^1 = x$.
   - **Conclusion: REFLEXIVE HOLDS.**
2. **Symmetric**:
   - Condition: $(x, y) \in R \implies (y, x) \in R$.
   - Counterexample: Choose $x = 2, y = 4$.
     $2^2 = 4$ with $n = 2 \in \mathbb{N}$, so $(2, 4) \in R$.
     For $(4, 2) \in R$, we need $4^n = 2$ for some $n \in \mathbb{N} = \{1, 2, 3, \dots\}$.
     For $n \ge 1$, $4^n \ge 4 > 2$. No natural number $n$ exists.
   - **Conclusion: SYMMETRIC FAILS.**
3. **Anti-symmetric**:
   - Condition: $(x, y) \in R \land (y, x) \in R \implies x = y$.
   - Proof: Assume $(x, y) \in R$ and $(y, x) \in R$.
     Then $\exists n_1, n_2 \in \mathbb{N}$ such that $x^{n_1} = y$ and $y^{n_2} = x$.
     Substituting gives:
     $$x = (x^{n_1})^{n_2} = x^{n_1 \cdot n_2}$$
     - If $x = 1$: Then $y = 1^{n_1} = 1$, so $x = y = 1$.
     - If $x > 1$: Then $x^1 = x^{n_1 n_2} \implies n_1 \cdot n_2 = 1$.
       Since $n_1, n_2 \in \mathbb{N}$, the only positive integers whose product is 1 are $n_1 = 1$ and $n_2 = 1$.
       Substituting $n_1 = 1$ gives $y = x^1 = x$.
   - **Conclusion: ANTI-SYMMETRIC HOLDS.**

---

### C.2 Solution to End-Semester Examination Dec 2024 (Full Solutions)

#### Problem 1(b): Hypercube Intersection Graph Isolation Analysis
*Question*: Consider a graph $G$ constructed with $2^n$ vertices, each representing a unique subset of an $n$-element set $S$ ($n \ge 6$). Vertices are adjacent solely if their subsets intersect in exactly two elements ($|A \cap B| = 2$). Determine how many vertices possess no connections to any other vertices (isolated / degree 0).

**Solution**:
1. Vertices of $G$ correspond to all subsets $A \in \mathcal{P}(S)$. Total vertices $= 2^n$.
2. Two distinct vertices $A, B \subseteq S$ are connected by an edge iff:
   $$|A \cap B| = 2$$
3. A vertex $A$ has degree 0 (no incident edges) iff there is NO other subset $B \subseteq S$ ($B \neq A$) such that $|A \cap B| = 2$.
4. **Case 1: $|A| = 0$ ($A = \emptyset$)**:
   For any subset $B \subseteq S$, $|A \cap B| = |\emptyset \cap B| = 0 \neq 2$.
   It is impossible for $\emptyset$ to intersect any set in 2 elements.
   Thus, $A = \emptyset$ has degree 0.
   Number of such subsets = $\binom{n}{0} = 1$.
5. **Case 2: $|A| = 1$ (Singletons $A = \{x\}$)**:
   For any subset $B \subseteq S$, $A \cap B \subseteq A$, which means:
   $$|A \cap B| \le |A| = 1 < 2$$
   It is mathematically impossible for a 1-element subset to share 2 elements with any subset!
   Thus, every singleton subset has degree 0.
   Number of such subsets = $\binom{n}{1} = n$.
6. **Case 3: $|A| \ge 2$**:
   Can we always find a distinct subset $B \neq A$ such that $|A \cap B| = 2$?
   - Subcase 3a ($|A| = 2$, say $A = \{x_1, x_2\}$):
     Since $n \ge 6$, there are at least $6 - 2 = 4$ elements in $S \setminus A$.
     Pick any element $y \in S \setminus A$, and define $B = \{x_1, x_2, y\}$.
     Clearly $B \neq A$, and $A \cap B = \{x_1, x_2\}$, so $|A \cap B| = 2$.
     Thus, any 2-element subset is adjacent to at least one other subset (e.g., $B$).
   - Subcase 3b ($|A| \ge 3$):
     Choose any two elements $\{x_1, x_2\} \subseteq A$, and define $B = \{x_1, x_2\}$.
     Since $|A| \ge 3$, $B \neq A$.
     Then $|A \cap B| = |\{x_1, x_2\}| = 2$.
     Thus, $A$ is adjacent to $B$.
7. **Total Isolated Vertices**:
   The ONLY vertices with degree 0 are those with $|A| < 2$:
   $$N_{\text{isolated}} = \binom{n}{0} + \binom{n}{1} = 1 + n$$
8. **Answer**: Exactly **$n + 1$ vertices** possess no connections to any other vertices.

---

#### Problem 2(a): Poset Isomorphism with $\mathcal{P}(\{a, b, c\})$
*Question*: Identify which ancient artifact poset is isomorphic to $(\mathcal{P}(S), \subseteq)$ where $S = \{a, b, c\}$:
1. Inscription I: $\{1, 2, 5, 7, 10, 14, 35, 70\}$ with $\le$.
2. Inscription II: $\{1, 2, 3, 6, 14, 21, 42\}$ with $\mid$.
3. Inscription III: $\{1, 2, 3, 6, 11, 22, 33, 66\}$ with $\mid$.

**Solution**:
1. **Analyze Target Poset $(\mathcal{P}(S), \subseteq)$**:
   - Cardinality: $|\mathcal{P}(S)| = 2^3 = 8$ elements.
   - Hasse diagram: 3-dimensional Boolean cube $B_3$.
   - Minimal element: $\emptyset$ (1 element).
   - Atoms (level 1): $\{a\}, \{b\}, \{c\}$ (3 elements, each covers $\emptyset$).
   - Level 2: $\{a,b\}, \{b,c\}, \{a,c\}$ (3 elements).
   - Maximal element: $\{a,b,c\}$ (1 element).
   - It is a **complemented distributive lattice** (not a chain).
2. **Analyze Inscription I**:
   - Relation is standard linear order $\le$.
   - This forms a **total order (chain)**: $1 < 2 < 5 < 7 < 10 < 14 < 35 < 70$.
   - In a chain, every pair is comparable. In $\mathcal{P}(S)$, $\{a\}$ and $\{b\}$ are incomparable.
   - **NOT ISOMORPHIC.**
3. **Analyze Inscription II**:
   - The set has only **7 elements**!
   - Since $|\mathcal{P}(S)| = 8 \neq 7$, no bijection can exist.
   - **NOT ISOMORPHIC.**
4. **Analyze Inscription III**:
   - Set: $D_{66} = \{1, 2, 3, 6, 11, 22, 33, 66\}$.
   - Cardinality: Exactly $8$ elements.
   - Notice $66 = 2 \times 3 \times 11$ is a product of 3 distinct primes (square-free).
   - The divisor poset $(D_{p_1 p_2 p_3}, \mid)$ is canonically isomorphic to $(\mathcal{P}(\{p_1, p_2, p_3\}), \subseteq)$ via the mapping:
     $$f(d) = \{p \in \{2, 3, 11\} \mid p \text{ divides } d\}$$
     - $f(1) = \emptyset$
     - $f(2) = \{2\}$, $f(3) = \{3\}$, $f(11) = \{11\}$ (3 atoms)
     - $f(6) = \{2, 3\}$, $f(22) = \{2, 11\}$, $f(33) = \{3, 11\}$
     - $f(66) = \{2, 3, 11\}$
   - This mapping is a strict order-isomorphism.
5. **Answer**: **Inscription III** is the unique artifact that mimics the powerset poset.

---
