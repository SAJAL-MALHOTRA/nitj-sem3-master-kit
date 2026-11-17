# Data Structures Notes: Complexity Analysis, Arrays & Searching (C++)

> Covers Unit 1 (Introduction & Complexity) and part of Unit 2 (Arrays) topics — directly matching Q1 and Q2(a)/(b) style questions from the Sept 2025 Mid-Sem paper.

---

## 1. Linear vs Non-Linear Data Structures

### Linear Data Structure
Elements are arranged **sequentially/linearly**, where each element (except first & last) has exactly one predecessor and one successor. Only a **single level** is involved — easy to traverse in one pass.

**Examples:** Array, Stack, Queue, Linked List.

```cpp
int arr[5] = {10, 20, 30, 40, 50};   // linear: 10→20→30→40→50, single level
```

### Non-Linear Data Structure
Elements are arranged **hierarchically**; an element can be connected to **multiple** other elements, so traversal may require multiple passes/paths.

**Examples:** Tree, Graph.

```
        A                (Non-linear: Tree)
       / \
      B   C
     / \
    D   E
```

| Linear DS | Non-Linear DS |
|---|---|
| Single-level arrangement | Hierarchical / multi-level arrangement |
| Easy to implement, sequential traversal | Traversal is complex (DFS/BFS) |
| Memory utilization is efficient for fixed size | Memory utilization depends on structure |
| E.g. Array, Stack, Queue, Linked List | E.g. Tree, Graph |

---

## 2. Algorithm Efficiency & Time-Space Complexity

**Time Complexity:** Amount of time an algorithm takes as a function of input size `n`.
**Space Complexity:** Amount of memory an algorithm needs as a function of `n`.
**Time-Space Trade-off:** Often you can reduce time complexity by using more memory (e.g., hashing, memoization) and vice versa — you rarely optimize both simultaneously.

### Asymptotic Notations

| Notation | Meaning | Represents |
|---|---|---|
| **Big-O (O)** | Upper bound | Worst-case time |
| **Big-Omega (Ω)** | Lower bound | Best-case time |
| **Big-Theta (Θ)** | Tight bound (both upper & lower) | Average/exact-order time |

- `f(n) = O(g(n))` if there exist constants `c > 0, n0` such that `f(n) ≤ c·g(n)` for all `n ≥ n0`.
- Common growth orders (fastest to slowest):
  `O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)`

### Worked Example — Finding Time Complexity of Recursive Code

```c
int gcd(int n, int m) {
    if (n % m == 0) return m;
    n = n % m;
    return gcd(m, n);
}
```

**Analysis:**
- This is the **Euclidean algorithm** for GCD, implemented recursively.
- Each recursive call reduces the values roughly by a factor related to the modulo operation — it can be shown that after **two** recursive calls, the value of `m` reduces to **less than half** its original value (a classic result for the Euclidean algorithm).
- Therefore the number of recursive calls is bounded by **O(log(min(n, m)))**.
- **Time Complexity: O(log n)** (logarithmic in the smaller of the two inputs).
- **Space Complexity: O(log n)** — due to the recursive call stack (each call adds a stack frame until the base case `n % m == 0`).

> **Exam tip:** For recursive functions, always check (1) how much the problem size shrinks per call, and (2) the recursion depth → that depth times work-per-call gives you the complexity.

### Worked Example — Ordering Functions by Growth Rate

**Given:** `f1 = 10n`, `f2 = n^(2 log n)`, `f3 = n^(√n)`

**Approach:** Take `log` of each function to compare exponents easily (log simplifies comparison of exponential-type functions):
- `log(f1) = log(10n) = O(log n)`
- `log(f2) = 2·log(n)·log(n) = O((log n)²)`
- `log(f3) = √n · log(n)`

Now compare the exponents' growth:
- `log n` grows slower than `(log n)²`
- `(log n)²` grows slower than `√n · log n` (since `√n` grows much faster than `log n`)

So: `log(f1) < log(f2) < log(f3)` ⟹ **`f1 < f2 < f3`**

**Answer (increasing order of asymptotic growth rate):** `f1 = 10n  <  f2 = n^(2 log n)  <  f3 = n^(√n)`

---

## 3. Arrays

### 3.1 Definition
An array is a collection of elements of the **same data type**, stored in **contiguous memory locations**, accessed using an index.

### 3.2 1D Array — Address Calculation Formula

```
Address(A[i]) = Base Address + (i - Lower Bound) × Size of each element
```
(If array is 0-indexed, Lower Bound = 0, so it simplifies to `Base + i × size`.)

**Worked Example:** Find the address of the **6th element** of a 1D array where **Base Address = 1000** and each element occupies **8 bytes**.

- If array indexing starts at 1 (1-based, as commonly assumed in these problems):
  `Address(A[6]) = Base + (6 - 1) × 8 = 1000 + 5×8 = 1000 + 40 = 1040`

- If array indexing is 0-based and "6th element" means index 5:
  `Address(A[5]) = Base + 5 × 8 = 1000 + 40 = 1040` (same result either way here since "6th element" = 5 elements before it)

**Answer: 1040**

```cpp
int addressOf1D(int base, int elementSize, int index /* 1-based position */) {
    return base + (index - 1) * elementSize;
}
```

### 3.3 2D Array Address Calculation

**Row-Major Order:** elements stored row by row.
```
Address(A[i][j]) = Base + [(i - LR) × N + (j - LC)] × Size
```
where `N` = number of columns, `LR`/`LC` = lower bounds of row/column index.

**Column-Major Order:** elements stored column by column.
```
Address(A[i][j]) = Base + [(j - LC) × M + (i - LR)] × Size
```
where `M` = number of rows.

### 3.4 Sparse Matrix
A matrix where **most elements are zero**. Storing it as a full 2D array wastes memory, so it's represented compactly — typically as a list of triplets:

```cpp
struct Triplet {
    int row, col, value;
};
```
Each non-zero element is stored as `(row, col, value)`, drastically reducing space for large, mostly-empty matrices. Common representations: **Triplet (coordinate list)** and **Linked list representation**.

---

## 4. Searching Algorithms

### 4.1 Linear (Sequential) Search
Check every element one by one until found or the list ends.

```cpp
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (arr[i] == key) return i;
    return -1;
}
```
**Time Complexity:** Best O(1), Worst/Average **O(n)**. Works on unsorted arrays.

### 4.2 Binary Search
Works only on a **sorted array**. Repeatedly divide the search interval in half.

**Algorithm:**
1. Set `low = 0`, `high = n - 1`.
2. While `low <= high`:
   - `mid = (low + high) / 2`
   - If `arr[mid] == key` → found.
   - If `arr[mid] < key` → search right half: `low = mid + 1`
   - Else → search left half: `high = mid - 1`
3. If loop ends without finding, key is not present.

```cpp
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) return mid;
        else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
```

**Worked Example:** Search `key = 23` in sorted array `[4, 8, 15, 16, 23, 42, 56]` (n=7, indices 0-6).

| Step | low | high | mid | arr[mid] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 16 | 16 < 23 → low = 4 |
| 2 | 4 | 6 | 5 | 42 | 42 > 23 → high = 4 |
| 3 | 4 | 4 | 4 | 23 | Found at index 4 ✅ |

**Time Complexity:** O(log n) — halves the search space each step.
**Space Complexity:** O(1) iterative, O(log n) if implemented recursively (call stack).

### 4.3 Linear vs Binary Search

| Linear Search | Binary Search |
|---|---|
| Works on unsorted/sorted array | Requires **sorted** array |
| O(n) time | O(log n) time |
| Simple, no pre-processing | Needs sorted input |

---

## 5. Sorting — Insertion Sort

### 5.1 Idea
Builds the sorted array **one element at a time** — like sorting playing cards in hand. Take the next element and insert it into its correct position among the already-sorted portion.

### 5.2 Algorithm
```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        // shift elements of arr[0..i-1] that are greater than key
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

### 5.3 Worked Example
Array: `[12, 11, 13, 5, 6]`

| Pass | Array State | Explanation |
|---|---|---|
| Start | 12, 11, 13, 5, 6 | key = 11 |
| 1 | 11, 12, 13, 5, 6 | 11 inserted before 12 |
| 2 | 11, 12, 13, 5, 6 | key=13, already in place |
| 3 | 5, 11, 12, 13, 6 | key=5, shifted to front |
| 4 | 5, 6, 11, 12, 13 | key=6, inserted after 5 |

**Final sorted array:** `[5, 6, 11, 12, 13]`

### 5.4 Time & Space Complexity Analysis

| Case | Complexity | Reason |
|---|---|---|
| Best Case | **O(n)** | Array already sorted → inner `while` never executes (only comparisons) |
| Average Case | **O(n²)** | Roughly half of the elements need shifting on average |
| Worst Case | **O(n²)** | Array sorted in reverse → every new element shifts all previous elements |
| Space Complexity | **O(1)** | Sorts in-place, no extra array needed |

**Stability:** Insertion sort is a **stable** sort (equal elements retain relative order) — useful to mention in exams.

---

## 6. Likely Exam Questions
1. Differentiate linear and non-linear data structures with examples.
2. Find time complexity of a given recursive/iterative code snippet (show step-by-step reasoning).
3. Arrange given functions in increasing/decreasing order of asymptotic growth rate (use log-comparison trick).
4. Calculate the address of an element in a 1D/2D array (row-major & column-major).
5. Write and trace the Binary Search algorithm on a sorted array; state its complexity.
6. Write and trace the Insertion Sort algorithm; analyze best/worst/average case complexity.
7. Explain sparse matrix representation and why it saves memory.
8. Compare Big-O, Big-Omega, and Big-Theta notations with examples.
