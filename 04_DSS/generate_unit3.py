# generate_unit3.py
# Generates Unit 3: Graph Theory

def get_unit3_text():
    return r"""# UNIT 3: GRAPH THEORY & NETWORK ARCHITECTURES

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
"""

if __name__ == "__main__":
    print(f"Unit 3 generated: {len(get_unit3_text())} characters")
