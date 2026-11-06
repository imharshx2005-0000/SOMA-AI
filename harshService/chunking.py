# ──────────────────────────────────────────────────────────
# chunking.py — Recursive Character Text Splitter
# ──────────────────────────────────────────────────────────
#
# GOAL:
#   Chunk the extracted text using recursive chunking.
#
# WHAT TO DO:
#   1. Import RecursiveCharacterTextSplitter from langchain-text-splitters.
#   2. Load CHUNK_SIZE and CHUNK_OVERLAP from config.
#   3. Set up separators suited for medical text:
#        ["\n\n", "\n", ". ", " ", ""]
#   4. Split the input text and return list of chunks.
#
# FUNCTION SIGNATURE:
#   chunk_text(text: str) -> list[str]
# ──────────────────────────────────────────────────────────


def chunk_text(text: str) -> list[str]:
    """Takes raw text, returns list of overlapping chunks."""
    pass
