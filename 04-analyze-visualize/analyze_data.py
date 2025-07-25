"""
Step 4 – Analyze & Visualize
----------------------------

This script connects to the SQLite database created in Step 3,
and analyzes basic cost statistics by vendor.

It produces a summary showing:
- Total records per vendor
- Total, min, max cost
- Sorted by total cost

The summary is printed to the console and saved to `analysis_summary.md`
"""

import sqlite3
import pandas as pd
from pathlib import Path


def main():
    # Get the current script directory
    script_dir = Path(__file__).resolve().parent

    # Build the path to the database (located in step 3 folder)
    db_path = script_dir.parent / "03-export-to-sqlite" / "database.db"

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # SQL query: Analyze total cost by vendor
    query = """
        SELECT
            vendor_name,
            COUNT(*) AS record_count,
            SUM(cost) AS total_cost,
            MIN(cost) AS min_cost,
            MAX(cost) AS max_cost
        FROM cleaned_data
        GROUP BY vendor_name
        ORDER BY total_cost DESC
    """

    # Run the query and load into DataFrame
    df = pd.read_sql_query(query, conn)

    # Output to markdown file
    summary_path = script_dir / "analysis_summary.md"
    summary_path.write_text(df.to_markdown(index=False), encoding="utf-8")

    # Print results
    print(df)
    print(f"\n✅ Summary saved to {summary_path.resolve()}")


if __name__ == "__main__":
    main()
