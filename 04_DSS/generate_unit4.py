# generate_unit4.py
# Generates Unit 4: Binary Trees & Tree Algorithms

def get_unit4_text():
    return r"""# UNIT 4: BINARY TREES, TREE ALGORITHMS & DATA STRUCTURES

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
"""

if __name__ == "__main__":
    print(f"Unit 4 generated: {len(get_unit4_text())} characters")
