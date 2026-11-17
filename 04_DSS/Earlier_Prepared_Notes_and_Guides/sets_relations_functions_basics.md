# Sets, Relations & Functions — From Scratch (Quiz-Linked Notes)

## PART 1: SETS

A **set** is just a well-defined collection of things. `S = {x, y, z}` means S contains exactly x, y, z.

### Power Set
The **power set** of S, written `P(S)`, is the set of *all subsets* of S (including the empty set `{}` and S itself).

**Key formula:** If `|S| = n`, then `|P(S)| = 2^n`.

*Why?* For each of the n elements, you independently decide "in the subset or not" → 2 choices per element → 2×2×...×2 (n times) = 2^n total subsets.

**→ Solves Q5:** `{0, 1, 2, ..., 10}` has 11 elements (0 through 10 inclusive — don't miscount this, it's a classic trap).
`|P(S)| = 2^11 = 2048`.

---

## PART 2: RELATIONS

A **relation R on a set A** is just a subset of `A × A` (the set of all ordered pairs from A). If `(a,b) ∈ R`, we say "a is related to b."

### The core properties (memorize these definitions cold — every MCQ hinges on precise wording)

| Property | Definition | Plain meaning |
|---|---|---|
| **Reflexive** | `(a,a) ∈ R` for *every* a ∈ A | Everything relates to itself |
| **Irreflexive** | `(a,a) ∉ R` for *any* a | Nothing relates to itself |
| **Symmetric** | if `(a,b) ∈ R` then `(b,a) ∈ R` | Relation works both ways |
| **Antisymmetric** | if `(a,b) ∈ R` AND `(b,a) ∈ R`, then `a = b` | The *only* way both directions can hold is if it's the same element |
| **Asymmetric** | if `(a,b) ∈ R` then `(b,a) ∉ R` (no exceptions, ever) | Strictly one-directional |
| **Transitive** | if `(a,b) ∈ R` and `(b,c) ∈ R` then `(a,c) ∈ R` | Chains carry through |

**Trap most students fall into:** "not symmetric" and "antisymmetric" are NOT opposites. A relation can be neither, or even both (e.g., the empty relation, or the identity relation `{(a,a)}` — both symmetric AND antisymmetric, since there's no pair violating either).

### Special relation types

- **Equivalence relation** = Reflexive + Symmetric + Transitive. (Groups things into "equivalence classes" — think "=", or "same remainder mod n".)
- **Partial order** = Reflexive + Antisymmetric + Transitive. (Think "≤" or "subset ⊆" — you can compare *some* pairs but not necessarily all.)
- **Total order** = Partial order where *every* pair is comparable (for any a,b: either `(a,b)∈R` or `(b,a)∈R`). (Think "≤" on real numbers — any two numbers can be compared.)

### → Solves Q2
`R = {(x,y), (x,z), (z,x), (z,y)}` on `{x,y,z}`.

- **Symmetric?** `(x,y) ∈ R` but `(y,x) ∉ R` → fails → **NOT symmetric**.
- **Antisymmetric?** `(x,z) ∈ R` AND `(z,x) ∈ R`, but `x ≠ z` → this directly violates the antisymmetric definition → **NOT antisymmetric**.

**Answer: D — neither symmetric nor antisymmetric.**

### → Solves Q3
Every equivalence relation must at least contain the diagonal (reflexivity forces every `(a,a)` in).

- **Smallest possible equivalence relation** on an n-element set = just the diagonal = `{(a,a) : a ∈ S}` → **n ordered pairs**. (This is called the *identity relation* — check reflexive ✓, symmetric ✓ trivially, transitive ✓ trivially.)
- **Largest possible equivalence relation** = the *universal relation* = everything related to everything = `S × S` → **n² ordered pairs**.

**Answer: n and n².**

### → Solves Q4
`(x,y) R (u,v)` iff `x < u AND y > v`.

Check reflexive first (it's required for both Partial Order and Equivalence Relation, so if it fails, both options die immediately): does `(x,y) R (x,y)` hold? That needs `x < x`, which is **always false**.

→ Not reflexive → can't be a partial order, can't be a total order, can't be an equivalence relation.

**Answer: D — neither a Partial Order nor an Equivalence Relation.**

*(Lesson: always check reflexivity first on these "is it a partial order/equivalence relation" questions — it's the cheapest property to test and eliminates options fast.)*

---

## PART 3: COUNTING RELATIONS ON A SET

This is pure combinatorics once you see the trick. A relation on an n-element set is a subset of `A × A`, and `|A × A| = n²`. So:

- **Total number of relations** on an n-element set = `2^(n²)` (each of the n² possible pairs is either in or out).
- **Reflexive relations**: the n diagonal pairs `(a,a)` are *forced* to be in. Only the remaining `n² - n` off-diagonal pairs are free choices → `2^(n² - n)`.
- **Symmetric relations**: pairs come in mirror couples `(a,b)` & `(b,a)` (except the diagonal, which mirrors itself). You choose independently for each *pair of mirrors*, and there are `n(n+1)/2` such independent slots (n diagonal + n(n-1)/2 off-diagonal mirror-pairs) → `2^(n(n+1)/2)`.
- **Reflexive AND Symmetric relations**: diagonal is forced in (reflexive), so only the `n(n-1)/2` off-diagonal mirror-pairs are free → `2^(n(n-1)/2)`.

### → Solves Q6
"Reflexive as well as symmetric" = relations that are both → use the last formula, n = 14:
`n(n-1)/2 = 14×13/2 = 91`

**Answer: 2^91.**

---

## PART 4: FUNCTIONS

A **function** `f: A → B` assigns *exactly one* output in B to every input in A. (A = domain, B = codomain.)

### Types
- **Injective (one-to-one):** different inputs → different outputs. No two x's share an output.
- **Surjective (onto):** every element of B is hit by some input.
- **Bijective:** both injective and surjective — a perfect pairing.
- **Identity function:** `f(x) = x` — maps everything to itself. It's the "do nothing" function, always bijective.

### Inverse function
`f⁻¹` exists **as a true function** only when f is **bijective**. If f isn't injective, multiple inputs map to the same output, so "undoing" it doesn't give you back a single unique value — you get a *set* of possible inputs (the **preimage**) instead of one.

### → Solves Q1
`f: R → R, f(x) = x² + 1`. Find `f⁻¹(10)`.

Set `f(x) = 10`: `x² + 1 = 10 → x² = 9 → x = ±3`.

**Important subtlety:** `f(x) = x²+1` is NOT injective on all of R (e.g., f(3) = f(-3) = 10), so strictly speaking f doesn't have a true inverse *function* here. What you're really finding is the **preimage** of 10: `f⁻¹(10) = {-3, 3}`.

Most intro courses are loose with notation and just want you to solve `f(x) = 10` and report the value(s) — so practically, the expected answer is **x = ±3** (often written as just 3, if the course is implicitly assuming a restricted/positive domain — check what your professor expects, but mathematically both roots are valid preimages).

---

## PART 5: A GENERAL "IS THIS RELATION A TOTAL ORDER" TRICK — Q7

Q7 defines: for distinct subsets U, V of S (|S| = 2024), `U < V` if the **minimum element of the symmetric difference `U Δ V`** belongs to U.

You don't need to hand-simulate every subset. The key insight:

**This relation is a strict total order on the power set of S.** (You can verify: it's well-defined for every pair of distinct subsets since `UΔV` is never empty when U≠V, and one can show it's transitive and every pair is comparable.)

**The theorem that solves it instantly:** *Any total order on a finite set has a unique maximum element and a unique minimum element.* Power set of a 2024-element set is huge but still **finite** (2^2024 subsets) — so both must exist.

- S1 ("a subset larger than every other") = existence of a maximum → **True**.
- S2 ("a subset smaller than every other") = existence of a minimum → **True**.

**Answer: A — Both S1 and S2 are true.**

*(For the curious: working small cases like S={1,2} shows the full set S ends up as the minimum and the empty set `{}` as the maximum under this particular rule — but you don't need that to answer the question, the finite-total-order argument alone is airtight and fast in an exam.)*

---

## PART 6: REFLEXIVE ∩ ASYMMETRIC — Q8

Two facts to combine:
1. **R reflexive** → R contains **all** n diagonal pairs `(a,a)`.
2. **A asymmetric** → A contains **zero** diagonal pairs. (Proof: if `(a,a) ∈ A`, asymmetry demands `(a,a) ∉ A` — a direct contradiction. So asymmetric relations are automatically irreflexive.)

So on the diagonal, R and A have *nothing* in common — R∩A can never include any `(a,a)` pair.

**Honest caveat for you:** knowing only "R is reflexive" and "A is asymmetric" tells you the diagonal contributes 0 to the intersection, but it does **not** by itself fix the total cardinality of `A ∩ R`, because R could contain extra off-diagonal pairs that A also happens to contain. If your course/answer key expects a single number here, they're almost certainly assuming R is taken as just the diagonal (identity) relation, in which case `A ∩ R = 0`. Worth double-checking this one against your professor's intended reading — the reasoning above (why the diagonal is excluded) is the part that's solid regardless.

---

## PART 7: PROPOSITIONAL LOGIC — Converse / Inverse / Contrapositive & Tautologies

For a conditional `p → q`:

| Name | Form | Relationship |
|---|---|---|
| Original | `p → q` | — |
| **Converse** | `q → p` | swap |
| **Inverse** | `¬p → ¬q` | negate both |
| **Contrapositive** | `¬q → ¬p` | swap AND negate |

**Golden rule:** a statement is always logically equivalent to its **contrapositive** (this is the one guaranteed equivalence). Converse and Inverse are equivalent *to each other* (each is the contrapositive of the other) but generally **not** equivalent to the original.

### → Solves Q10
`(¬p) → (¬q)` is the **Inverse** of `p → q`. Inverse ≡ Converse.

**Answer: B — q → p.**

### Tautology
A **tautology** is a statement that's true under *every* possible truth assignment. To disprove one, you just need **one** counterexample assignment that makes it false.

### → Solves Q9
Check option B: `(a ↔ c) → (¬b → (a ∧ c))`.

Try `a = F, b = F, c = F`:
- `a ↔ c` = F↔F = **True**
- `¬b` = **True**
- `a ∧ c` = F∧F = **False**
- `¬b → (a∧c)` = True → False = **False**
- Whole statement: True → False = **False**

Found a counterexample → **not a tautology**.

(Quick sanity check on the others: A is the classic hypothetical syllogism, C simplifies to "if a∧b∧c then c∨a" which is trivially always true, D is `a → (b → a)` — always true since if a is true the conclusion is automatically true, and if a is false the whole implication is vacuously true. All three check out as tautologies.)

**Answer: B is the one that is NOT a tautology.**

---

## Quick-reference cheat sheet

- `|P(S)| = 2^n`
- Total relations on n elements: `2^(n²)`
- Reflexive: `2^(n²-n)` | Symmetric: `2^(n(n+1)/2)` | Reflexive+Symmetric: `2^(n(n-1)/2)`
- Equivalence = Reflexive + Symmetric + Transitive
- Partial order = Reflexive + Antisymmetric + Transitive
- Asymmetric ⇒ automatically Irreflexive
- Inverse function exists only for bijections
- Contrapositive ≡ Original always; Converse ≡ Inverse always (but not ≡ Original in general)
- Finite total order ⇒ guaranteed unique max and min element
