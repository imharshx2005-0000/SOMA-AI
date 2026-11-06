# ──────────────────────────────────────────────────────────
# embedding.py — Gemma 2 Text Embeddings
# ──────────────────────────────────────────────────────────
#
# GOAL:
#   Embed all chunks using Gemma 2 (text) via sentence-transformers.
#
# WHAT TO DO:
#   1. Import SentenceTransformer from sentence-transformers.
#   2. Load EMBEDDING_MODEL_NAME from config (e.g. "google/gemma-2-2b").
#   3. Load the model.
#   4. Encode the list of chunks into dense vectors.
#   5. Return list of vectors (list of list of floats).
#
# FUNCTION SIGNATURE:
#   embed_chunks(chunks: list[str]) -> list[list[float]]
# ──────────────────────────────────────────────────────────


def embed_chunks(chunks: list[str]) -> list[list[float]]:
    """Takes list of text chunks, returns list of embedding vectors."""
    pass
