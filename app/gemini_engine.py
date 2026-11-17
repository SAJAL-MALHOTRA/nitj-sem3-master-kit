"""
gemini_engine.py
Handles Gemini API client management, prompt grounding, context injection, and streaming responses.
"""

import os
from typing import Iterator, List, Dict, Any, Optional
from google import genai
from google.genai import types

AVAILABLE_MODELS = [
    {"id": "gemini-2.5-flash", "name": "Gemini 2.5 Flash (Fastest & 1M Context - Recommended)"},
    {"id": "gemini-2.0-flash", "name": "Gemini 2.0 Flash (Next-Gen Multimodal)"},
    {"id": "gemini-1.5-pro", "name": "Gemini 1.5 Pro (Deepest Academic Reasoning & Complex Proofs)"},
    {"id": "gemini-1.5-flash", "name": "Gemini 1.5 Flash (High Efficiency)"}
]

DEFAULT_MODEL = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """You are the Senior Professor, Academic Mentor, and Chief Exam Evaluator for Dr. B. R. Ambedkar National Institute of Technology (NIT) Jalandhar, Department of Computer Science & Engineering / Information Technology. You are serving as the AI intellect behind this NotebookLM-style study environment for B.Tech Semester 3.

You are provided with the exhaustive official theory textbooks (Units 1 to 5) and the complete compendium of solved previous year examination papers (PYQs 2019-2024) across the 6 semester subjects:
1. Computer System Architecture (CSA)
2. Database Management Systems (DBMS)
3. Data Structures & Algorithms (DSA)
4. Discrete Structures (DSS)
5. Object-Oriented Programming (OOPS with C++)
6. Web Technologies (WT)

CORE INSTRUCTIONS & GROUNDING RULES:
1. STRICT GROUNDING: Ground your answers strictly on the provided course materials and solved PYQs. Never fabricate syllabus topics or cite external ungrounded facts.
2. EXPLICIT CITATIONS: In every answer, cite the exact source section and unit. For instance:
   - `[Source: DSA Master Book § Unit 3.2 - AVL Tree Rotations]`
   - `[Tested in NIT Jalandhar End-Sem Nov 2023, Question 3(b) - 6 Marks]`
3. ACADEMIC RIGOR & DETAIL: The student is aiming for top academic grades (10 CGPA / S Grade). Do not give brief superficial summaries. Provide deep, rigorous, end-term ready answers with:
   - Step-by-step mathematical derivations and proofs (using LaTeX $...$ and $$...$$).
   - Time and space complexity breakdowns (Best, Average, Worst case).
   - Clean, standards-compliant code implementations (C++17 for DSA/OOPS, ANSI SQL for DBMS, modern ES6+ for WT) with descriptive comments.
   - ASCII, Mermaid or text diagrammatic illustrations of memory layouts (vptr/vtable), pipeline stages, B-Trees, or ER diagrams.
4. EXAM-ORIENTED FOCUS: When solving problems, show the step-by-step mark allocation rubric typical of NIT Jalandhar examinations (e.g. 2-mark definition, 4-mark derivation/working, 2-mark diagram/example).
5. TONE: Encouraging, authoritative, intellectually thorough, and pedagogical.
"""


def get_gemini_client(api_key: Optional[str] = None) -> Optional[genai.Client]:
    """Initializes and returns a Google GenAI client."""
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        return None
    try:
        return genai.Client(api_key=key.strip())
    except Exception as e:
        print(f"Failed to initialize Gemini Client: {e}")
        return None


def format_context_prompt(selected_sources_data: List[Dict[str, Any]]) -> str:
    """Formats the selected subject theory and PYQ texts into an authoritative context block."""
    if not selected_sources_data:
        return "No specific course documents selected. Use general syllabus knowledge for NIT Jalandhar B.Tech Sem 3."

    parts = ["### OFFICIAL NIT JALANDHAR COURSE DOCUMENTS & EXAM REVISION CORPUS ###\n"]
    for src in selected_sources_data:
        meta = src.get("meta", {})
        parts.append(f"\n=======================================================")
        parts.append(f"SUBJECT: {meta.get('name', 'Subject')} ({meta.get('code', '')})")
        parts.append(f"=======================================================\n")

        if src.get("theory_text"):
            parts.append(f"--- [THEORY MASTER BOOK: {meta.get('short', '')}] ---")
            parts.append(src["theory_text"])
            parts.append("\n")

        if src.get("pyq_text"):
            parts.append(f"--- [SOLVED PAST YEAR EXAM PAPERS & AUDIT: {meta.get('short', '')}] ---")
            parts.append(src["pyq_text"])
            parts.append("\n")

        earlier = src.get("earlier_notes", {})
        if earlier:
            for title, content in earlier.items():
                parts.append(f"--- [SUPPLEMENTARY GUIDE: {title}] ---")
                parts.append(content)
                parts.append("\n")

    return "\n".join(parts)


def stream_gemini_response(
    client: genai.Client,
    model: str,
    messages: List[Dict[str, str]],
    context_text: str,
    temperature: float = 0.2
) -> Iterator[str]:
    """Streams responses from Gemini model using the official google-genai SDK."""
    # Build contents with context injected into the prompt
    full_system = f"{SYSTEM_INSTRUCTION}\n\n{context_text}"

    config = types.GenerateContentConfig(
        system_instruction=full_system,
        temperature=temperature,
        max_output_tokens=8192
    )

    # Format multi-turn chat contents
    contents = []
    for msg in messages:
        contents.append(types.Content(
            role="user" if msg["role"] == "user" else "model",
            parts=[types.Part.from_text(text=msg["content"])]
        ))

    try:
        response_stream = client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=config
        )
        for chunk in response_stream:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"\n\n**API Error**: `{str(e)}`\n\nPlease verify your Gemini API key or try switching to `gemini-1.5-flash` or `gemini-2.0-flash`."


def generate_single_response(
    client: genai.Client,
    model: str,
    prompt: str,
    context_text: str,
    temperature: float = 0.3
) -> str:
    """Synchronous single-shot content generation for Studio tools (Study Guide, Quiz, Audio Script)."""
    full_system = f"{SYSTEM_INSTRUCTION}\n\n{context_text}"
    config = types.GenerateContentConfig(
        system_instruction=full_system,
        temperature=temperature,
        max_output_tokens=8192
    )
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=config
        )
        return response.text or "No response generated."
    except Exception as e:
        return f"Error generating content: {e}"
