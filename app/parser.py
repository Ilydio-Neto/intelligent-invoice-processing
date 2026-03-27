import re
from typing import Dict, Optional


def _search_pattern(patterns: list[str], text: str) -> Optional[str]:
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def parse_invoice_data(text: str) -> Dict[str, Optional[str]]:
    """
    Extracts key invoice fields from raw text using regex patterns.
    This is an MVP and can be expanded later.
    """

    supplier = _search_pattern(
        [
            r"Fornecedor[:\s]+(.+)",
            r"Emitente[:\s]+(.+)",
            r"Raz[aã]o Social[:\s]+(.+)",
        ],
        text,
    )

    invoice_number = _search_pattern(
        [
            r"N[uú]mero da fatura[:\s]+([\w\-/\.]+)",
            r"N[uú]mero[:\s]+([\w\-/\.]+)",
            r"Invoice Number[:\s]+([\w\-/\.]+)",
            r"NF[:\s]+([\w\-/\.]+)",
        ],
        text,
    )

    issue_date = _search_pattern(
        [
            r"Data de emiss[aã]o[:\s]+(\d{2}/\d{2}/\d{4})",
            r"Data[:\s]+(\d{2}/\d{2}/\d{4})",
            r"Issue Date[:\s]+(\d{2}/\d{2}/\d{4})",
        ],
        text,
    )

    total_amount = _search_pattern(
        [
            r"Valor total[:\s]+R?\$?\s*([\d\.\,]+)",
            r"Total[:\s]+R?\$?\s*([\d\.\,]+)",
            r"Valor a pagar[:\s]+R?\$?\s*([\d\.\,]+)",
            r"Amount Due[:\s]+\$?\s*([\d\.\,]+)",
        ],
        text,
    )

    tax_id = _search_pattern(
        [
            r"CNPJ[:\s]+([\d\.\-/]+)",
            r"CPF/CNPJ[:\s]+([\d\.\-/]+)",
            r"Tax ID[:\s]+([\w\.\-/]+)",
        ],
        text,
    )

    return {
        "supplier": supplier,
        "invoice_number": invoice_number,
        "issue_date": issue_date,
        "total_amount": total_amount,
        "tax_id": tax_id,
        "raw_text_preview": text[:500],
    }
