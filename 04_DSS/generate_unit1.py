# generate_unit1.py
# Generates Unit 1: Introduction to Preliminaries and Predicate Calculus

def get_unit1_text():
    return r"""# UNIT 1: INTRODUCTION TO PRELIMINARIES AND PREDICATE CALCULUS

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
"""

if __name__ == "__main__":
    print(f"Unit 1 generated: {len(get_unit1_text())} characters")
