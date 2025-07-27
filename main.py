import os
import json
from heading_extractor import extract_outline

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def process_all_pdfs():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"Looking inside: {INPUT_DIR}")
    print(f"Files: {os.listdir(INPUT_DIR)}")

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            print(f"Processing: {filename}")
            pdf_path = os.path.join(INPUT_DIR, filename)

            try:
                title, outline = extract_outline(pdf_path)

                result = {
                    "title": title,
                    "outline": outline
                }

                output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                print(f"✅ Output saved to {output_path}")

            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_all_pdfs()
