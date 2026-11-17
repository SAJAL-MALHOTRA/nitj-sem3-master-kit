# Discrete Structures (ITDC0211) — Exam Notes
### Unit 1: Preliminaries & Predicate Calculus | Unit 2: Set Theory, Relations, Functions, Counting

---

## PART A — UNIT 1: PRELIMINARIES AND PREDICATE CALCULUS

### 1. Propositions

A **proposition** is a declarative sentence that is either **True (T)** or **False (F)**, never both.

- "5 is a prime number" → proposition (True)
- "Close the door" → NOT a proposition (command)
- "x + 2 = 5" → NOT a proposition unless x is fixed (open sentence / predicate)

**Compound propositions** are built using logical connectives:

| Connective | Symbol | Name | Read as |
|---|---|---|---|
| NOT | ¬p | Negation | "not p" |
| AND | p ∧ q | Conjunction | "p and q" |
| OR | p ∨ q | Disjunction | "p or q" |
| XOR | p ⊕ q | Exclusive OR | "either p or q, not both" |
| IF...THEN | p → q | Conditional/Implication | "if p then q" |
| IFF | p ↔ q | Biconditional | "p if and only if q" |

**Truth tables:**

| p | q | ¬p | p∧q | p∨q | p⊕q | p→q | p↔q |
|---|---|----|----|-----|-----|-----|-----|
| T | T | F | T | T | F | T | T |
| T | F | F | F | T | T | F | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | F | F | T | T |

**Key intuitions (exam favorite — Q3a-type):**
- **p → q**: False ONLY when p=T, q=F. (You broke your promise only if the condition happened but the promised result didn't.)
- **p ∧ q**: True only when BOTH true.
- **p ∨ q**: True when AT LEAST ONE is true (inclusive or).
- **p ⊕ q**: True when exactly one is true (excludes both-true case).

### 2. The Many Faces of p → q (recurring exam topic)

All of these are **equivalent phrasings** of p → q:
1. If p, then q
2. p implies q
3. **p is sufficient for q**
4. **p only if q**
5. **q is necessary for p**
6. q if p
7. q follows from p
8. q is a consequence of p
9. p unless ¬q (informally)

**Related conditional forms — VERY important for exam (Q3a in your PYQ: "converse of I stay only if you go"):**

Given p → q:

| Form | Statement | Logically equivalent to |
|---|---|---|
| **Converse** | q → p | NOT equivalent to original |
| **Inverse** | ¬p → ¬q | NOT equivalent to original (but IS the converse's contrapositive) |
| **Contrapositive** | ¬q → ¬p | **Equivalent to original p → q** |

**Worked example (from your PYQ):** *"I stay only if you go."*
- Let p = "I stay", q = "you go"
- "p only if q" means **p → q**
- **Converse** = q → p = "If you go, then I stay" → in English: **"You go only if I stay"** or **"If you go, I stay."**

### 3. Tautology, Contradiction, Contingency

- **Tautology**: A compound proposition that is **TRUE for every possible truth value** of its variables.
  - Example: p ∨ ¬p (Law of Excluded Middle) — always true.
- **Contradiction**: **FALSE for every** combination.
  - Example: p ∧ ¬p — always false.
- **Contingency**: Neither always true nor always false — depends on p, q.

**How to check**: Build the full truth table. If the final column is all T → tautology; all F → contradiction; mixed → contingency.

**Common tautologies to know:**
- p → p
- (p ∧ (p → q)) → q *(Modus Ponens as a tautology)*
- ((p → q) ∧ ¬q) → ¬p *(Modus Tollens)*
- (p → q) ↔ (¬q → ¬p) *(shows p→q ≡ its contrapositive)*

### 4. Laws of Logical Equivalence (memorize — used to simplify/prove statements)

| Law | Form |
|---|---|
| Identity | p ∧ T ≡ p ; p ∨ F ≡ p |
| Domination | p ∨ T ≡ T ; p ∧ F ≡ F |
| Idempotent | p ∧ p ≡ p ; p ∨ p ≡ p |
| Double Negation | ¬(¬p) ≡ p |
| Commutative | p ∧ q ≡ q ∧ p ; p ∨ q ≡ q ∨ p |
| Associative | (p∧q)∧r ≡ p∧(q∧r) |
| Distributive | p∧(q∨r) ≡ (p∧q)∨(p∧r) |
| **De Morgan's** | ¬(p∧q) ≡ ¬p∨¬q ; ¬(p∨q) ≡ ¬p∧¬q |
| Absorption | p∨(p∧q) ≡ p ; p∧(p∨q) ≡ p |
| Negation | p∨¬p ≡ T ; p∧¬p ≡ F |
| **Conditional identity** | p → q ≡ ¬p ∨ q |
| **Biconditional identity** | p ↔ q ≡ (p→q) ∧ (q→p) |

**De Morgan's is the #1 exam trap** — always double-check negations of ∧/∨ statements and of ∀/∃ (see predicate section below).

### 5. Rules of Substitution and Transitivity

- **Rule of Substitution**: If S is a tautology and you uniformly replace every occurrence of a variable p in S with any proposition, the result is still a tautology.
- **Rule of Transitivity**: If p ≡ q and q ≡ r, then p ≡ r. (Used to chain equivalences step-by-step in simplification proofs — show each step citing the law used.)

### 6. Normal Forms

Every compound proposition can be converted into a standard form built from minterms/maxterms.

- **Disjunctive Normal Form (DNF)**: OR of AND terms → (p∧q) ∨ (¬p∧r) ∨ ...
- **Conjunctive Normal Form (CNF)**: AND of OR terms → (p∨q) ∧ (¬p∨r) ∧ ...
- **Principal DNF (PDNF)**: DNF where every term (minterm) contains ALL variables (each either plain or negated) — built directly from truth-table rows where result = T.
- **Principal CNF (PCNF)**: CNF where every term (maxterm) contains ALL variables — built from rows where result = F.

**How to find PDNF from truth table:**
1. Find all rows where output = T.
2. For each such row, write the AND of variables (variable as-is if T in that row, negated if F).
3. OR all these terms together.

**How to find PCNF:** Same but use rows where output = F, and OR the variables (negated if T, as-is if F) inside each term, then AND all terms.

### 7. Predicate Calculus (Quantifiers)

A **predicate** P(x) becomes a proposition once x is assigned a specific value or bound by a quantifier.

- **Universal quantifier**: ∀x P(x) → "P(x) is true for ALL x in the domain"
- **Existential quantifier**: ∃x P(x) → "P(x) is true for AT LEAST ONE x"

**Negating quantifiers (De Morgan's for predicates — exam favorite, appears as your PYQ Q3d):**
- ¬(∀x P(x)) ≡ ∃x ¬P(x)
- ¬(∀x∃y P(x,y)) ≡ ∃x∀y ¬P(x,y) — *flip every quantifier and negate the innermost predicate*
- ¬(∃x P(x)) ≡ ∀x ¬P(x)

**Worked example (your PYQ Q3d style):**
*"∀x∃y∃t(¬F(x,y,t))"* where F(x,y,t) = "x can fool y at time t"
- Reading directly: "For every person x, there exists some person y and some time t such that x **cannot** fool y at t."
- In plain English: **"Everyone fails to fool at least one person at least once"**, i.e., **no one can fool everybody all the time.**
- Contrast with the famous saying "You can fool some people all the time, and all people some of the time, but not all people all the time" — this statement formalizes that last part.

**Multiple quantifiers — order matters:**
- ∀x∃y P(x,y): for every x, SOME y exists (y can depend on x)
- ∃y∀x P(x,y): there is ONE y that works for ALL x (much stronger claim)

**Translating English to predicate logic (your PYQ Q3b, Q3c style):**

*"Tigers and lions attack if they are hungry or threatened"*
- Let T(x): x is a tiger, L(x): x is a lion, H(x): x is hungry, Th(x): x is threatened, A(x): x attacks
- ∀x [(T(x) ∨ L(x)) ∧ (H(x) ∨ Th(x)) → A(x)]

*"Some boys in the class are taller than all the girls"* (taller(x,y): x taller than y)
- Let B(x): x is a boy, G(y): y is a girl
- **∃x [B(x) ∧ ∀y (G(y) → taller(x,y))]**
- Read carefully: this needs "there exists a boy such that for ALL girls, he is taller" — the ∃ and ∀ order is critical here; swapping them changes the meaning entirely.

### 8. Proof Techniques

| Technique | Idea |
|---|---|
| **Direct Proof** | Assume p is true, use logical steps to show q must be true. |
| **Proof by Contrapositive** | To prove p→q, instead prove ¬q→¬p (equivalent, sometimes easier). |
| **Proof by Contradiction** | Assume p is true AND q is false; derive a contradiction (something false); conclude p→q must hold. |
| **Proof by Cases** | Split into exhaustive cases, prove the result in each case separately. |
| **Mathematical Induction** | Base case (n=1 or n=0) + Inductive step (assume true for n=k, prove for n=k+1). Used for statements about all natural numbers. |
| **Vacuous Proof** | If p is always false, p→q is automatically true regardless of q. |
| **Trivial Proof** | If q is always true, p→q is automatically true regardless of p. |

---

## PART B — UNIT 2: SET THEORY AND FUNCTIONS

### 1. Basic Set Concepts

- **Set**: unordered collection of distinct elements. Written {a, b, c}.
- **Cardinality** |A|: number of elements.
- **Subset**: A ⊆ B if every element of A is in B.
- **Power Set** P(A): the set of ALL subsets of A (including ∅ and A itself).
  - **|P(A)| = 2ⁿ** where n = |A|.

**Worked example (your PYQ Q4):** T = {2, 4, {6}, {8,9}} → this set has **4 elements**: `2`, `4`, `{6}`, `{8,9}` (note: `{6}` and `{8,9}` are themselves treated as single elements here, since they're sets nested inside T).
- |P| = 2⁴ = **16**
- **{4, {6}} ∈ P?** → We need {4,{6}} to be an element of P(T), i.e., a subset of T. Since both 4 and {6} are elements of T, {4,{6}} IS a valid subset of T → **TRUE**
- **{6} ⊆ P?** → This asks if {6} is a subset of the power set P (not of T!). For {6} ⊆ P, the element `6` must belong to P. But P's elements are subsets of T, and `6` alone is not a subset of T (only `{6}` is, as an element of T). So **FALSE**
- **{{8,9}} ∈ P?** → Is the set containing {8,9} a subset of T? Since {8,9} ∈ T, yes {{8,9}} ⊆ T → **TRUE**
- **∅ ∈ P?** → The empty set is a subset of every set, so ∅ ∈ P(T) always → **TRUE**

⚠️ **This question tests ∈ vs ⊆ carefully — the #1 mistake students make.** Remember:
- **∈** asks "is this a single element of the set?"
- **⊆** asks "is every element of this collection also in the set?"

### 2. Venn Diagrams & Set Operations

- Union (A∪B), Intersection (A∩B), Difference (A−B), Complement (A′ or Ā)
- **|A ∪ B| = |A| + |B| − |A ∩ B|** (Inclusion-Exclusion for 2 sets)
- **|A ∪ B ∪ C| = |A|+|B|+|C| − |A∩B|−|B∩C|−|A∩C| + |A∩B∩C|** (for 3 sets)

**Your PYQ Q5a** applies this idea to *relations* rather than plain sets — see Relations section below (Reflexive vs Antisymmetric Venn diagram).

### 3. Relations

A **relation R** from set A to set B is a subset of A × B. If A = B, it's a relation **on** A.

**Representations:**
- **Set of ordered pairs**: R = {(a,b) | condition}
- **Matrix**: rows/columns = elements; entry = 1 if related, 0 if not.
- **Directed graph (digraph)**: arrow from a to b if (a,b) ∈ R; self-loop if (a,a) ∈ R.

#### Properties of Relations (core exam topic — your PYQ Q2a)

For relation R on set A:

| Property | Definition | How to check on digraph/matrix |
|---|---|---|
| **Reflexive** | ∀a∈A, (a,a) ∈ R | Every node has a self-loop / diagonal is all 1s |
| **Irreflexive** | ∀a∈A, (a,a) ∉ R | NO node has a self-loop |
| **Symmetric** | (a,b)∈R ⟹ (b,a)∈R | Matrix is symmetric about diagonal; every arrow has a matching reverse arrow |
| **Antisymmetric** | (a,b)∈R ∧ (b,a)∈R ⟹ a=b | No two DISTINCT nodes have arrows both ways |
| **Transitive** | (a,b)∈R ∧ (b,c)∈R ⟹ (a,c)∈R | Every 2-step path has a direct shortcut arrow |

**Worked example (your PYQ Q2a — digraph on {0,1,2}):**
From the diagram: R = {(0,0), (1,1), (2,2), (0,2), (1,0), (2,1)}
- **Reflexive?** Self-loops at 0, 1, 2 → all present → **YES, reflexive**
- **Symmetric?** (0,2) ∈ R but (2,0) ∉ R → **NOT symmetric**
- **Antisymmetric?** Need: no distinct pair (a,b) with both (a,b) and (b,a) in R. Checking (0,2): is (2,0) also there? No. Checking (1,0): is (0,1) there? No. Checking (2,1): is (1,2) there? No. No violations found → **YES, antisymmetric**
- **Transitive?** Check (0,2) and (2,1) → need (0,1). Is it there? **No** → **NOT transitive**

#### Equivalence Relations (your PYQ Q2b-I)

A relation is an **equivalence relation** if it is **Reflexive + Symmetric + Transitive**. It partitions the set into disjoint **equivalence classes**.

**Worked example (your PYQ — "similar interests" relation on 500 users, need ≥3 shared categories out of 8):**
- **Reflexive?** Does a user share ≥3 interests with themself? A user trivially shares ALL their own interests with themself (up to 8), so R is reflexive (assuming users have ≥3 interests) — generally **assumed reflexive** if every user has at least 3 interests.
- **Symmetric?** If a,b share ≥3 categories, then b,a share the same ≥3 categories → **YES, symmetric** (sharing is mutual by definition).
- **Transitive?** **NO** — this is the key insight. If A and B share {Gaming, Sports, Music} and B and C share {Travel, Food, Fashion}, A and C might share ZERO categories. Just because A~B and B~C doesn't mean A~C.
- **Conclusion: R is NOT an equivalence relation** (fails transitivity), even though it's reflexive and symmetric. This is a classic "tolerance relation," not equivalence.

**Part II (max community size):** With 8 categories, the maximum group where everyone shares ≥3 categories from the SAME core set is bounded by how many users can be assigned overlapping category-subsets. If every user in the group must pairwise share ≥3 of the 8 categories, in the best case **all 500 users could belong if they all share the same ≥3 categories** — so the theoretical **maximum possible community size = 500** (all users share at least 3 identical interest categories, e.g., everyone into Gaming, Sports, Music).

#### Partial Order Relations / POSET (your PYQ Q5b)

A relation that is **Reflexive + Antisymmetric + Transitive** is called a **partial order**, and the set with this relation is a **Partially Ordered Set (POSET)**, written (A, ≤).

**"Partial"** because not every pair of elements needs to be comparable (unlike a *total order* like ≤ on real numbers).

**Classic example:** Divisibility relation "a divides b" on positive integers.
- Reflexive: a | a ✓
- Antisymmetric: if a|b and b|a then a=b ✓
- Transitive: if a|b and b|c then a|c ✓
- But 2 and 3 are **incomparable** — neither divides the other. That's the "partial" part.

**Another classic example:** Subset relation ⊆ on P(A) — the power set of any set, ordered by inclusion.

**Practical significance:** POSETs model hierarchies and dependency structures — e.g., task scheduling (task A must finish before task B), file system directory structures, version/release dependencies, organizational hierarchies. Visualized using a **Hasse diagram** (simplified digraph — omits loops, transitive edges, and arrowheads; higher elements drawn above lower ones).

#### Venn Diagram: Reflexive vs Antisymmetric relations on a set of size n (your PYQ Q5a)

Total number of relations on a set of size n = **2^(n²)** (since A×A has n² pairs, each either in or out of R).

- Total reflexive relations: all n diagonal entries fixed as 1, remaining (n²−n) entries free → **2^(n²−n)**
- Total antisymmetric relations: for each of the n²−n off-diagonal pairs (grouped into (n²−n)/2 symmetric pairs {(a,b),(b,a)}), each pair has 3 valid choices (neither, only (a,b), only (b,a) — not both) and diagonal entries are free (2 choices each) → **3^((n²−n)/2) × 2ⁿ**

Let k(X) denote count of relations satisfying property X, and let U = universal set of all 2^(n²) relations.

- **k(Antisym ∩ Ref)**: relations that are BOTH reflexive AND antisymmetric — diagonal forced to 1 (reflexive), off-diagonal pairs must avoid "both directions" (antisymmetric) → each of the (n²−n)/2 pairs has 3 choices (neither / one way / other way) → **k(Antisym ∩ Ref) = 3^((n²−n)/2)**
- **k(Antisym ∪ Ref)** = k(Antisym) + k(Ref) − k(Antisym ∩ Ref) = **3^((n²−n)/2)·2ⁿ + 2^(n²−n) − 3^((n²−n)/2)**
- **k(Ref − Antisym)** = k(Ref) − k(Antisym ∩ Ref) = **2^(n²−n) − 3^((n²−n)/2)**
- **k(Antisym − Ref)** = k(Antisym) − k(Antisym ∩ Ref) = **3^((n²−n)/2)·2ⁿ − 3^((n²−n)/2)** = **3^((n²−n)/2)·(2ⁿ − 1)**

*(Draw two overlapping circles inside a rectangle U; label one "Reflexive," other "Antisymmetric"; the overlap region = k(Antisym∩Ref); use the formulas above to label each region.)*

### 4. Functions

A **function** f: X→Y assigns exactly one element of Y to each element of X.

| Type | Definition |
|---|---|
| **One-to-one (injective)** | Different inputs → different outputs. f(a)=f(b) ⟹ a=b |
| **Onto (surjective)** | Every element of Y is hit by some element of X (range = codomain) |
| **Bijective** | Both one-to-one AND onto → has a well-defined **inverse function** f⁻¹ |

**Counting functions:** Number of functions f: X→Y (with |X|=m, |Y|=n) = **nᵐ** (each of the m elements of X independently picks 1 of n outputs).

**Worked example (your PYQ Q1):** "6561 functions f: X→Y, |Y|=3. X is the power set of A."
- Total functions = |Y|^|X| = 3^|X| = 6561
- 3⁸ = 6561, so **|X| = 8**
- Since X = P(A), |X| = 2^|A| = 8 → **|A| = 3**
- Now: "how many binary relations on A are possible which are neither reflexive nor irreflexive?"
- Total relations on A (|A|=3) = 2^(3²) = 2⁹ = 512
- Reflexive relations: diagonal fixed (3 entries =1), remaining 6 entries free → 2⁶ = 64
- Irreflexive relations: diagonal fixed (3 entries =0), remaining 6 entries free → 2⁶ = 64
- Reflexive ∩ Irreflexive = 0 (a relation can't require diagonal both all-1 and all-0 simultaneously, unless n=0) → they're disjoint
- Reflexive ∪ Irreflexive = 64 + 64 − 0 = 128
- **Neither reflexive nor irreflexive = Total − (Reflexive ∪ Irreflexive) = 512 − 128 = 384**

**Composition & Identity:**
- (f∘g)(x) = f(g(x))
- Identity function: I(x) = x for all x; f∘I = I∘f = f
- If f is bijective, f∘f⁻¹ = f⁻¹∘f = I

### 5. Counting Techniques

- **Principle of Inclusion-Exclusion**: |A∪B| = |A|+|B|−|A∩B| (extend for 3+ sets as shown above). Used to count "neither/nor" or "at least one of" scenarios (exactly the technique used in the Q1 worked example above).
- **Euclidean Algorithm**: to find GCD(a,b): repeatedly apply a = bq + r, then GCD(a,b) = GCD(b,r), until remainder = 0. The last nonzero remainder is the GCD.
- **Elements of Probability**: P(E) = (favorable outcomes)/(total outcomes); basic addition/multiplication rules for combined events.
- **Recurrence Relations**: express a term in a sequence using previous terms, e.g., Fibonacci: F(n) = F(n−1) + F(n−2).

---

## Quick Revision Checklist Before the Exam

- [ ] Truth tables for all 6 connectives — can build from memory
- [ ] All laws of equivalence (esp. De Morgan's) — can apply in a proof chain
- [ ] Converse / Inverse / Contrapositive — know which one is logically equivalent to the original
- [ ] PDNF/PCNF construction from a truth table
- [ ] Negating quantified statements (∀↔∃ flip)
- [ ] Translating English ↔ predicate logic (watch quantifier ORDER)
- [ ] Checking reflexive/symmetric/antisymmetric/transitive from a digraph or matrix
- [ ] Equivalence relation vs POSET — know the 3 defining properties for each
- [ ] ∈ vs ⊆ distinction (power set questions)
- [ ] |P(A)| = 2ⁿ, total relations on A = 2^(n²)
- [ ] Inclusion-Exclusion for "neither/nor" counting problems
- [ ] One-to-one vs onto vs bijective, and counting functions nᵐ
