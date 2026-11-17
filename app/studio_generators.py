"""
studio_generators.py
Generates NotebookLM-style Studio artifacts:
- Audio Overview / Deep Dive Podcast Script
- Comprehensive Study Guide
- NIT Jalandhar PYQ Exam Simulator & Marking Scheme
- Cheat Sheet / Formula & Complexity Matrix
- High-Yield FAQ / 2-Mark Drill
"""

from typing import Dict, Any, List
import gemini_engine


def generate_podcast_script(
    client,
    model: str,
    subject_name: str,
    topic_or_unit: str,
    context_text: str
) -> str:
    """Generates a NotebookLM-style 2-host audio podcast transcript."""
    prompt = f"""Generate a high-energy, educational, and engaging 2-host "NotebookLM Deep Dive" Audio Podcast Script on the topic:
SUBJECT: {subject_name}
FOCUS TOPIC / UNIT: {topic_or_unit}

CAST:
- **Alex (Host 1 - The Inquisitive Learner)**: Asks the exact questions that confuse students, brings up tricky exam questions, and reacts with "Wait, so why does that happen?"
- **Jamie (Host 2 - The Senior Expert / Exam Veteran)**: Explains concepts with crisp real-world analogies, breaks down technical jargon, reveals examiner tricks, and cites past paper traps.

FORMATTING REQUIREMENTS:
- Structure the script as a full back-and-forth dialogue:
  - **Alex**: ...
  - **Jamie**: ...
- Include stage directions in brackets like *[chuckles]*, *[pauses thoughtfully]*, *[leans forward]*.
- Cover the foundational concept, the tricky mathematical/algorithmic mechanics, real exam question patterns from NIT Jalandhar, and a memorable memory hook/mnemonic.
- Keep the tone lively, intellectually deep, and memorable. Make it feel like two brilliant friends having an incredible late-night revision session before the end-term exam.
"""
    return gemini_engine.generate_single_response(client, model, prompt, context_text)


def generate_study_guide(
    client,
    model: str,
    subject_name: str,
    topic_or_unit: str,
    context_text: str
) -> str:
    """Generates an exhaustive, high-yield examination briefing document."""
    prompt = f"""Generate an authoritative, comprehensive End-Term Examination Study Guide for:
SUBJECT: {subject_name}
TOPIC / UNIT: {topic_or_unit}

Please organize the guide into the following structured sections:
1. **Executive Overview & Unit Blueprint**: High-level mental model of why this unit exists and its weightage in NIT Jalandhar end-term exams.
2. **Key Concepts & Formal Definitions**: Crystal-clear definitions of core terms that examiners test in 2-mark questions.
3. **Core Theorems, Proofs & Algorithms**: In-depth mathematical derivations and algorithm steps formatted in LaTeX ($...$ and $$...$$).
4. **Historical PYQ Frequency & Pattern Analysis**: Analysis of how this topic appeared in past NIT Jalandhar exams (2019–2024).
5. **High-Yield Comparison Tables**: Side-by-side markdown comparison matrices for frequently contrasted concepts.
6. **Common Exam Traps & Examiner Pitfalls**: The exact errors students make that cause grade deductions.
7. **Quick 5-Minute Pre-Exam Checklist**: Bullet points of must-remember formulas, rules, and edge cases.
"""
    return gemini_engine.generate_single_response(client, model, prompt, context_text)


def generate_exam_simulator(
    client,
    model: str,
    subject_name: str,
    difficulty: str,
    context_text: str
) -> str:
    """Generates a realistic mock exam paper matching NIT Jalandhar standards with answer key."""
    prompt = f"""Create an authentic NIT Jalandhar End-Term Examination Mock Paper for:
SUBJECT: {subject_name}
TARGET DIFFICULTY: {difficulty}

Format the mock test strictly according to the NIT Jalandhar End-Term format:
- **Total Marks**: 50 Marks (Standard End-Sem Pattern)
- **Time Allowed**: 2 Hours

SECTIONS:
- **SECTION A (5 Questions x 2 Marks = 10 Marks)**: Short, precise conceptual definitions, differences, or one-line calculations.
- **SECTION B (4 Questions x 5 Marks = 20 Marks)**: Algorithmic walkthroughs, state machines, normalization problems, or proofs.
- **SECTION C (2 Questions x 10 Marks = 20 Marks - Choose any 2 out of 3)**: Comprehensive design problems, long derivations, complex code implementations, or pipeline hazard analyses.

AFTER THE QUESTION PAPER:
Provide a **COMPLETE, RIGOROUS MARKING SCHEME & STEP-BY-STEP SOLUTION KEY** with point-by-point mark distribution for every question so students can self-evaluate.
"""
    return gemini_engine.generate_single_response(client, model, prompt, context_text)


def generate_cheat_sheet(
    client,
    model: str,
    subject_name: str,
    context_text: str
) -> str:
    """Generates an ultra-dense revision cheat sheet with formulas, complexities, and tables."""
    prompt = f"""Generate an ultra-dense, 1-page equivalent Examination Revision Cheat Sheet for:
SUBJECT: {subject_name}

Include:
1. **Time & Space Complexity Reference Matrix**: Best, Average, Worst case, In-place?, Stable?
2. **Mathematical Formulas & Recurrence Solutions**: Exact closed-form equations.
3. **Key Syntax, Code Snippets & Signatures**: Clean C++ / SQL / JS syntactical skeletons.
4. **Architecture / Protocol / State Machine Diagrams**: ASCII diagrammatic cheat sheets.
5. **Golden Rules & Heuristics**: 10 one-line memory heuristics for solving tricky questions fast.
"""
    return gemini_engine.generate_single_response(client, model, prompt, context_text)


def generate_faq_drill(
    client,
    model: str,
    subject_name: str,
    context_text: str
) -> str:
    """Generates 15 rapid-fire 2-mark viva and short answer questions with ideal model answers."""
    prompt = f"""Generate a high-intensity "15 High-Yield 2-Mark & Viva Questions Drill" for:
SUBJECT: {subject_name}

For each question:
- State the Question clearly.
- Note which exam year / unit it appears in.
- Provide the **Model Answer** (exact 3 to 4 lines that get full 2/2 marks from the examiner).
- Add an **Examiner's Note**: What key buzzword the professor searches for when grading.
"""
    return gemini_engine.generate_single_response(client, model, prompt, context_text)
