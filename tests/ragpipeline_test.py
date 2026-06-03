from services.rag_pipeline import rag_chat

def test_rag_returns_response():
    response, sources = rag_chat("What is LangChain?")
    assert "langchain" in response.lower()

def test_rag_knows_groq():
    response, sources = rag_chat("What is Groq?")
    assert "groq" in response.lower()