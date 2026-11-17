# generate_appendices.py
# Generates Appendices: Cheat Sheets, C++ Implementations, and NIT Jalandhar Exam Solutions

def get_appendices_text():
    return r"""# APPENDICES: CODE IMPLEMENTATIONS, PYQ SOLUTIONS & EXAM CHEAT SHEET

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
"""

if __name__ == "__main__":
    print(f"Appendices generated: {len(get_appendices_text())} characters")
