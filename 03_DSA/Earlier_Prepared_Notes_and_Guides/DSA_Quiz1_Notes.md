# Data Structures (ITDC0203) — Quiz 1 Prep Notes
*Covers: Intro to DS/Algorithms, Complexity, ADTs, Arrays, Sparse Matrices, Singly Linked Lists*

---

## 1. Basic Terminology & Elementary Data Organization

**Data** = raw facts. **Information** = processed data with meaning.
**Data Structure** = a way of organizing data so it can be used efficiently — considers both storage and the operations allowed on it (insert, delete, search, traverse, sort).

**Elementary Data Organization** — the hierarchy:
- **Field** → smallest unit of data (e.g., a single number or name)
- **Record** → collection of related fields (e.g., a student record: roll no, name, marks)
- **File** → collection of related records

**Types of Data Structures:**
- **Primitive**: int, float, char, boolean — built into the language
- **Non-primitive**:
  - *Linear* (elements in sequence): Array, Linked List, Stack, Queue
  - *Non-linear* (elements branch/hierarchical or networked): Tree, Graph

**Operations commonly performed:** Traversal, Insertion, Deletion, Searching, Sorting, Merging.

### Practice Questions
1. Fill in the blank: A ______ is a collection of related data items treated as a single unit, and a ______ is a collection of related records. *(Answer: record; file)*
2. Which of the following is a non-linear data structure? a) Array b) Stack c) Tree d) Queue *(Answer: c)*
3. True/False: A linked list is a non-primitive linear data structure. *(Answer: True)*
4. Why is "int" considered a primitive data type while "array" is not?

---

## 2. Algorithm & Efficiency of an Algorithm

**Algorithm** = a finite, well-defined, ordered sequence of steps to solve a problem, with:
- **Finiteness** — must terminate after finite steps
- **Definiteness** — each step precisely defined, unambiguous
- **Input** — zero or more inputs
- **Output** — at least one output
- **Effectiveness** — steps must be basic enough to be carried out

**Efficiency of an algorithm** is judged by two resources it consumes:
- **Time complexity** — how run time grows with input size *n*
- **Space complexity** — how memory usage grows with input size *n*

This is the classic **fill-in-the-blank PYQ style**: *"The performance of algorithms can be measured on the scale of __(time)__ and __(space)__."*

### Practice Questions
1. The performance of algorithms can be measured on the scale of ……… and ………. *(Answer: Time, Space — this is literally Q1 from your quiz PDF)*
2. Which property of an algorithm ensures it does NOT run forever? a) Input b) Output c) Finiteness d) Effectiveness *(Answer: c)*
3. Give one real-world example where a slower algorithm might be preferred over a faster one. *(Hint: space-constrained embedded systems)*
4. State the five characteristics of an algorithm in your own words.

---

## 3. Time and Space Complexity

**Time complexity** = number of elementary operations as a function of input size *n* (not actual clock time — machine-independent).

**Space complexity** = total memory used = **fixed part** (constants, simple variables, program size) + **variable part** (dynamic memory, recursion stack, depends on *n*).

**Formula:** S(P) = c + S_p(instance characteristics), where c is constant.

**Common complexity classes (fastest → slowest):**
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

| Structure/Operation | Time Complexity |
|---|---|
| Access element at index *i* in a 1D array | **O(1)** |
| Linear search | O(n) |
| Binary search (sorted array) | O(log n) |
| Bubble/Selection/Insertion sort | O(n²) |
| Merge/Quick sort (avg) | O(n log n) |

### Practice Questions (PYQ-style)
1. In a 1D array arr[0...n−1], what is the time complexity of accessing the element at index *i*? a) O(1) b) O(n log n) c) O(log n) d) O(n) *(Answer: a — direct address calculation, no traversal needed)*
2. What is the time complexity for deleting a node at a specific position in a linked list? a) O(1) b) O(n) c) O(n log n) d) O(log n) *(Answer: b — must traverse to reach the position first)*
3. Why is array access O(1) but linked list access at a given position O(n)? Explain using how each stores elements in memory.
4. What is the space complexity of an algorithm that uses a fixed number of variables regardless of input size? *(Answer: O(1) — constant space)*
5. A recursive function that calls itself n times (no branching) has what space complexity due to the call stack? *(Answer: O(n))*

---

## 4. Asymptotic Notations & Time-Space Tradeoff

**Big-O (O)** — **upper bound**; worst-case growth rate. "Algorithm takes *at most* this long."
Formally: f(n) = O(g(n)) if there exist constants c > 0, n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀.

**Big-Omega (Ω)** — lower bound; best-case. f(n) grows *at least* this fast.

**Big-Theta (Θ)** — tight bound; both upper and lower — the *average/exact* growth rate.

*(Your syllabus emphasizes Big-O specifically — know it cold, but recognize Ω and Θ if they appear as distractors in MCQs.)*

**Time–Space Tradeoff**: You can often reduce time complexity by using more memory (e.g., hash tables, memoization/lookup tables) or reduce memory by accepting more computation time (e.g., recomputing values instead of storing them). Neither is universally "better" — depends on constraints.

### Practice Questions
1. Which notation represents the worst-case (upper bound) time complexity of an algorithm? a) Ω b) Θ c) O d) None *(Answer: c)*
2. If f(n) = 3n² + 5n + 2, what is its Big-O complexity? *(Answer: O(n²) — drop constants and lower-order terms)*
3. Give one example of a time-space tradeoff technique. *(Answer: e.g., memoization — storing computed results to avoid recomputation, trading memory for speed)*
4. Is Big-O concerned with the best case, worst case, or average case of an algorithm? *(Answer: worst case — upper bound on growth)*
5. True/False: O(n) is a tighter (smaller) bound than O(n²) for large n. *(Answer: True)*

---

## 5. Abstract Data Types (ADT)

An **ADT** is a mathematical model for a data type defined purely by its **behavior** (the operations you can perform, and what they do) — **not** by how it's implemented internally. It separates *what* from *how*.

Example: A **Stack ADT** is defined by operations `push`, `pop`, `peek`, `isEmpty` — it doesn't matter whether it's implemented using an array or a linked list underneath; the user only sees the defined behavior (LIFO).

| ADT | Key Operations | Behavior |
|---|---|---|
| Stack | push, pop, peek | LIFO |
| Queue | enqueue, dequeue | FIFO |
| List | insert, delete, get | Ordered collection |

### Practice Questions
1. Which data structure is used for implementing recursion? a) Stack b) Queue c) List d) Array *(Answer: a — function call stack is LIFO, matching recursive call/return order)*
2. Why is a Stack called an ADT rather than just a data structure? *(Answer: because it's defined by its operations/behavior, independent of whether it's array- or linked-list-based)*
3. Match: Queue → ______ order; Stack → ______ order. *(Answer: FIFO; LIFO)*
4. Can a Stack ADT be implemented using an array? Using a linked list? Explain briefly why both are valid.

---

## 6. Arrays: Definition, Single & Multidimensional, Applications

**Array** = a collection of homogeneous (same-type) elements stored in **contiguous memory locations**, accessed via an index.

**1D Array:** `arr[0...n-1]` — address of arr[i] = Base + i × size_of_element (this is why access is O(1)).

**Multidimensional Array (2D)**: a "table" of rows and columns, `A[rows][cols]`. Stored in memory using either:

### Row-Major Order
Elements stored row-by-row. For array `A[m][n]` (0-indexed) with base address `B` and element size `w`:
```
Address(A[i][j]) = B + [(i × n) + j] × w
```
(n = number of columns)

### Column-Major Order
Elements stored column-by-column. For `A[m][n]`:
```
Address(A[i][j]) = B + [(j × m) + i] × w
```
(m = number of rows)

**Worked PYQ example:** `int A[3][4]` (row-major), base address = 1000, int = 4 bytes. Find address of A[2][3].
- n (cols) = 4
- Address = 1000 + [(2×4) + 3] × 4 = 1000 + [11] × 4 = 1000 + 44 = **1044**

**Applications of arrays:** storing lists (marks, inventory), matrix representation, implementing other structures (stacks/queues via array), lookup tables, sparse matrix storage, image/pixel data (2D arrays).

### Practice Questions (PYQ-style — practice the address formula, it WILL be tested)
1. Assume `int A[3][4]` is a 2D array in row-major order. What is the address of element A[2][3], if base address is 1000 and each integer takes 4 bytes? a) 1012 b) 1032 c) 1044 d) 1056 *(Answer: c — shown worked above)*
2. Same array, but in **column-major** order — find the address of A[2][3]. *(Work it out: Address = 1000 + [(3×3)+2]×4 = 1000 + 11×4 = 1044. Try changing the indices yourself, e.g., A[1][2], to make sure you're not just pattern-matching the answer.)*
3. For `int B[5][6]`, base address 2000, element size 4 bytes, row-major order — find address of B[3][2].
4. Why is direct address calculation possible for arrays but not for linked lists?
5. Name two real-world applications of 2D arrays.
6. What is the time complexity of accessing element A[i][j] in a 2D array using the address formula? *(Answer: O(1))*

---

## 7. Sparse Matrices and Their Representations

A **sparse matrix** is a matrix in which **most elements are zero**. Storing all elements (including zeros) wastes memory — so we store only the **non-zero elements**.

**Common representations:**

1. **Triplet / 3-Tuple (Array) Representation**: store each non-zero element as `(row, column, value)`. The first row of the triplet table itself stores `(total_rows, total_cols, total_nonzero_count)`.

2. **Linked List Representation**: each node stores `(row, column, value, next)` — useful when the number of non-zero elements changes dynamically.

**Why it matters:** if a matrix is m×n but has only *t* non-zero elements (t << m×n), triplet representation uses O(t) space instead of O(m×n) — a huge saving.

### Practice Questions
1. What defines a matrix as "sparse"? a) All elements are zero b) Most elements are non-zero c) Most elements are zero d) It is always square *(Answer: c)*
2. In triplet representation, what three values are stored for each non-zero element? *(Answer: row index, column index, value)*
3. A 100×100 matrix has only 20 non-zero elements. Compare the space used by normal (2D array) storage vs. triplet representation. *(Normal: 100×100 = 10,000 entries. Triplet: ~20×3 = 60 entries — massive saving)*
4. Give one real-world scenario where sparse matrices naturally occur. *(e.g., adjacency matrix of a graph with few edges, or a document-term matrix in text processing)*
5. True/False: Sparse matrix representation always uses less time for arbitrary element access compared to a normal 2D array. *(Answer: False — triplet form trades O(1) access for O(t) search since it isn't directly indexable)*

---

## 8. Singly Linked Lists

A **Singly Linked List** is a linear data structure where each element (**node**) contains:
- **data**
- **next** — a pointer/reference to the next node (last node's `next` = NULL)

```c
struct Node {
    int data;
    Node* next;
};
```

Unlike arrays, linked list nodes are **not** stored in contiguous memory — they're linked via pointers, so **no direct/random access** (must traverse from `head`).

**Key operations & complexities:**

| Operation | Time Complexity | Why |
|---|---|---|
| Access/Search element | O(n) | must traverse from head |
| Insert at head | O(1) | just repoint head |
| Insert at tail (no tail pointer) | O(n) | must traverse to find last node |
| Insert at given position | O(n) | must traverse to that position |
| Delete at given position | O(n) | must traverse to find it, per your PYQ Q7 |
| Delete at head | O(1) | just move head pointer |

**Recognizing a Circular Linked List (from your PYQ Q8):** If the **last node's `next` points back to `head`** (instead of NULL), it's a **circular linked list**. In your quiz example:
```
head -> Node(10) -> Node(20) -> Node(30) -> head   // last node points back to head!
```
This is a **circular (singly) linked list** — because `next` only goes one direction (no `prev` pointer), it's not doubly linked; because it loops back to head, it's not a plain singly linked list either.

**Counting nodes in a circular linked list** (completing your PYQ Q9's do-while loop):
```c
int countNodes(Node* head) {
    if (head == nullptr) { return 0; }
    Node* current = head;
    int count = 0;
    do {
        count++;
        current = current->next;
    } while (current != head);   // loop until we circle back to head
    return count;
}
```
Key idea: in a **do-while**, the body runs first (correctly counting `head` itself), then the condition `current != head` checks if we've come full circle — this is exactly why do-while (not while) is used here, since a while-loop checking `current != head` *before* entering would need current initialized differently.

**Sorted insertion — worst case (PYQ Q10 style):** Inserting n elements one-by-one into an initially empty linked list, **maintaining sorted order**, each insertion may require traversing up to the full current length to find the correct spot.
- Insertion of the k-th element takes O(k) in the worst case.
- Total: 1 + 2 + ... + n = n(n+1)/2 → **O(n²)** worst case overall.

### Practice Questions (PYQ-style)
1. The time complexity for deleting a node at specific position in a linked list is: a) O(1) b) O(n) c) O(nlogn) d) O(logn) *(Answer: b)*
2. Given: `head -> Node(10) -> Node(20) -> Node(30) -> head`. What does this represent? a) Singly linked list b) Circular linked list c) Doubly linked list d) Not a valid list *(Answer: b)*
3. Complete the do-while loop to count nodes in a circular linked list (write the "statements" and "statement" yourself before checking the version above).
4. ……………. is the worst-case time complexity of inserting n elements into an empty linked list, if the list must remain sorted at all times. *(Answer: O(n²))*
5. Why is insertion at the **head** of a singly linked list O(1), but insertion at the **tail** is O(n) (without a tail pointer)?
6. What is the key structural difference between a singly linked list and a doubly linked list?
7. Write pseudocode to traverse a singly linked list and print all elements.
8. If you only have a pointer to a node (not the head), can you delete that node in a singly linked list in O(1)? Why or why not? *(Hint: think about whether you can access the previous node)*

---

## 9. Sorting-Related Time Complexity (Bubble Sort / Selection Sort — from your PYQ)

**Bubble Sort:** repeatedly swaps adjacent out-of-order elements. Worst case: O(n²) comparisons, and the number of **swaps** varies by input — it equals the number of **inversions** in the array (pairs out of order).

**PYQ walkthrough — counting swaps in bubble sort for `8, 22, 7, 9, 31, 5, 13`:**
Count inversions (pairs (i,j) where i<j but arr[i]>arr[j]):
- 8 > 7, 8 > 5 → 2
- 22 > 7, 22 > 9, 22 > 5, 22 > 13 → 4
- 7 > 5 → 1
- 9 > 5 → 1
- 31 > 5, 31 > 13 → 2
- Total = 2+4+1+1+2 = **10**
*(Matches option (c) in your PYQ — walk through it yourself on paper to build the skill, since these numbers change every year.)*

**Selection Sort:** finds the minimum in the unsorted portion and swaps it into place — **at most one swap per pass**. For n elements, there are n−1 passes → maximum swaps = **n−1**.

### Practice Questions
1. What is the maximum number of swaps in Selection Sort for n elements? a) n−1 b) n c) 1 d) n−2 *(Answer: a)*
2. Count the number of swaps bubble sort performs to sort: `5, 1, 4, 2, 8` in ascending order. *(Try it — count inversions, then verify by simulating the sort manually)*
3. Why does Selection Sort always perform at most n−1 swaps regardless of the input, while Bubble Sort's swap count varies with input? *(Hint: think about what "inversions" measure)*
4. What is the time complexity of Bubble Sort in the worst case? Best case (already sorted, with an early-exit optimization)? *(Answer: O(n²) worst; O(n) best with optimization)*

---

## Quick Self-Test Before the Quiz
Try answering these cold, no notes:
1. Row-major address formula for A[i][j] in an m×n array?
2. What's the time complexity of array access vs. linked list access at index i, and why the difference?
3. Define ADT in one sentence.
4. What makes a linked list "circular"?
5. Worst-case time to build a sorted linked list by repeated sorted insertion?
6. Big-O vs Big-Omega — which is upper bound, which is lower?

Good luck tomorrow!
