# assemble_master_notes.py
# Combines all units and appendices into the final master book

import os
import sys

from generate_unit1 import get_unit1_text
from generate_unit2 import get_unit2_text
from generate_unit3 import get_unit3_text
from generate_unit4 import get_unit4_text
from generate_unit5 import get_unit5_text
from generate_appendices import get_appendices_text

FRONT_MATTER = r"""# DISCRETE STRUCTURES (COURSE CODE: ITDC0211 / ITPC-309)
## ULTIMATE END-SEMESTER EXAMINATION THEORY MASTER BOOK
### Dr B R Ambedkar National Institute of Technology, Jalandhar (NIT Jalandhar)
#### Department of Information Technology | B.Tech Semester 3 / 5

---

> ### 📘 ACADEMIC PREFACE & PEDAGOGICAL OBJECTIVE
> This volume constitutes the definitive, exhaustive, and mathematically rigorous Theory Master Guide for **Discrete Structures (ITDC0211 / ITPC-309)**.
> Engineered specifically for end-semester academic examinations, this guide covers every concept from the foundational syllabus with zero omissions, zero high-level handwaving, and complete analytical proofs.
> 
> **Every unit integrates**:
> - Formal mathematical axioms, definitions, and domain constraints.
> - Step-by-step analytical derivations and formal logic truth tables.
> - ASCII architectural diagrams, Hasse lattices, state machines, and digraphs.
> - Full mathematical proofs (Handshaking Lemma, Euler's Planar Formula $V - E + F = 2$, Lagrange's Subgroup Theorem, Tree Edge-Vertex Theorem, Bipartite Cycle Characterization).
> - Fully worked step-by-step numerical problems and execution traces (Warshall, Dijkstra, Prim, Kruskal, Huffman, Extended Euclidean Algorithm).
> - Annotated C++ implementations for core discrete algorithms.
> - Complete, fully verified solutions to the actual NIT Jalandhar Mid-Semester and End-Semester examination questions.
> - Student Exam Traps, Common Pitfalls, and Scoring Strategies.

---

## MASTER TABLE OF CONTENTS

1. [UNIT 1: INTRODUCTION TO PRELIMINARIES AND PREDICATE CALCULUS](#unit-1-introduction-to-preliminaries-and-predicate-calculus)
   - 1.1 Foundations of Mathematical Logic & Discrete Mathematics
   - 1.2 Logical Connectives & Full Truth Tables
   - 1.3 Compound Propositions & Propositional Classification
   - 1.4 Laws of Logical Equivalence (Algebra of Propositions)
   - 1.5 Predicates and Quantifiers (First-Order Logic)
   - 1.6 Rules of Inference & Formal Deductive Proofs
   - 1.7 Normal Forms (DNF, CNF, PDNF, PCNF)
   - 1.8 Methods of Mathematical Proof
   - 1.9 High-Probability Exam Questions & Student Traps
2. [UNIT 2: SET THEORY, RELATIONS, FUNCTIONS, POSETS, LATTICES, COUNTING & DISCRETE STRUCTURES](#unit-2-set-theory-relations-functions-posets-lattices-counting--discrete-structures)
   - 2.1 Set Theory Foundations & Algebra of Sets
   - 2.2 Relations and Their Algebraic Properties
   - 2.3 Partial Orders (Posets) & Lattices
   - 2.4 Functions and Bijections
   - 2.5 Advanced Counting Principles & Combinatorics
   - 2.6 Number Theory & Modular Arithmetic
   - 2.7 Elements of Probability & Bayes' Theorem
   - 2.8 Recurrence Relations
3. [UNIT 3: GRAPH THEORY & NETWORK ARCHITECTURES](#unit-3-graph-theory--network-architectures)
   - 3.1 Fundamental Concepts & Classification of Graphs
   - 3.2 Special Families of Graphs & Topological Metrics
   - 3.3 Connectivity, Matrix Representations & Warshall's Algorithm
   - 3.4 Eulerian and Hamiltonian Graphs
   - 3.5 Planar Graphs & Graph Coloring
   - 3.6 Graph Isomorphism
4. [UNIT 4: BINARY TREES, TREE ALGORITHMS & DATA STRUCTURES](#unit-4-binary-trees-tree-algorithms--data-structures)
   - 4.1 Tree Architectures & Mathematical Foundations
   - 4.2 Binary Tree Traversals
   - 4.3 Binary Search Trees (BST)
   - 4.4 Spanning Trees & Minimum Spanning Trees (MST)
   - 4.5 Heaps: Min-Heap & Max-Heap
   - 4.6 Huffman's Data Compression Algorithm
5. [UNIT 5: ALGEBRAIC STRUCTURES & MATHEMATICAL INDUCTION](#unit-5-algebraic-structures--mathematical-induction)
   - 5.1 Mathematical Induction
   - 5.2 Binary Operations & Their Algebraic Properties
   - 5.3 Hierarchy of Algebraic Structures
   - 5.4 Subgroups & Subgroup Tests
   - 5.5 Cyclic Groups & Number of Generators
   - 5.6 Cosets & Lagrange's Theorem
   - 5.7 Rings, Integral Domains, and Fields
6. [APPENDICES: CODE IMPLEMENTATIONS, PYQ SOLUTIONS & EXAM CHEAT SHEET](#appendices-code-implementations-pyq-solutions--exam-cheat-sheet)
   - Appendix A: Master Formula & Theorem Quick Reference Cheat Sheet
   - Appendix B: Annotated C++ Implementations for Core Discrete Algorithms
   - Appendix C: NIT Jalandhar Comprehensive Examination Solutions (Midsem & Endsem)

---

"""

def assemble():
    output_path = r"C:\Users\2006s\Desktop\SEM3_ENDTERM_MASTER_KIT\04_DSS\EXHAUSTIVE_THEORY_NOTES.md"
    print(f"Assembling master book into: {output_path}")

    parts = [
        FRONT_MATTER,
        get_unit1_text(),
        get_unit2_text(),
        get_unit3_text(),
        get_unit4_text(),
        get_unit5_text(),
        get_appendices_text()
    ]

    total_content = "\n\n".join(parts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(total_content)

    print(f"Assembly completed successfully!")
    print(f"Total file size: {len(total_content)} characters / {len(total_content.splitlines())} lines")

if __name__ == "__main__":
    assemble()
