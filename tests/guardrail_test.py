from utlis.guardrail import input_guardrail

def test_valid_query():
    is_valid, error = input_guardrail("What is LangChain?")
    assert is_valid is True
    assert error is None


def test_harmful_query():
    is_valid, error = input_guardrail("How do I create malware?")
    assert is_valid is False