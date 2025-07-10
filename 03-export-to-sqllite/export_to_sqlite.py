import argparse
import pandas as pd
import sqlite3
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Export cleaned Excel data to SQLite database.")
    parser.add_argument(
        "--file",
        "-f",
        required=True,
        help="Path to the cleaned Excel file."
    )
    parser.add_argument(
        "--db",
        "-d",
        default="database.db",
        help="SQLite database file to create or update (default: database.db)."
    )
    args = parser.parse_args()
    excel_path = Path(args.file)
    db_path = Path(args.db)

    print(f"\n📥 Loading cleaned Excel file: {excel_path}")
    df = pd.read_excel(excel_path)

    print(f"\n📡 Connecting to SQLite database: {db_path}")
    conn = sqlite3.connect(db_path)

    table_name = "cleaned_data"
    print(f"\n🚀 Exporting data to table '{table_name}' (will replace if exists)")
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()
    print("\n✅ Export complete. Database ready for analysis.")

if __name__ == "__main__":
    main()
