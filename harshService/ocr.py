# ──────────────────────────────────────────────────────────
# ocr.py — Medical OCR using Gemini 2.5 Flash
# ──────────────────────────────────────────────────────────
#
# GOAL:
#   Extract ALL text from a medical report image using google-genai
#   gemini-2.5-flash model.
#
# WHAT TO DO:
#   1. Import google-genai and load GEMINI_API_KEY from config.
#   2. Write a strict system prompt — tell the model:
#      - You are a Medical OCR Engine.
#      - Extract text EXACTLY as it appears (values, units, ranges, tables, dates).
#      - Use Markdown tables for tabular data.
#      - Preserve reading order and clear line breaks between sections
#        (so output is recursive-chunking friendly).
#      - Do NOT add commentary, interpretation, or medical advice.
#      - Write [ILLEGIBLE] for unreadable parts.
#   3. Read the image file, detect its MIME type.
#   4. Send image + prompt to gemini-2.5-flash with temperature=0.
#   5. Return the extracted text as a string.
#
# FUNCTION SIGNATURE:
#   extract_text(image_path: str) -> str
# ──────────────────────────────────────────────────────────


def extract_text(image_path: str) -> str:
    """Takes an image path, returns all extracted text."""
    pass
