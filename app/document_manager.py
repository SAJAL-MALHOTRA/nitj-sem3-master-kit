"""
document_manager.py
Manages indexing, loading, outline generation, and stats for the Semester 3 Master Kit.
"""

import os
import re
from typing import Dict, List, Any, Optional

SUBJECT_METADATA = {
    "01_CSA": {
        "short": "CSA",
        "code": "ITX-201 / CSX-201",
        "name": "Computer System Architecture",
        "icon": "🖥️",
        "color": "#3B82F6",
        "description": "Digital logic, CPU organization, Pipeline hazards, Cache memory hierarchy & 8086 Assembly.",
        "units": [
            "Unit 1: Register Transfer & Microoperations",
            "Unit 2: Basic Computer Organization & Design",
            "Unit 3: Central Processing Unit & Addressing Modes",
            "Unit 4: Pipeline & Vector Processing (Tomasulo, Scoreboard)",
            "Unit 5: Memory Organization (Cache mapping, Virtual memory) & I/O"
        ],
        "sample_prompts": [
            "Explain direct, associative, and set-associative cache mapping with numerical calculations.",
            "Compare Tomasulo's Algorithm with Scoreboarding for dynamic instruction scheduling.",
            "Explain all 8086 addressing modes with examples from the solved PYQs.",
            "Derive pipeline speedup with hazards and branch penalties."
        ]
    },
    "02_DBMS": {
        "short": "DBMS",
        "code": "CSX-205 / ITX-205",
        "name": "Database Management Systems",
        "icon": "🗄️",
        "color": "#10B981",
        "description": "Relational algebra, SQL, Normalization (1NF to BCNF/5NF), Concurrency & Indexing.",
        "units": [
            "Unit 1: Intro to Database Architecture & ER Modeling",
            "Unit 2: Relational Model, Relational Algebra & Calculus",
            "Unit 3: Advanced SQL, Triggers, Views & Subqueries",
            "Unit 4: Relational Database Design & Normalization (1NF to 5NF)",
            "Unit 5: Transaction Processing, Concurrency Control (2PL, Timestamp) & Recovery"
        ],
        "sample_prompts": [
            "Step-by-step test for Conflict Serializability using Precedence Graphs.",
            "How do you decompose a relation into BCNF without losing dependencies?",
            "Explain Strict 2PL vs Rigorous 2PL and how they prevent cascading aborts.",
            "Write SQL queries for complex correlated subqueries and group-by having."
        ]
    },
    "03_DSA": {
        "short": "DSA",
        "code": "CSX-201 / ITX-201",
        "name": "Data Structures & Algorithms",
        "icon": "🌳",
        "color": "#F59E0B",
        "description": "Asymptotic analysis, Stacks/Queues, AVL & Red-Black Trees, Graphs & Dynamic Programming.",
        "units": [
            "Unit 1: Asymptotic Notations & Array Applications",
            "Unit 2: Linked Lists, Stacks & Queues (Infix to Postfix conversions)",
            "Unit 3: Non-Linear Structures: Trees, BST, AVL Rotations & Red-Black Trees",
            "Unit 4: Graph Algorithms: BFS, DFS, Dijkstra, Prim & Kruskal",
            "Unit 5: Sorting & Searching: Quick, Merge, Heap Sort & Hashing collision techniques"
        ],
        "sample_prompts": [
            "Walk through AVL Tree LL, RR, LR, and RL rotations with diagrams.",
            "Derive the Master Theorem cases for recursive time complexity.",
            "Solve the 0/1 Knapsack problem using dynamic programming table construction.",
            "Show Dijkstra's shortest path algorithm step-by-step on a 6-node weighted graph."
        ]
    },
    "04_DSS": {
        "short": "DSS",
        "code": "MAX-206",
        "name": "Discrete Structures",
        "icon": "📐",
        "color": "#8B5CF6",
        "description": "Propositional logic, Set theory, Relations/Lattices, Recurrence relations & Graph theory.",
        "units": [
            "Unit 1: Mathematical Logic & Propositional Equivalence",
            "Unit 2: Sets, Relations, Equivalence Classes & POSETs / Lattices",
            "Unit 3: Functions, Pigeonhole Principle & Combinatorics",
            "Unit 4: Recurrence Relations & Generating Functions",
            "Unit 5: Graph Theory: Euler vs Hamiltonian paths, Planar graphs & Coloring"
        ],
        "sample_prompts": [
            "Check if a relation is an Equivalence Relation or a Partial Order relation.",
            "Solve second-order linear homogeneous recurrence relations with initial conditions.",
            "Prove Euler's formula V - E + F = 2 for planar graphs using induction.",
            "Explain the Pigeonhole Principle with typical NIT Jalandhar exam questions."
        ]
    },
    "05_OOPS": {
        "short": "OOPS",
        "code": "CSX-203 / ITX-203",
        "name": "Object-Oriented Programming (C++)",
        "icon": "⚡",
        "color": "#EC4899",
        "description": "C++ classes, Constructors, Virtual functions/vtable, Diamond inheritance, Templates & STL.",
        "units": [
            "Unit 1: Paradigms, C++ Foundations, Classes & Access Specifiers",
            "Unit 2: Constructors, Destructors, Copy Constructors & Friend Functions",
            "Unit 3: Inheritance Types, Diamond Problem & Virtual Base Classes",
            "Unit 4: Polymorphism: Virtual Functions, Pure Virtual, VTABLE & VPTR internals",
            "Unit 5: Templates, Exception Handling & Standard Template Library (STL)"
        ],
        "sample_prompts": [
            "Explain VTABLE and VPTR internal memory layout for dynamic dispatch in C++.",
            "How does `virtual` inheritance resolve the Diamond Inheritance Problem?",
            "Write a complete C++ generic template Stack class with exception handling.",
            "Differentiate between shallow copy and deep copy with copy constructor code."
        ]
    },
    "06_WT": {
        "short": "WT",
        "code": "ITX-207",
        "name": "Web Technologies",
        "icon": "🌐",
        "color": "#06B6D4",
        "description": "HTML5, CSS3, JavaScript Event Loop & Closures, Node.js, Express, React & REST APIs.",
        "units": [
            "Unit 1: Internet Architecture, HTTP/HTTPS, Web Protocols & HTML5 Semantic Elements",
            "Unit 2: CSS3 Box Model, Flexbox, CSS Grid & Responsive Web Design",
            "Unit 3: Modern JavaScript: ES6+, DOM Manipulation, Closures, Promises & Event Loop",
            "Unit 4: Server-Side Engineering: Node.js runtime, Express.js middleware & RESTful APIs",
            "Unit 5: Frontend Frameworks (React Component Lifecycle, Hooks, State) & Web Security (XSS, CSRF)"
        ],
        "sample_prompts": [
            "Explain the JavaScript Event Loop, Call Stack, Microtask queue, and Macrotask queue.",
            "Compare CSS Flexbox vs CSS Grid and provide layout code examples.",
            "How does React's Virtual DOM reconciliation and diffing algorithm work?",
            "Explain CORS, XSS, and CSRF security vulnerabilities and their mitigations."
        ]
    }
}


def find_kit_root() -> str:
    """Finds the root path of the SEM3_ENDTERM_MASTER_KIT directory."""
    # 1. Check relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    if os.path.exists(os.path.join(parent_dir, "01_CSA")):
        return parent_dir

    # 2. Check current working directory
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "01_CSA")):
        return cwd
    if os.path.exists(os.path.join(cwd, "SEM3_ENDTERM_MASTER_KIT", "01_CSA")):
        return os.path.join(cwd, "SEM3_ENDTERM_MASTER_KIT")

    # 3. Check standard absolute desktop path
    default_path = r"C:\Users\2006s\Desktop\SEM3_ENDTERM_MASTER_KIT"
    if os.path.exists(default_path):
        return default_path

    return parent_dir


def load_file_content(path: str) -> str:
    """Reads a text file safely with utf-8 encoding."""
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        return f"Error loading file {path}: {e}"


def get_subject_sources(subject_key: str) -> Dict[str, Any]:
    """
    Loads all core sources for a subject:
    - theory_text
    - pyq_text
    - earlier_notes (dict of title -> content)
    - pyq_pdf_files (list of file names)
    - diagram_files (list of file paths)
    """
    root = find_kit_root()
    subj_dir = os.path.join(root, subject_key)

    data: Dict[str, Any] = {
        "subject_key": subject_key,
        "meta": SUBJECT_METADATA.get(subject_key, {}),
        "theory_path": os.path.join(subj_dir, "EXHAUSTIVE_THEORY_NOTES.md"),
        "theory_pdf": os.path.join(subj_dir, "EXHAUSTIVE_THEORY_NOTES.pdf"),
        "pyq_path": os.path.join(subj_dir, "PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md"),
        "pyq_pdf": os.path.join(subj_dir, "PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.pdf"),
        "theory_text": "",
        "pyq_text": "",
        "earlier_notes": {},
        "official_pyqs": [],
        "diagrams": []
    }

    if os.path.exists(data["theory_path"]):
        data["theory_text"] = load_file_content(data["theory_path"])

    if os.path.exists(data["pyq_path"]):
        data["pyq_text"] = load_file_content(data["pyq_path"])

    # Load earlier notes
    earlier_dir = os.path.join(subj_dir, "Earlier_Prepared_Notes_and_Guides")
    if os.path.exists(earlier_dir):
        for fname in os.listdir(earlier_dir):
            if fname.endswith(".md"):
                p = os.path.join(earlier_dir, fname)
                data["earlier_notes"][fname] = load_file_content(p)

    # Official PYQs
    pyq_dir = os.path.join(subj_dir, "Official_PYQ_PDFs")
    if os.path.exists(pyq_dir):
        data["official_pyqs"] = [f for f in os.listdir(pyq_dir) if f.endswith(".pdf")]

    # Diagrams
    diag_dir = os.path.join(subj_dir, "Diagrams")
    if os.path.exists(diag_dir):
        data["diagrams"] = [os.path.join(diag_dir, f) for f in os.listdir(diag_dir) if f.endswith((".png", ".jpg"))]

    return data


def extract_outline(text: str) -> List[Dict[str, Any]]:
    """Extracts markdown headers to build a Table of Contents tree."""
    outline = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,4})\s+(.+)$", line.strip())
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            # Clean up markdown formatting in title
            clean_title = re.sub(r"[\*\_`]", "", title)
            outline.append({
                "level": level,
                "title": clean_title,
                "line": i + 1
            })
    return outline


def get_full_corpus_stats() -> Dict[str, Any]:
    """Computes total word counts, lines, and token estimates across the whole kit."""
    root = find_kit_root()
    total_words = 0
    total_lines = 0
    total_md_files = 0
    subject_stats = {}

    for subj_key, meta in SUBJECT_METADATA.items():
        subj_dir = os.path.join(root, subj_key)
        theory_path = os.path.join(subj_dir, "EXHAUSTIVE_THEORY_NOTES.md")
        pyq_path = os.path.join(subj_dir, "PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md")

        t_text = load_file_content(theory_path)
        p_text = load_file_content(pyq_path)

        combined = t_text + "\n" + p_text
        words = len(combined.split())
        lines = len(combined.split("\n"))
        tokens_est = int(len(combined) / 4)

        total_words += words
        total_lines += lines
        total_md_files += 2

        subject_stats[subj_key] = {
            "name": meta["name"],
            "short": meta["short"],
            "words": words,
            "lines": lines,
            "tokens_est": tokens_est
        }

    return {
        "total_words": total_words,
        "total_lines": total_lines,
        "total_tokens_est": int(total_words * 1.3),
        "total_subjects": len(SUBJECT_METADATA),
        "subject_stats": subject_stats
    }
