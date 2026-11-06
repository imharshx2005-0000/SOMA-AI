# ──────────────────────────────────────────────────────────
# upsert.py — Upsert Vectors + Metadata into Qdrant Cloud
# ──────────────────────────────────────────────────────────
#
# GOAL:
#   Upsert embedded vectors with filterable metadata into Qdrant Cloud.
#
# WHAT TO DO:
#   1. Import QdrantClient from qdrant-client.
#   2. Load QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION_NAME from config.
#   3. Connect to Qdrant Cloud using url + api_key.
#   4. Check if collection exists — if not, create it with correct vector size
#      and COSINE distance.
#   5. Build PointStruct for each chunk with:
#        - id: uuid
#        - vector: the embedding
#        - payload metadata:
#            • text         (the chunk text)
#            • user_id      (who owns this report)
#            • source_image (original image filename)
#            • chunk_index  (position in the document)
#            • ReportDate   (date of the report — for filtering)
#   6. Upsert all points into the collection.
#   7. Return list of generated point IDs.
#
# FUNCTION SIGNATURE:
#   upsert_vectors(chunks, vectors, *, user_id, source_image, report_date) -> list[str]
# ──────────────────────────────────────────────────────────


def upsert_vectors(
    chunks: list[str],
    vectors: list[list[float]],
    *,
    user_id: str,
    source_image: str,
    report_date: str | None = None,
) -> list[str]:
    """Upsert vectors + metadata into Qdrant. Returns list of point IDs."""
    pass
