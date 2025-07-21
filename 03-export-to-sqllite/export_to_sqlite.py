"""
Step 3 – Export to SQLite
-------------------------
This script loads the cleaned Excel file (from Step 2) and exports it into a SQLite database.

- Input: cleaned_output.xlsx (placed in the parent directory or passed via --file)
- Output: SQLite database file (default: database.db)
"""


import argparse
import pandas as pd
import sqlite3
from pathlib import Path

def main():
    # --- 1. Parse CLI arguments ---
    parser = argparse.ArgumentParser(description="Export cleaned Excel to SQLite.")
    parser.add_argument(
        "--file",
        "-f",
        help="Path to the cleaned Excel file (default: ../cleaned_output.xlsx)"
    )
    parser.add_argument(
        "--db",
        "-d",
        default="database.db",
        help="SQLite database file to create or update (default: database.db)"
    )
    args = parser.parse_args()

    # --- 2. Resolve paths ---
    script_dir = Path(__file__).resolve().parent

    if args.file:
        input_path = Path(args.file).resolve()
    else:
        input_path = script_dir.parent / "cleaned_output.xlsx"

    db_path = script_dir / args.db

    # --- 3. Load Excel file ---
    print(f"\n📥 Reading Excel from: {input_path}")
    try:
        df = pd.read_excel(input_path)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_path}")
        return

    # --- 4. Export to SQLite ---
    print(f"💾 Writing to SQLite DB: {db_path}")
    conn = sqlite3.connect(db_path)
    df.to_sql("cleaned_data", conn, if_exists="replace", index=False)
    conn.close()

    # --- 5. Done ---
    print("✅ Export complete!")

if __name__ == "__main__":
    main()
