import pdfplumber
import re

def extract_outline(pdf_path):
    outline = []
    title = None
    font_sizes = {}

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            lines = page.extract_text().split("\n") if page.extract_text() else []

            for line in lines:
                cleaned = line.strip()
                if not cleaned:
                    continue

                # Heuristic rules: adjust based on your PDF fonts/sizes
                if re.match(r'^[A-Z][A-Z\s]{3,}$', cleaned):  # ALL CAPS = likely title
                    if not title:
                        title = cleaned

                elif len(cleaned.split()) < 8 and cleaned[0].isupper():
                    # Short and starts with uppercase
                    if cleaned.endswith(":"):
                        cleaned = cleaned[:-1]
                    level = "H1"
                    if cleaned.count(" ") >= 2:
                        level = "H2"
                    if cleaned.count(" ") >= 4:
                        level = "H3"

                    outline.append({
                        "level": level,
                        "text": cleaned,
                        "page": i + 1
                    })

    return title or "Unknown Title", outline
