from src.rag_pipeline import generate_answer

test_cases = [
    "58-year-old with chest pain radiating to left arm, sweating, nausea",
    "36-year-old with fever, productive cough, pleuritic chest pain",
    "24-year-old with polyuria, polydipsia, weight loss, blurred vision"
]

for i, case in enumerate(test_cases, 1):
    print("=" * 80)
    print(f"CASE {i}: {case}")
    print("=" * 80)
    escalation, response = generate_answer(case)
    if escalation:
        print("ESCALATION:", escalation)
    print(response)
