from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "data" / "pdf" / "genai-principles.pdf"
TEXT_PATH = BASE_DIR /"data" /"text_files" /"python_intro.txt"
from utlis.chunking import load_and_chunk

def test_pdf_chunking():
    chunks = load_and_chunk("pdf",str(PDF_PATH))
    assert len(chunks) > 0


def test_text_chunking():
    chunks = load_and_chunk("text",TEXT_PATH)
    assert len(chunks) > 0


def test_chunk_has_content():
    chunks = load_and_chunk("text",TEXT_PATH)
    assert chunks[0].page_content != ""