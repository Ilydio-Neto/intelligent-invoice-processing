from datetime import datetime
from typing import Dict, Any


def _is_valid_date(date_str: str | None) -> bool:
    if not date_str:
        return False

    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def _normalize_amount(amount_str: str | None) -> float | None:
    if not amount_str:
        return None

    try:
        normalized = amount_str.replace(".", "").replace(",", ".")
        return float(normalized)
    except ValueError:
        return None


def validate_invoice_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates extracted invoice data and appends validation fields.
    """
    required_fields = ["supplier", "invoice_number", "issue_date", "total_amount"]

    missing_fields = [field for field in required_fields if not data.get(field)]

    valid_date = _is_valid_date(data.get("issue_date"))
    normalized_amount = _normalize_amount(data.get("total_amount"))

    issues = []

    if missing_fields:
        issues.append(f"Missing fields: {', '.join(missing_fields)}")

    if data.get("issue_date") and not valid_date:
        issues.append("Invalid issue date format")

    if data.get("total_amount") and normalized_amount is None:
        issues.append("Invalid total amount format")

    if not issues:
        status = "success"
    elif len(missing_fields) < len(required_fields):
        status = "partial"
    else:
        status = "failed"

    validated_data = data.copy()
    validated_data["normalized_amount"] = normalized_amount
    validated_data["status"] = status
    validated_data["validation_issues"] = " | ".join(issues) if issues else ""

    return validated_data
