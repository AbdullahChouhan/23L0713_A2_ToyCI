"""Task 6.6 Toy CI Test File (Commit 1: Intentional Failure for Red Run)."""


def normalize_confidence(prob_ai: float, threshold: float = 0.50) -> tuple[str, float]:
    if prob_ai >= threshold:
        return "AI-Generated", round(prob_ai, 4)
    return "Real", round(1.0 - prob_ai, 4)


def test_ai_prediction():
    label, conf = normalize_confidence(0.85, threshold=0.50)
    assert label == "AI-Generated"
    # Intentional wrong assertion (0.99 instead of 0.85) to trigger RED CI run:
    assert conf == 0.99
