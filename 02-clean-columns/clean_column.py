"""
2 – Clean Columns
-----------------------
This script loads the Excel file from Step 1, performs basic data cleaning, and saves a new cleaned version:
- Standardizes column names (lowercase, trimmed, spaces to underscores)
- Removes fully empty rows
- Optionally drops duplicate rows

Input:  ../01-read-inspect/sample_input.xlsx  
Output: cleaned_output.xlsx
"""

import pandas as pd
from pathlib import Path

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names: lowercase, trimmed, and underscores."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(r"\s+", "_", regex=True)
    )
    return df

def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows that are completely empty."""
    return df.dropna(how='all')

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove fully duplicated rows."""
    return df.drop_duplicates()

def main():
    input_path = Path("../01-read-inspect/sample_input.xlsx")
    output_path = Path("cleaned_output.xlsx")

    print(f"🔹 Loading: {input_path}")
    df = pd.read_excel(input_path)

    print("🔹 Cleaning column names...")
    df = clean_column_names(df)

    print("🔹 Removing empty rows...")
    df = remove_empty_rows(df)

    print("🔹 Removing duplicate rows...")
    df = remove_duplicates(df)

    print(f"✅ Saving cleaned data to: {output_path}")
    df.to_excel(output_path, index=False)

    print("✅ Done.")

if __name__ == "__main__":
    main()
