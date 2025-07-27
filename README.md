# Adobe India Hackathon 2025 - Round 1A Solution

## 🔍 Problem Statement

You are given PDF documents (up to 50 pages). The goal is to **automatically extract a structured outline** of each document, consisting of:

- **Title**  
- **Headings** (H1, H2, H3)  
  - With their text  
  - Heading level (H1, H2, or H3)  
  - Page number  

The output must be a **valid JSON file** capturing this hierarchy and metadata.

## 🎯 Objective

Create a **Dockerized CLI tool** that:

- Processes all PDFs inside `/app/input` directory  
- Extracts the **title** and **hierarchical headings**  
- Produces JSON output files in `/app/output` (one per PDF)  
- Runs **offline** on CPU with no external API calls  
- Completes processing within 10 seconds for 50-page PDFs  
- Uses models or libraries ≤ 200MB  

## 🧠 Approach & Methodology

1. **PDF Parsing & Text Extraction:**  
   Used [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) for reliable offline extraction of text, font sizes, and page info.

2. **Heading Level Inference:**  
   Since PDFs don’t tag headings explicitly, inferred headings based on **font size clustering**:  
   - Extract all text spans with font sizes  
   - Cluster the top 3 frequent font sizes → mapped to H1, H2, H3 respectively  
   - Text with other font sizes ignored or treated as body text

3. **Title Extraction:**  
   - Picked the **largest font text on page 1** as the title.  
   - If no clear candidate found, defaulted to `"Untitled Document"`.

4. **Output Formatting:**  
   - Created JSON files in the specified format, preserving order and page numbers.
8

## 🏗️ Project Structure
```
adobe-hackathon-round1a/
│
├── app/
│ ├── main.py # Main extraction script
│ └── utils.py # Helper functions (if any)
│
├── input/ # Folder to place input PDFs (for local testing)
├── output/ # Folder where JSON results will be saved (for local testing)
│
├── Dockerfile # Docker setup
├── requirements.txt # Python dependencies
└── README.md # This document
```
## ⚙️ How to Build and Run

### Build Docker Image
```bash
docker build --platform linux/amd64 -t heading-extractor:solution .


