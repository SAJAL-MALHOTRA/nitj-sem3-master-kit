"""
test_portal.py
Comprehensive test suite verifying all FastAPI backend endpoints, security boundaries,
catalog accuracy, study data integrity, and frontend HTML components.
"""

import os
import sys
import unittest
from fastapi.testclient import TestClient

# Ensure web directory is in path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from server import app, root_dir
from study_data import STUDY_DATA


class TestStudyPortal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_01_serve_index(self):
        """Verify root / serves the revamped Sketchmorphic index.html."""
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("text/html", res.headers["content-type"])
        html = res.text
        # Verify Sketchmorphism typography & styles
        self.assertIn("Architects+Daughter", html)
        self.assertIn("Patrick+Hand", html)
        self.assertIn("bg-graph-paper", html)
        self.assertIn("sketch-border", html)
        self.assertIn("sketch-shadow", html)
        self.assertIn("scratchCanvas", html)
        self.assertIn("card-flipper", html)
        self.assertIn("modalTimerDisplay", html)

    def test_02_catalog_structure(self):
        """Verify /api/catalog returns all 6 subjects with complete sections."""
        res = self.client.get("/api/catalog")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("catalog", data)
        catalog = data["catalog"]
        self.assertEqual(len(catalog), 6)
        
        subject_ids = [s["id"] for s in catalog]
        expected_ids = ["01_CSA", "02_DBMS", "03_DSA", "04_DSS", "05_OOPS", "06_WT"]
        self.assertEqual(subject_ids, expected_ids)

        for subj in catalog:
            self.assertIn("sections", subj)
            sections = subj["sections"]
            self.assertIn("theory", sections)
            self.assertIn("pyqs_solved", sections)
            self.assertIn("pyqs_official", sections)
            self.assertIn("diagrams", sections)
            self.assertIn("references", sections)
            # Ensure at least theory notes exist for each subject
            self.assertTrue(len(sections["theory"]) > 0, f"Theory missing in {subj['id']}")
            self.assertTrue(sections["theory"][0]["has_md"], f"Markdown missing in {subj['id']}")

    def test_03_study_data_endpoint(self):
        """Verify /api/study_data returns comprehensive academic data for all 6 subjects."""
        res = self.client.get("/api/study_data")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("study_data", data)
        
        for subj_id in ["01_CSA", "02_DBMS", "03_DSA", "04_DSS", "05_OOPS", "06_WT"]:
            self.assertIn(subj_id, data["study_data"])
            s_data = data["study_data"][subj_id]
            self.assertEqual(len(s_data["units"]), 5, f"Units count not 5 for {subj_id}")
            self.assertTrue(len(s_data["formulas"]) >= 3, f"Not enough formulas in {subj_id}")
            self.assertTrue(len(s_data["flashcards"]) >= 3, f"Not enough flashcards in {subj_id}")

        # Test single subject query
        res_csa = self.client.get("/api/study_data?subject=01_CSA")
        self.assertEqual(res_csa.status_code, 200)
        self.assertEqual(res_csa.json()["subject"], "01_CSA")

        # Test invalid subject query
        res_invalid = self.client.get("/api/study_data?subject=99_INVALID")
        self.assertEqual(res_invalid.status_code, 404)

    def test_04_search_endpoint(self):
        """Verify /api/search accurately searches catalog titles and markdown books."""
        # Search for a hardware topic in CSA
        res_pipeline = self.client.get("/api/search?q=pipeline")
        self.assertEqual(res_pipeline.status_code, 200)
        data = res_pipeline.json()
        self.assertTrue(data["total"] > 0)
        csa_hits = [r for r in data["results"] if r["subject_short"] == "CSA"]
        self.assertTrue(len(csa_hits) > 0)

        # Search for an algorithm in DSA
        res_dijkstra = self.client.get("/api/search?q=dijkstra")
        self.assertEqual(res_dijkstra.status_code, 200)
        self.assertTrue(res_dijkstra.json()["total"] > 0)

        # Search with subject filter
        res_scoped = self.client.get("/api/search?q=pipeline&subject=01_CSA")
        self.assertEqual(res_scoped.status_code, 200)
        for r in res_scoped.json()["results"]:
            self.assertEqual(r["subject_id"], "01_CSA")

    def test_05_pdf_serving(self):
        """Verify /api/pdf serves PDF inline."""
        res = self.client.get("/api/pdf?path=01_CSA/EXHAUSTIVE_THEORY_NOTES.pdf")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["content-type"], "application/pdf")
        self.assertIn("inline", res.headers.get("content-disposition", ""))

    def test_06_markdown_serving(self):
        """Verify /api/md serves raw markdown text with stats."""
        res = self.client.get("/api/md?path=01_CSA/EXHAUSTIVE_THEORY_NOTES.md")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["title"], "EXHAUSTIVE_THEORY_NOTES.md")
        self.assertTrue(data["words"] > 1000)
        self.assertTrue(data["lines"] > 500)

    def test_07_diagram_serving(self):
        """Verify /api/image serves diagram with correct MIME type."""
        res = self.client.get("/api/image?path=01_CSA/Diagrams/memory_hierarchy.png")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["content-type"], "image/png")

    def test_08_download_endpoint(self):
        """Verify /api/download serves file with attachment disposition."""
        res = self.client.get("/api/download?path=01_CSA/EXHAUSTIVE_THEORY_NOTES.pdf")
        self.assertEqual(res.status_code, 200)
        self.assertIn("attachment", res.headers.get("content-disposition", ""))

    def test_09_security_path_traversal_prevention(self):
        """Verify directory traversal attacks are blocked with 403 Forbidden."""
        bad_paths = [
            "../../secret.txt",
            "..\\..\\windows\\system32\\drivers\\etc\\hosts",
            "01_CSA/../../app/app.py"
        ]
        for p in bad_paths:
            res_pdf = self.client.get(f"/api/pdf?path={p}")
            self.assertEqual(res_pdf.status_code, 403)
            res_md = self.client.get(f"/api/md?path={p}")
            self.assertEqual(res_md.status_code, 403)
            res_img = self.client.get(f"/api/image?path={p}")
            self.assertEqual(res_img.status_code, 403)
            res_dl = self.client.get(f"/api/download?path={p}")
            self.assertEqual(res_dl.status_code, 403)

    def test_10_not_found_handling(self):
        """Verify non-existent files return 404."""
        res = self.client.get("/api/pdf?path=01_CSA/non_existent.pdf")
        self.assertEqual(res.status_code, 404)
        res = self.client.get("/api/md?path=01_CSA/non_existent.md")
        self.assertEqual(res.status_code, 404)

    def test_11_dom_integrity(self):
        """Verify that every DOM element ID accessed in JavaScript exists in index.html."""
        import re
        index_file = os.path.join(current_dir, "static", "index.html")
        with open(index_file, "r", encoding="utf-8") as f:
            html = f.read()

        js_ids = set(re.findall(r"getElementById\(['\"](.*?)['\"]\)", html))
        dom_ids = set(re.findall(r"id=['\"](.*?)['\"]", html))
        missing = js_ids - dom_ids
        self.assertEqual(len(missing), 0, f"Missing DOM elements referenced in JS: {missing}")

    def test_12_search_study_data_and_formulas(self):
        """Verify search indexes formulas, flashcards, and exam questions."""
        # 1. Search formula
        res = self.client.get("/api/search?q=amdahl")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["total"] > 0)
        formula_hits = [r for r in data["results"] if r.get("type") == "formula"]
        self.assertTrue(len(formula_hits) > 0)
        self.assertEqual(formula_hits[0]["subject_short"], "CSA")

        # 2. Search flashcard
        res_card = self.client.get("/api/search?q=closure")
        self.assertEqual(res_card.status_code, 200)
        self.assertTrue(res_card.json()["total"] > 0)

        # 3. Search exam question
        res_eq = self.client.get("/api/search?q=booth")
        self.assertEqual(res_eq.status_code, 200)
        self.assertTrue(res_eq.json()["total"] > 0)

    def test_13_exam_question_endpoint(self):
        """Verify /api/exam_question endpoint returns structured questions."""
        # Query 5-mark question for CSA
        res = self.client.get("/api/exam_question?subject=01_CSA&marks=5")
        self.assertEqual(res.status_code, 200)
        q = res.json()["question"]
        self.assertEqual(q["marks"], 5)
        self.assertEqual(q["subject_id"], "01_CSA")
        self.assertIn("hint", q)
        self.assertIn("marking_scheme", q)
        self.assertIn("model_answer", q)

        # Query specific question by ID
        res_id = self.client.get(f"/api/exam_question?q_id={q['id']}")
        self.assertEqual(res_id.status_code, 200)
        self.assertEqual(res_id.json()["question"]["id"], q["id"])

        # Invalid ID should 404
        res_invalid = self.client.get("/api/exam_question?q_id=invalid_id_999")
        self.assertEqual(res_invalid.status_code, 404)

    def test_14_catalog_syllabus_and_labs(self):
        """Verify /api/catalog includes official syllabus and local lab files."""
        res = self.client.get("/api/catalog")
        self.assertEqual(res.status_code, 200)
        catalog = res.json()["catalog"]

        # Check CSA has syllabus and labs
        csa = next(s for s in catalog if s["id"] == "01_CSA")
        self.assertIn("syllabus", csa["sections"])
        self.assertIn("labs", csa["sections"])
        self.assertTrue(len(csa["sections"]["syllabus"]) > 0, "CSA syllabus PDF missing")
        self.assertTrue(len(csa["sections"]["labs"]) > 0, "CSA lab files missing")

    def test_15_scratchpad_touch_and_persistence_elements(self):
        """Verify scratchpad includes touch events, undo, eraser, and persistence."""
        index_file = os.path.join(current_dir, "static", "index.html")
        with open(index_file, "r", encoding="utf-8") as f:
            html = f.read()

        self.assertIn("touchstart", html)
        self.assertIn("touchmove", html)
        self.assertIn("touchend", html)
        self.assertIn("undoScratchBtn", html)
        self.assertIn("eraserBrushBtn", html)
        self.assertIn("nitj_scratchpad_data", html)

    def test_16_pomodoro_tally_and_audio(self):
        """Verify Pomodoro does not hardcode completed tally marks and synthesizes acoustic chime."""
        index_file = os.path.join(current_dir, "static", "index.html")
        with open(index_file, "r", encoding="utf-8") as f:
            html = f.read()

        # Should not hardcode 6 sprints '<s>||||</s> |' in initial HTML
        self.assertNotIn('<span id="sprintTallyMarks" class="font-sketch font-bold text-lg text-emerald-700 tracking-widest"><s>||||</s> |</span>', html)
        self.assertIn("playAcousticChime", html)
        self.assertIn("AudioContext", html)

    def test_17_generative_ui_widgets(self):
        """Verify all rich generative UI widgets exist in index.html."""
        index_file = os.path.join(current_dir, "static", "index.html")
        with open(index_file, "r", encoding="utf-8") as f:
            html = f.read()

        # Exam simulator
        self.assertIn("examSimulatorContainer", html)
        self.assertIn("generateExamBtn", html)
        self.assertIn("simMarkingSchemeBox", html)
        # Calculators
        self.assertIn("calculatorsContainer", html)
        self.assertIn("amdahlFractionSlider", html)
        self.assertIn("amatHitRateSlider", html)
        self.assertIn("pipeInstructionsSlider", html)
        # Math protection
        self.assertIn("protectMathInMarkdown", html)
        self.assertIn("restoreMathInHtml", html)


if __name__ == "__main__":
    unittest.main()


