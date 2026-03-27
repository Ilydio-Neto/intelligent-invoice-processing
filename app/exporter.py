from pathlib import Path
import pandas as pd
from typing import Dict, Any


def export_to_csv(data: Dict[str, Any], output_path: str) -> None:
    """
    Exports invoice data to CSV.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame([data])
    df.to_csv(path, index=False, encoding="utf-8-sig")


def export_to_excel(data: Dict[str, Any], output_path: str) -> None:
    """
    Exports invoice data to Excel.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame([data])
    df.to_excel(path, index=False)
