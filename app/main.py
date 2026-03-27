from pathlib import Path

from extractor import extract_text_from_pdf
from parser import parse_invoice_data
from validator import validate_invoice_data
from exporter import export_to_csv, export_to_excel


def process_invoice(pdf_path: str) -> dict:
    text = extract_text_from_pdf(pdf_path)
    parsed_data = parse_invoice_data(text)
    validated_data = validate_invoice_data(parsed_data)
    return validated_data


def main() -> None:
    input_dir = Path("data/input")
    output_dir = Path("data/output")

    pdf_files = list(input_dir.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in data/input")
        return

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")

        try:
            result = process_invoice(str(pdf_file))

            csv_output = output_dir / f"{pdf_file.stem}.csv"
            excel_output = output_dir / f"{pdf_file.stem}.xlsx"

            export_to_csv(result, str(csv_output))
            export_to_excel(result, str(excel_output))

            print("Done.")
            print(f"Status: {result['status']}")
            print(f"CSV: {csv_output}")
            print(f"Excel: {excel_output}")
            print("-" * 50)

        except Exception as exc:
            print(f"Error processing {pdf_file.name}: {exc}")


if __name__ == "__main__":
    main()
