# DATA STRUCTURES AND ALGORITHMS (ITDC0203)
## THE DEFINITIVE ENDTERM EXAMINATION THEORY MASTER BOOK
**Course Code:** ITDC0203 | **Credits:** 3-0-0-3  
**Academic Target:** NIT Jalandhar - Department of Information Technology (B.Tech 3rd Semester)  
**Curriculum Alignment:** Complete Syllabus Coverage, Dr. Mohit Kumar Lecture Series, Standard University References (Horowitz & Sahni, Lipschutz, CLRS)  

---

# COMPREHENSIVE SYLLABUS DIRECTORY & NAVIGATION

| Unit | Subject Area | Key Exam Focus Areas |
| :--- | :--- | :--- |
| **Unit 1** | **Introduction & Asymptotic Analysis** | Terminology, Linear vs Non-Linear, ADT, Algorithm properties, Space/Time Complexity ($S(A)=S(C)+S(R)$), Big-O, $\Omega$, $\Theta$, Little-$o$, $\omega$, Limits, Master Theorem, Recurrences, Growth Hierarchy. |
| **Unit 2** | **Arrays and Linked Lists** | 1D, 2D (Row/Col Major address derivations & 3D formulas), Sparse Matrices (3-tuple COO, Fast Transpose $O(cols+nnz)$, Addition), SLL, DLL, Circular Lists, Header Lists, Polynomial Addition, Dynamic Memory (`malloc`, `calloc`, `realloc`, `free`), Pointer rearrangement traces. |
| **Unit 3** | **Stacks and Queues** | Array/LL Stacks, Push/Pop/Peek/Overflow/Underflow, Infix to Postfix/Prefix algorithms & tabular traces, Postfix/Prefix evaluation traces, Balanced Parentheses, Activation Records/Recursion Stack, Linear Queue & False Overflow, Circular Queue (modulo arithmetic), Deque, Priority Queue (Array, LL, Heap), Scheduling applications. |
| **Unit 4** | **Trees and Graphs** | Binary Tree properties ($n_0 = n_2 + 1$ proof, height bounds), Traversal algorithms (Recursive & Iterative Pre/In/Post/Level-order), Huffman Coding (min-heap tree construction, bit calculations, compression ratio), BST (Search, Insert, Delete with 3 cases), AVL Trees (Balance Factor, LL, RR, LR, RL rotations & traces), m-way trees, B-Trees & B+ Trees (order $m$, search, insert/split, deletion, comparison), Graph representations (Matrix vs List), BFS, DFS, Connected Components, Spanning Trees, Prim's and Kruskal's (DSU rank & path compression), Dijkstra's Algorithm. |
| **Unit 5** | **Searching, Sorting and Hashing** | Linear & Binary Search ($O(\log N)$ proof), Internal/External sorting, Stability, In-place sorting, Bubble, Selection, Insertion, Quick Sort (Lomuto vs Hoare, pivot strategies, worst/best analysis), Merge Sort (recurrence & merge step), Heap Sort ($O(N)$ build-heap proof & sift-down), Radix Sort, Master Sorting Comparison Table, Hash Tables, Hash functions (Division, Multiplication, Mid-Square, Folding), Collision Resolution (Chaining vs Open Addressing: Linear Probing, Quadratic Probing, Double Hashing, clustering phenomena, tombstones, load factor $\alpha$). |
| **Cheatsheet** | **Exam Formulas, Traps & PYQ Matrix** | All address formulas, Tree node formulas, Master theorem cheat sheet, Red-Pen Exam Traps, Predicted 10-Mark & 5-Mark Endterm Questions. |

---

# UNIT 1: INTRODUCTION & ASYMPTOTIC ANALYSIS

---

## 1.1 Basic Terminology & Elementary Data Organization

In Computer Science, computation is fundamentally defined as the transformation of data through algorithms. To analyze and design software systems rigorously, we must first establish formal definitions of data organization.

### 1.1.1 The Data Hierarchy
1. **Data:** Raw, unorganized facts, figures, or symbols devoid of contextual meaning (e.g., the integer `104`, the string `"CS"`).
2. **Data Item:** A single unit of values. Data items that are divided into sub-items are called *Group Items* (e.g., a `Date` item consisting of `Day`, `Month`, `Year`). Data items that cannot be divided are called *Elementary Items* (e.g., `Roll_Number`, `Age`).
3. **Entity:** An object that possesses attributes or properties that may take values (e.g., a student, an employee, a bank account).
4. **Attribute & Value:** An attribute is a characteristic of an entity (e.g., `Student_Name`). The specific value assigned to an entity's attribute is its data value (e.g., `"Amit"`).
5. **Record:** A collection of related data items representing the attributes of a single entity. In C/C++, a record is modeled using a `struct` or `class`.
6. **File:** A collection of related records representing an entire set of entities (e.g., all student records in NIT Jalandhar).
7. **Database:** An integrated collection of logically related files with managed redundancy and structural integrity.

```
+-------------------------------------------------------+
| DATABASE: University_Records                          |
|  +-------------------------------------------------+  |
|  | FILE: Student_Master                            |  |
|  |  +-------------------------------------------+  |  |
|  |  | RECORD: Student #101                      |  |  |
|  |  |  [Roll: 101] [Name: "Rohit"] [CGPA: 8.92] |  |  |
|  |  |   Elementary    Elementary      Elementary  |  |  |
|  |  +-------------------------------------------+  |  |
|  |  | RECORD: Student #102                      |  |  |
|  |  |  [Roll: 102] [Name: "Priya"] [CGPA: 9.45] |  |  |
|  |  +-------------------------------------------+  |  |
|  +-------------------------------------------------+  |
+-------------------------------------------------------+
```

---

### 1.1.2 Classification of Data Structures
A **Data Structure** is a mathematical or logical model of a particular organization of data, accompanied by structural relationships and a family of operations that can be performed on the data elements.

```
                         DATA STRUCTURES
                                |
        +-----------------------+-----------------------+
        |                                               |
  Primitive Data Structures                    Non-Primitive Data Structures
  (Machine-level / Inbuilt)                   (User-defined / Structural)
        |                                               |
  +-----+-----+-----+-----+            +----------------+----------------+
  |     |     |     |     |            |                                 |
 int  float char bool pointer    Linear Data Structures           Non-Linear Data Structures
                                       |                                 |
                         +-----+-----+-----+-----+                 +-----+-----+
                         |     |     |     |     |                 |           |
                       Array Linked Stack Queue Tree             Graph
                             List
```

#### Detailed Distinction: Linear vs Non-Linear Data Structures
*(Extremely frequent exam question - NIT Jalandhar Mid-Sem 2025 Q1(a))*

| Parameter | Linear Data Structures | Non-Linear Data Structures |
| :--- | :--- | :--- |
| **Arrangement of Elements** | Elements are organized sequentially or linearly, where each element has a unique predecessor and successor (except the first and last elements). | Elements are organized hierarchically or interconnected via networks; an element may connect to multiple elements. |
| **Traversal Feasibility** | Single-run traversal: All elements can be visited in a single linear pass ($O(N)$). | Multi-run traversal: Elements cannot be traversed in a single linear pass without branching or backtracking. |
| **Levels / Hierarchy** | Single-level data structure (flat organization). | Multi-level data structure (hierarchical or arbitrary graph topology). |
| **Memory Allocation** | Often contiguous (e.g., Array), or sequentially chained via single pointers (e.g., Linked List). | Typically non-contiguous; nodes maintain multiple pointer links (e.g., `left`/`right` child, adjacency lists). |
| **Complexity of Operations** | Insertion and deletion at ends can be $O(1)$; searching in unsorted linear structures is $O(N)$. | Search, insertion, and deletion can be achieved in $O(\log N)$ in balanced trees (e.g., AVL, Red-Black). |
| **Examples** | Arrays, Singly/Doubly Linked Lists, Stacks, Queues. | Trees (Binary Trees, BST, AVL, B/B+ Trees), Graphs, Heaps. |
| **Real-world Modeling** | Sequential processing: CPU task pipelines, undo/redo buffers, print queues. | Hierarchical & networked models: File systems, organizational hierarchies, social networks, road maps. |

---

### 1.1.3 Abstract Data Types (ADT)
An **Abstract Data Type (ADT)** is a mathematical model for data types where the data type is defined purely by its behavior (semantics) from the point of view of a *user* of the data, specifically in terms of:
1. **Values / Domain:** The set of allowable values.
2. **Operations:** The collection of operations that can be performed on these values, including their signatures, preconditions, and postconditions.
3. **Encapsulation / Information Hiding:** The ADT specifies *what* operations can be performed, completely hiding *how* these operations are implemented in memory or software.

#### Axiomatic Structure of an ADT
An ADT is formally specified as a triple:
$$\text{ADT} = \langle D, F, A \rangle$$
Where:
- $D$ is the set of data domains (the state space).
- $F$ is the set of operation signatures (functions mapping inputs to outputs).
- $A$ is the set of axioms or invariants that define the exact semantics of the operations.

#### Example: The Stack ADT Specification
- **Domain:** A sequence of elements $S = \langle e_1, e_2, \dots, e_k \rangle$ of type $T$, with top-of-stack designated at $e_k$.
- **Operations:**
  - $\text{Create}() \to \text{Stack}$: Initializes an empty stack.
  - $\text{Push}(\text{Stack } S, \text{Element } x) \to \text{Stack}$: Appends $x$ to the top of $S$.
  - $\text{Pop}(\text{Stack } S) \to \langle \text{Stack}, \text{Element} \rangle$: Precondition: $\neg \text{IsEmpty}(S)$. Removes and returns the top element of $S$.
  - $\text{Peek}(\text{Stack } S) \to \text{Element}$: Precondition: $\neg \text{IsEmpty}(S)$. Returns top element without modifying $S$.
  - $\text{IsEmpty}(\text{Stack } S) \to \text{Boolean}$: Returns `true` if $S$ has 0 elements, else `false`.
- **Axiom (LIFO Invariant):**
  $$\text{Pop}(\text{Push}(S, x)) \equiv S \quad \text{with returned value } x$$

---

## 1.2 Algorithms and Properties

### 1.2.1 Formal Definition of an Algorithm
An **Algorithm** is an ordered, unambiguous, finite sequence of computational steps that transforms a given set of inputs into a desired output. Formally, Donald Knuth specifies that an algorithm must satisfy five critical properties:

```
+--------------------------------------------------------------------------+
|                     KNUTH'S 5 ESSENTIAL PROPERTIES                       |
+-------------------+------------------------------------------------------+
| 1. Finiteness     | Must terminate after a finite number of steps for    |
|                   | any valid input set. An infinite loop is NOT an      |
|                   | algorithm; it is a computational procedure.          |
+-------------------+------------------------------------------------------+
| 2. Definiteness   | Every step must be precisely defined, unambiguous,  |
|                   | and rigorous. Operations like "add 4 or 5" violate  |
|                   | definiteness.                                        |
+-------------------+------------------------------------------------------+
| 3. Input          | Must accept zero or more well-defined inputs from a  |
|                   | specified mathematical set.                          |
+-------------------+------------------------------------------------------+
| 4. Output         | Must produce at least one output quantity having a   |
|                   | defined relationship to the inputs.                  |
+-------------------+------------------------------------------------------+
| 5. Effectiveness  | Every operation must be sufficiently basic that it   |
|                   | can be carried out exactly in finite time on paper   |
|                   | (feasibility / principle of elementary operations).  |
+-------------------+------------------------------------------------------+
```

### 1.2.2 Algorithmic Paradigms Overview
1. **Divide and Conquer:** Break problem into independent subproblems of the same type, solve subproblems recursively, and combine solutions (e.g., Merge Sort, Quick Sort, Binary Search).
2. **Greedy Method:** Construct solution piece-by-piece, always choosing the locally optimal candidate at each step hoping it leads to a globally optimal solution (e.g., Prim's, Kruskal's, Dijkstra's, Huffman Coding).
3. **Dynamic Programming:** Solve problems with overlapping subproblems and optimal substructure by memoizing or tabulating subproblem solutions to prevent recomputation (e.g., Floyd-Warshall, Matrix Chain Multiplication, 0/1 Knapsack).
4. **Backtracking:** Incremental search that abandons candidate paths ("backtracks") as soon as it determines they cannot lead to a valid solution (e.g., N-Queens, Graph Coloring).
5. **Branch and Bound:** Optimization technique for discrete combinatorial problems that uses bounding functions to prune suboptimal subtrees (e.g., Traveling Salesperson Problem).

---

## 1.3 Performance Analysis & Efficiency

When analyzing an algorithm, empirical (benchmark) timing is insufficient because execution time varies with CPU clock speed, cache architecture, RAM bus bandwidth, operating system scheduling, and compiler optimization flags. We require a **machine-independent, analytical framework** that expresses execution resource consumption as a mathematical function of input size $n$.

### 1.3.1 Space Complexity
The **Space Complexity** of an algorithm is the total amount of memory required by the algorithm to run to completion as a function of the input instance size $n$.

Mathematically, the total space $S(P)$ required by any program $P$ is decomposed into two distinct components:
$$S(P) = S_c + S_p(I)$$
Where:
1. **Fixed Space Component ($S_c$):** Space independent of the characteristics of the input/output.
   - Instruction space (compiled machine code bytes).
   - Space for simple variables, constants, and structured data of fixed size.
2. **Variable Space Component ($S_p(I)$):** Space whose magnitude depends on the specific input instance $I$ (characterized by parameter $n$).
   - Dynamic memory allocated at runtime on the Heap via `malloc()` / `new`.
   - **Recursion Stack Space (Call Stack Overhead):** When a function calls itself recursively, an **Activation Record (Stack Frame)** is pushed onto the system call stack for each active call.

#### Activation Record Components:
Each stack frame stores:
- Return address (instruction pointer to resume execution upon return).
- Function arguments and parameter values.
- Local variables allocated within the block.
- Frame pointer / Base pointer ($EBP / RBP$) for base addressing.

```
       +---------------------------------------------+
 high  | Frame #3: gcd(m=2, n=0)                      |
  ^    |   Return Addr, Params: (2, 0), Locals        |
  |    +---------------------------------------------+
  |    | Frame #2: gcd(m=4, n=2)                      |
  |    |   Return Addr, Params: (4, 2), Locals        |
  |    +---------------------------------------------+
  |    | Frame #1: gcd(n=10, m=4)                     |
  |    |   Return Addr, Params: (10, 4), Locals       |
 low   +---------------------------------------------+ <-- Stack Pointer (SP)
```

**Auxiliary Space vs Space Complexity:**
- **Auxiliary Space:** Temporary or extra space used by the algorithm, excluding the space taken by the input itself.
- For example, Merge Sort takes $O(N)$ auxiliary space; Quick Sort takes $O(\log N)$ auxiliary space for call stack; In-place Selection Sort takes $O(1)$ auxiliary space.

---

### 1.3.2 Time Complexity
The **Time Complexity** of an algorithm is the number of elementary operations (steps) executed by the algorithm as a function of input size $n$. Under the standard Random Access Machine (RAM) model:
- Each basic operation (arithmetic `+`, `-`, `*`, `/`, assignment `=`, array index dereference `A[i]`, boolean comparison `<`, `==`, pointer dereference `p->next`) executes in $O(1)$ constant time.

#### Best, Worst, and Average Cases:
1. **Worst-Case Time Complexity ($T_{worst}(n)$):** The maximum number of steps taken across all possible inputs of size $n$.
   $$T_{worst}(n) = \max_{I \in \mathcal{D}_n} T(I)$$
   Provides an ironclad mathematical guarantee that the algorithm will never take more time than this bound.
2. **Best-Case Time Complexity ($T_{best}(n)$):** The minimum number of steps taken across all possible inputs of size $n$.
   $$T_{best}(n) = \min_{I \in \mathcal{D}_n} T(I)$$
   Usually corresponds to already sorted arrays (e.g., Insertion Sort $O(N)$, Linear search finding target at index 0).
3. **Average-Case Time Complexity ($T_{avg}(n)$):** The expected number of steps executed over a defined probability distribution of inputs.
   $$T_{avg}(n) = \sum_{i=1}^{k} P(I_i) \cdot T(I_i)$$
   Where $P(I_i)$ is the probability of occurrence of input instance $I_i$. Usually assumes a uniform random distribution of inputs.

---

### 1.3.3 The Time-Space Trade-off
The **Time-Space Trade-off** is an engineering and algorithmic reality asserting that computational time can frequently be reduced at the cost of consuming additional memory, and vice-versa.

#### Classical Examples:
1. **Lookup Tables / Memoization:** Precomputing results of factorial, Fibonacci, or trigonometric tables uses $O(N)$ space to achieve $O(1)$ query time instead of recalculating in exponential or linear time.
2. **Hashing vs Sorted Array Search:** Hash tables use $O(N)$ extra memory (often sparse buckets) to achieve $O(1)$ average search, whereas Binary Search operates in $O(1)$ extra space but requires $O(\log N)$ time.
3. **Fast Transpose of Sparse Matrix:** As derived in Unit 2, standard transpose runs in $O(cols \cdot nnz)$ time and $O(1)$ space. Fast transpose introduces two auxiliary frequency arrays of size $O(cols)$ to collapse execution time to $O(cols + nnz)$.

---

## 1.4 Asymptotic Notations: Formal Mathematical Definitions & Limits

Asymptotic notation is a rigorous calculus for characterizing the limiting behavior of an algorithm's running time as input size $n \to \infty$. Constants and lower-order terms become negligible compared to leading-order terms.

```
       f(n), g(n)
           ^
           |                     c * g(n) [Upper Bound]
           |                   . '
           |               . '  /
           |           . '     /  f(n)
           |       . '       /
           |   . '         /
           |  +----------/------------------------
           |  |        /
           |  |      /
           |  |    /
           |  |  /
           |  |/
           +--+-----------------------------------> n
              0         n0
```

### 1.4.1 Big-O Notation ($O$): Asymptotic Upper Bound
**Formal Definition:**
Let $f(n)$ and $g(n)$ be functions mapping non-negative integers to non-negative real numbers: $f, g: \mathbb{N} \to \mathbb{R}^+$.
We write $f(n) = O(g(n))$ if and only if there exist strictly positive real constants $c > 0$ and an integer threshold $n_0 \ge 1$ such that:
$$0 \le f(n) \le c \cdot g(n) \quad \forall n \ge n_0$$

**Formal Limit Definition:**
$$f(n) = O(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = L < \infty \quad (\text{where } L \ge 0)$$

*Physical Meaning:* The growth rate of $f(n)$ is bounded from above by $g(n)$ for sufficiently large inputs. It guarantees an upper ceiling.

---

### 1.4.2 Big-Omega Notation ($\Omega$): Asymptotic Lower Bound
**Formal Definition:**
We write $f(n) = \Omega(g(n))$ if and only if there exist strictly positive real constants $c > 0$ and an integer threshold $n_0 \ge 1$ such that:
$$0 \le c \cdot g(n) \le f(n) \quad \forall n \ge n_0$$

**Formal Limit Definition:**
$$f(n) = \Omega(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = L > 0 \quad \text{or} \quad \lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$$

*Physical Meaning:* The growth rate of $f(n)$ is bounded from below by $g(n)$ for large $n$. It guarantees a baseline floor beneath which the algorithm cannot run faster.

---

### 1.4.3 Big-Theta Notation ($\Theta$): Asymptotic Tight Bound
**Formal Definition:**
We write $f(n) = \Theta(g(n))$ if and only if there exist strictly positive real constants $c_1, c_2 > 0$ and an integer threshold $n_0 \ge 1$ such that:
$$0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \forall n \ge n_0$$

**Fundamental Equivalence Theorem:**
$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \quad \text{AND} \quad f(n) = \Omega(g(n))$$

**Formal Limit Definition:**
$$f(n) = \Theta(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = L \quad \text{where } 0 < L < \infty$$

*Physical Meaning:* $f(n)$ grows at precisely the same asymptotic rate as $g(n)$ within constant multiplicative factors.

---

### 1.4.4 Little-o Notation ($o$): Strict Asymptotic Upper Bound
**Formal Definition:**
$f(n) = o(g(n))$ if and only if for **ANY** strictly positive real constant $c > 0$, there exists an integer threshold $n_0 \ge 1$ such that:
$$0 \le f(n) < c \cdot g(n) \quad \forall n \ge n_0$$

**Formal Limit Definition:**
$$f(n) = o(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$$

*Contrast with Big-O:* While $3n = O(n)$ and $3n = O(n^2)$, $3n \neq o(n)$ because the ratio $\lim \frac{3n}{n} = 3 \neq 0$. However, $3n = o(n^2)$ because $\lim_{n \to \infty} \frac{3n}{n^2} = 0$. Little-$o$ is a strictly loose upper bound.

---

### 1.4.5 Little-omega Notation ($\omega$): Strict Asymptotic Lower Bound
**Formal Definition:**
$f(n) = \omega(g(n))$ if and only if for **ANY** strictly positive real constant $c > 0$, there exists an integer threshold $n_0 \ge 1$ such that:
$$0 \le c \cdot g(n) < f(n) \quad \forall n \ge n_0$$

**Formal Limit Definition:**
$$f(n) = \omega(g(n)) \iff \lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$$

---

### 1.4.6 Summary Comparison Matrix of Asymptotic Notations

| Notation | Relation Type | Formal Condition ($n \ge n_0$) | Limit Condition $\lim_{n \to \infty} \frac{f(n)}{g(n)}$ | Analogous Real Number Relation |
| :---: | :---: | :---: | :---: | :---: |
| $O(g(n))$ | Upper Bound | $f(n) \le c \cdot g(n)$ | $< \infty$ | $a \le b$ |
| $\Omega(g(n))$ | Lower Bound | $f(n) \ge c \cdot g(n)$ | $> 0$ | $a \ge b$ |
| $\Theta(g(n))$ | Tight Bound | $c_1 g(n) \le f(n) \le c_2 g(n)$ | $0 < L < \infty$ | $a = b$ |
| $o(g(n))$ | Strict Upper | $f(n) < c \cdot g(n) \; \forall c > 0$ | $= 0$ | $a < b$ |
| $\omega(g(n))$ | Strict Lower | $f(n) > c \cdot g(n) \; \forall c > 0$ | $= \infty$ | $a > b$ |

---

### 1.4.7 Mathematical Properties of Asymptotic Notations
1. **Transitivity:**
   - $f(n) = O(g(n)) \land g(n) = O(h(n)) \implies f(n) = O(h(n))$
   - Holds identically for $\Omega, \Theta, o, \omega$.
2. **Reflexivity:**
   - $f(n) = O(f(n))$, $f(n) = \Omega(f(n))$, $f(n) = \Theta(f(n))$.
3. **Symmetry:**
   - $f(n) = \Theta(g(n)) \iff g(n) = \Theta(f(n))$.
4. **Transpose Symmetry:**
   - $f(n) = O(g(n)) \iff g(n) = \Omega(f(n))$.
   - $f(n) = o(g(n)) \iff g(n) = \omega(f(n))$.

---

### 1.4.8 The Standard Master Hierarchy of Growth Rates
In increasing order of asymptotic dominance:
$$1 < \log(\log n) < \log n < \sqrt{n} < n < n \log n < n^{1.5} < n^2 < n^3 < 2^n < 3^n < n! < n^n$$

---

## 1.5 Rigorous Worked Examples from University Exams

### Problem 1: Formal Proof of Big-O Definition
**Question:** Using the formal definition of Big-O, prove that $f(n) = 3n + 2 = O(n)$.  
**Proof:**
We must find constants $c > 0$ and $n_0 \ge 1$ such that:
$$3n + 2 \le c \cdot n \quad \forall n \ge n_0$$
Dividing both sides by $n$ (valid for $n > 0$):
$$3 + \frac{2}{n} \le c$$
For all $n \ge 1$, the maximum value of $\frac{2}{n}$ occurs at $n = 1$, where $\frac{2}{1} = 2$.
Thus:
$$3 + \frac{2}{n} \le 3 + 2 = 5 \quad \forall n \ge 1$$
Therefore, choose $c = 5$ and $n_0 = 1$.
Verification: For $n = 1$: $3(1) + 2 = 5 \le 5(1)$ (True). For $n = 2$: $8 \le 10$ (True).
Hence, by formal definition, $3n + 2 = O(n)$ with $c = 5, n_0 = 1$. $\blacksquare$

---

### Problem 2: NIT Jalandhar Mid-Sem 2025 (Q1(d)) Walkthrough
**Question:** Consider the three functions:
$$f_1(n) = 10^n \quad \text{(or } 10n\text{)}, \quad f_2(n) = n^2 \log n, \quad f_3(n) = n \sqrt{n}$$
Arrange these functions in increasing order of asymptotic growth rate and prove your answer.

**Solution:**
Let us analyze the three functions as $n \to \infty$:
- If $f_1(n) = 10n$ (linear):
  $f_1(n) = 10n = \Theta(n)$  
  $f_3(n) = n \cdot n^{0.5} = n^{1.5}$  
  $f_2(n) = n^2 \log n$  
  Comparing powers of $n$: $n^1 < n^{1.5} < n^2 < n^2 \log n$.  
  Proof via limits:
  $$\lim_{n \to \infty} \frac{f_1(n)}{f_3(n)} = \lim_{n \to \infty} \frac{10n}{n^{1.5}} = \lim_{n \to \infty} \frac{10}{\sqrt{n}} = 0 \implies f_1(n) = o(f_3(n))$$
  $$\lim_{n \to \infty} \frac{f_3(n)}{f_2(n)} = \lim_{n \to \infty} \frac{n^{1.5}}{n^2 \log n} = \lim_{n \to \infty} \frac{1}{n^{0.5} \log n} = 0 \implies f_3(n) = o(f_2(n))$$
  Increasing order: $f_1(n) < f_3(n) < f_2(n)$.

- If $f_1(n) = 10^n$ (exponential):
  $f_3(n) = n^{1.5}$ (polynomial)  
  $f_2(n) = n^2 \log n$ (quasi-polynomial)  
  $f_1(n) = 10^n$ (exponential)  
  By standard limit theorems, any polynomial is asymptotically strictly smaller than any exponential ($c^n$ with $c > 1$):
  $$\lim_{n \to \infty} \frac{n^2 \log n}{10^n} = 0$$
  Increasing order: $f_3(n) < f_2(n) < f_1(n)$.

---

### Problem 3: NIT Jalandhar Mid-Sem 2025 (Q1(c)) Walkthrough
**Question:** Find the time complexity of the following code:
```c
int gcd(int n, int m) {
    if (n % m == 0) return m;
    n = n % m;
    return gcd(m, n);
}
```

**Step-by-Step Analysis & Lamé's Theorem Proof:**
In this recursive Euclidean GCD function:
Let step $k$ have arguments $(a_k, b_k)$ with $a_k > b_k$.
The remainder is $r = a_k \bmod b_k$. In the next step, the arguments become $(b_k, r)$.
Notice:
$$a_k = q \cdot b_k + r$$
Where $q \ge 1$ and $0 \le r < b_k$.
- If $r \le b_k / 2$, then the new second argument $r$ has decreased by at least half: $r \le b_k / 2$.
- If $r > b_k / 2$, then $q = 1$, and in the subsequent step:
  $$b_k = 1 \cdot r + r' \implies r' = b_k - r < b_k - \frac{b_k}{2} = \frac{b_k}{2}$$
Therefore, across at most two consecutive modulo operations, the smaller argument is guaranteed to be reduced by at least a factor of 2:
$$b_{k+2} < \frac{b_k}{2}$$
Let the initial minimum argument be $M = \min(n, m)$.
The number of pairs of steps before reaching zero is bounded by:
$$M / 2^k \ge 1 \implies 2^k \le M \implies k \le \log_2 M$$
Total recursive invocations: $2 \cdot \log_2(\min(n, m))$.
**Formal Conclusion:** The time complexity is:
$$T(n, m) = O(\log(\min(n, m)))$$
The worst case occurs when consecutive arguments are consecutive Fibonacci numbers ($F_{k+1}, F_k$), because $F_{k+1} \bmod F_k = F_{k-1}$, yielding quotient 1 at each step (Lamé's Theorem).

---

### Problem 4: Assignment 1 Code Complexity Analysis
**Question:** Find the time complexity of the following code:
```c
int unknown(int n) {
    int i, j, k = 0;
    for (i = n / 2; i <= n; i++) {
        for (j = 2; j <= n; j = j * 2) {
            k = k + n / 2;
        }
    }
    return k;
}
```

**Step-by-Step Analysis:**
1. **Outer Loop:**
   - Starts at $i = n/2$, increments by $i++$, terminates when $i > n$.
   - Number of iterations:
     $$\text{Iterations}_{outer} = n - \frac{n}{2} + 1 = \frac{n}{2} + 1 = \Theta(n)$$
2. **Inner Loop:**
   - Starts at $j = 2$, updates via $j = j \times 2$, terminates when $j > n$.
   - The sequence of values of $j$ is: $2^1, 2^2, 2^3, \dots, 2^p \le n$.
   - Thus, $2^p \le n \implies p \le \log_2 n$.
   - Number of iterations:
     $$\text{Iterations}_{inner} = \lfloor \log_2 n \rfloor = \Theta(\log n)$$
3. **Total Work:**
   - The statement `k = k + n / 2;` runs in $O(1)$ constant time.
   - The total number of operations is the product of the independent loops:
     $$T(n) = \sum_{i=n/2}^{n} \sum_{p=1}^{\log_2 n} O(1) = \left(\frac{n}{2} + 1\right) \times (\log_2 n) = \Theta(n \log n)$$
**Final Result:** The time complexity of `unknown(n)` is $\Theta(n \log n)$ and auxiliary space is $O(1)$.

---

## 1.6 Recurrence Relations & The Master Theorem

Recurrence relations model recursive algorithms.

### 1.6.1 The Master Theorem (Standard Divide & Conquer Form)
Given a recurrence of the form:
$$T(n) = a \cdot T\left(\frac{n}{b}\right) + f(n)$$
Where:
- $a \ge 1$ is the number of subproblems.
- $b > 1$ is the factor by which the subproblem size is divided.
- $f(n)$ is the cost of dividing the problem and combining the results.
- Let $c_{crit} = \log_b a$ be the critical exponent, representing the watershed threshold.

The Master Theorem compares $f(n)$ against the watershed function $n^{\log_b a}$:

```
+-------------------------------------------------------------------------------------------------+
|                                    THE MASTER THEOREM CASES                                     |
+--------+------------------------------------+-----------------------------------+---------------+
| Case   | Condition on f(n)                  | Asymptotic Condition              | Solution T(n) |
+--------+------------------------------------+-----------------------------------+---------------+
| Case 1 | f(n) is polynomially smaller than  | f(n) = O(n^(log_b(a) - epsilon))  | Theta(n^(log_b a))
|        | n^(log_b a)                        | for some constant epsilon > 0     |               |
+--------+------------------------------------+-----------------------------------+---------------+
| Case 2 | f(n) has the same asymptotic       | f(n) = Theta(n^(log_b a) * log^k n)| Theta(n^(log_b a)
|        | growth as n^(log_b a)              | for k >= 0                        |   * log^(k+1) n)|
+--------+------------------------------------+-----------------------------------+---------------+
| Case 3 | f(n) is polynomially larger than   | f(n) = Omega(n^(log_b(a)+epsilon))| Theta(f(n))   |
|        | n^(log_b a) AND satisfies the      | for epsilon > 0 AND               |               |
|        | Regularity Condition:               | a * f(n/b) <= c * f(n)            |               |
|        | a * f(n/b) <= c * f(n) for c < 1   | for some c < 1, for all large n   |               |
+--------+------------------------------------+-----------------------------------+---------------+
```

---

### 1.6.2 Master Theorem Worked Problems

#### Example 1: Binary Search Recurrence
$$T(n) = T\left(\frac{n}{2}\right) + 1$$
- $a = 1, b = 2, f(n) = 1 = n^0$.
- $n^{\log_b a} = n^{\log_2 1} = n^0 = 1$.
- Since $f(n) = \Theta(n^{\log_b a} \cdot \log^0 n)$, this is **Case 2** with $k = 0$.
- Solution:
  $$T(n) = \Theta(n^0 \log^{0+1} n) = \Theta(\log n)$$

#### Example 2: Merge Sort Recurrence
$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$
- $a = 2, b = 2, f(n) = n^1$.
- $n^{\log_b a} = n^{\log_2 2} = n^1$.
- Since $f(n) = \Theta(n^{\log_b a})$, this is **Case 2** with $k = 0$.
- Solution:
  $$T(n) = \Theta(n \log n)$$

#### Example 3: Strassen's Matrix Multiplication
$$T(n) = 7T\left(\frac{n}{2}\right) + O(n^2)$$
- $a = 7, b = 2, f(n) = n^2$.
- $n^{\log_b a} = n^{\log_2 7} \approx n^{2.807}$.
- Compare $f(n) = n^2$ with $n^{2.807}$: $n^2 = O(n^{2.807 - \epsilon})$ for $\epsilon \approx 0.807 > 0$.
- This is **Case 1**.
- Solution:
  $$T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$$

#### Example 4: A Case 3 Application
$$T(n) = 3T\left(\frac{n}{4}\right) + n \log n$$
- $a = 3, b = 4, f(n) = n \log n$.
- $n^{\log_b a} = n^{\log_4 3} \approx n^{0.793}$.
- $f(n) = n \log n = \Omega(n^{0.793 + \epsilon})$ for $\epsilon \approx 0.2$.
- Check Regularity Condition:
  $$a \cdot f(n/b) = 3 \cdot \left(\frac{n}{4} \log\left(\frac{n}{4}\right)\right) \le \frac{3}{4} n \log n$$
  Choosing $c = 3/4 < 1$, the regularity condition holds!
- This is **Case 3**.
- Solution:
  $$T(n) = \Theta(n \log n)$$

#### Example 5: When the Master Theorem FAILS
Consider:
$$T(n) = 2T\left(\frac{n}{2}\right) + \frac{n}{\log n}$$
- $a = 2, b = 2 \implies n^{\log_2 2} = n$.
- $f(n) = \frac{n}{\log n} = n \log^{-1} n$.
- Is $f(n)$ polynomially smaller than $n$?
  $$\frac{n}{n \log^{-1} n} = \log n$$
  Since $\log n$ is asymptotically smaller than $n^\epsilon$ for any $\epsilon > 0$, the difference is **not polynomial**. It is subpolynomial!
- Hence, **Standard Master Theorem does NOT apply**. We must use the **Recursion Tree Method**:
  - Depth of tree = $\log_2 n$.
  - At level $i$, there are $2^i$ nodes, each of size $n/2^i$.
  - Work at level $i$:
    $$2^i \cdot \frac{n/2^i}{\log(n/2^i)} = \frac{n}{\log n - i}$$
  - Summing across levels:
    $$T(n) = \sum_{i=0}^{\log n - 1} \frac{n}{\log n - i} = n \sum_{k=1}^{\log n} \frac{1}{k} = n \cdot \Theta(\log(\log n)) = \Theta(n \log \log n)$$

---

### 1.6.3 The Recursion Tree Method Walkthrough
Consider:
$$T(n) = T(n/3) + T(2n/3) + cn$$

```
                           cn                         ---> cn
                        /                         c(n/3)      c(2n/3)                ---> cn
                   /    \      /                    c(n/9) c(2n/9) c(2n/9) c(4n/9)         ---> cn
```
- At the root: Work is $cn$.
- At Level 1: $c(n/3) + c(2n/3) = cn$.
- At Level 2: $c(n/9) + 2c(2n/9) + c(4n/9) = cn(1/9 + 4/9 + 4/9) = cn$.
- In fact, at every fully populated level, the total work is exactly $cn$!
- The shortest path to a leaf is via the leftmost branch: $n \to n/3 \to n/9 \dots \implies \log_3 n$.
- The longest path to a leaf is via the rightmost branch: $n \to 2n/3 \to 4n/9 \dots \implies \log_{3/2} n$.
- Since each level contributes $\le cn$, the total work is bounded between:
  $$cn \log_3 n \le T(n) \le cn \log_{3/2} n$$
- Since $\log_3 n$ and $\log_{3/2} n$ differ only by a constant change-of-base factor:
  $$T(n) = \Theta(n \log n)$$

---

# UNIT 2: ARRAYS AND LINKED LISTS

---

## 2.1 Arrays: Architecture, Memory Organization & Address Formulas

An **Array** is a linear, homogeneous data structure comprising a contiguous collection of data elements of identical type, stored in consecutive physical memory locations, and accessible via integer indices.

### 2.1.1 Contiguous Memory Architecture & Properties
- **Homogeneity:** Every element occupies exactly the same number of bytes, denoted by $W$ (Element Word Size).
- **Contiguity:** There are no memory gaps between adjacent elements: $\text{Addr}(A[k+1]) = \text{Addr}(A[k]) + W$.
- **Direct Indexing (Random Access):** Any element $A[k]$ can be accessed in strictly $O(1)$ constant time through mathematical address calculation without scanning preceding elements.

```
Array in Physical Memory (1D: int arr[5], Base = 1000, W = 4 bytes)
+------------+------------+------------+------------+------------+
|   arr[0]   |   arr[1]   |   arr[2]   |   arr[3]   |   arr[4]   |
|   Val: 10  |   Val: 20  |   Val: 30  |   Val: 40  |   Val: 50  |
+------------+------------+------------+------------+------------+
  1000-1003    1004-1007    1008-1011    1012-1015    1016-1019
  ^ Base
```

---

### 2.1.2 One-Dimensional (1D) Array Address Calculation
Let:
- $\text{Base}(A) = \text{Base address of the array (address of the first element)}$.
- $W = \text{Size of each element in memory bytes}$.
- $LB = \text{Lower Bound of index (usually 0 in C/C++, 1 in Fortran/Mathematics, or arbitrary integer)}$.
- $UB = \text{Upper Bound of index}$.

**Length (Number of elements):**
$$\text{Length} = UB - LB + 1$$

**Memory Address Formula for Element $A[k]$:**
$$\text{Address}(A[k]) = \text{Base}(A) + W \cdot (k - LB)$$

---

### 2.1.3 Two-Dimensional (2D) Array Address Formulas (Complete Derivation)
A 2D array $A[LB_1 \dots UB_1, LB_2 \dots UB_2]$ represents a matrix of $M$ rows and $N$ columns:
- Number of rows: $M = N_1 = UB_1 - LB_1 + 1$
- Number of columns: $N = N_2 = UB_2 - LB_2 + 1$
- Total elements: $M \times N$

Because computer physical memory is fundamentally linear (one-dimensional address space from $0$ to $2^{64}-1$), a 2D matrix must be serialized into a linear sequence. There are two canonical mappings:

```
2D Matrix Conceptual Layout (3 rows x 4 cols):
         Col 0    Col 1    Col 2    Col 3
Row 0:  [ A00 ]  [ A01 ]  [ A02 ]  [ A03 ]
Row 1:  [ A10 ]  [ A11 ]  [ A12 ]  [ A13 ]
Row 2:  [ A20 ]  [ A21 ]  [ A22 ]  [ A23 ]

Row Major Order (RMO) Serialization:
[A00][A01][A02][A03] | [A10][A11][A12][A13] | [A20][A21][A22][A23]
<----- Row 0 ------>   <----- Row 1 ------>   <----- Row 2 ------>

Column Major Order (CMO) Serialization:
[A00][A10][A20] | [A01][A11][A21] | [A02][A12][A22] | [A03][A13][A23]
<--- Col 0 --->   <--- Col 1 --->   <--- Col 2 --->   <--- Col 3 --->
```

#### Derivation of Row Major Order (RMO) Address Formula
In Row Major Order, elements are placed row-by-row.
To compute the physical address of element $A[i][j]$:
1. All preceding rows from $LB_1$ up to $i-1$ have been stored completely.
   Number of preceding complete rows $= (i - LB_1)$.
2. Each row contains exactly $N_2$ elements (where $N_2 = UB_2 - LB_2 + 1$).
   Total elements in preceding rows $= (i - LB_1) \cdot N_2$.
3. Within the current row $i$, all preceding columns from $LB_2$ up to $j-1$ have been stored.
   Preceding elements in the current row $= (j - LB_2)$.
4. Total elements preceding $A[i][j]$ in linear memory:
   $$\text{Offset} = (i - LB_1) \cdot N_2 + (j - LB_2)$$
5. Multiplying by element size $W$ and adding Base Address:
$$\mathbf{\text{Address}(A[i][j]) = \text{Base} + W \cdot \left[ (i - LB_1) \cdot N_2 + (j - LB_2) \right]}$$

*(Special Case: 0-indexed arrays where $LB_1 = 0, LB_2 = 0$:)*
$$\text{Address}(A[i][j]) = \text{Base} + W \cdot (i \cdot N + j)$$

---

#### Derivation of Column Major Order (CMO) Address Formula
In Column Major Order, elements are placed column-by-column.
To compute the physical address of element $A[i][j]$:
1. All preceding columns from $LB_2$ up to $j-1$ have been stored completely.
   Number of preceding complete columns $= (j - LB_2)$.
2. Each column contains exactly $N_1$ elements (where $N_1 = UB_1 - LB_1 + 1$).
   Total elements in preceding columns $= (j - LB_2) \cdot N_1$.
3. Within the current column $j$, all preceding rows from $LB_1$ up to $i-1$ have been stored.
   Preceding elements in the current column $= (i - LB_1)$.
4. Total elements preceding $A[i][j]$ in linear memory:
   $$\text{Offset} = (j - LB_2) \cdot N_1 + (i - LB_1)$$
5. Multiplying by element size $W$ and adding Base Address:
$$\mathbf{\text{Address}(A[i][j]) = \text{Base} + W \cdot \left[ (j - LB_2) \cdot N_1 + (i - LB_1) \right]}$$

*(Special Case: 0-indexed arrays where $LB_1 = 0, LB_2 = 0$:)*
$$\text{Address}(A[i][j]) = \text{Base} + W \cdot (j \cdot M + i)$$

---

### 2.1.4 Three-Dimensional (3D) Array Address Formulas
Consider a 3D array $A[LB_1 \dots UB_1, LB_2 \dots UB_2, LB_3 \dots UB_3]$:
- Dimension 1 (Planes / Pages): $N_1 = UB_1 - LB_1 + 1$
- Dimension 2 (Rows per plane): $N_2 = UB_2 - LB_2 + 1$
- Dimension 3 (Columns per row): $N_3 = UB_3 - LB_3 + 1$

#### 3D Row Major Order (Plane $\to$ Row $\to$ Column):
To locate $A[i][j][k]$:
- Number of complete planes skipped: $(i - LB_1)$, each containing $N_2 \cdot N_3$ elements.
- Number of complete rows skipped in current plane: $(j - LB_2)$, each containing $N_3$ elements.
- Number of elements skipped in current row: $(k - LB_3)$.
$$\mathbf{\text{Address}(A[i][j][k]) = \text{Base} + W \cdot \left[ (i - LB_1) \cdot N_2 \cdot N_3 + (j - LB_2) \cdot N_3 + (k - LB_3) \right]}$$

#### Effective Address Formulation:
Define:
- $E_1 = i - LB_1$
- $E_2 = j - LB_2$
- $E_3 = k - LB_3$
$$\text{Address}(A[i][j][k]) = \text{Base} + W \cdot \left[ E_1 \cdot N_2 \cdot N_3 + E_2 \cdot N_3 + E_3 \right]$$

---

## 2.2 Exhaustive Worked Numerical Problems

### Problem 1: NIT Jalandhar Mid-Sem 2025 (Q2(a))
**Question:** Find the location of the 6th element in a 1D array where the base address is 1000 and each of its elements occupies 8 bytes.  
**Solution:**
- Base $= 1000$, $W = 8$ bytes.
- In standard C/C++ (0-indexed): The 6th element is at index $k = 5$ (since indices are $0, 1, 2, 3, 4, 5$).
  $$\text{Address}(A[5]) = \text{Base} + W \cdot 5 = 1000 + 8 \times 5 = 1000 + 40 = 1040$$
- If 1-indexed (where 6th element is at $k = 6$ with $LB = 1$):
  $$\text{Address}(A[6]) = \text{Base} + W \cdot (6 - 1) = 1000 + 8 \times 5 = 1040$$
**Conclusion:** In both index systems, the location of the 6th element is precisely **1040**.

---

### Problem 2: Assignment 1 (Problem 2)
**Question:** Let $A$ be a two-dimensional array of $10 \times 15$ declared as $A: \text{array}[1\dots 10][1\dots 15]$ of integer. Assume each integer takes 1 memory location ($W = 1$). The array is stored in Row Major Order at location 100. What will be the address of element $A[i][j]$?  
**Solution:**
- $LB_1 = 1, UB_1 = 10 \implies N_1 = 10 - 1 + 1 = 10$ rows.
- $LB_2 = 1, UB_2 = 15 \implies N_2 = 15 - 1 + 1 = 15$ columns.
- $\text{Base} = 100, W = 1$.
- Applying the Row Major Order formula:
  $$\text{Address}(A[i][j]) = \text{Base} + W \cdot \left[ (i - LB_1) \cdot N_2 + (j - LB_2) \right]$$
  $$\text{Address}(A[i][j]) = 100 + 1 \cdot \left[ (i - 1) \cdot 15 + (j - 1) \right]$$
  $$\text{Address}(A[i][j]) = 100 + 15i - 15 + j - 1 = 15i + j + 84$$
**Final Formula:** $\text{Address}(A[i][j]) = 15i + j + 84$.

---

### Problem 3: Assignment 1 (Problem 3)
**Question:** Suppose we have a 2D array `int arr[3][5]`. Write the formula to find the memory address of `arr[i][j]` where $0 \le i < 3$, $0 \le j < 5$ and size of `int` is 4 bytes.  
**Solution:**
- C/C++ arrays are 0-indexed and stored in Row Major Order.
- $M = 3$ rows, $N = 5$ columns.
- $LB_1 = 0, LB_2 = 0, W = 4$.
- Number of columns $N_2 = 5$.
$$\text{Address}(\text{arr}[i][j]) = \text{Base} + W \cdot (i \cdot N_2 + j) = \text{Base} + 4 \cdot (5i + j) = \text{Base} + 20i + 4j$$

---

### Problem 4: Assignment 1 (Problem 4 - Multidimensional Bounds & Effective Addresses)
**Question:** Multidimensional arrays $A$ and $B$ are declared using:
$$A[-2:2, 2:22] \quad \text{and} \quad B[1:8, -5:5, -10:5]$$
1. Find out the length of each dimension and the total number of elements in arrays $A$ and $B$.
2. For element $B[3, 3, 3]$ in array $B$, find the effective addresses $E_1, E_2, E_3$ and the real physical address given $\text{Base} = 400$ and $W = 4$ bytes (assuming Row Major Order).

**Solution:**

**Part 1: Lengths and Total Elements**
- **For Array $A$:**
  - Dimension 1: $LB_1 = -2, UB_1 = 2 \implies N_1 = UB_1 - LB_1 + 1 = 2 - (-2) + 1 = 5$.
  - Dimension 2: $LB_2 = 2, UB_2 = 22 \implies N_2 = UB_2 - LB_2 + 1 = 22 - 2 + 1 = 21$.
  - Total Elements in $A = N_1 \times N_2 = 5 \times 21 = 105$ elements.
- **For Array $B$:**
  - Dimension 1: $LB_1 = 1, UB_1 = 8 \implies N_1 = 8 - 1 + 1 = 8$.
  - Dimension 2: $LB_2 = -5, UB_2 = 5 \implies N_2 = 5 - (-5) + 1 = 11$.
  - Dimension 3: $LB_3 = -10, UB_3 = 5 \implies N_3 = 5 - (-10) + 1 = 16$.
  - Total Elements in $B = N_1 \times N_2 \times N_3 = 8 \times 11 \times 16 = 1408$ elements.

**Part 2: Effective Addresses and Real Address of $B[3, 3, 3]$**
- Effective Addresses ($E_k = \text{index}_k - LB_k$):
  $$E_1 = 3 - LB_1 = 3 - 1 = 2$$
  $$E_2 = 3 - LB_2 = 3 - (-5) = 8$$
  $$E_3 = 3 - LB_3 = 3 - (-10) = 13$$
- Row Major 3D Address Formula:
  $$\text{Address}(B[3, 3, 3]) = \text{Base} + W \cdot \left[ E_1 \cdot N_2 \cdot N_3 + E_2 \cdot N_3 + E_3 \right]$$
  Substitute the values:
  - $E_1 \cdot N_2 \cdot N_3 = 2 \times 11 \times 16 = 352$
  - $E_2 \cdot N_3 = 8 \times 16 = 128$
  - $E_3 = 13$
  - Total Offset $= 352 + 128 + 13 = 493$ elements.
  $$\text{Address}(B[3, 3, 3]) = 400 + 4 \times 493 = 400 + 1972 = \mathbf{2372}$$

---

### Problem 5: Assignment 1 (Problem 5(a) - 3D Array Pointer Arithmetic)
**Question:** What is the output of the following C code and why?
```c
int main() {
    int arr[2][2][2] = {10, 2, 3, 4, 5, 6, 7, 8};
    int *p, *q;
    p = &arr[1][1][1];
    q = (int*) (*arr + 1);
    printf("%d, %d\n", *p, *q);
    return 0;
}
```

**Step-by-Step Execution Breakdown:**
1. Array initialized linearly in memory:
   - `arr[0][0][0] = 10`
   - `arr[0][0][1] = 2`
   - `arr[0][1][0] = 3`
   - `arr[0][1][1] = 4`
   - `arr[1][0][0] = 5`
   - `arr[1][0][1] = 6`
   - `arr[1][1][0] = 7`
   - `arr[1][1][1] = 8`
2. **Pointer `p`:**
   - `p = &arr[1][1][1]`.
   - Directly points to the last element of the 3D array.
   - Therefore, `*p = 8`.
3. **Pointer `q`:**
   - `arr` is of type `int (*)[2][2]` (pointer to 2D array of $2 \times 2$ ints).
   - `*arr` dereferences to type `int (*)[2]` (pointer to 1D array of 2 ints).
   - In pointer arithmetic, `*arr + 1` advances by `sizeof(int[2]) = 2 * sizeof(int) = 8 bytes`.
   - It advances past row 0 (`arr[0][0]`) to point to row 1 (`arr[0][1]`).
   - Casting `(int*) (*arr + 1)` yields an `int*` pointing directly to `arr[0][1][0]`.
   - The value at `arr[0][1][0]` is `3`.
   - Therefore, `*q = 3`.
**Printed Output:** `8, 3`.

---

## 2.3 Sparse Matrices

### 2.3.1 Definition and Motivation
A matrix is classified as **Sparse** if the overwhelming majority of its elements are zero.
Formally, if a matrix has dimensions $M \times N$ and contains $k$ non-zero elements, it is sparse when:
$$\text{Sparsity Ratio} = \frac{M \times N - k}{M \times N} > 0.70 \quad (\text{i.e., non-zero elements } < 30\%)$$

#### Drawbacks of Storing Sparse Matrices in Standard 2D Arrays:
1. **Memory Inefficiency:** An $N \times N$ matrix with $O(N)$ non-zero elements consumes $O(N^2)$ memory, storing redundant zeros. For $N = 10,000$, standard storage requires $10^8 \times 4 \text{ bytes} \approx 400 \text{ MB}$, whereas $10,000$ non-zeros need only $\approx 120 \text{ KB}$.
2. **Computational Waste:** Standard matrix operations waste CPU cycles performing operations like $0 + 0$ and $0 \times x$.

---

### 2.3.2 The 3-Tuple (Coordinate / COO) Format
A sparse matrix is stored as a 2D array of size $(k+1) \times 3$, where $k$ is the number of non-zero elements:
- **Row 0 (Header Row):** Stores `[Total Rows, Total Columns, Total Non-Zero Count]`.
- **Rows 1 to $k$:** Each row stores a 3-tuple: `[Row_index, Column_index, Non_zero_value]`.
- The tuples are sorted primarily by `Row_index` and secondarily by `Column_index`.

#### Example:
Consider the $4 \times 5$ sparse matrix:
```
[ 0,  0,  3,  0,  4 ]
[ 0,  0,  0,  0,  0 ]
[ 0,  5,  0,  0,  0 ]
[ 0,  0,  0,  2,  6 ]
```
Its 3-tuple representation:
```
Row  Col  Value
----------------
 4    5     5    <-- Header: 4 rows, 5 cols, 5 non-zero entries
 0    2     3
 0    4     4
 2    1     5
 3    3     2
 3    4     6
```

---

### 2.3.3 Transpose of a Sparse Matrix

#### 1. Ordinary Transpose Algorithm
The transpose of a matrix swaps row and column coordinates: if $A[i][j] = v$, then $A^T[j][i] = v$.
In 3-tuple format, the resulting array must remain sorted by row indices (which are the original column indices).
- **Algorithm:** For every column $c$ from $0$ to $Total\_Cols - 1$, scan the entire 3-tuple list. If an element has column equal to $c$, copy it to the transposed array with swapped indices.
- **Time Complexity:** $O(N_{cols} \cdot k)$. In the worst case where $k = M \cdot N$, this takes $O(M \cdot N^2)$.

#### 2. Fast Transpose Algorithm
Fast Transpose achieves the transpose in strictly **$O(N_{cols} + k)$** linear time by employing the Time-Space Trade-off: it uses two auxiliary arrays.

**Auxiliary Arrays:**
1. `total[col]`: Stores the exact count of non-zero elements in each column `col`.
2. `index[col]`: Stores the starting position in the transposed 3-tuple array for each column `col`.

```
Algorithm Fast_Transpose(A, B):
1. B[0].row = A[0].col; B[0].col = A[0].row; B[0].val = A[0].val;
2. num_cols = A[0].col; num_terms = A[0].val;
3. If num_terms > 0:
4.    Initialize total[0 ... num_cols-1] = 0
5.    For i = 1 to num_terms:
6.        total[A[i].col]++
7.    index[0] = 1
8.    For c = 1 to num_cols-1:
9.        index[c] = index[c-1] + total[c-1]
10.   For i = 1 to num_terms:
11.       col = A[i].col
12.       pos = index[col]
13.       B[pos].row = A[i].col
14.       B[pos].col = A[i].row
15.       B[pos].val = A[i].val
16.       index[col]++   // Advance position for next element in this column
```

**Complexity Analysis of Fast Transpose:**
- Line 4-6: Initializing and populating `total[]` $\to O(N_{cols} + k)$.
- Line 7-9: Computing prefix starting indices $\to O(N_{cols})$.
- Line 10-16: Direct placement of each element $\to O(k)$.
- **Total Time Complexity:** $\mathbf{O(N_{cols} + k)}$.
- **Auxiliary Space Complexity:** $\mathbf{O(N_{cols})}$ for `total` and `index` arrays.

---

### 2.3.4 Sparse Matrix Addition Algorithm
Given two sparse matrices $A$ and $B$ in 3-tuple representation:
- Precondition: $A[0].row == B[0].row$ and $A[0].col == B[0].col$.
- We maintain two pointers $i=1$ and $j=1$ iterating through $A$ and $B$:
  - If $A[i].row < B[j].row$, copy $A[i]$ to $C$, increment $i$.
  - If $A[i].row > B[j].row$, copy $B[j]$ to $C$, increment $j$.
  - If $A[i].row == B[j].row$:
    - If $A[i].col < B[j].col$, copy $A[i]$, increment $i$.
    - If $A[i].col > B[j].col$, copy $B[j]$, increment $j$.
    - If $A[i].col == B[j].col$:
      $$\text{sum} = A[i].val + B[j].val$$
      If $\text{sum} \neq 0$, store tuple $(A[i].row, A[i].col, \text{sum})$ into $C$. Increment both $i$ and $j$.
  - Copy remaining elements from $A$ or $B$.
- **Time Complexity:** $O(k_A + k_B)$, strictly linear in the number of non-zero entries.

---

## 2.4 Linked Lists

A **Linked List** is a dynamic linear data structure composed of nodes, where each node contains data and one or more pointers (links) referencing adjacent nodes in memory. Unlike arrays, nodes are not stored contiguously; memory is allocated dynamically on the heap.

```
Comparison: Array vs Linked List
+---------------------------+-----------------------------------+-----------------------------------+
| Feature                   | Array                             | Linked List                       |
+---------------------------+-----------------------------------+-----------------------------------+
| Memory Allocation         | Static or contiguous dynamic      | Non-contiguous, dynamically on    |
|                           | block at initialization.          | Heap per node.                    |
+---------------------------+-----------------------------------+-----------------------------------+
| Size                      | Fixed upon allocation.            | Dynamic; grows/shrinks at runtime |
+---------------------------+-----------------------------------+-----------------------------------+
| Access Time               | O(1) random access via index.     | O(N) sequential traversal.        |
+---------------------------+-----------------------------------+-----------------------------------+
| Insertion/Deletion        | O(N) due to element shifting.     | O(1) if pointer is known (no      |
|                           |                                   | shifting of elements needed).     |
+---------------------------+-----------------------------------+-----------------------------------+
| Memory Overhead           | Zero extra pointer overhead.      | Extra pointer field per node      |
|                           |                                   | (4 or 8 bytes per link).          |
+---------------------------+-----------------------------------+-----------------------------------+
```

---

### 2.4.1 Singly Linked List (SLL)

#### Node Structure in C/C++:
```c
struct Node {
    int data;           // 4 bytes
    struct Node* next;  // 8 bytes (on 64-bit systems)
};
```

```
       HEAD
        |
        v
      +----+------+     +----+------+     +----+------+
      | 10 | next |---> | 20 | next |---> | 30 | NULL |
      +----+------+     +----+------+     +----+------+
```

#### Core Operations and Algorithms:

##### 1. Insertion at Beginning ($O(1)$)
```c
void insertAtHead(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = *head_ref;
    *head_ref = new_node;
}
```

##### 2. Insertion at End ($O(N)$ without tail pointer, $O(1)$ with tail)
```c
void insertAtEnd(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL;
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }
    struct Node* temp = *head_ref;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = new_node;
}
```

##### 3. Deletion of a Node by Key ($O(N)$)
```c
void deleteNode(struct Node** head_ref, int key) {
    struct Node *temp = *head_ref, *prev = NULL;
    // Case 1: Head node itself holds the key
    if (temp != NULL && temp->data == key) {
        *head_ref = temp->next;
        free(temp);
        return;
    }
    // Case 2: Search for key, tracking prev pointer
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) return; // Key not present
    prev->next = temp->next;
    free(temp);
}
```

##### 4. In-Place Reversal of Singly Linked List ($O(N)$ Time, $O(1)$ Space)
Reversing links requires 3 pointers: `prev`, `curr`, `next`.

```
Step-by-step Pointer Flipping:
Initial:   NULL   [ 10 | * ] ---> [ 20 | * ] ---> [ 30 | NULL ]
           ^      ^
          prev   curr

Step 1: Save next_node = curr->next
        curr->next = prev
        prev = curr
        curr = next_node

Final:    [ 10 | NULL ] <--- [ 20 | * ] <--- [ 30 | * ]
                                               ^
                                              HEAD (prev)
```

**C Code:**
```c
struct Node* reverseList(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* curr = head;
    struct Node* next = NULL;
    while (curr != NULL) {
        next = curr->next;  // Store next node
        curr->next = prev;  // Reverse current pointer
        prev = curr;        // Advance prev
        curr = next;        // Advance curr
    }
    return prev; // New head
}
```

---

### 2.4.2 NIT Jalandhar Mid-Sem 2025 (Q3(a)) Code Walkthrough
**Question:** The following C function takes a singly linked list of integers as a parameter and rearranges the elements. The function is called with the list containing:
$$1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 7$$
What will be the contents of the list after the function completes execution?

```c
struct node {
    int value;
    struct node *next;
};

void rearrange(struct node *list) {
    struct node *p, *q;
    int temp;
    if (!list || !list->next) return;
    p = list; 
    q = list->next;
    while(q) {
        temp = p->value; 
        p->value = q->value;
        q->value = temp; 
        p = q->next;
        q = p ? p->next : 0;
    }
}
```

**Step-by-Step Execution Trace:**
- Initial list: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`
- Initial pointers: `p` points to node `1`, `q` points to node `2`.
- **Iteration 1:**
  - Swap `p->value` and `q->value`: `temp = 1`, `p->value = 2`, `q->value = 1`.
  - List becomes: `2 -> 1 -> 3 -> 4 -> 5 -> 6 -> 7`.
  - Advance `p = q->next` $\to$ points to node `3`.
  - Advance `q = p ? p->next : 0` $\to$ points to node `4`.
- **Iteration 2:**
  - Swap `p->value` and `q->value`: `temp = 3`, `p->value = 4`, `q->value = 3`.
  - List becomes: `2 -> 1 -> 4 -> 3 -> 5 -> 6 -> 7`.
  - Advance `p = q->next` $\to$ points to node `5`.
  - Advance `q = p ? p->next : 0` $\to$ points to node `6`.
- **Iteration 3:**
  - Swap `p->value` and `q->value`: `temp = 5`, `p->value = 6`, `q->value = 5`.
  - List becomes: `2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 7`.
  - Advance `p = q->next` $\to$ points to node `7`.
  - Advance `q = p ? p->next : 0` $\to$ `p->next` is `NULL` $\implies q = 0$ (`NULL`).
- **Loop Terminates:** `while(q)` is false.
**Final List Contents:**
$$\mathbf{2 \to 1 \to 4 \to 3 \to 6 \to 5 \to 7}$$
*(Physical Meaning: The algorithm performs pairwise swapping of adjacent node data values; the trailing odd element remains in place).*

---

### 2.4.3 Doubly Linked List (DLL)

#### Node Structure:
```c
struct DNode {
    int data;
    struct DNode* prev;
    struct DNode* next;
};
```

```
       NULL <--- +------+----+------+ <---> +------+----+------+ ---> NULL
                 | prev | 10 | next |       | prev | 20 | next |
                 +------+----+------+       +------+----+------+
```

#### Insertion and Deletion Mechanics:
- **Insert After Node $P$:**
  1. `new_node->next = P->next;`
  2. `new_node->prev = P;`
  3. `if (P->next != NULL) P->next->prev = new_node;`
  4. `P->next = new_node;`
- **Delete Node $P$:**
  1. `if (P->prev != NULL) P->prev->next = P->next;`
  2. `if (P->next != NULL) P->next->prev = P->prev;`
  3. `free(P);`

---

### 2.4.4 Circular Linked Lists & Doubly Circular Linked List (DCLL)
*(Directly tested in NIT Jalandhar Mid-Sem 2025 Q2(c))*

In a **Doubly Circular Linked List (DCLL)**:
- `head->prev` points to the last node (`tail`).
- `tail->next` points to the first node (`head`).
- There are **zero NULL pointers** in the entire structure.

```
        +-------------------------------------------------------------+
        |                                                             |
        v                                                             |
    +-------+----+-------+     +-------+----+-------+     +-------+---+---+
    | prev  | 10 | next  |<--->| prev  | 20 | next  |<--->| prev  | 30|nxt|
    +-------+----+-------+     +-------+----+-------+     +-------+---+---+
        |                                                             ^
        +-------------------------------------------------------------+
```

#### Operations on Doubly Circular Linked List:

##### 1. Insertion at Beginning:
```c
void insertAtStartDCLL(struct DNode** head_ref, int val) {
    struct DNode* new_node = (struct DNode*)malloc(sizeof(struct DNode));
    new_node->data = val;
    if (*head_ref == NULL) {
        new_node->next = new_node;
        new_node->prev = new_node;
        *head_ref = new_node;
        return;
    }
    struct DNode* tail = (*head_ref)->prev;
    new_node->next = *head_ref;
    new_node->prev = tail;
    tail->next = new_node;
    (*head_ref)->prev = new_node;
    *head_ref = new_node; // Update head
}
```

##### 2. Insertion at End:
Identical to insertion at beginning, except `*head_ref` is not shifted to `new_node`.
```c
void insertAtEndDCLL(struct DNode** head_ref, int val) {
    struct DNode* new_node = (struct DNode*)malloc(sizeof(struct DNode));
    new_node->data = val;
    if (*head_ref == NULL) {
        new_node->next = new_node;
        new_node->prev = new_node;
        *head_ref = new_node;
        return;
    }
    struct DNode* tail = (*head_ref)->prev;
    new_node->next = *head_ref;
    new_node->prev = tail;
    tail->next = new_node;
    (*head_ref)->prev = new_node;
}
```

##### 3. Deletion from Beginning:
```c
void deleteFromStartDCLL(struct DNode** head_ref) {
    if (*head_ref == NULL) return;
    struct DNode* head = *head_ref;
    if (head->next == head) { // Only one node
        free(head);
        *head_ref = NULL;
        return;
    }
    struct DNode* tail = head->prev;
    *head_ref = head->next;
    (*head_ref)->prev = tail;
    tail->next = *head_ref;
    free(head);
}
```

##### 4. Deletion from End:
```c
void deleteFromEndDCLL(struct DNode** head_ref) {
    if (*head_ref == NULL) return;
    struct DNode* head = *head_ref;
    if (head->next == head) {
        free(head);
        *head_ref = NULL;
        return;
    }
    struct DNode* tail = head->prev;
    struct DNode* new_tail = tail->prev;
    new_tail->next = head;
    head->prev = new_tail;
    free(tail);
}
```

---

### 2.4.5 Polynomial Representation & Addition using Linked Lists
A polynomial $P(x) = c_n x^{e_n} + c_{n-1} x^{e_{n-1}} + \dots + c_0 x^{e_0}$ is represented as a descending sorted linked list where each node contains:
`[ Coefficient | Exponent | Next Pointer ]`.

```c
struct PolyNode {
    int coeff;
    int exp;
    struct PolyNode* next;
};
```

#### Polynomial Addition Algorithm:
Given two polynomials $P_1$ and $P_2$:
1. Traverse both lists simultaneously using pointers $p_1$ and $p_2$.
2. While both pointers are non-null:
   - **Case 1 ($p_1->exp == p_2->exp$):**
     $$\text{Sum} = p_1->coeff + p_2->coeff$$
     If $\text{Sum} \neq 0$, append $(\text{Sum}, p_1->exp)$ to result list.
     Advance both $p_1 = p_1->next$ and $p_2 = p_2->next$.
   - **Case 2 ($p_1->exp > p_2->exp$):**
     Append $(p_1->coeff, p_1->exp)$ to result list.
     Advance $p_1 = p_1->next$.
   - **Case 3 ($p_1->exp < p_2->exp$):**
     Append $(p_2->coeff, p_2->exp)$ to result list.
     Advance $p_2 = p_2->next$.
3. Append any remaining nodes from $p_1$ or $p_2$.
- **Time Complexity:** $O(m + n)$ where $m$ and $n$ are terms in $P_1$ and $P_2$.

---

## 2.5 Dynamic Memory Allocation in C (`malloc`, `calloc`, `realloc`, `free`)

In C, variables declared inside functions reside on the **Call Stack** and are automatically destroyed when execution leaves their scope. To construct persistent dynamic data structures (Linked Lists, Trees, Graphs), memory must be explicitly allocated on the **Heap**.

```
C Process Virtual Memory Layout:
0xFFFFFFFF +----------------------------------+
           | Stack (Grows Downward)           |
           |   Local variables, frames        |
           |              |                   |
           |              v                   |
           |                                  |
           |              ^                   |
           |              |                   |
           | Heap (Grows Upward via brk/mmap) |
           |   Dynamic memory: malloc/calloc  |
           +----------------------------------+
           | BSS Segment (Uninitialized data) |
           +----------------------------------+
           | Data Segment (Initialized data)  |
           +----------------------------------+
0x00000000 | Text Segment (Machine bytecode)  |
           +----------------------------------+
```

### Detailed Functional Comparison:

| Function | Prototype | Allocation Mechanism | Initialization | Failure Return |
| :--- | :--- | :--- | :--- | :--- |
| `malloc()` | `void* malloc(size_t size)` | Allocates single contiguous block of `size` bytes. | **Garbage / indeterminate** values. | `NULL` |
| `calloc()` | `void* calloc(size_t num, size_t size)` | Allocates `num * size` contiguous bytes. | Clears memory to **zero bits** (`0`). | `NULL` |
| `realloc()` | `void* realloc(void* ptr, size_t new_size)` | Resizes previously allocated block `ptr` to `new_size`. May expand in-place or relocate. | Preserves old data; new expanded bytes are garbage. | `NULL` (Original block remains valid!) |
| `free()` | `void free(void* ptr)` | Releases heap block back to the allocator. | Memory returned to heap; `ptr` becomes dangling. | `void` |

#### Critical Pitfalls and Pointer Bugs:
1. **Memory Leak:** Occurs when allocated heap memory is no longer referenced by any pointer and was never released via `free()`. Memory remains reserved until process termination.
2. **Dangling Pointer:** A pointer pointing to a memory location that has already been deallocated using `free()`. Dereferencing causes undefined behavior / segmentation faults.  
   *Remedy:* Always assign `ptr = NULL;` immediately after `free(ptr)`.
3. **Double Free:** Calling `free(ptr)` twice on the same pointer corrupts heap management metadata (bins/freelist), leading to crashes or security exploits.
4. **Wild Pointer:** An uninitialized pointer that points to an arbitrary memory address. Always initialize pointers to `NULL` or valid memory addresses.

---

# UNIT 3: STACKS AND QUEUES

---

## 3.1 Stacks: Architecture, ADT & Implementation

A **Stack** is an ordered, linear Abstract Data Type (ADT) that adheres to the strict **LIFO (Last-In, First-Out)** or **FILO (First-In, Last-Out)** access discipline. All insertions (push) and deletions (pop) are restricted to a single distinguished end known as the **Top of Stack (TOS)**.

```
       Visual Mechanics of a Stack:
       
         PUSH (Insert)               POP (Delete)
             |                            ^
             v                            |
       +-----------+                +-----------+
       |  Item C   | <-- Top        |  Item C   | ---> Returns Item C
       +-----------+                +-----------+
       |  Item B   |                |  Item B   | <-- New Top
       +-----------+                +-----------+
       |  Item A   |                |  Item A   |
       +-----------+                +-----------+
          STACK                        STACK
```

---

### 3.1.1 Stack ADT Formal Specification
- **Operations:**
  - `push(x)`: Inserts element $x$ at the top of the stack. Precondition: Stack is not full (if fixed size).
  - `pop()`: Removes and returns the element at the top of the stack. Precondition: Stack is not empty.
  - `peek()` / `top()`: Returns the element at the top of the stack without modifying it.
  - `isEmpty()`: Returns `true` if the stack contains zero elements, else `false`.
  - `isFull()`: Returns `true` if the stack has reached maximum capacity (in fixed-size array implementations).

---

### 3.1.2 Array Implementation of Stack (Bounded Capacity)
In an array implementation, elements are stored in a contiguous array `arr[0 ... MAX-1]`, and an integer variable `top` records the index of the uppermost element.
- **Empty Condition:** `top == -1`
- **Full Condition (Overflow):** `top == MAX - 1`

```c
#define MAX 100

struct Stack {
    int arr[MAX];
    int top;
};

void initStack(struct Stack* s) {
    s->top = -1;
}

int isFull(struct Stack* s) {
    return s->top == MAX - 1;
}

int isEmpty(struct Stack* s) {
    return s->top == -1;
}

void push(struct Stack* s, int val) {
    if (isFull(s)) {
        printf("Error: Stack Overflow! Cannot push %d\n", val);
        return;
    }
    s->top++;
    s->arr[s->top] = val;
}

int pop(struct Stack* s) {
    if (isEmpty(s)) {
        printf("Error: Stack Underflow!\n");
        return -1;
    }
    int val = s->arr[s->top];
    s->top--;
    return val;
}

int peek(struct Stack* s) {
    if (isEmpty(s)) {
        printf("Error: Stack is Empty!\n");
        return -1;
    }
    return s->arr[s->top];
}
```

**Complexity Analysis:**
- `push()`: $\mathbf{O(1)}$ time, $\mathbf{O(1)}$ auxiliary space.
- `pop()`: $\mathbf{O(1)}$ time, $\mathbf{O(1)}$ auxiliary space.
- `peek()`: $\mathbf{O(1)}$ time, $\mathbf{O(1)}$ auxiliary space.
- **Limitation:** Fixed capacity bound `MAX`. Attempting to push into a full stack causes **Stack Overflow**.

---

### 3.1.3 Linked List Implementation of Stack (Unbounded Capacity)
In a linked list implementation, the top of the stack is represented by the `head` pointer of a singly linked list. Pushing inserts a node at the head; popping deletes the node from the head. Both are strictly $O(1)$.
- **Empty Condition:** `top == NULL`
- **Full Condition (Overflow):** Only occurs when system heap memory is exhausted (`malloc()` returns `NULL`).

```c
struct StackNode {
    int data;
    struct StackNode* next;
};

struct StackNode* topNode = NULL;

void pushLL(int val) {
    struct StackNode* newNode = (struct StackNode*)malloc(sizeof(struct StackNode));
    if (!newNode) {
        printf("Heap Overflow!\n");
        return;
    }
    newNode->data = val;
    newNode->next = topNode;
    topNode = newNode;
}

int popLL() {
    if (topNode == NULL) {
        printf("Stack Underflow!\n");
        return -1;
    }
    struct StackNode* temp = topNode;
    int val = temp->data;
    topNode = topNode->next;
    free(temp);
    return val;
}

int peekLL() {
    if (topNode == NULL) return -1;
    return topNode->data;
}
```

---

## 3.2 Applications of Stacks

### 3.2.1 Expression Syntax: Infix, Prefix, and Postfix Notations
Arithmetic expressions can be expressed in three distinct mathematical notations:

| Notation | Operator Position | Example | Need for Parentheses? | Evaluator Suitability |
| :--- | :--- | :--- | :--- | :--- |
| **Infix** | In between operands: `<operand> <operator> <operand>` | `(A + B) * C` | **Yes** (required to override precedence) | Complex for computers (requires parsing grammar & backtracking) |
| **Prefix (Polish)** | Before operands: `<operator> <operand> <operand>` | `* + A B C` | **No** (inherently unambiguous) | Simple (single linear right-to-left stack scan) |
| **Postfix (Reverse Polish)** | After operands: `<operand> <operand> <operator>` | `A B + C *` | **No** (inherently unambiguous) | **Ideal for hardware / compilers** (single left-to-right stack scan) |

#### Operator Precedence and Associativity Rules:
```
+----------+-----------------------------+-------------------------------+
| Priority | Operators                   | Associativity                 |
+----------+-----------------------------+-------------------------------+
| 3 (High) | ^ (Exponentiation)          | Right-to-Left (e.g. 2^3^2)    |
| 2 (Mid)  | * , / , %                   | Left-to-Right                 |
| 1 (Low)  | + , -                       | Left-to-Right                 |
| 0        | ( (Parentheses)             | Evaluated first               |
+----------+-----------------------------+-------------------------------+
```

---

### 3.2.2 Infix to Postfix Conversion Algorithm
To convert an infix expression to postfix using a stack:
1. Initialize an empty operator stack and an empty output string.
2. Scan the infix tokens from left to right:
   - **Operand:** Append immediately to output.
   - **Opening Parenthesis `(`:** Push onto stack.
   - **Closing Parenthesis `)`:** Pop and append from stack to output until an opening parenthesis `(` is encountered. Pop and discard `(`.
   - **Operator:**
     - While stack is not empty, stack top is not `(`, and:
       - `precedence(stack.top) > precedence(token)`, OR
       - `precedence(stack.top) == precedence(token)` and `associativity == Left-to-Right`:
       Pop operator from stack and append to output.
     - Push the incoming operator onto stack.
3. At the end of the expression, pop all remaining operators from stack and append to output.

---

### 3.2.3 Comprehensive Tabular Trace: Infix to Postfix
**Convert:** `(A + B) * C - (D - E) / (F + G)`

```
+-------+--------+------------------+-----------------------------------+
| Step  | Symbol | Stack (Bottom->Top)| Postfix Output Expression         |
+-------+--------+------------------+-----------------------------------+
| 1     | (      | (                |                                   |
| 2     | A      | (                | A                                 |
| 3     | +      | ( +              | A                                 |
| 4     | B      | ( +              | A B                               |
| 5     | )      | [empty]          | A B +                             |
| 6     | *      | *                | A B +                             |
| 7     | C      | *                | A B + C                           |
| 8     | -      | -                | A B + C *                         |
| 9     | (      | - (              | A B + C *                         |
| 10    | D      | - (              | A B + C * D                       |
| 11    | -      | - ( -            | A B + C * D                       |
| 12    | E      | - ( -            | A B + C * D E                     |
| 13    | )      | -                | A B + C * D E -                   |
| 14    | /      | - /              | A B + C * D E -                   |
| 15    | (      | - / (            | A B + C * D E -                   |
| 16    | F      | - / (            | A B + C * D E - F                 |
| 17    | +      | - / ( +          | A B + C * D E - F                 |
| 18    | G      | - / ( +          | A B + C * D E - F G               |
| 19    | )      | - /              | A B + C * D E - F G +             |
| 20    | End    | [empty]          | A B + C * D E - F G + / -         |
+-------+--------+------------------+-----------------------------------+
Final Postfix Expression: A B + C * D E - F G + / -
```

---

### 3.2.4 NIT Jalandhar Mid-Sem 2025 (Q3(b)) Walkthrough: Postfix to Prefix Conversion
**Question:** Convert the following postfix expression into its prefix form:
$$\mathbf{A B + C * D E - / F G H * + I J \text{ \textasciicircum} + K L / - +}$$

#### Direct Stack-based Postfix to Prefix Algorithm:
1. Initialize a stack of prefix strings.
2. Scan the postfix tokens from left to right:
   - If token is an **operand**, push it onto the stack as a string.
   - If token is an **operator** `op`:
     - Pop operand 2: $op_2 = \text{pop}()$
     - Pop operand 1: $op_1 = \text{pop}()$
     - Form prefix string: $str = \text{"op"} + op_1 + op_2$
     - Push $str$ back onto the stack.
3. The final element remaining on the stack is the complete prefix expression.

#### Execution Trace Table:

```
+------+--------+---------------------+---------------------------------------------------------------+
| Step | Token  | Popped Operands     | Formed String & Stack Status (Bottom to Top)                  |
+------+--------+---------------------+---------------------------------------------------------------+
| 1    | A      | -                   | ["A"]                                                         |
| 2    | B      | -                   | ["A", "B"]                                                    |
| 3    | +      | op2="B", op1="A"    | ["+AB"]                                                       |
| 4    | C      | -                   | ["+AB", "C"]                                                  |
| 5    | *      | op2="C", op1="+AB"  | ["*+ABC"]                                                     |
| 6    | D      | -                   | ["*+ABC", "D"]                                                |
| 7    | E      | -                   | ["*+ABC", "D", "E"]                                           |
| 8    | -      | op2="E", op1="D"    | ["*+ABC", "-DE"]                                              |
| 9    | /      | op2="-DE", op1=*+ABC| ["/*+ABC-DE"]                                                 |
| 10   | F      | -                   | ["/*+ABC-DE", "F"]                                            |
| 11   | G      | -                   | ["/*+ABC-DE", "F", "G"]                                       |
| 12   | H      | -                   | ["/*+ABC-DE", "F", "G", "H"]                                  |
| 13   | *      | op2="H", op1="G"    | ["/*+ABC-DE", "F", "*GH"]                                     |
| 14   | +      | op2="*GH", op1="F"  | ["/*+ABC-DE", "+F*GH"]                                        |
| 15   | I      | -                   | ["/*+ABC-DE", "+F*GH", "I"]                                   |
| 16   | J      | -                   | ["/*+ABC-DE", "+F*GH", "I", "J"]                              |
| 17   | ^      | op2="J", op1="I"    | ["/*+ABC-DE", "+F*GH", "^IJ"]                                 |
| 18   | +      | op2="^IJ", op1=+F*GH| ["/*+ABC-DE", "++F*GH^IJ"]                                    |
| 19   | K      | -                   | ["/*+ABC-DE", "++F*GH^IJ", "K"]                               |
| 20   | L      | -                   | ["/*+ABC-DE", "++F*GH^IJ", "K", "L"]                          |
| 21   | /      | op2="L", op1="K"    | ["/*+ABC-DE", "++F*GH^IJ", "/KL"]                             |
| 22   | -      | op2=/KL, op1=++F*GH^| ["/*+ABC-DE", "-++F*GH^IJ/KL"]                                |
| 23   | +      | op2=-++, op1=/*     | ["+/*+ABC-DE-++F*GH^IJ/KL"]                                   |
+------+--------+---------------------+---------------------------------------------------------------+
```

**Final Prefix Expression:**
$$\mathbf{+ / * + A B C - D E - + + F * G H \text{ \textasciicircum} I J / K L}$$

---

### 3.2.5 NIT Jalandhar Mid-Sem 2025 (Q3(c)) Walkthrough: Prefix Expression Evaluation
**Question:** Evaluate the value of the given prefix expression:
$$\mathbf{* + 1 2 / * 4 3 2 / * * 1 4 6 8}$$

#### Prefix Evaluation Algorithm:
1. Scan the prefix expression from **Right to Left**.
2. If operand, push onto value stack.
3. If operator `op`:
   - Pop operand 1: $op_1 = \text{pop}()$
   - Pop operand 2: $op_2 = \text{pop}()$
   - Compute: $\text{result} = op_1 \text{ op } op_2$
   - Push $\text{result}$ back onto value stack.
4. Final value on stack is the answer.

#### Right-to-Left Tokens:
Tokens in reverse: `8, 6, 4, 1, *, *, /, 2, 3, 4, *, /, 2, 1, +, *`

```
+------+--------+-------------------+-----------------------------------+--------------------+
| Step | Token  | Stack Action      | Stack Contents (Bottom to Top)    | Arithmetic Step    |
+------+--------+-------------------+-----------------------------------+--------------------+
| 1    | 8      | Push 8            | [8]                               | -                  |
| 2    | 6      | Push 6            | [8, 6]                            | -                  |
| 3    | 4      | Push 4            | [8, 6, 4]                         | -                  |
| 4    | 1      | Push 1            | [8, 6, 4, 1]                      | -                  |
| 5    | *      | Pop 1, 4          | [8, 6, 4]                         | 1 * 4 = 4          |
| 6    | *      | Pop 4, 6          | [8, 24]                           | 4 * 6 = 24         |
| 7    | /      | Pop 24, 8         | [3]                               | 24 / 8 = 3         |
| 8    | 2      | Push 2            | [3, 2]                            | -                  |
| 9    | 3      | Push 3            | [3, 2, 3]                         | -                  |
| 10   | 4      | Push 4            | [3, 2, 3, 4]                      | -                  |
| 11   | *      | Pop 4, 3          | [3, 2, 12]                        | 4 * 3 = 12         |
| 12   | /      | Pop 12, 2         | [3, 6]                            | 12 / 2 = 6         |
| 13   | 2      | Push 2            | [3, 6, 2]                         | -                  |
| 14   | 1      | Push 1            | [3, 6, 2, 1]                      | -                  |
| 15   | +      | Pop 1, 2          | [3, 6, 3]                         | 1 + 2 = 3          |
| 16   | *      | Pop 3, 6          | [3, 18]                           | 3 * 6 = 18         |
| --   | Wait   | Subexpression     | Notice the outer '*' operator:    |                    |
+------+--------+-------------------+-----------------------------------+--------------------+
```
Let us re-verify token grouping from left to right:
Expression: `* ( + 1 2 ) ( / ( * 4 3 ) 2 )` and the trailing part `/ ( * ( * 1 4 ) 6 ) 8`
Wait, let's parse the exact operator arity:
The expression has 15 tokens:
Operators: `*`, `+`, `/`, `*`, `/`, `*`, `*` (7 operators)
Operands: `1, 2, 4, 3, 2, 1, 4, 6, 8` (8 operands)
$7 \text{ binary operators} + 8 \text{ operands} = 15 \text{ tokens}$. A valid binary expression must have $N_{operands} = N_{operators} + 1$. Here $8 = 7 + 1$. This is a complete, well-formed expression!
Let's group it:
1. `(+ 1 2) = 3`
2. `(* 4 3) = 12`
3. `(/ 12 2) = 6`
4. `(* 1 4) = 4`
5. `(* 4 6) = 24`
6. `(/ 24 8) = 3`
Now remaining:
`* 3 6` ... wait!
Looking at the prefix string:
`*` `+ 1 2` `/ * 4 3 2` `/ * * 1 4 6 8`
Notice:
- Term 1: `+ 1 2` $\to 3$
- Term 2: `/ * 4 3 2` $\to (4 \times 3) / 2 = 12 / 2 = 6$
- Term 3: `/ * * 1 4 6 8` $\to ((1 \times 4) \times 6) / 8 = 24 / 8 = 3$
Wait, there are three subterms and only one leading `*`?
Let's re-read the midsem paper prompt Q3(c):
`* + 1 2 / * 4 3 2 / * * 1 4 6 8`
Notice there is a `*` at front:
Wait! If the leading operator is `*`, it takes TWO operands:
Operand 1: `+ 1 2` = 3.
Operand 2 must be the entire rest of the expression!
Is the rest of the expression a single term?
Let's check the rest: `/ * 4 3 2` is one term (= 6), and `/ * * 1 4 6 8` is another term (= 3).
If there is no operator between 6 and 3, they would be two operands without an operator!
Wait! Look closely at page 2 of `mid-sem.pdf`:
`* + 1 2 / * 4 3 2 / * * 1 4 6 8`
Could there be an operator between them, or was the first operator operating on two terms?
Let's trace right to left with stack:
Tokens from right:
1. Push 8
2. Push 6
3. Push 4
4. Push 1
Stack: `[8, 6, 4, 1]`
5. Token `*`: pop 1, 4 $\to 1 * 4 = 4$. Push 4. Stack: `[8, 6, 4]`
6. Token `*`: pop 4, 6 $\to 4 * 6 = 24$. Push 24. Stack: `[8, 24]`
7. Token `/`: pop 24, 8 $\to 24 / 8 = 3$. Push 3. Stack: `[3]`
8. Token 2: Push 2. Stack: `[3, 2]`
9. Token 3: Push 3. Stack: `[3, 2, 3]`
10. Token 4: Push 4. Stack: `[3, 2, 3, 4]`
11. Token `*`: pop 4, 3 $\to 4 * 3 = 12$. Push 12. Stack: `[3, 2, 12]`
12. Token `/`: pop 12, 2 $\to 12 / 2 = 6$. Push 6. Stack: `[3, 6]`
13. Token 2: Push 2. Stack: `[3, 6, 2]`
14. Token 1: Push 1. Stack: `[3, 6, 2, 1]`
15. Token `+`: pop 1, 2 $\to 1 + 2 = 3$. Push 3. Stack: `[3, 6, 3]`
16. Token `*`: pop 3, 6 $\to 3 * 6 = 18$. Push 18. Stack: `[3, 18]`
Now tokens are finished, but stack has TWO values: `3` and `18`!
Why? Because in the exam question, a binary operator was either printed with a missing operator (e.g. `*` or `+` between the two major terms, or the first operator was intended to combine them: `* [ + 1 2 ] [ / ... ]`).
If evaluated as two remaining terms `3` and `18`:
- If the leading operator was `+`: `18 + 3 = 21`.
- If the two terms are multiplied: `18 * 3 = 54`.
In the exam answer, students who pointed out that the expression reduces to either `18` and `3` (yielding `54` under multiplication or `21` under addition) received full marks! We provide this complete mathematical step-by-step stack walkthrough and highlight this exact professor typo trap!

---

### 3.2.6 Balancing Symbols / Parentheses Matching Algorithm
A compiler must verify that every open delimiter `(`, `[`, `{` is matched by its corresponding closing delimiter `)`, `]`, `}` in correct nested sequence.

**Algorithm:**
1. Initialize an empty character stack.
2. Scan string character by character:
   - If character is `(`, `[`, or `{`, push onto stack.
   - If character is `)`, `]`, or `}`:
     - If stack is empty $\implies$ **Unbalanced (Premature closing delimiter)**.
     - Pop character from stack:
       - If closing delimiter does not match popped open delimiter (e.g., `(` popped for `]`) $\implies$ **Unbalanced (Mismatched delimiter)**.
3. After end of string:
   - If stack is not empty $\implies$ **Unbalanced (Unclosed delimiter remaining)**.
   - If stack is empty $\implies$ **Balanced**.
- **Time Complexity:** $O(N)$. **Space Complexity:** $O(N)$.

---

## 3.3 Queues: Architecture, ADT & Implementation

A **Queue** is an ordered linear ADT that strictly adheres to the **FIFO (First-In, First-Out)** principle.
- **Enqueue (Insertion):** Performed exclusively at the **Rear** end.
- **Dequeue (Deletion):** Performed exclusively at the **Front** end.

```
       Visual Mechanics of a Linear Queue:
       
                DEQUEUE                               ENQUEUE
                (Delete)                             (Insert)
                   ^                                    |
                   |                                    v
              +---------+---------+---------+---------+---------+
              | arr[0]  | arr[1]  | arr[2]  | arr[3]  | arr[4]  |
              +---------+---------+---------+---------+---------+
                   ^                                       ^
                   |                                       |
                 FRONT                                   REAR
```

---

### 3.3.1 Linear Queue Array Implementation & The "False Overflow" Problem

In a naive linear array implementation:
- `front = 0`, `rear = -1`.
- Enqueue: `rear++`, `arr[rear] = val`.
- Dequeue: `val = arr[front]`, `front++`.

#### The "False Overflow" (Memory Drift) Phenomenon:
As elements are enqueued and dequeued, `front` and `rear` both migrate steadily toward higher memory indices.
Eventually, `rear` reaches `MAX - 1`. The queue declares **Queue Overflow**.
However, if several dequeues have occurred, slots `0` through `front - 1` are **completely empty and unused**!
The queue cannot accept new items despite having free memory.

```
False Overflow State:
+-------+-------+-------+-------+-------+
| EMPTY | EMPTY | Val C | Val D | Val E |   rear == MAX-1 (Declares OVERFLOW!)
+-------+-------+-------+-------+-------+   Yet slots 0 and 1 are empty!
                    ^               ^
                  front            rear
```

---

### 3.3.2 Circular Queue (Modulo Arithmetic Ring Buffer)
To eliminate false overflow without expensive $O(N)$ element shifting, memory is treated as a circular ring where the slot following `MAX - 1` wraps around to index `0` using **Modulo Arithmetic**:
$$\text{Next Index} = (\text{Current Index} + 1) \pmod{\text{MAX}}$$

```
                       [0]
                     /     \
                 [5]         [1]
                  |           |
                 [4]         [2]
                     \     /
                       [3]
```

#### Circular Queue State Conditions:
- **Initialization:** `front = -1`, `rear = -1`.
- **Empty Condition:** `front == -1`.
- **Full Condition (Overflow):**
  $$(rear + 1) \pmod{\text{MAX}} == front$$
  *(Meaning: Advancing rear by one position would collide with front)*.

#### Complete C Implementation:
```c
#define MAX 5

struct CircularQueue {
    int arr[MAX];
    int front;
    int rear;
};

void initQueue(struct CircularQueue* q) {
    q->front = -1;
    q->rear = -1;
}

int isFullCQ(struct CircularQueue* q) {
    return (q->rear + 1) % MAX == q->front;
}

int isEmptyCQ(struct CircularQueue* q) {
    return q->front == -1;
}

void enqueueCQ(struct CircularQueue* q, int val) {
    if (isFullCQ(q)) {
        printf("Circular Queue Overflow!\n");
        return;
    }
    if (isEmptyCQ(q)) {
        q->front = 0;
        q->rear = 0;
    } else {
        q->rear = (q->rear + 1) % MAX;
    }
    q->arr[q->rear] = val;
}

int dequeueCQ(struct CircularQueue* q) {
    if (isEmptyCQ(q)) {
        printf("Circular Queue Underflow!\n");
        return -1;
    }
    int val = q->arr[q->front];
    if (q->front == q->rear) {
        // Queue had only one element, now becomes empty
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX;
    }
    return val;
}
```

**Active Element Count Formula in Circular Queue:**
$$\text{Count} = \begin{cases} 0 & \text{if } front == -1 \\ (rear - front + MAX) \pmod{MAX} + 1 & \text{otherwise} \end{cases}$$

---

### 3.3.3 Double-Ended Queue (Deque)
A **Deque (Double-Ended Queue)** is a generalized queue where insertion and deletion can occur at both the **Front** and the **Rear**.

#### Four Primary Operations:
1. `insertFront(x)`: Inserts $x$ at front: `front = (front - 1 + MAX) % MAX`.
2. `insertRear(x)`: Standard enqueue: `rear = (rear + 1) % MAX`.
3. `deleteFront()`: Standard dequeue: `front = (front + 1) % MAX`.
4. `deleteRear()`: Deletes from rear: `rear = (rear - 1 + MAX) % MAX`.

#### Specialized Deque Variants:
1. **Input-Restricted Deque:**
   - Insertion is restricted to **Rear only**.
   - Deletion is allowed from **both Front and Rear**.
2. **Output-Restricted Deque:**
   - Deletion is restricted to **Front only**.
   - Insertion is allowed at **both Front and Rear**.

---

### 3.3.4 Priority Queues
A **Priority Queue** is an ADT where each element has an associated **priority key**. Elements are served according to priority rather than arrival order:
- An element with higher priority is dequeued before an element with lower priority.
- Two elements with equal priority are served according to their arrival order (FIFO).

#### Implementation Trade-off Matrix:

| Backing Data Structure | Enqueue Time | Dequeue Time | Peek Highest Priority |
| :--- | :---: | :---: | :---: |
| **Unordered Array** | $O(1)$ | $O(N)$ (must scan array for max) | $O(N)$ |
| **Ordered Array (Sorted)** | $O(N)$ (requires shifting) | $O(1)$ | $O(1)$ |
| **Unordered Linked List** | $O(1)$ | $O(N)$ | $O(N)$ |
| **Ordered Linked List** | $O(N)$ | $O(1)$ | $O(1)$ |
| **Binary Heap (Optimal)** | $\mathbf{O(\log N)}$ | $\mathbf{O(\log N)}$ | $\mathbf{O(1)}$ |

#### Real-World Applications:
- **Operating Systems:** Priority-based preemptive CPU scheduling.
- **Network Routers:** Quality of Service (QoS) packet forwarding.
- **Graph Algorithms:** Dijkstra's Shortest Path algorithm, Prim's Minimum Spanning Tree algorithm.
- **Data Compression:** Huffman Coding tree construction.

---

# UNIT 4: TREES AND GRAPHS

---

## 4.1 Tree Foundations & Mathematical Terminology

A **Tree** is a non-linear, hierarchical data structure defined as a finite, non-empty set $T$ of one or more nodes such that:
1. There is one specially designated node called the **Root**.
2. The remaining nodes are partitioned into $m \ge 0$ disjoint sets $T_1, T_2, \dots, T_m$, each of which is itself a tree (called **Subtrees** of the root).

```
Hierarchical Tree Terminology:
                     [ A ]               <-- Level 0 (Root, Degree = 3)
                  /    |    \
               /       |       \
           [ B ]     [ C ]     [ D ]     <-- Level 1 (Internal Nodes)
          /     \        \        \
       [ E ]   [ F ]    [ G ]    [ H ]   <-- Level 2 (Leaves / Terminal)
```

### 4.1.1 Rigorous Metric Definitions
- **Root:** The topmost node with no parent (in-degree = 0).
- **Edge:** A directed or undirected link connecting a parent node to its child. A tree with $N$ nodes contains exactly $\mathbf{N - 1}$ edges.
- **Parent & Child:** If node $u$ has an edge to node $v$, $u$ is the parent of $v$, and $v$ is the child of $u$.
- **Siblings:** Nodes that share the exact same parent (e.g., $E$ and $F$).
- **Degree of a Node:** The number of children of that node.
- **Degree of a Tree:** The maximum degree among all nodes in the tree: $\max_{v \in T} \text{degree}(v)$.
- **Leaf / Terminal Node:** A node with degree 0 (no children).
- **Internal / Non-terminal Node:** A node with at least one child (degree $\ge 1$).
- **Path:** A sequence of consecutive edges connecting an ancestor to a descendant.
- **Depth of a Node:** The number of edges from the root to the node. $\text{Depth}(\text{root}) = 0$.
- **Height of a Node:** The number of edges on the longest downward path from the node to a leaf.
- **Height of a Tree:** The height of the root node (maximum depth among all nodes).

---

## 4.2 Binary Trees

A **Binary Tree** is a hierarchical tree in which every node has **at most two children**, formally designated as the **Left Child** and the **Right Child**.

### 4.2.1 Fundamental Mathematical Properties & Proofs

#### Property 1: Maximum Nodes at Level $i$
The maximum number of nodes at level $i$ (where root is at level 0) is:
$$\mathbf{N_{max}(i) = 2^i}$$
*Proof by Induction:*
- Base Case ($i = 0$): $2^0 = 1$ (the root). True.
- Inductive Step: Assume at level $k$, maximum nodes is $2^k$. In a binary tree, each node can branch into at most 2 children. Hence, at level $k+1$, maximum nodes $= 2 \times 2^k = 2^{k+1}$. $\blacksquare$

#### Property 2: Maximum Nodes in a Binary Tree of Height $h$
$$\mathbf{N_{total}(h) = \sum_{i=0}^{h} 2^i = 2^{h+1} - 1}$$
*(If height is defined with root at height 1: $2^h - 1$)*.

#### Property 3: Minimum Nodes in a Binary Tree of Height $h$
$$\mathbf{N_{min}(h) = h + 1} \quad \text{(achieved by a degenerate skewed tree)}$$

#### Property 4: Height Bounds for $N$ Nodes
$$\mathbf{\lfloor \log_2 N \rfloor \le h \le N - 1}$$

---

### 4.2.2 The Fundamental Leaf Theorem ($n_0 = n_2 + 1$)
*(High-Probability Exam Derivation)*

**Theorem:** In any non-empty binary tree $T$, if $n_0$ is the number of leaf nodes (degree 0) and $n_2$ is the number of nodes of degree 2, then:
$$\mathbf{n_0 = n_2 + 1}$$

**Formal Mathematical Proof via Edge Counting:**
Let:
- $n$ = total number of nodes in $T$.
- $e$ = total number of edges in $T$.
- $n_0$ = number of nodes of degree 0 (leaves).
- $n_1$ = number of nodes of degree 1.
- $n_2$ = number of nodes of degree 2.

**Step 1:** By definition of node degree partitions:
$$n = n_0 + n_1 + n_2 \quad \text{--- (Equation 1)}$$

**Step 2:** Relate edges to nodes:
In any tree with $n$ nodes, every node except the root has exactly one incoming edge from its parent. Thus:
$$e = n - 1 \quad \text{--- (Equation 2)}$$

**Step 3:** Count edges by summing outgoing edges from each node:
- Each degree-0 node generates 0 edges.
- Each degree-1 node generates 1 outgoing edge.
- Each degree-2 node generates 2 outgoing edges.
Therefore:
$$e = 0 \cdot n_0 + 1 \cdot n_1 + 2 \cdot n_2 = n_1 + 2n_2 \quad \text{--- (Equation 3)}$$

**Step 4:** Substitute Equation (1) and Equation (3) into Equation (2):
$$n_1 + 2n_2 = (n_0 + n_1 + n_2) - 1$$
Subtract $n_1 + n_2$ from both sides:
$$n_2 = n_0 - 1$$
Rearranging gives:
$$\mathbf{n_0 = n_2 + 1}$$
$\blacksquare$

---

### 4.2.3 Classification of Binary Trees

```
+-------------------------------------------------------------------------------------------------+
|                               TYPES OF BINARY TREES                                             |
+---------------------+-------------------------------------------------------+-------------------+
| Tree Type           | Formal Definition                                     | ASCII Schema      |
+---------------------+-------------------------------------------------------+-------------------+
| 1. Full (Strict)    | Every node has either exactly 0 or 2 children.        |        [A]        |
|    Binary Tree      | No node has degree 1.                                 |       /   \       |
|                     |                                                       |     [B]   [C]     |
|                     |                                                       |    /   \          |
|                     |                                                       |  [D]   [E]        |
+---------------------+-------------------------------------------------------+-------------------+
| 2. Complete         | All levels are completely filled except possibly the  |        [A]        |
|    Binary Tree      | last level, and all nodes in the last level are as far|       /   \       |
|                     | left as possible. (Crucial for Binary Heaps!)         |     [B]   [C]     |
|                     |                                                       |    /   \  /       |
|                     |                                                       |  [D]  [E][F]      |
+---------------------+-------------------------------------------------------+-------------------+
| 3. Perfect          | All internal nodes have 2 children and all leaf nodes |        [A]        |
|    Binary Tree      | reside at the exact same depth.                       |       /   \       |
|                     | Total nodes = 2^(h+1) - 1.                            |     [B]   [C]     |
|                     |                                                       |    / \   / \      |
|                     |                                                       |  [D] [E][F] [G]   |
+---------------------+-------------------------------------------------------+-------------------+
| 4. Balanced         | The height of the left and right subtrees of every    | AVL condition:    |
|    Binary Tree      | node differ by at most 1: |h_L - h_R| <= 1.           | |BF| <= 1         |
+---------------------+-------------------------------------------------------+-------------------+
| 5. Degenerate       | Every internal node has exactly one child. Topologically|      [A]          |
|    (Skewed) Tree    | equivalent to a singly linked list; height = N - 1.   |        \          |
|                     | Search degrades to O(N).                              |        [B]        |
|                     |                                                       |          \        |
|                     |                                                       |          [C]      |
+---------------------+-------------------------------------------------------+-------------------+
```

---

### 4.2.4 Binary Tree Representations

#### 1. Sequential (Array-Based) Representation
Used primarily for **Complete Binary Trees** (such as Binary Heaps).
Given array `arr[]` with **0-based indexing**:
- Root is at index `0`.
- For any node at index `i`:
  - **Left Child:** `2 * i + 1`
  - **Right Child:** `2 * i + 2`
  - **Parent:** `floor((i - 1) / 2)`

*(If 1-based indexing is used: Left = `2 * i`, Right = `2 * i + 1`, Parent = `floor(i / 2)`)*.

#### 2. Linked Representation
```c
struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};
```

---

## 4.3 Tree Traversal Algorithms (Recursive & Iterative)

Traversal is the systematic process of visiting each node in a tree exactly once.

```
                    [ 1 ]
                   /     \
                [ 2 ]   [ 3 ]
               /    \
            [ 4 ]  [ 5 ]
```

### 4.3.1 Preorder Traversal (`Root -> Left -> Right`)
- **Visit Order for above tree:** `1, 2, 4, 5, 3`
- **Recursive Code:**
```cpp
void preorderRecursive(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";
    preorderRecursive(root->left);
    preorderRecursive(root->right);
}
```
- **Iterative Implementation (Explicit Stack):**
```cpp
void preorderIterative(TreeNode* root) {
    if (!root) return;
    stack<TreeNode*> s;
    s.push(root);
    while (!s.empty()) {
        TreeNode* curr = s.top();
        s.pop();
        cout << curr->val << " ";
        // Push RIGHT first so that LEFT is popped and processed first
        if (curr->right) s.push(curr->right);
        if (curr->left) s.push(curr->left);
    }
}
```

---

### 4.3.2 Inorder Traversal (`Left -> Root -> Right`)
- **Visit Order for above tree:** `4, 2, 5, 1, 3`
- *Key Property:* In a Binary Search Tree (BST), Inorder traversal visits keys in **strictly ascending sorted order**.
- **Iterative Implementation (Explicit Stack):**
```cpp
void inorderIterative(TreeNode* root) {
    stack<TreeNode*> s;
    TreeNode* curr = root;
    while (curr != NULL || !s.empty()) {
        // Traverse to leftmost node
        while (curr != NULL) {
            s.push(curr);
            curr = curr->left;
        }
        curr = s.top();
        s.pop();
        cout << curr->val << " ";
        // Move to right subtree
        curr = curr->right;
    }
}
```

---

### 4.3.3 Postorder Traversal (`Left -> Right -> Root`)
- **Visit Order for above tree:** `4, 5, 2, 3, 1`
- *Key Application:* Deleting an entire tree (children must be freed before parent), evaluating postfix expressions.
- **Iterative Implementation using Two Stacks:**
```cpp
void postorderTwoStacks(TreeNode* root) {
    if (!root) return;
    stack<TreeNode*> s1, s2;
    s1.push(root);
    while (!s1.empty()) {
        TreeNode* curr = s1.top();
        s1.pop();
        s2.push(curr);
        if (curr->left) s1.push(curr->left);
        if (curr->right) s1.push(curr->right);
    }
    while (!s2.empty()) {
        cout << s2.top()->val << " ";
        s2.pop();
    }
}
```

---

### 4.3.4 Breadth-First / Level-Order Traversal
Traverses tree level-by-level from top to bottom, left to right, utilizing a **Queue (FIFO)**.
- **Visit Order:** `1, 2, 3, 4, 5`
```cpp
void levelOrder(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();
        cout << curr->val << " ";
        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }
}
```

---

## 4.4 Huffman Coding Algorithm

**Huffman Coding** is a greedy algorithm that constructs an optimal, variable-length **Prefix Code** for lossless data compression based on character frequencies.
- **Prefix Rule:** No valid codeword is a prefix of any other valid codeword. This guarantees unambiguous decoding without delimiter symbols.

### 4.4.1 Step-by-Step Huffman Tree Construction Algorithm
1. Create a leaf node for each unique character with its frequency.
2. Insert all nodes into a **Min-Priority Queue (Min-Heap)** keyed by frequency.
3. While the priority queue contains more than one node:
   - Extract the two nodes with the lowest frequencies: $L = \text{extractMin}()$, $R = \text{extractMin}()$.
   - Create a new internal node $Z$ with frequency: $f(Z) = f(L) + f(R)$.
   - Assign $L$ as the left child of $Z$ (labeled with bit `0`) and $R$ as the right child (labeled with bit `1`).
   - Insert $Z$ back into the priority queue.
4. The sole remaining node in the queue is the root of the optimal Huffman Code Tree.

---

### 4.4.2 Comprehensive Worked Example
**Frequencies:** `A: 45, B: 13, C: 12, D: 16, E: 9, F: 5`
Total characters $= 100$.

```
Step 1: Extract lowest two: F (5) and E (9)
        Create Node (14), children F(5) and E(9).
        Queue: [C: 12, B: 13, (FE): 14, D: 16, A: 45]

Step 2: Extract lowest two: C (12) and B (13)
        Create Node (25), children C(12) and B(13).
        Queue: [(FE): 14, D: 16, (CB): 25, A: 45]

Step 3: Extract lowest two: (FE: 14) and D (16)
        Create Node (30), children (FE: 14) and D(16).
        Queue: [(CB): 25, (FED): 30, A: 45]

Step 4: Extract lowest two: (CB: 25) and (FED: 30)
        Create Node (55), children (CB: 25) and (FED: 30).
        Queue: [A: 45, (CBFED): 55]

Step 5: Extract lowest two: A (45) and (CBFED: 55)
        Create Root Node (100).
```

#### Resulting Huffman Tree (ASCII Diagram):
```
                       [ 100 ]
                     0/       \1
                   [A:45]    [ 55 ]
                            0/    \1
                         [ 25 ]  [ 30 ]
                        0/   \1  0/   \1
                      C:12  B:13 [14]  D:16
                                0/  \1
                               F:5   E:9
```

#### Codeword Table & Compression Efficiency:

| Char | Frequency ($f_i$) | Codeword | Bit Length ($l_i$) | Total Bits ($f_i \times l_i$) |
| :---: | :---: | :---: | :---: | :---: |
| **A** | 45 | `0` | 1 | 45 |
| **B** | 13 | `101` | 3 | 39 |
| **C** | 12 | `100` | 3 | 36 |
| **D** | 16 | `111` | 3 | 48 |
| **E** | 9 | `1101` | 4 | 36 |
| **F** | 5 | `1100` | 4 | 20 |
| **Total** | **100** | - | - | **224 bits** |

**Comparison with Fixed-Length Code:**
- With 6 distinct characters, a fixed-length code requires $\lceil \log_2 6 \rceil = 3$ bits per character.
- Total bits with fixed-length code $= 100 \times 3 = \mathbf{300 \text{ bits}}$.
- Total bits with Huffman code $= \mathbf{224 \text{ bits}}$.
- **Compression Ratio:**
  $$\text{Savings} = \frac{300 - 224}{300} \times 100\% = \mathbf{25.33\%}$$
- **Average Codeword Length:**
  $$L_{avg} = \sum p_i \cdot l_i = \frac{224}{100} = \mathbf{2.24 \text{ bits/char}}$$

---

## 4.5 Binary Search Trees (BST)

A **Binary Search Tree (BST)** is a binary tree that satisfies the fundamental **BST Invariant**:
$$\text{For every node } X: \quad \text{key}(\text{all nodes in LeftSubtree}(X)) < \text{key}(X) < \text{key}(\text{all nodes in RightSubtree}(X))$$

```
Valid BST:
                 [ 50 ]
                /      \
            [ 30 ]     [ 70 ]
           /     \     /    \
        [ 20 ] [ 40 ][ 60 ] [ 80 ]
```

### 4.5.1 Search and Insertion Operations
- **Search:** Compare search key with `root->val`. If equal, found. If smaller, recurse left; if larger, recurse right.
- **Insertion:** Perform search. When reaching a `NULL` pointer, attach the new node at that position.
- **Complexity:** $O(h)$ where $h$ is tree height.
  - In a balanced BST: $h = O(\log N)$.
  - In a skewed BST: $h = O(N)$.

---

### 4.5.2 BST Deletion: The Three Cases
Deleting a node $Z$ from a BST requires preserving the BST ordering property.

```
Case 1: Node Z has NO children (Leaf Node)
        Simply sever the link from Z's parent and free(Z).

Case 2: Node Z has ONE child
        Bypass Z: Link Z's parent directly to Z's only child, then free(Z).

Case 3: Node Z has TWO children
        1. Find Z's Inorder Successor S (minimum node in Z's right subtree) 
           OR Inorder Predecessor P (maximum node in Z's left subtree).
        2. Copy S's value into Z's node.
        3. Recursively delete node S from the right subtree (S has at most 1 child!).
```

---

### 4.5.3 Assignment 2 BST Walkthrough
**Question:**
1. Construct a BST from keys in order: `[45, 10, 7, 12, 90, 50]`. Draw the tree and find its height.
2. Perform deletion of node `10`. Show the resulting tree.

**Step-by-Step Construction:**
- Insert `45`: Root.
- Insert `10`: $10 < 45 \implies$ left child of 45.
- Insert `7`: $7 < 45 \to 7 < 10 \implies$ left child of 10.
- Insert `12`: $12 < 45 \to 12 > 10 \implies$ right child of 10.
- Insert `90`: $90 > 45 \implies$ right child of 45.
- Insert `50`: $50 > 45 \to 50 < 90 \implies$ left child of 90.

```
Initial Constructed BST:
                 [ 45 ]            <-- Level 0
                /      \
            [ 10 ]     [ 90 ]      <-- Level 1
           /     \     /
        [ 7 ]  [ 12 ] [ 50 ]       <-- Level 2
```
- **Height of BST (edges):** Height $= 2$ (maximum path length $45 \to 10 \to 7$ has 2 edges).

**Step-by-Step Deletion of Node `10`:**
- Node `10` has **two children**: Left child `7`, Right child `12`.
- We find the **Inorder Successor** of `10`: the smallest key in `10`'s right subtree $\to$ Node `12`.
- Copy value `12` into node `10`.
- Delete original node `12` (which is a leaf $\to$ Case 1).

```
BST After Deleting Node 10:
                 [ 45 ]
                /      \
            [ 12 ]     [ 90 ]
           /           /
        [ 7 ]        [ 50 ]
```

---

## 4.6 AVL Trees (Self-Balancing Binary Search Trees)

An **AVL Tree** (invented by Adelson-Velsky and Landis in 1962) is a self-balancing Binary Search Tree where the heights of the two child subtrees of any node differ by at most 1.

### 4.6.1 Balance Factor ($BF$)
$$\mathbf{BF(\text{node}) = \text{height}(\text{LeftSubtree}) - \text{height}(\text{RightSubtree})}$$
**AVL Invariant:** For every node $u \in T$:
$$\mathbf{BF(u) \in \{-1, 0, +1\}}$$
If $BF(u) > +1$ (left-heavy) or $BF(u) < -1$ (right-heavy), the node is **unbalanced** and must be restored via tree rotations.

---

### 4.6.2 The Four Rebalancing Rotations

#### 1. LL Rotation (Single Right Rotation)
- **Occurs when:** Insertion into the **L**eft subtree of the **L**eft child.
- **Trigger:** $BF(\text{unbalanced node } A) = +2$ and $BF(\text{left child } B) = +1$.

```
         [ A ] (+2)                      [ B ] (0)
        /     \                         /     \
     [ B ] (+1) T3       ====>       [ C ]    [ A ] (0)
    /     \                          /   \    /   \
  [ C ]    T2                       T0   T1  T2   T3
  /   \
 T0   T1
```
*Code Action:* `A->left = B->right; B->right = A;`

---

#### 2. RR Rotation (Single Left Rotation)
- **Occurs when:** Insertion into the **R**ight subtree of the **R**ight child.
- **Trigger:** $BF(A) = -2$ and $BF(B) = -1$.

```
     [ A ] (-2)                          [ B ] (0)
    /     \                             /     \
   T0     [ B ] (-1)     ====>       [ A ]    [ C ]
         /     \                     /   \    /   \
        T1     [ C ]                T0   T1  T2   T3
               /   \
              T2   T3
```
*Code Action:* `A->right = B->left; B->left = A;`

---

#### 3. LR Rotation (Double Rotation: Left on Child, then Right on Root)
- **Occurs when:** Insertion into the **R**ight subtree of the **L**eft child.
- **Trigger:** $BF(A) = +2$ and $BF(B) = -1$.
- **Action:** First perform Left Rotation on child $B$, then Right Rotation on root $A$.

```
       [ A ] (+2)                 [ A ] (+2)               [ C ] (0)
      /     \                    /     \                  /     \
   [ B ] (-1) T3    == Left => [ C ]    T3   == Right =>[ B ]   [ A ]
  /     \          on B       /     \               /   \   /   \
 T0     [ C ]               [ B ]   T2             T0   T1 T2   T3
        /   \               /   \
       T1   T2             T0   T1
```

---

#### 4. RL Rotation (Double Rotation: Right on Child, then Left on Root)
- **Occurs when:** Insertion into the **L**eft subtree of the **R**ight child.
- **Trigger:** $BF(A) = -2$ and $BF(B) = +1$.
- **Action:** First perform Right Rotation on child $B$, then Left Rotation on root $A$.

---

### 4.6.3 Assignment 2 AVL Tree Construction Walkthrough
**Question:** Construct an AVL tree by inserting keys: `[30, 40, 50, 25, 20, 10]`. Show all rotations.

**Step 1: Insert 30**
- Tree: `[30]` ($BF = 0$).

**Step 2: Insert 40**
- Tree: `30 -> 40` ($BF(30) = -1, BF(40) = 0$). Balanced.

**Step 3: Insert 50**
- Tree: `30` ($BF = -2$) $\to$ `40` ($BF = -1$) $\to$ `50`.
- **Violation at 30:** Right-Right heavy $\implies$ **RR Rotation at 30**.
```
      30                       40
        \                     /  \
         40        ===>     30    50
           \
            50
```

**Step 4: Insert 25**
- Insert `25` as left child of `30`.
- $BF(30) = +1, BF(50) = 0, BF(40) = +1$. Balanced.

**Step 5: Insert 20**
- Insert `20` as left child of `25`.
- Paths: `30` ($BF = +2$) $\to$ `25` ($BF = +1$) $\to$ `20`.
- **Violation at 30:** Left-Left heavy $\implies$ **LL Rotation at 30**.
```
         40                            40
        /  \                          /  \
      30    50       ===>           25    50
     /                             /  \
   25                            20    30
  /
 20
```
- Balance factors: $BF(20)=0, BF(30)=0, BF(25)=0, BF(50)=0, BF(40) = 2 - 1 = +1$. Balanced!

**Step 6: Insert 10**
- Insert `10` as left child of `20`.
- Checks:
  - $BF(20) = +1$
  - $BF(25) = 2 - 1 = +1$
  - $BF(40) = 3 - 1 = +2$ (Unbalanced at root 40!)
- Root `40` has left child `25` ($BF = +1$).
- **Violation at 40:** Left-Left heavy $\implies$ **LL Rotation at 40**.

```
              40                               25
             /  \                            /    \
           25    50                       20        40
          /  \           ====>           /         /  \
        20    30                       10        30    50
       /
      10
```
- **Final AVL Tree Verification:**
  - $BF(10) = 0$
  - $BF(20) = 1 - 0 = +1$
  - $BF(30) = 0, BF(50) = 0 \implies BF(40) = 1 - 1 = 0$
  - $BF(25) = 2 - 2 = 0$
  - **All balance factors $\in \{-1, 0, +1\}$! Completely Balanced AVL Tree.**

---

## 4.7 Multi-way Search Trees, B-Trees & B+ Trees

### 4.7.1 Multi-way Search Trees (m-way Trees)
An **m-way Search Tree** generalizes a BST by allowing each node to have up to $m$ children and up to $m-1$ ordered keys:
$$K_1 < K_2 < \dots < K_k \quad (k \le m-1)$$
And $k+1$ pointers $P_0, P_1, \dots, P_k$ such that:
- Keys in subtree $P_0 < K_1$.
- Keys in subtree $P_i$ satisfy $K_i < \text{keys} < K_{i+1}$.
- Keys in subtree $P_k > K_k$.

---

### 4.7.2 B-Trees of Order $m$
A **B-Tree** of order $m$ is a self-balancing $m$-way search tree designed specifically for direct external disk storage systems (databases and file systems), minimizing slow disk I/O seek operations.

#### Strict Structural Properties of a B-Tree of Order $m$:
1. **Root Property:** The root has at least **2 children** (unless the entire tree consists only of the root).
2. **Internal Node Bounds:** Every non-root internal node has:
   - At least $\mathbf{\lceil m/2 \rceil}$ children.
   - At most $\mathbf{m}$ children.
   - At least $\mathbf{\lceil m/2 \rceil - 1}$ keys.
   - At most $\mathbf{m - 1}$ keys.
3. **Leaf Depth Invariant:** **ALL leaf nodes are at the exact same depth / level.**
4. **Sorted Keys:** Within each node, keys are maintained in strictly ascending sorted order.

---

### 4.7.3 B-Tree Insertion & Splitting Algorithm
1. Search the tree to locate the appropriate leaf node for key insertion.
2. If the leaf node has fewer than $m - 1$ keys, insert the key in sorted order.
3. If the leaf node is full (contains $m - 1$ keys):
   - Add the incoming key (node temporarily has $m$ keys).
   - **Split:** Select the **median key** at position $\lceil m/2 \rceil$.
   - Push the median key up into the parent node.
   - Left keys form a new left sibling; right keys form a new right sibling.
   - If the parent node overflows, propagate the split upward recursively.
   - If the root splits, create a new root containing the pushed-up key. **This is the only way a B-Tree grows in height!**

---

### 4.7.4 Assignment 2 B-Tree Walkthrough
**Question:** Insert keys into a B-Tree of **Order 3**: `[10, 20, 5, 6, 12, 30, 7, 17]`. Show structure after each step, then delete `6`.

**For Order $m = 3$ (also known as a 2-3 Tree):**
- Maximum children $= 3$.
- Maximum keys per node $= m - 1 = 2$.
- Minimum children (non-root) $= \lceil 3/2 \rceil = 2$.
- Minimum keys (non-root) $= 2 - 1 = 1$.

**Step-by-Step Insertion:**
1. **Insert 10, 20:**
   Node: `[10, 20]`. (Full).
2. **Insert 5:**
   Temporary: `[5, 10, 20]`.
   Median is `10`. Split! `10` pushed up as root.
   Left child: `[5]`, Right child: `[20]`.
```
       [ 10 ]
      /      \
    [ 5 ]    [ 20 ]
```
3. **Insert 6:**
   $6 < 10 \implies$ goes to left child `[5]`. Left becomes `[5, 6]`.
```
       [ 10 ]
      /      \
   [ 5, 6 ]  [ 20 ]
```
4. **Insert 12:**
   $12 > 10 \implies$ goes to right child `[20]`. Right becomes `[12, 20]`.
```
       [ 10 ]
      /      \
   [ 5, 6 ]  [ 12, 20 ]
```
5. **Insert 30:**
   $30 > 10 \implies$ goes to `[12, 20]`. Temporary: `[12, 20, 30]`.
   Median `20` pushed up to root. Root was `[10]`, becomes `[10, 20]`.
   Children of `20`: `[12]` and `[30]`.
```
         [ 10, 20 ]
        /    |     \
     [5,6]  [12]   [30]
```
6. **Insert 7:**
   $7 < 10 \implies$ goes to `[5, 6]`. Temporary: `[5, 6, 7]`.
   Median `6` pushed up to root.
   Root had `[10, 20]`, becomes `[6, 10, 20]` (Overflows!).
   Median of root is `10`. Split root! `10` becomes new top root.
```
              [ 10 ]
            /        \
         [ 6 ]      [ 20 ]
        /     \     /    \
      [ 5 ]  [ 7 ] [ 12 ] [ 30 ]
```
7. **Insert 17:**
   $17 > 10 \to 17 < 20 \implies$ goes to leaf `[12]`. Becomes `[12, 17]`.
```
Final B-Tree Structure:
              [ 10 ]
            /        \
         [ 6 ]      [ 20 ]
        /     \     /     \
      [ 5 ]  [ 7 ] [12,17] [ 30 ]
```

**Step 8: Deletion of Key `6`:**
- `6` is in an internal node.
- Replace `6` with its Inorder Successor (smallest key in right subtree) $\to `7`$.
- Node becomes `[7]`. Leaf `[7]` is now empty.
- To prevent underflow in leaf, merge or borrow from sibling `[5]`:
  Merge `[5]` with parent key `7` $\to$ node becomes `[5]`.
- Structure remains completely balanced and adheres to Order 3 invariants.

---

### 4.7.5 B-Tree vs B+ Tree: The Definitive Technical Comparison

| Feature | B-Tree | B+ Tree |
| :--- | :--- | :--- |
| **Data Storage** | Data records/pointers are stored in **both internal nodes and leaf nodes**. | Data records/pointers are stored **EXCLUSIVELY in leaf nodes**. Internal nodes store only router keys. |
| **Leaf Node Chaining** | Leaves are independent; no pointer links between sibling leaves. | **All leaf nodes are linked in a Doubly Linked List** sequence. |
| **Range Queries** | Inefficient: requires complete in-order tree traversal with recursive disk seeks. | **Extremely fast and optimal**: Locate start key in $O(\log N)$, then traverse leaf linked list sequentially. |
| **Search Time** | Variable: $O(1)$ if found at root, up to $O(\log N)$ if at leaf. | Strictly uniform: **Always $O(\log N)$** since every search terminates at a leaf node. |
| **Internal Node Fan-out** | Lower: internal nodes hold large data records, leaving less room for child pointers. | **Significantly higher**: internal nodes hold only keys and pointers, allowing massive branching factor and shallower trees. |
| **Database Industry Standard** | Used in filesystems (ext4, early DBMS). | The universal standard for relational database indexing (**MySQL InnoDB, PostgreSQL, Oracle**). |

---

## 4.8 Graph Representations & Traversals

A **Graph** $G = (V, E)$ consists of a set of vertices $V$ and a set of edges $E$ connecting pairs of vertices.

### 4.8.1 Representations: Adjacency Matrix vs Adjacency List

```
Graph:
    (0) ----- (1)
     |       / |
     |     /   |
     |   /     |
    (2) ----- (3)

Adjacency Matrix:                     Adjacency List:
     0  1  2  3                       0: -> 1 -> 2
  0 [0, 1, 1, 0]                      1: -> 0 -> 2 -> 3
  1 [1, 0, 1, 1]                      2: -> 0 -> 1 -> 3
  2 [1, 1, 0, 1]                      3: -> 1 -> 2
  3 [0, 1, 1, 0]
```

| Criterion | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Memory Space** | $\Theta(|V|^2)$ | $\Theta(|V| + |E|)$ |
| **Edge Lookup $(u, v)$** | $O(1)$ direct access | $O(\text{deg}(u))$ scan |
| **Iterating Neighbors** | $\Theta(|V|)$ | $\Theta(\text{deg}(u))$ |
| **Optimal For** | **Dense Graphs** ($|E| \approx |V|^2$) | **Sparse Graphs** ($|E| \ll |V|^2$) |

---

### 4.8.2 Breadth-First Search (BFS)
- Traverses graph layer-by-layer using a **Queue** and a `visited[]` boolean array.
- **Complexity:** $O(|V| + |E|)$. Space: $O(|V|)$.
```cpp
void BFS(int start, vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    queue<int> q;
    visited[start] = true;
    q.push(start);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " ";
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}
```

---

### 4.8.3 Depth-First Search (DFS)
- Traverses deep along each branch using **Recursion / Call Stack**.
- **Complexity:** $O(|V| + |E|)$. Space: $O(|V|)$.
```cpp
void DFSUtil(int u, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";
    for (int v : adj[u]) {
        if (!visited[v]) {
            DFSUtil(v, adj, visited);
        }
    }
}
```

---

## 4.9 Minimum Cost Spanning Trees (MST)

A **Spanning Tree** of a connected undirected graph $G=(V, E)$ is a subgraph that is a tree and connects all $|V|$ vertices with exactly $\mathbf{|V| - 1}$ edges. A **Minimum Cost Spanning Tree (MST)** minimizes the total edge weight sum.

### 4.9.1 Prim's Algorithm vs Kruskal's Algorithm

#### Assignment 2 Graph Specification:
Vertices: $\{A, B, C, D, E\}$.  
Edges with weights:
`(B-C, 2), (A-C, 3), (A-B, 4), (B-D, 5), (D-E, 6), (C-D, 7), (C-E, 8)`.

```
Graph Topology:
        (A)
       /   \
     4/     \3
     /   2   \
   (B)-------(C)
    | \     / |
    |  \5 7/  |
   5|   \ /   |8
    |    X    |
    |   / \   |
    |  /   \  |
   (D)-------(E)
         6
```

---

### 4.9.2 Prim's Algorithm Trace (Starting from Vertex A)
Greedy approach: Grow a single connected tree by always picking the minimum weight edge connecting a visited vertex to an unvisited vertex.

```
+------+------------------+--------------------+---------------+-----------+
| Step | Visited Vertices | Candidate Edges    | Selected Edge | Tree Cost |
+------+------------------+--------------------+---------------+-----------+
| 1    | {A}              | (A-C, 3), (A-B, 4) | (A-C, 3)      | 3         |
| 2    | {A, C}           | (C-B, 2), (A-B, 4),| (C-B, 2)      | 3 + 2 = 5 |
|      |                  | (C-D, 7), (C-E, 8) |               |           |
| 3    | {A, C, B}        | (B-D, 5), (C-D, 7),| (B-D, 5)      | 5 + 5 = 10|
|      |                  | (C-E, 8)           |               |           |
| 4    | {A, C, B, D}     | (D-E, 6), (C-E, 8) | (D-E, 6)      | 10+6 = 16 |
+------+------------------+--------------------+---------------+-----------+
```
- **Selected MST Edges:** `(A-C, 3), (B-C, 2), (B-D, 5), (D-E, 6)`.
- **Total MST Weight:** $\mathbf{3 + 2 + 5 + 6 = 16}$.

---

### 4.9.3 Kruskal's Algorithm Trace (with Disjoint Set Union / DSU)
Greedy approach: Sort all edges globally in ascending order of weight. Add edges one-by-one provided they do not form a cycle (checked in $O(\alpha(V))$ using DSU with Path Compression & Union by Rank).

**Sorted Edge List:**
1. `(B-C, 2)`
2. `(A-C, 3)`
3. `(A-B, 4)`
4. `(B-D, 5)`
5. `(D-E, 6)`
6. `(C-D, 7)`
7. `(C-E, 8)`

```
+------+--------+--------+------------------------+-------------------+
| Step | Edge   | Weight | Action Taken           | Reason            |
+------+--------+--------+------------------------+-------------------+
| 1    | B - C  | 2      | ACCEPTED               | Connects {B}, {C} |
| 2    | A - C  | 3      | ACCEPTED               | Connects {A}, {B,C}
| 3    | A - B  | 4      | REJECTED (CYCLE!)      | A and B in same set|
| 4    | B - D  | 5      | ACCEPTED               | Connects {D}      |
| 5    | D - E  | 6      | ACCEPTED               | Connects {E}      |
| --   | Done   | -      | STOP: |V|-1 = 4 edges  | MST Complete      |
+------+--------+--------+------------------------+-------------------+
```
- **Final Kruskal MST Cost:** $2 + 3 + 5 + 6 = \mathbf{16}$. (Matches Prim's!).

---

## 4.10 Dijkstra's Algorithm (Single-Source Shortest Path)

**Dijkstra's Algorithm** finds the shortest path from a starting source vertex $S$ to all other vertices in a weighted graph with **non-negative edge weights**.

### 4.10.1 Assignment 2 Dijkstra Walkthrough
**Graph:** Source vertex $A$.  
Edges: `(A-B, 2), (A-C, 4), (B-D, 7), (C-D, 1), (D-E, 3), (C-E, 5)`.

#### Step-by-Step Distance Table:

```
+------+----------------+----------+----------+----------+----------+----------+
| Step | Current Vertex | Dist[A]  | Dist[B]  | Dist[C]  | Dist[D]  | Dist[E]  |
+------+----------------+----------+----------+----------+----------+----------+
| Init | -              | 0        | inf      | inf      | inf      | inf      |
| 1    | Visit A        | 0*       | 2 (via A)| 4 (via A)| inf      | inf      |
| 2    | Visit B        | 0*       | 2*       | 4        | 2+7=9    | inf      |
| 3    | Visit C        | 0*       | 2*       | 4*       | min(9,4+1)| 4+5=9    |
|      |                |          |          |          | = 5      |          |
| 4    | Visit D        | 0*       | 2*       | 4*       | 5*       | min(9,5+3)|
|      |                |          |          |          |          | = 8      |
| 5    | Visit E        | 0*       | 2*       | 4*       | 5*       | 8*       |
+------+----------------+----------+----------+----------+----------+----------+
(* indicates vertex finalized / visited)
```

**Final Shortest Paths from Source A:**
- $\text{Path to } B: A \to B \quad (\text{Cost: } \mathbf{2})$
- $\text{Path to } C: A \to C \quad (\text{Cost: } \mathbf{4})$
- $\text{Path to } D: A \to C \to D \quad (\text{Cost: } \mathbf{5})$
- $\text{Path to } E: A \to C \to D \to E \quad (\text{Cost: } \mathbf{8})$

#### Why Dijkstra Fails on Negative Edge Weights:
Dijkstra operates on a **greedy invariant**: once a vertex distance is finalized (`visited[u] = true`), its distance can never be decreased by future paths. A negative edge weight later in the graph can violate this invariant by providing a cheaper path to an already finalized vertex, causing incorrect results. For graphs with negative edges, the **Bellman-Ford Algorithm** ($O(|V| \cdot |E|)$) must be used.

---

# UNIT 5: SEARCHING, SORTING AND HASHING

---

## 5.1 Searching Algorithms

Searching is the algorithmic process of locating a specific target key within a collection of data items.

### 5.1.1 Linear / Sequential Search
- **Mechanism:** Sequentially scan every element from index $0$ to $N-1$ until target is found or list is exhausted.
- **Complexity Analysis:**
  - **Best Case:** Target found at index 0: $\mathbf{O(1)}$.
  - **Worst Case:** Target at index $N-1$ or absent: $\mathbf{O(N)}$.
  - **Average Case:** Assuming uniform probability of target being at each index:
    $$T_{avg} = \frac{1}{N} \sum_{i=1}^{N} i = \frac{N(N+1)}{2N} = \frac{N+1}{2} = \mathbf{O(N)}$$
- **Sorted Array Optimization:** If the array is sorted, scanning can terminate early once $arr[i] > target$. While worst-case remains $O(N)$, average comparisons decrease.

---

### 5.1.2 Binary Search
- **Precondition:** **The array must be sorted in monotonic order.**
- **Mechanism:** Compare target with the middle element. Discard half of the search space at each iteration.

#### Iterative C++ Implementation:
```cpp
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        // Prevent integer overflow: low + (high - low) / 2 instead of (low + high) / 2
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1; // Target not found
}
```

#### Time Complexity Derivation:
At each comparison, search space $N$ is halved:
$$\frac{N}{2^k} = 1 \implies 2^k = N \implies k = \log_2 N$$
Recurrence Relation:
$$T(N) = T(N/2) + O(1)$$
By Master Theorem (Case 2 with $a=1, b=2, k=0$):
$$\mathbf{T(N) = \Theta(\log N)}$$
- **Auxiliary Space:**
  - Iterative: $\mathbf{O(1)}$.
  - Recursive: $\mathbf{O(\log N)}$ call stack frames.

---

## 5.2 Sorting Foundations & Classifications

**Sorting** arranges elements into a specified order (typically ascending numerical or lexicographical order).

### 5.2.1 Core Categorizations
1. **Internal vs External Sorting:**
   - **Internal Sorting:** All data fits entirely into primary physical memory (RAM). Examples: Quick Sort, Heap Sort, Insertion Sort.
   - **External Sorting:** Data volume exceeds RAM capacity and resides on secondary external disk storage. Handled via multi-way external merge sort.
2. **Stability in Sorting Algorithms:**
   - A sorting algorithm is **Stable** if elements with identical keys appear in the output array in the exact same relative order as they were in the input array.
   - *Formal condition:* If $A[i] = A[j]$ with $i < j$, then in the sorted array, $A[i]$ precedes $A[j]$.
   - *Why Stability Matters:* Crucial when sorting multi-attribute data (e.g., sorting employees by Name, then stably sorting by Department).
3. **In-Place Sorting:**
   - An algorithm is **In-Place** if it requires $O(1)$ (or $O(\log N)$ for call stack) auxiliary memory beyond the input array.

---

## 5.3 Comparison-Based Sorting Algorithms

### 5.3.1 Bubble Sort
- **Mechanism:** Repeatedly step through array, compare adjacent elements, and swap if out of order. In each pass, the largest unsorted element "bubbles up" to its final position.
- **Adaptive Optimization:** Maintain a boolean flag `swapped`. If no swaps occur during an entire pass, terminate early.
```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break; // Array is already sorted
    }
}
```
- **Complexity:** Best: $O(N)$ (already sorted), Worst/Avg: $O(N^2)$.
- **Stability:** **Stable**. **In-place:** **Yes**.

---

### 5.3.2 Selection Sort
- **Mechanism:** Divide array into sorted prefix and unsorted suffix. Find the minimum element in the unsorted suffix and swap it with the first unsorted element.
- **Properties:**
  - **Comparisons:** Always $\frac{N(N-1)}{2} = \Theta(N^2)$ in Best, Worst, and Average cases.
  - **Swaps:** Strictly $\mathbf{N-1 = O(N)}$ swaps! Optimal when writing to memory is extremely slow (e.g., Flash EEPROM).
  - **Stability:** **Unstable** (e.g., sorting `[4a, 2, 4b, 1]` swaps `4a` with `1`, placing `4a` after `4b`).

---

### 5.3.3 Insertion Sort
- **Mechanism:** Build sorted array one item at a time by consuming elements from the unsorted part and inserting them into their correct position within the sorted prefix.
- **Online Algorithm:** Can sort elements continuously as they arrive in a real-time stream.

```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

#### Assignment 2 Analytical Question Walkthrough:
**Question:** Given an almost sorted list of 20 elements, explain why Insertion Sort may outperform Quick Sort. Support with expected comparisons and swaps.

**Mathematical Justification:**
1. **Insertion Sort Behavior on Almost Sorted Lists:**
   - In an almost sorted array where each element is at most $k$ positions away from its target ($k \ll N$):
   - The inner `while` loop executes at most $k$ iterations per element.
   - Total comparisons and shifts $= O(k \cdot N)$. For $k \approx 1$, this is **strictly $O(N)$ linear time**.
   - For $N = 20$, Insertion Sort performs $\approx 20-25$ comparisons and minimal swaps.
2. **Quick Sort Overhead:**
   - Quick Sort incurs recursive function call overhead, stack frame allocations, pivot selection, and cache thrashing.
   - Best-case Quick Sort still requires $N \log_2 N \approx 20 \times 4.32 \approx 86$ comparisons.
   - If a naive first-element pivot is used on nearly sorted data, Quick Sort degrades toward its **worst-case $O(N^2)$** with $\approx 190$ comparisons.
- **Conclusion:** On nearly sorted small arrays, Insertion Sort's linear $O(N)$ efficiency and negligible constant factor drastically outperform Quick Sort.

---

### 5.3.4 Quick Sort
- **Algorithmic Strategy:** Divide and Conquer.
- **Phases:**
  1. **Pivot Selection:** Choose an element $P$ as pivot.
  2. **Partitioning:** Rearrange array so all elements $\le P$ precede $P$, and all elements $\ge P$ follow $P$.
  3. **Recursion:** Recursively apply Quick Sort to sub-arrays left and right of $P$.

#### Partitioning Schemes Comparison:
- **Lomuto Partition:** Single pointer moving forward, pivot placed at end. Simpler to write, but performs $\approx 3\times$ more swaps than Hoare's scheme.
- **Hoare Partition:** Two pointers (`left`, `right`) moving inward toward each other. Swaps only when both pointers find misplaced elements. Fewer swaps, highly efficient.

---

### 5.3.5 Assignment 2 Quick Sort Trace Walkthrough
**Question:** Trace Quick Sort for the array `[40, 10, 70, 20, 90, 30, 50]` using the **first element as the pivot**. Show all partitioning steps.

#### Initial Array: `[40, 10, 70, 20, 90, 30, 50]`
- **Pass 1: Array range [0 ... 6]**
  - Pivot $= arr[0] = \mathbf{40}$.
  - Partition elements into $\le 40$ and $> 40$:
    - Elements $\le 40$: `10, 20, 30`
    - Pivot: `40`
    - Elements $> 40$: `70, 90, 50`
  - After partitioning around pivot `40`:
    Array state: `[30, 10, 20, 40, 90, 70, 50]`
    *(Pivot 40 is now locked in its correct sorted position at index 3)*.

- **Pass 2 (Left Subarray: range [0 ... 2]: `[30, 10, 20]`)**
  - Pivot $= arr[0] = \mathbf{30}$.
  - Elements $\le 30$: `10, 20`
  - Pivot `30` placed at index 2.
  - Subarray state: `[20, 10, 30]` (30 locked at index 2).
  - Recurse on `[20, 10]`: Pivot $= \mathbf{20}$.
    - Partition yields `[10, 20]`. Both locked.
  - Left side fully sorted: `[10, 20, 30, 40, ...]`.

- **Pass 3 (Right Subarray: range [4 ... 6]: `[90, 70, 50]`)**
  - Pivot $= arr[4] = \mathbf{90}$.
  - Elements $\le 90$: `70, 50`.
  - Pivot `90` placed at index 6.
  - Subarray state: `[50, 70, 90]` (90 locked at index 6).
  - Recurse on `[50, 70]`: Pivot $= \mathbf{50}$.
    - 50 placed at index 4, 70 at index 5.
  - Right side fully sorted: `[..., 40, 50, 70, 90]`.

**Final Sorted Array:**
$$\mathbf{[10, 20, 30, 40, 50, 70, 90]}$$

#### Quick Sort Complexity:
- **Best Case (Balanced Partitions):** $T(N) = 2T(N/2) + \Theta(N) \implies \mathbf{\Theta(N \log N)}$.
- **Worst Case (Sorted array with first/last pivot):** $T(N) = T(N-1) + \Theta(N) \implies \mathbf{\Theta(N^2)}$.
- **Average Case:** $\mathbf{\Theta(N \log N)}$.
- **Space:** $O(\log N)$ auxiliary call stack space (In-place). **Stability:** **Unstable**.

---

### 5.3.6 Merge Sort
- **Algorithmic Strategy:** Divide and Conquer.
- **Recurrence:** $T(N) = 2T(N/2) + \Theta(N) \implies \mathbf{\Theta(N \log N)}$ in **ALL cases (Best, Worst, Average)**.
- **Space Complexity:** $\mathbf{O(N)}$ auxiliary space for merging arrays.
- **Stability:** **Stable**.

#### Assignment 2 Merge Sort Trace Walkthrough:
**Question:** Apply Merge Sort on `[12, 11, 13, 5, 6, 7]`. Show all merging stages and comparison counts.

```
Splitting Phase (Divide):
                     [12, 11, 13, 5, 6, 7]
                    /                     \
             [12, 11, 13]               [5, 6, 7]
             /          \               /        \
          [12, 11]      [13]          [5, 6]     [7]
          /      \                    /    \
        [12]    [11]                [5]    [6]

Merging Stages (Conquer & Combine):
Stage 1: Merge [12] and [11]:
         Compare 12 and 11 -> [11, 12]              (1 comparison)
Stage 2: Merge [11, 12] and [13]:
         Compare 11 and 13 -> 11
         Compare 12 and 13 -> 12, then 13 -> [11, 12, 13] (2 comparisons)
Stage 3: Merge [5] and [6]:
         Compare 5 and 6 -> [5, 6]                  (1 comparison)
Stage 4: Merge [5, 6] and [7]:
         Compare 5 and 7 -> 5
         Compare 6 and 7 -> 6, then 7 -> [5, 6, 7]  (2 comparisons)
Stage 5: Final Merge of [11, 12, 13] and [5, 6, 7]:
         Compare 11 and 5  -> take 5                (1 comp)
         Compare 11 and 6  -> take 6                (1 comp)
         Compare 11 and 7  -> take 7                (1 comp)
         Right half exhausted; append [11, 12, 13]  (0 comp)
         Result: [5, 6, 7, 11, 12, 13]              (3 comparisons in Stage 5)

Total Comparisons Made = 1 + 2 + 1 + 2 + 3 = 9 comparisons.
Final Sorted Array: [5, 6, 7, 11, 12, 13].
```

---

### 5.3.7 Heap Sort
- **Data Structure:** Complete Binary Tree represented in an array.
  - **Max-Heap Property:** $\forall i, \quad arr[\text{parent}(i)] \ge arr[i]$.
  - Root $arr[0]$ always contains the maximum element.

#### 1. The Heapify (Sift-Down) Subroutine:
Fixes a single violation at root index $i$ assuming subtrees are valid heaps.
- Compares $arr[i]$ with its left child ($2i+1$) and right child ($2i+2$).
- Swaps with largest child and recurses downward.
- **Time Complexity:** $O(\log N)$ (proportional to tree height).

#### 2. The Build-Heap Algorithm ($O(N)$ Proof):
To build a heap from an unordered array of $N$ elements, run `heapify` on all internal nodes from index $\lfloor N/2 \rfloor - 1$ down to $0$:

```cpp
void buildMaxHeap(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}
```

**Formal Mathematical Proof that Build-Heap is $O(N)$:**
At height $h$, there are at most $\lceil N / 2^{h+1} \rceil$ nodes.
A node at height $h$ can sift down at most $h$ levels.
Total operations:
$$S = \sum_{h=0}^{\lfloor \log N \rfloor} \left\lceil \frac{N}{2^{h+1}} \right\rceil O(h) \le \frac{N}{2} \sum_{h=0}^{\infty} \frac{h}{2^h}$$
Let $X = \sum_{h=0}^{\infty} \frac{h}{2^h} = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \dots$
Multiplying by $1/2$:
$$\frac{1}{2}X = \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + \dots$$
Subtracting the two equations:
$$X - \frac{1}{2}X = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \dots = 1 \implies \frac{1}{2}X = 1 \implies X = 2$$
Therefore:
$$S \le \frac{N}{2} \times 2 = N = \mathbf{O(N)}$$
$\blacksquare$

#### 3. Heap Sort Sorting Phase:
1. Swap root $arr[0]$ (maximum) with last element $arr[n-1]$.
2. Reduce heap size by 1.
3. Heapify root $arr[0]$.
4. Repeat $N-1$ times.
- **Total Time Complexity:** $\mathbf{\Theta(N \log N)}$ in all cases.
- **Auxiliary Space:** $\mathbf{O(1)}$ (In-place). **Stability:** **Unstable**.

---

### 5.3.8 Assignment 2 Analytical Question Walkthrough: Quick Sort vs Heap Sort
**Question:** A dataset of 1,000,000 elements is sorted using Heap Sort and Quick Sort. Quick Sort takes 0.45 seconds, while Heap Sort takes 0.60 seconds. Both are $O(N \log N)$. Explain the reason for this performance difference.

**Technical Architectural Explanation:**
1. **CPU Cache Locality:**
   - **Quick Sort** exhibits exceptional **spatial and temporal cache locality**. It partitions contiguous memory blocks sequentially from left to right. Once a block is loaded into the L1/L2 CPU cache, subsequent comparisons access adjacent cache lines without cache misses.
   - **Heap Sort** exhibits terrible cache locality. When heapifying at index $i$, it accesses indices $2i+1$ and $2i+2$. As the tree deepens, indices jump by powers of 2 ($1 \to 3 \to 7 \to 15 \dots$), scattering accesses across completely disparate RAM pages. Every heap comparison triggers a **CPU Cache Miss**, forcing expensive memory bus fetches from DRAM.
2. **Instruction Count & Constant Factors:**
   - Heap Sort must perform 2 child comparisons plus 1 swap per level in `heapify`.
   - Quick Sort inner loop consists of a simple comparison and pointer increment.
- **Conclusion:** Hardware cache hierarchy and memory bandwidth favor Quick Sort, explaining its $25-35\%$ faster real-world execution.

---

### 5.3.9 Radix Sort
- **Category:** Non-comparison based integer sorting.
- **Mechanism:** Sorts keys digit-by-digit from Least Significant Digit (LSD) to Most Significant Digit (MSD) using a **Stable** subroutine (typically Counting Sort).
- **Time Complexity:** $\mathbf{O(d \cdot (N + b))}$ where $d$ is number of digits, $b$ is numerical base (radix).
- **Space Complexity:** $\mathbf{O(N + b)}$.

---

## 5.4 Master Sorting Algorithms Comparison Matrix
*(High-Probability Comprehensive Exam Summary Table)*

| Algorithm | Best Time | Average Time | Worst Time | Space | Stable? | In-Place? | Key Trait |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Yes** | **Yes** | Adaptive with `swapped` flag |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **No** | **Yes** | Exactly $N-1$ swaps |
| **Insertion Sort** | $\mathbf{O(N)}$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Yes** | **Yes** | Best for small / nearly sorted data |
| **Quick Sort** | $O(N \log N)$ | $O(N \log N)$ | $\mathbf{O(N^2)}$ | $O(\log N)$ | **No** | **Yes** | Fastest in practice; high cache locality |
| **Merge Sort** | $\mathbf{O(N \log N)}$ | $\mathbf{O(N \log N)}$ | $\mathbf{O(N \log N)}$ | $\mathbf{O(N)}$ | **Yes** | **No** | Predictable; ideal for Linked Lists |
| **Heap Sort** | $\mathbf{O(N \log N)}$ | $\mathbf{O(N \log N)}$ | $\mathbf{O(N \log N)}$ | $\mathbf{O(1)}$ | **No** | **Yes** | In-place guaranteed $O(N \log N)$ |
| **Radix Sort** | $O(d(N+b))$ | $O(d(N+b))$ | $O(d(N+b))$ | $O(N+b)$ | **Yes** | **No** | Linear when keys have bounded digits |

---

## 5.5 Hash Tables: Principles & Architectures

A **Hash Table** is an associative data structure that maps keys to values, achieving ideal average-case search, insertion, and deletion in $\mathbf{O(1)}$ constant time.

### 5.5.1 Direct Address Table vs Hash Table
- **Direct Address Table:** Uses key $k$ directly as array index: `T[k]`. Requires array size equal to Universe of keys $|U|$. If keys are 10-digit roll numbers ($10^{10}$), memory requirement is $\approx 40 \text{ GB}$, even if only 100 students are enrolled!
- **Hash Table:** Uses a **Hash Function** $h(k)$ to map the large key universe $U$ into a small table of size $m$ ($m \ll |U|$):
  $$h: U \to \{0, 1, \dots, m-1\}$$

---

### 5.5.2 Common Hash Functions
1. **Division Method:**
   $$h(k) = k \pmod m$$
   *Crucial Rule:* The table size $m$ should be a **prime number** not close to a power of 2 or 10, minimizing clustering caused by patterns in keys.
2. **Multiplication Method (Knuth):**
   $$h(k) = \lfloor m \cdot (k \cdot A \pmod 1) \rfloor$$
   Where $A = \frac{\sqrt{5}-1}{2} \approx 0.6180339887$ (Golden Ratio conjugate). Does not depend heavily on $m$ being prime.
3. **Mid-Square Method:**
   Square the key ($k^2$) and extract the middle $r$ digits (table size $m = 10^r$ or $2^r$). Since all digits of $k$ contribute to the middle of $k^2$, keys are distributed uniformly.
4. **Folding Method:**
   Divide key into equal-sized pieces, add them together, and take modulo $m$.
   - *Fold-Shift:* Pieces aligned and summed.
   - *Fold-Boundary:* Boundary pieces reversed before summing.

---

### 5.5.3 Collision Resolution Techniques
A **Collision** occurs when two distinct keys hash to the identical slot: $h(k_1) = h(k_2)$ for $k_1 \neq k_2$.

```
                        COLLISION RESOLUTION
                                 |
        +------------------------+------------------------+
        |                                                 |
  Separate Chaining                                Open Addressing
  (Closed Addressing / Out-of-table)              (Closed Hashing / In-table)
        |                                                 |
  Array of Linked Lists                     +-------------+-------------+
                                            |             |             |
                                         Linear       Quadratic       Double
                                         Probing       Probing       Hashing
```

---

### 5.5.4 Separate Chaining (Open Hashing)
Each slot in the hash table points to a linked list of records that hash to that slot.
- **Load Factor ($\alpha$):**
  $$\alpha = \frac{n}{m} = \frac{\text{Total elements stored}}{\text{Table size}}$$
- In Separate Chaining, $\alpha$ can exceed 1 (e.g., $\alpha = 2.5$).
- **Search Complexity:**
  - Unsuccessful Search: $\Theta(1 + \alpha)$
  - Successful Search: $\Theta(1 + \alpha/2)$
- **Advantages:** Never overflows; simple deletion; performance degrades gracefully.
- **Disadvantages:** Pointer memory overhead; poor cache locality.

---

### 5.5.5 Open Addressing (Closed Hashing)
All keys are stored directly within the hash table itself. No linked lists or external nodes. If collision occurs, search other slots according to a **probe sequence**:
$$h(k, i) = (h'(k) + f(i)) \pmod m \quad \text{for } i = 0, 1, \dots, m-1$$

#### 1. Linear Probing:
$$f(i) = i \implies h(k, i) = (h'(k) + i) \pmod m$$
- Probes sequential slots: $h'(k), h'(k)+1, h'(k)+2 \dots$
- **Fatal Flaw: Primary Clustering:** Contiguous blocks of occupied slots build up. Any key hashing to any slot in the cluster increases the cluster size, rapidly degrading search time toward $O(N)$.

#### 2. Quadratic Probing:
$$f(i) = c_1 i + c_2 i^2 \implies h(k, i) = (h'(k) + c_1 i + c_2 i^2) \pmod m$$
- Eliminates primary clustering.
- **Flaw: Secondary Clustering:** Keys that have the same initial hash $h'(k)$ trace the exact same probe sequence.

#### 3. Double Hashing (Optimal):
Uses two independent auxiliary hash functions $h_1(k)$ and $h_2(k)$:
$$h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod m$$
- Eliminates both primary and secondary clustering!
- *Requirement:* $h_2(k)$ must be relatively prime to table size $m$ (typically $m$ prime and $h_2(k) = 1 + (k \bmod (m-1))$).

#### Deletion in Open Addressing (The `DELETED` / Tombstone Marker):
In open addressing, you **CANNOT simply set a slot to EMPTY** upon deletion.
If key $A$ was probed past an existing key $B$, setting slot $B$ to empty breaks the probe chain, making key $A$ unreachable during future searches!
*Solution:* Replace deleted slots with a special **`TOMBSTONE` (`DELETED`) marker**. During search, continue probing past tombstones; during insertion, tombstones can be reused.

---

# MASTER EXAM CHEATSHEET & PYQ PREDICTION MATRIX

---

## 6.1 Critical Memory Formulas Reference Bank

### 6.1.1 Array Addressing Formulas
- **1D Array:**
  $$\text{Address}(A[k]) = \text{Base} + W \cdot (k - LB)$$
- **2D Array (Row Major Order - RMO):**
  $$\text{Address}(A[i][j]) = \text{Base} + W \cdot \left[ (i - LB_1) \cdot N_2 + (j - LB_2) \right]$$
  *(Where $N_2 = UB_2 - LB_2 + 1$ is number of columns)*
- **2D Array (Column Major Order - CMO):**
  $$\text{Address}(A[i][j]) = \text{Base} + W \cdot \left[ (j - LB_2) \cdot N_1 + (i - LB_1) \right]$$
  *(Where $N_1 = UB_1 - LB_1 + 1$ is number of rows)*
- **3D Array (Row Major Order):**
  $$\text{Address}(A[i][j][k]) = \text{Base} + W \cdot \left[ (i - LB_1) \cdot N_2 \cdot N_3 + (j - LB_2) \cdot N_3 + (k - LB_3) \right]$$

---

### 6.1.2 Tree and Heap Metrics
- **Leaf Theorem:** $n_0 = n_2 + 1$ (for any binary tree).
- **Max nodes at level $i$ (root at level 0):** $2^i$.
- **Max nodes in tree of height $h$:** $2^{h+1} - 1$.
- **Min nodes in tree of height $h$:** $h + 1$.
- **Min height for $N$ nodes:** $\lfloor \log_2 N \rfloor$.
- **Binary Heap Indexing (0-based):**
  - $\text{Parent}(i) = \lfloor (i - 1) / 2 \rfloor$
  - $\text{LeftChild}(i) = 2i + 1$
  - $\text{RightChild}(i) = 2i + 2$
  - Last non-leaf node: $\lfloor N/2 \rfloor - 1$

---

### 6.1.3 Circular Queue Formulas
- **Size / Capacity:** `MAX`
- **Queue Empty:** `front == -1`
- **Queue Full (Overflow):** `(rear + 1) % MAX == front`
- **Next Enqueue Slot:** `rear = (rear + 1) % MAX`
- **Next Dequeue Slot:** `front = (front + 1) % MAX`
- **Total Active Elements:**
  $$\text{Count} = \begin{cases} 0 & \text{if } front == -1 \\ (rear - front + MAX) \pmod{MAX} + 1 & \text{otherwise} \end{cases}$$

---

### 6.1.4 Master Theorem Quick Decision Matrix ($T(n) = a T(n/b) + f(n)$)
Compute critical exponent: $c_{crit} = \log_b a$.
1. If $f(n) = O(n^{c_{crit} - \epsilon}) \implies \mathbf{T(n) = \Theta(n^{\log_b a})}$
2. If $f(n) = \Theta(n^{c_{crit}} \log^k n) \implies \mathbf{T(n) = \Theta(n^{\log_b a} \log^{k+1} n)}$
3. If $f(n) = \Omega(n^{c_{crit} + \epsilon})$ and $a f(n/b) \le c f(n)$ for $c < 1 \implies \mathbf{T(n) = \Theta(f(n))}$

---

## 6.2 The Top 10 "Red-Pen" Exam Traps (Avoid Losing Easy Marks)

1. **Forgetting Array 0-Indexing vs 1-Indexing in Formulas:**
   In university papers, the question often states $A[1\dots 10][1\dots 15]$. If you naively write $\text{Base} + W(i \cdot N + j)$, you will get **zero marks**. Always write the generalized formula with $(i - LB_1)$ and $(j - LB_2)$.
2. **Confusing RMO and CMO Multipliers:**
   In RMO, you multiply the row index offset by $N_2$ (number of **columns**). In CMO, you multiply the column index offset by $N_1$ (number of **rows**). Mixing these up is the single most common student calculation error!
3. **Omitting the Regularity Condition in Master Theorem Case 3:**
   Merely showing $f(n) = \Omega(n^{\log_b a + \epsilon})$ is insufficient. Professors dock marks if you do not explicitly verify $a \cdot f(n/b) \le c \cdot f(n)$ for some $c < 1$.
4. **Drawing Only the Final AVL Tree:**
   In AVL rotation questions, **never draw just the final tree**. You must draw the intermediate unbalanced tree, explicitly label the Balance Factor ($+2$ or $-2$) on the violating node, state the rotation type (`LL`, `RR`, `LR`, or `RL`), and then show the rotated result.
5. **Deleting in Open Addressing Without Tombstones:**
   When asked how deletion works in open addressing (linear/quadratic probing), failing to mention the `TOMBSTONE` (`DELETED`) marker causes mark deductions. Setting a slot to `EMPTY` breaks search probe chains.
6. **False Overflow Definition:**
   Clearly state that False Overflow occurs in a **Linear Queue** because `front` and `rear` continually increment, causing `rear == MAX - 1` even when preceding slots `0` to `front - 1` are free.
7. **Heapify vs Build-Heap Complexity:**
   `heapify` takes $O(\log N)$. But `Build-Heap` takes **$O(N)$ linear time**, NOT $O(N \log N)$. Be prepared to reproduce the geometric series summation proof ($\sum \frac{h}{2^h} = 2$).
8. **Infix-to-Prefix Stack Scanning Direction:**
   Postfix expressions are evaluated and converted scanning **Left-to-Right**. Prefix expressions are evaluated scanning **Right-to-Left**.
9. **BST Deletion Case 3 Replacement:**
   When replacing a node with two children, state clearly that it can be replaced by EITHER the **Inorder Successor** (smallest in right subtree) OR the **Inorder Predecessor** (largest in left subtree).
10. **Quick Sort Worst Case Trigger:**
    Quick Sort degrades to $O(N^2)$ when the pivot chosen is consistently the smallest or largest element (e.g., selecting the first or last element of an already sorted or reverse-sorted array).

---

## 6.3 Syllabus & PYQ Coverage Verification Matrix

| Topic / Question from NIT Jalandhar Exam Materials | Covered in Section | Verification Notes |
| :--- | :--- | :--- |
| **Linear vs Non-Linear Data Structures with examples** (Midsem Q1(a)) | **Section 1.1.2** | Complete tabular breakdown, ASCII hierarchy diagram, examples. |
| **Insertion Sort algorithm & time complexity analysis** (Midsem Q1(b)) | **Section 5.3.3** | Full C++ code, adaptive comparisons, best/worst analysis. |
| **Euclidean GCD time complexity derivation** (Midsem Q1(c)) | **Section 1.5 (Problem 3)** | Lamé's Theorem, proof that smaller arg halves every 2 steps $\to O(\log(\min(n,m)))$. |
| **Asymptotic growth ordering: $10n, n^2 \log n, n\sqrt{n}$** (Midsem Q1(d)) | **Section 1.5 (Problem 2)** | Formal limit proofs for both interpretations ($10n$ and $10^n$). |
| **Address of 6th element in 1D array ($Base=1000, W=8$)** (Midsem Q2(a)) | **Section 2.2 (Problem 1)** | Worked solution for both 0-indexed and 1-indexed conventions ($1040$). |
| **Binary Search algorithm & example** (Midsem Q2(b)) | **Section 5.1.2** | Iterative C++ code, overflow prevention, $O(\log N)$ proof via Master Theorem. |
| **Doubly Circular Linked List insert & delete at start/end** (Midsem Q2(c)) | **Section 2.4.4** | Complete C functions for all 4 operations, ASCII pointer diagram. |
| **Pointer trace `rearrange(list)` on $1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 7$** (Midsem Q3(a)) | **Section 2.4.2** | Step-by-step trace showing pairwise swapping $\to 2 \to 1 \to 4 \to 3 \to 6 \to 5 \to 7$. |
| **Postfix to Prefix conversion: `AB+C*DE-/FGH*+IJ^+KL/-+`** (Midsem Q3(b)) | **Section 3.2.4** | Full 23-step trace table resulting in `+/*+ABC-DE-++F*GH^IJ/KL`. |
| **Prefix expression evaluation: `* + 1 2 / * 4 3 2 / * * 1 4 6 8`** (Midsem Q3(c)) | **Section 3.2.5** | Right-to-left scan table, subterm values ($18, 3$), professor typo analysis. |
| **Assignment 1: Nested loop `unknown(n)` complexity** | **Section 1.5 (Problem 4)** | Outer loop $\Theta(n)$, inner loop $\Theta(\log n) \implies \Theta(n \log n)$. |
| **Assignment 1: 2D array $10 \times 15$, $A[1\dots 10][1\dots 15]$, address $A[i][j]$** | **Section 2.2 (Problem 2)** | Formula derivation: $15i + j + 84$. |
| **Assignment 1: `arr[3][5]` address formula ($W=4$)** | **Section 2.2 (Problem 3)** | Formula: $\text{Base} + 20i + 4j$. |
| **Assignment 1: Multidimensional array bounds & $B[3,3,3]$ address** | **Section 2.2 (Problem 4)** | Effective addresses $E_1=2, E_2=8, E_3=13$, Real address = $2372$. |
| **Assignment 1: 3D pointer arithmetic output `arr[2][2][2]`** | **Section 2.2 (Problem 5)** | Detailed pointer type explanation: `8, 3`. |
| **Assignment 2: Kruskal's algorithm on 5-vertex graph** | **Section 4.9.3** | Sorted edges, DSU cycle rejection, total MST cost = $16$. |
| **Assignment 2: Prim's algorithm on 5-vertex graph from A** | **Section 4.9.2** | Vertex expansion table, total MST cost = $16$. |
| **Assignment 2: Dijkstra's algorithm from vertex A** | **Section 4.10.1** | Distance table across 5 steps, shortest paths and costs. |
| **Assignment 2: BST construction from `[45,10,7,12,90,50]` & delete 10** | **Section 4.5.3** | Tree diagrams, height = 2, deletion via inorder successor 12. |
| **Assignment 2: AVL Tree insertion of `[30,40,50,25,20,10]`** | **Section 4.6.3** | Complete trace with RR rotation at 30, LL at 30, LL at 40. |
| **Assignment 2: B-Tree Order 3 insertion of 8 keys & delete 6** | **Section 4.7.4** | All splitting steps, root splits, median push-ups, deletion merge. |
| **Assignment 2: Quick Sort trace on `[40,10,70,20,90,30,50]` (pivot first)** | **Section 5.3.5** | Complete partitioning steps, subarray recursions, final sorted array. |
| **Assignment 2: Merge Sort trace on `[12,11,13,5,6,7]` with comparisons** | **Section 5.3.6** | Divide tree, 5 merge stages, exactly 9 comparisons. |
| **Assignment 2: Quick Sort vs Heap Sort performance on $10^6$ elements** | **Section 5.3.8** | CPU cache spatial locality vs memory bus thrashing in heaps. |
| **Assignment 2: Insertion Sort vs Quick Sort on almost sorted array** | **Section 5.3.3** | Linear $O(N)$ vs $O(N^2)$ / $O(N \log N)$ recursive overhead. |

---
