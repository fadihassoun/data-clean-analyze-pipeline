Part of my workflow project: Excel ➜ Python ➜ SQLite ➜ Power BI

04 – Analyze and Visualize Data
-------------------------------

This is Step 4 in my data pipeline. Here, I analyze the structured data that was exported to SQLite in Step 3. Using Python, I query the database and generate summaries — which are then used for visualization in tools like Power BI.

---

What This Does
--------------

- Connects to `database.db` (from Step 3)
- Groups data by **Cost Type**
- Calculates:
  - Average unit price
  - Minimum and maximum prices
  - Item counts per cost type
- Saves the result as `summary_stats.csv`

This CSV file can then be **easily loaded into Power BI** to create interactive dashboards.

---

Files Included
--------------

| File              | Purpose                                                  |
|-------------------|----------------------------------------------------------|
| `analyze_data.py` | Python script to query and summarize from SQLite         |
| `summary_stats.csv` | Output of the analysis for use in Power BI             |

---

How to Use
----------

1) Activate your virtual environment:

Windows (CMD or PowerShell)
```bash
.venv\Scripts\activate
