"""
server.py
Lightweight, ultra-fast FastAPI backend for the NIT Jalandhar Sem 3 Study Portal & PDF Reader.
Zero AI dependencies, zero quota limits, pure high-performance document serving.
"""

import os
import sys
import json
from typing import List, Dict, Any, Optional
from urllib.parse import unquote

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

try:
    from study_data import STUDY_DATA
except ImportError:
    from web.study_data import STUDY_DATA

web_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(web_dir)
root_dir = parent_dir

app = FastAPI(title="NIT Jalandhar Sem 3 Study Portal", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_path = os.path.join(web_dir, "static")
if not os.path.exists(static_path):
    os.makedirs(static_path, exist_ok=True)

app.mount("/static", StaticFiles(directory=static_path), name="static")

SUBJECTS_CONFIG = [
    {
        "id": "01_CSA",
        "code": "ITX-201 / CSX-201",
        "short": "CSA",
        "name": "Computer System Architecture",
        "description": "Digital logic, CPU organization, Pipeline hazards, Cache memory hierarchy & 8086 Assembly."
    },
    {
        "id": "02_DBMS",
        "code": "CSX-205 / ITX-205",
        "short": "DBMS",
        "name": "Database Management Systems",
        "description": "Relational algebra, SQL, Normalization (1NF-5NF/BCNF), Concurrency & Indexing."
    },
    {
        "id": "03_DSA",
        "code": "CSX-201 / ITX-201",
        "short": "DSA",
        "name": "Data Structures & Algorithms",
        "description": "Asymptotic analysis, Stacks/Queues, AVL & Red-Black Trees, Graphs & Dynamic Programming."
    },
    {
        "id": "04_DSS",
        "code": "MAX-206",
        "short": "DSS",
        "name": "Discrete Structures",
        "description": "Propositional logic, Set theory, Relations, Recurrence relations & Graph theory."
    },
    {
        "id": "05_OOPS",
        "code": "CSX-203 / ITX-203",
        "short": "OOPS",
        "name": "Object-Oriented Programming (C++)",
        "description": "C++ classes, Constructors, Virtual functions, vtable/vptr, Templates & STL."
    },
    {
        "id": "06_WT",
        "code": "ITX-207",
        "short": "WT",
        "name": "Web Technologies",
        "description": "HTML5, CSS3, JavaScript Event Loop & Closures, Node.js, Express & React."
    }
]


def format_size(bytes_sz: int) -> str:
    """Formats file size into human-readable string."""
    if bytes_sz < 1024:
        return f"{bytes_sz} B"
    elif bytes_sz < 1024 * 1024:
        return f"{bytes_sz / 1024:.1f} KB"
    else:
        return f"{bytes_sz / (1024 * 1024):.1f} MB"


@app.api_route("/", methods=["GET", "HEAD"], response_class=HTMLResponse)
async def serve_index():
    index_file = os.path.join(static_path, "index.html")
    if not os.path.exists(index_file):
        raise HTTPException(status_code=404, detail="index.html not found")
    with open(index_file, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/api/catalog")
async def get_catalog():
    """Scans and categorizes all PDFs, Markdown books, diagrams, syllabus, and labs across all 6 subjects."""
    catalog = []

    for subj in SUBJECTS_CONFIG:
        subj_id = subj["id"]
        subj_dir = os.path.join(root_dir, subj_id)

        # 1. Master Theory Books
        theory_items = []
        t_pdf = os.path.join(subj_dir, "EXHAUSTIVE_THEORY_NOTES.pdf")
        t_md = os.path.join(subj_dir, "EXHAUSTIVE_THEORY_NOTES.md")
        if os.path.exists(t_pdf):
            theory_items.append({
                "title": "Exhaustive Theory Master Book (Units 1–5)",
                "type": "pdf",
                "rel_path": f"{subj_id}/EXHAUSTIVE_THEORY_NOTES.pdf",
                "size": format_size(os.path.getsize(t_pdf)),
                "has_md": os.path.exists(t_md),
                "md_path": f"{subj_id}/EXHAUSTIVE_THEORY_NOTES.md" if os.path.exists(t_md) else None
            })

        # 2. Solved PYQ Compendiums
        pyq_solved_items = []
        p_pdf = os.path.join(subj_dir, "PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.pdf")
        p_md = os.path.join(subj_dir, "PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md")
        if os.path.exists(p_pdf):
            pyq_solved_items.append({
                "title": "Solved Past Year Papers & Audit (2019–2024)",
                "type": "pdf",
                "rel_path": f"{subj_id}/PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.pdf",
                "size": format_size(os.path.getsize(p_pdf)),
                "has_md": os.path.exists(p_md),
                "md_path": f"{subj_id}/PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md" if os.path.exists(p_md) else None
            })

        # 3. Official NITJ Past Exam Papers (Original PDFs)
        official_pyqs = []
        pyq_dir = os.path.join(subj_dir, "Official_PYQ_PDFs")
        if os.path.exists(pyq_dir):
            for f in sorted(os.listdir(pyq_dir)):
                if f.endswith(".pdf"):
                    fp = os.path.join(pyq_dir, f)
                    official_pyqs.append({
                        "title": f.replace(".pdf", "").replace("_", " "),
                        "type": "pdf",
                        "rel_path": f"{subj_id}/Official_PYQ_PDFs/{f}",
                        "size": format_size(os.path.getsize(fp))
                    })

        # Additional official past papers in Drive_Materials
        for sub_folder in ["last-year-end-sem", "mid-sem-exams", "end-sem", "mid-sem", "paper", "quiz"]:
            cand_dir = os.path.join(subj_dir, "Drive_Materials", sub_folder)
            if os.path.exists(cand_dir):
                for f in sorted(os.listdir(cand_dir)):
                    if f.endswith(".pdf"):
                        fp = os.path.join(cand_dir, f)
                        official_pyqs.append({
                            "title": f"Exam Paper: {f.replace('.pdf', '').replace('_', ' ').replace('-', ' ')}",
                            "type": "pdf",
                            "rel_path": f"{subj_id}/Drive_Materials/{sub_folder}/{f}",
                            "size": format_size(os.path.getsize(fp))
                        })

        # 4. Technical Diagrams
        diagrams = []
        diag_dir = os.path.join(subj_dir, "Diagrams")
        if os.path.exists(diag_dir):
            for f in sorted(os.listdir(diag_dir)):
                if f.endswith((".png", ".jpg", ".svg")):
                    fp = os.path.join(diag_dir, f)
                    diagrams.append({
                        "title": f.replace(".png", "").replace(".jpg", "").replace("_", " ").title(),
                        "type": "image",
                        "rel_path": f"{subj_id}/Diagrams/{f}",
                        "size": format_size(os.path.getsize(fp))
                    })

        # 5. Reference Textbooks & Lab Guides
        reference_items = []
        earlier_dir = os.path.join(subj_dir, "Earlier_Prepared_Notes_and_Guides")
        if os.path.exists(earlier_dir):
            for f in sorted(os.listdir(earlier_dir)):
                if f.endswith((".pdf", ".md")):
                    fp = os.path.join(earlier_dir, f)
                    reference_items.append({
                        "title": f.replace(".pdf", "").replace(".md", "").replace("_", " "),
                        "type": "pdf" if f.endswith(".pdf") else "md",
                        "rel_path": f"{subj_id}/Earlier_Prepared_Notes_and_Guides/{f}",
                        "size": format_size(os.path.getsize(fp))
                    })

        drive_dir = os.path.join(subj_dir, "Drive_Materials")
        if os.path.exists(drive_dir):
            for f in sorted(os.listdir(drive_dir)):
                if f.endswith(".pdf"):
                    fp = os.path.join(drive_dir, f)
                    reference_items.append({
                        "title": f"Reference: {f.replace('.pdf', '').replace('_', ' ')}",
                        "type": "pdf",
                        "rel_path": f"{subj_id}/Drive_Materials/{f}",
                        "size": format_size(os.path.getsize(fp))
                    })

        # 6. Official NITJ Scheme & Syllabus
        syllabus_items = []
        s_dir = os.path.join(subj_dir, "Syllabus")
        if os.path.exists(s_dir):
            for f in sorted(os.listdir(s_dir)):
                if f.endswith((".pdf", ".png")):
                    fp = os.path.join(s_dir, f)
                    syllabus_items.append({
                        "title": f"Official Syllabus: {f.replace('.pdf', '').replace('.png', '').replace('_', ' ')}",
                        "type": "pdf" if f.endswith(".pdf") else "image",
                        "rel_path": f"{subj_id}/Syllabus/{f}",
                        "size": format_size(os.path.getsize(fp))
                    })

        # 7. Local Labs, Quizzes & Practical Guides
        lab_items = []
        lab_dir = os.path.join(subj_dir, "Local_Labs_and_Notes")
        if os.path.exists(lab_dir):
            for root_w, _, files_w in os.walk(lab_dir):
                for f in sorted(files_w):
                    if f.endswith((".pdf", ".md", ".png", ".jpg")):
                        fp = os.path.join(root_w, f)
                        rel_f = os.path.relpath(fp, root_dir).replace("\\", "/")
                        lab_items.append({
                            "title": f.replace(".pdf", "").replace(".md", "").replace(".png", "").replace(".jpg", "").replace("_", " "),
                            "type": "pdf" if f.endswith(".pdf") else "md" if f.endswith(".md") else "image",
                            "rel_path": rel_f,
                            "size": format_size(os.path.getsize(fp))
                        })

        catalog.append({
            "id": subj_id,
            "short": subj["short"],
            "code": subj["code"],
            "name": subj["name"],
            "description": subj["description"],
            "sections": {
                "theory": theory_items,
                "pyqs_solved": pyq_solved_items,
                "pyqs_official": official_pyqs,
                "diagrams": diagrams,
                "references": reference_items,
                "syllabus": syllabus_items,
                "labs": lab_items
            }
        })

    return {"catalog": catalog}


@app.get("/api/study_data")
async def get_study_data(subject: Optional[str] = None):
    """Serves high-yield formulas, active recall flashcards, unit roadmaps, and exam questions."""
    subj_filter = subject if isinstance(subject, str) and subject else None
    if subj_filter:
        if subj_filter in STUDY_DATA:
            return {"subject": subj_filter, "data": STUDY_DATA[subj_filter]}
        raise HTTPException(status_code=404, detail=f"Subject {subj_filter} not found in study data")
    return {"study_data": STUDY_DATA}


@app.get("/api/exam_question")
async def get_exam_question(
    subject: Optional[str] = None,
    marks: Optional[int] = None,
    q_id: Optional[str] = None
):
    """
    Serves authentic NIT Jalandhar exam questions by subject and mark weightage (2, 5, 10 marks),
    complete with hints, step-by-step marking schemes, and model answers.
    """
    all_questions = []
    for s_id, s_data in STUDY_DATA.items():
        if subject and s_id != subject:
            continue
        for q in s_data.get("exam_questions", []):
            item = dict(q)
            item["subject_id"] = s_id
            item["subject_name"] = s_data.get("name", s_id)
            item["subject_short"] = s_data.get("short", s_id)
            all_questions.append(item)

    if q_id:
        for q in all_questions:
            if q["id"] == q_id:
                return {"question": q}
        raise HTTPException(status_code=404, detail=f"Question ID {q_id} not found")

    if marks:
        all_questions = [q for q in all_questions if q["marks"] == marks]

    if not all_questions:
        raise HTTPException(status_code=404, detail="No matching exam questions found")

    import random
    picked = random.choice(all_questions)
    return {"question": picked, "total_available": len(all_questions), "pool": all_questions}


@app.get("/api/search")
async def search_content(q: str = Query(..., min_length=2), subject: Optional[str] = None):
    """
    Ultra-fast unified full-text search across:
    1. High-yield formulas, flashcards, unit roadmaps, and exam practice questions
    2. Document catalog titles across all 6 subjects
    3. Exhaustive theory notes and solved PYQ markdown books
    """
    query = q.strip().lower()
    results = []
    subj_filter = subject if isinstance(subject, str) and subject else None
    target_subjs = [s for s in SUBJECTS_CONFIG if not subj_filter or s["id"] == subj_filter]

    # 1. Search in STUDY_DATA (Formulas, Flashcards, Units, Exam Questions)
    for s in target_subjs:
        s_id = s["id"]
        s_data = STUDY_DATA.get(s_id, {})

        # Formulas
        for f in s_data.get("formulas", []):
            blob = f"{f['title']} {f['explanation']} {f.get('trap', '')} {f.get('example', '')} {f['latex']} {f['unit']}".lower()
            if query in blob:
                results.append({
                    "subject_id": s_id,
                    "subject_name": s["name"],
                    "subject_short": s["short"],
                    "doc_title": f"Formula: {f['title']} ({f['unit']})",
                    "type": "formula",
                    "formula_title": f["title"],
                    "unit": f["unit"],
                    "rel_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.md",
                    "pdf_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.pdf",
                    "has_md": True,
                    "md_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.md",
                    "line": 0,
                    "snippet": f"Formula: $${f['latex']}$$ — {f['explanation'][:160]}"
                })
                if len(results) >= 15:
                    break

        # Flashcards
        for c in s_data.get("flashcards", []):
            blob = f"{c['q']} {c['a']} {c.get('marks', '')}".lower()
            if query in blob:
                results.append({
                    "subject_id": s_id,
                    "subject_name": s["name"],
                    "subject_short": s["short"],
                    "doc_title": f"Flashcard: {c['q'][:55]}...",
                    "type": "flashcard",
                    "card_q": c["q"],
                    "rel_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.md",
                    "pdf_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.pdf",
                    "has_md": True,
                    "md_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.md",
                    "line": 0,
                    "snippet": f"Q: {c['q']} | Ans: {c['a'][:140]}..."
                })
                if len(results) >= 20:
                    break

        # Exam Questions
        for eq in s_data.get("exam_questions", []):
            blob = f"{eq['title']} {eq['question']} {eq['model_answer']} {eq.get('hint', '')} {eq.get('exam_source', '')}".lower()
            if query in blob:
                results.append({
                    "subject_id": s_id,
                    "subject_name": s["name"],
                    "subject_short": s["short"],
                    "doc_title": f"Exam PYQ [{eq['marks']}M]: {eq['title']}",
                    "type": "exam_question",
                    "q_id": eq["id"],
                    "rel_path": f"{s_id}/PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md",
                    "pdf_path": f"{s_id}/PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.pdf",
                    "has_md": True,
                    "md_path": f"{s_id}/PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md",
                    "line": 0,
                    "snippet": f"[{eq['marks']} Marks - {eq.get('exam_source', 'NITJ End-Sem')}]: {eq['question'][:150]}..."
                })
                if len(results) >= 25:
                    break

        # Unit Roadmaps
        for u in s_data.get("units", []):
            blob = f"Unit {u['unit']} {u['title']} {u['topics']} {u['high_yield_tip']}".lower()
            if query in blob:
                results.append({
                    "subject_id": s_id,
                    "subject_name": s["name"],
                    "subject_short": s["short"],
                    "doc_title": f"Unit {u['unit']} Roadmap: {u['title']}",
                    "type": "unit",
                    "unit_num": u["unit"],
                    "rel_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.md",
                    "pdf_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.pdf",
                    "has_md": True,
                    "md_path": f"{s_id}/EXHAUSTIVE_THEORY_NOTES.md",
                    "line": 0,
                    "snippet": f"Unit {u['unit']} ({u['weightage']}): {u['topics'][:120]} — Exam Secret: {u['high_yield_tip'][:100]}"
                })
                if len(results) >= 30:
                    break

    # 2. Search in catalog document titles
    cat = await get_catalog()
    for s in cat["catalog"]:
        if subj_filter and s["id"] != subj_filter:
            continue
        for sec_name, items in s["sections"].items():
            for it in items:
                if query in it["title"].lower():
                    results.append({
                        "subject_id": s["id"],
                        "subject_name": s["name"],
                        "subject_short": s["short"],
                        "doc_title": it["title"],
                        "type": it["type"],
                        "rel_path": it["rel_path"],
                        "pdf_path": it["rel_path"] if it["type"] == "pdf" else None,
                        "has_md": it.get("has_md", False),
                        "md_path": it.get("md_path", None),
                        "line": 0,
                        "snippet": f"Document [{sec_name.replace('_', ' ').title()}]: {it['title']} ({it.get('size', '')})"
                    })
                    if len(results) >= 40:
                        break
            if len(results) >= 40:
                break
        if len(results) >= 40:
            break

    # 3. Search in theory markdown & solved PYQs markdown lines
    for subj in target_subjs:
        subj_id = subj["id"]
        subj_dir = os.path.join(root_dir, subj_id)

        for fn in ["EXHAUSTIVE_THEORY_NOTES.md", "PYQ_COMPLETE_SOLUTIONS_AND_AUDIT.md"]:
            fp = os.path.join(subj_dir, fn)
            if os.path.exists(fp):
                is_theory = "THEORY" in fn
                doc_title = "Exhaustive Theory Master Book" if is_theory else "Solved PYQ Compendium"
                pdf_rel = f"{subj_id}/{fn[:-3]}.pdf"
                md_rel = f"{subj_id}/{fn}"

                try:
                    with open(fp, "r", encoding="utf-8", errors="replace") as f:
                        for line_idx, line in enumerate(f, 1):
                            if query in line.lower():
                                clean_line = line.strip().lstrip("#").strip()
                                if len(clean_line) >= 8:
                                    results.append({
                                        "subject_id": subj_id,
                                        "subject_name": subj["name"],
                                        "subject_short": subj["short"],
                                        "doc_title": f"{doc_title} (L{line_idx})",
                                        "type": "markdown",
                                        "rel_path": md_rel,
                                        "pdf_path": pdf_rel,
                                        "has_md": True,
                                        "md_path": md_rel,
                                        "line": line_idx,
                                        "snippet": clean_line[:180]
                                    })
                                    if len(results) >= 50:
                                        break
                except Exception:
                    pass
            if len(results) >= 50:
                break
        if len(results) >= 50:
            break

    return {"query": q, "total": len(results), "results": results}


@app.get("/api/pdf")
async def get_pdf(path: str = Query(...)):
    """Serves PDF inline for browser iframe reader."""
    clean_path = os.path.normpath(unquote(path)).lstrip("\\/")
    full_path = os.path.join(root_dir, clean_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(root_dir)):
        raise HTTPException(status_code=403, detail="Access denied")

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="PDF not found")

    return FileResponse(
        full_path,
        media_type="application/pdf",
        headers={"Content-Disposition": f'inline; filename="{os.path.basename(full_path)}"'}
    )


@app.get("/api/md")
async def get_markdown(path: str = Query(...)):
    """Serves raw markdown text."""
    clean_path = os.path.normpath(unquote(path)).lstrip("\\/")
    full_path = os.path.join(root_dir, clean_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(root_dir)):
        raise HTTPException(status_code=403, detail="Access denied")

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Markdown file not found")

    with open(full_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    return {
        "title": os.path.basename(full_path),
        "path": clean_path,
        "content": content,
        "words": len(content.split()),
        "lines": len(content.split("\n"))
    }


@app.get("/api/image")
async def get_image(path: str = Query(...)):
    """Serves high-resolution diagrams."""
    clean_path = os.path.normpath(unquote(path)).lstrip("\\/")
    full_path = os.path.join(root_dir, clean_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(root_dir)):
        raise HTTPException(status_code=403, detail="Access denied")

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Image not found")

    ext = os.path.splitext(full_path)[1].lower()
    media_type = "image/png" if ext == ".png" else "image/jpeg"
    return FileResponse(full_path, media_type=media_type)


@app.get("/api/download")
async def force_download(path: str = Query(...)):
    """Forces browser download for offline saving."""
    clean_path = os.path.normpath(unquote(path)).lstrip("\\/")
    full_path = os.path.join(root_dir, clean_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(root_dir)):
        raise HTTPException(status_code=403, detail="Access denied")

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        full_path,
        filename=os.path.basename(full_path),
        headers={"Content-Disposition": f'attachment; filename="{os.path.basename(full_path)}"'}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=False)
