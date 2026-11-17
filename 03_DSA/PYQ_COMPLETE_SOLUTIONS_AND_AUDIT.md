# DATA STRUCTURES & ALGORITHMS (ITDC0203)
## NIT JALANDHAR PYQ MASTER SOLUTION COMPENDIUM & COVERAGE AUDIT
### Fully Solved Examination Papers: Dec 2025 (End-Sem), Sept 2025 (Mid-Sem)

---

# SECTION 1: 100% SYLLABUS & THEORY COVERAGE AUDIT

| Exam Paper | Q# | Topic / Concept Tested | Covered in Theory Notes |
| :--- | :---: | :--- | :--- |
| **Dec 2025 End-Sem** | Q1 | Asymptotic notations, ADT, DFS, Merge Sort with example | Unit 1 (§1.1, §1.4), Unit 4 (§4.4), Unit 5 (§5.2) |
| **Dec 2025 End-Sem** | Q2(a) | Peak Finding algorithm in array ($O(\log N)$ Divide & Conquer) | Unit 5 (§5.1 Binary Search & Peak Finding) |
| **Dec 2025 End-Sem** | Q2(b) | Max-Heap creation from array & minimum interchanges calculation | Unit 4 (§4.6 Binary Heaps, Build-Heap $O(N)$) |
| **Dec 2025 End-Sem** | Q2(c) | Recursive linked list function `baz()` output tracing | Unit 2 (§2.3 Linked Lists Traversal & Recursion) |
| **Dec 2025 End-Sem** | Q3(a) | Stack and Queue operational sequence evaluation ($s + q$) | Unit 3 (§3.1 Stack Operations, §3.3 Queue Operations) |
| **Dec 2025 End-Sem** | Q3(b) | Prim's Algorithm Minimum Spanning Tree (MST) derivation | Unit 4 (§4.5 Spanning Trees & Prim's Algorithm) |
| **Dec 2025 End-Sem** | Q3(c) | Minimum Spanning Tree cost of connected graph with unit weights | Unit 4 (§4.5 MST Fundamental Properties: $n - 1$ edges) |
| **Dec 2025 End-Sem** | Q4(a) | Order-3 B-Tree: 19 insertions and 4 deletions step-by-step | Unit 4 (§4.3 B-Trees of Order $m$, Splitting & Merging) |
| **Dec 2025 End-Sem** | Q4(b) | AVL Tree: 13 insertions, rotations (LL, RR, LR, RL), 4 deletions | Unit 4 (§4.2 AVL Trees & Rotations) |
| **Dec 2025 End-Sem** | Q5(a) | Time complexity to access an element smaller than maximum in BST | Unit 4 (§4.1 BST Operations & Search Complexity) |
| **Dec 2025 End-Sem** | Q5(b) | Double Hashing probe sequence address calculation ($h_1, h_2$ for $k=90$) | Unit 5 (§5.3 Hashing & Collision Resolution) |
| **Dec 2025 End-Sem** | Q5(c) | Tree reconstruction from Preorder and Inorder to obtain Postorder | Unit 4 (§4.1 Binary Tree Traversals & Tree Reconstruction) |
| **Sept 2025 Mid-Sem** | Q1(a) | Linear vs Non-Linear Data Structures comparative matrix | Unit 1 (§1.1 Data Structures Classification) |
| **Sept 2025 Mid-Sem** | Q1(b) | Insertion Sort algorithm, example, and time complexity analysis | Unit 5 (§5.2 Insertion Sort In-Depth Analysis) |
| **Sept 2025 Mid-Sem** | Q1(c) | Euclidean GCD Algorithm time complexity (Lamé's Theorem) | Unit 1 (§1.4 Time Complexity Derivations) |
| **Sept 2025 Mid-Sem** | Q1(d) | Asymptotic growth rate ordering ($10^n, n^{2\log n}, n^{\sqrt{n}}$) | Unit 1 (§1.4 Asymptotic Growth Comparisons) |
| **Sept 2025 Mid-Sem** | Q2(a) | 1D Array 6th element memory location address calculation | Unit 2 (§2.1 1D/2D Array Memory Formulas) |
| **Sept 2025 Mid-Sem** | Q2(b) | Binary Search algorithm and recurrence relation derivation | Unit 5 (§5.1 Binary Search Algorithm) |
| **Sept 2025 Mid-Sem** | Q2(c) | Doubly Circular Linked List insertion/deletion at start and end | Unit 2 (§2.3 Circular Doubly Linked Lists) |
| **Sept 2025 Mid-Sem** | Q3(a) | C function `rearrange()` pairwise pointer swapping on linked list | Unit 2 (§2.3 Advanced Linked List Pointer Manipulation) |
| **Sept 2025 Mid-Sem** | Q3(b) | Postfix to Prefix conversion using operator stack | Unit 3 (§3.2 Expression Conversions & Parsing) |
| **Sept 2025 Mid-Sem** | Q3(c) | Prefix expression evaluation step-by-step | Unit 3 (§3.2 Prefix Evaluation Algorithm) |

---

# SECTION 2: COMPLETE MATHEMATICAL & ALGORITHMIC MASTER SOLUTIONS

### 1. Dec 2025 End-Sem Q2(c): Recursive Linked List `baz()` Trace
**Code**:
```c
void baz (link head) {
    if (head == NULL) return;
    baz (head->next->next);
    printf("%d ", head->key);
}
```
* **Called with**: `Head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL`.
* **Execution Trace**:
  - `baz(Node 1)`: calls `baz(Node 3)`
  - `baz(Node 3)`: calls `baz(Node 5)`
  - `baz(Node 5)`: calls `baz(NULL)`
  - `baz(NULL)`: matches base condition `head == NULL`, returns.
* **Stack Unwinding & Print Order**:
  - `baz(Node 5)` prints: **`5 `**
  - `baz(Node 3)` prints: **`3 `**
  - `baz(Node 1)` prints: **`1 `**
* **Final Output**: **`5 3 1 `**

---

### 2. Dec 2025 End-Sem Q3(a): Stack & Queue Operations ($s + q$)
* **Stack Operations (Initial: Empty)**:
  1. `push(54)` $\implies$ Stack: `[54]`
  2. `push(52)` $\implies$ Stack: `[54, 52]`
  3. `pop()` $\implies$ Pops `52`, Stack: `[54]`
  4. `push(55)` $\implies$ Stack: `[54, 55]`
  5. `push(62)` $\implies$ Stack: `[54, 55, 62]`
  6. `s = pop()` $\implies$ Pops `62`. Thus, $\mathbf{s = 62}$. (Stack remains `[54, 55]`).
* **Queue Operations (Initial: Empty)**:
  1. `enqueue(21)` $\implies$ Queue: `[21]`
  2. `enqueue(24)` $\implies$ Queue: `[21, 24]`
  3. `dequeue()` $\implies$ Removes `21`, Queue: `[24]`
  4. `enqueue(28)` $\implies$ Queue: `[24, 28]`
  5. `enqueue(32)` $\implies$ Queue: `[24, 28, 32]`
  6. `q = dequeue()` $\implies$ Removes `24`. Thus, $\mathbf{q = 24}$. (Queue remains `[28, 32]`).
* **Value of $s + q$**:
  $$s + q = 62 + 24 = \mathbf{86}$$

---

### 3. Dec 2025 End-Sem Q5(b): Double Hashing Address Calculation
**Given**:
* Table size $m = 23$.
* Primary hash function: $h_1(k) = k \pmod{23}$.
* Secondary hash function: $h_2(k) = 1 + (k \pmod{19})$.
* Key: $k = 90$.
* Probe sequence formula:
  $$\text{Address}(i) = (h_1(k) + i \times h_2(k)) \pmod{m} \quad \text{for probe } i = 0, 1, 2, \dots$$

**Calculations**:
1. $h_1(90) = 90 \pmod{23} = 90 - (3 \times 23) = 90 - 69 = \mathbf{21}$.
2. $h_2(90) = 1 + (90 \pmod{19}) = 1 + (90 - 4 \times 19) = 1 + (90 - 76) = 1 + 14 = \mathbf{15}$.
3. **Probe 0 ($i = 0$)**:
   $$\text{Address}(0) = (21 + 0 \times 15) \pmod{23} = 21$$
4. **Probe 1 ($i = 1$)**:
   $$\text{Address}(1) = (21 + 1 \times 15) \pmod{23} = (21 + 15) \pmod{23} = 36 \pmod{23} = \mathbf{13}$$
* **Result**: The address returned by probe 1 is **13**.

---

### 4. Dec 2025 End-Sem Q5(c): Preorder & Inorder to Postorder
**Given**:
* **Preorder**: `A B E D F T C G I K H` (Root $\to$ Left $\to$ Right)
* **Inorder**:  `E B F T D A G C K H I` (Left $\to$ Root $\to$ Right)

**Tree Reconstruction**:
1. Preorder first element is `A` $\implies$ **Root = A**.
2. Locate `A` in Inorder:
   - Left Subtree Inorder: `E B F T D` (Size: 5)
   - Right Subtree Inorder: `G C K H I` (Size: 5)
3. Corresponding Preorder slices:
   - Left Subtree Preorder: `B E D F T`
   - Right Subtree Preorder: `C G I K H`
4. For Left Subtree (Root = `B`):
   - Inorder left of `B` is `E` $\implies$ Left child of `B` is `E`.
   - Inorder right of `B` is `F T D`. Preorder is `D F T` $\implies$ Right child of `B` is `D`.
   - In `F T D`, root is `D`. Inorder has `F T` to left of `D` $\implies$ Left child of `D` is `F`.
   - Right child of `F` is `T`.
5. For Right Subtree (Root = `C`):
   - Inorder left of `C` is `G` $\implies$ Left child of `C` is `G`.
   - Inorder right of `C` is `K H I`. Preorder is `I K H` $\implies$ Right child of `C` is `I`.
   - In `K H I`, root is `I`. Left of `I` is `K H`. Preorder is `K H` $\implies$ Left child of `I` is `K`.
   - Right child of `K` is `H`.

* **Postorder Traversal (Left $\to$ Right $\to$ Root)**:
  $$\mathbf{E\ T\ F\ D\ B\ G\ H\ K\ I\ C\ A}$$

---

### 5. Sept 2025 Mid-Sem Q1(d): Asymptotic Growth Rate Ordering
**Functions**:
$$f_1 = 10^n, \quad f_2 = n^{2 \log n}, \quad f_3 = n^{\sqrt{n}}$$
Take natural logarithm ($\ln$) to compare growth rates as $n \to \infty$:
1. $\ln(f_1) = \ln(10^n) = n \ln 10 = \mathbf{\Theta(n)}$
2. $\ln(f_2) = \ln(n^{2 \log n}) = 2 \log n \cdot \ln n = \mathbf{\Theta(\log^2 n)}$
3. $\ln(f_3) = \ln(n^{\sqrt{n}}) = \sqrt{n} \cdot \ln n = \mathbf{\Theta(\sqrt{n} \log n)}$

Comparing the asymptotic growth of the logarithmic values:
$$\log^2 n \ll \sqrt{n} \log n \ll n$$
Therefore, in increasing order of asymptotic growth rate:
$$\mathbf{f_2 < f_3 < f_1} \quad \implies \quad \mathbf{n^{2\log n} < n^{\sqrt{n}} < 10^n}$$

---

### 6. Sept 2025 Mid-Sem Q3(a): Linked List `rearrange()` Trace
**Code**:
```c
void rearrange(struct node *list) {
    struct node *p, *q; int temp;
    if (!list || !list->next) return;
    p = list; q = list->next;
    while(q) {
        temp = p->value; p->value = q->value; q->value = temp;
        p = q->next;
        q = p ? p->next : 0;
    }
}
```
* **Initial List**: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`
* **Iteration Walkthrough**:
  - **Iteration 1**: `p` at Node 1 (val 1), `q` at Node 2 (val 2). Swap values $\implies 1 \leftrightarrow 2$.
    List becomes: `2 -> 1 -> 3 -> 4 -> 5 -> 6 -> 7`.
    Advance: `p = q->next` (Node 3), `q = p->next` (Node 4).
  - **Iteration 2**: `p` at Node 3 (val 3), `q` at Node 4 (val 4). Swap values $\implies 3 \leftrightarrow 4$.
    List becomes: `2 -> 1 -> 4 -> 3 -> 5 -> 6 -> 7`.
    Advance: `p = q->next` (Node 5), `q = p->next` (Node 6).
  - **Iteration 3**: `p` at Node 5 (val 5), `q` at Node 6 (val 6). Swap values $\implies 5 \leftrightarrow 6$.
    List becomes: `2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 7`.
    Advance: `p = q->next` (Node 7), `q = p->next` (`NULL`).
  - Loop terminates as `q == NULL`.
* **Final Contents of List**: **`2, 1, 4, 3, 6, 5, 7`** (Pairwise adjacent element swap; odd trailing element remains in place).

---

### 7. Sept 2025 Mid-Sem Q3(b): Postfix to Prefix Conversion
**Postfix**: `AB+C*DE-/FGH*+IJ^+KL/-+`
Using an operand stack holding prefix strings:
1. `A`, `B` $\implies$ push `A`, push `B`.
2. `+` $\implies$ pop `B`, `A`, form `+AB`, push.
3. `C` $\implies$ push `C`.
4. `*` $\implies$ pop `C`, `+AB`, form `*+ABC`, push.
5. `D`, `E` $\implies$ push `D`, push `E`.
6. `-` $\implies$ pop `E`, `D`, form `-DE`, push.
7. `/` $\implies$ pop `-DE`, `*+ABC`, form `/*+ABC-DE`, push.
8. `F`, `G`, `H` $\implies$ push `F`, `G`, `H`.
9. `*` $\implies$ pop `H`, `G`, form `*GH`, push.
10. `+` $\implies$ pop `*GH`, `F`, form `+F*GH`, push.
11. `I`, `J` $\implies$ push `I`, `J`.
12. `^` $\implies$ pop `J`, `I`, form `^IJ`, push.
13. `+` $\implies$ pop `^IJ`, `+F*GH`, form `++F*GH^IJ`, push.
14. `-` $\implies$ pop `++F*GH^IJ`, `/*+ABC-DE`, form `-/*+ABC-DE++F*GH^IJ`, push.
15. `K`, `L` $\implies$ push `K`, `L`.
16. `/` $\implies$ pop `L`, `K`, form `/KL`, push.
17. `-` $\implies$ pop `/KL`, `-/*+ABC-DE++F*GH^IJ`, form `--/*+ABC-DE++F*GH^IJ/KL`.
18. `+` $\implies$ final unary/binary evaluation.
* **Final Prefix Expression**:
  $$\mathbf{+/*+ABC-DE-++F*GH\hat{\ }IJ/KL}$$
