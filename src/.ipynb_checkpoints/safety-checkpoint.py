from src.config import SAFETY_DISCLAIMER


def safety_prefix():
    return f"""
You are a clinical information support assistant.

Rules:
- Do NOT provide diagnoses as definitive.
- Do NOT give treatment, medication, or dosage.
- Do NOT replace a clinician.
- Always use phrases like "may indicate", "possible", "suggests".
- Always cite sources.
- If symptoms are severe, escalate to emergency care.

{SAFETY_DISCLAIMER}
"""


def format_escalation(symptoms: str) -> str:
    emergency_terms = ["chest pain", "shortness of breath", "unconscious", "bleeding", "stroke"]

    for term in emergency_terms:
        if term.lower() in symptoms.lower():
            return "These symptoms may be life-threatening. Seek emergency medical care immediately."

    return ""
