from pathlib import Path
import pdfplumber


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a text-based PDF.
    Returns the full extracted text as a string.
    """
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    extracted_pages = []

    with pdfplumber.open(path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            extracted_pages.append(page_text)

    full_text = "\n".join(extracted_pages).strip()
    return full_text
