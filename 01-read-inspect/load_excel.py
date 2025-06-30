"""
1 – Read & Inspect Excel
----------------------------
This script loads an Excel file and gives a quick structural summary:
- Shape
- Column types
- Missing values

It saves the summary to `summary.md` and also prints it to the console.
"""

import argparse
import pandas as pd
from pathlib import Path

def inspect_df(df: pd.DataFrame) -> str:
    """Create a readable summary of the DataFrame."""
    lines = []

    # Shape of the dataset
    lines.append(f"Dataset shape: {df.shape}\n")

    # Column data types
    lines.append("Column dtypes:\n")
    lines.append(df.dtypes.astype(str).to_markdown())

    # Missing values per column
    lines.append("\n\nMissing values per column:\n")
    lines.append((df.isna().sum()).to_markdown())

    return "\n".join(lines)

def get_file_path() -> Path:
    """
    Parse the command-line argument for Excel file path.
    If not provided or invalid, prompt user interactively until a valid path is given.
    """
    parser = argparse.ArgumentParser(description="Read and inspect an Excel file.")
    parser.add_argument(
        "--file",
        "-f",
        required=False,  # Changed to optional
        help="Path to the input Excel file."
    )
    args = parser.parse_args()

    if args.file:
        path = Path(args.file)
        if path.is_file():
            return path
        else:
            print(f"File not found: {path}")
    # Interactive prompt fallback
    while True:
        user_input = input("Please enter the path to the Excel file: ").strip()
        path = Path(user_input)
        if path.is_file():
            return path
        print("Invalid file path, please try again.")

def main():
    # ---- STEP 0: GET FILE PATH ----
    path = get_file_path()

    # ---- STEP 1: LOAD ----
    print(f"\nLoading Excel file: {path}\n")
    df = pd.read_excel(path)

    # ---- STEP 2: SUMMARISE ----
    report = inspect_df(df)

    # ---- STEP 3: SAVE REPORT ----
    out_path = Path("summary.md")
    out_path.write_text(report, encoding="utf-8")

    # ---- STEP 4: OUTPUT ----
    print(report)
    print(f"\nSummary saved to {out_path.resolve()}")
    print("Done.")

if __name__ == "__main__":
    main()
