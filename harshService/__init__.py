# ──────────────────────────────────────────────────────────
# harshService/__init__.py — Exports imgUpsert
# ──────────────────────────────────────────────────────────
#
# GOAL:
#   Chain all 4 steps into one function:
#     OCR → Chunking → Embedding → Upsert
#
# WHAT TO DO:
#   1. Import extract_text   from harshService.ocr
#   2. Import chunk_text     from harshService.chunking
#   3. Import embed_chunks   from harshService.embedding
#   4. Import upsert_vectors from harshService.upsert
#   5. In imgUpsert:
#        text    = extract_text(image_path)
#        chunks  = chunk_text(text)
#        vectors = embed_chunks(chunks)
#        ids     = upsert_vectors(chunks, vectors, metadata...)
#        return result dict
#
# FUNCTION SIGNATURE:
#   imgUpsert(image_path, *, user_id, report_date) -> dict
# ──────────────────────────────────────────────────────────


def imgUpsert(
    image_path: str,
    *,
    user_id: str = "default_user",
    report_date: str | None = None,
) -> dict:
    """Full pipeline: OCR → Chunk → Embed → Upsert. Returns result dict."""
    pass
