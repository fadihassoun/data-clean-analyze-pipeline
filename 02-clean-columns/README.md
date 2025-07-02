Part of my workflow project: Excel ➜ Python ➜ SQLite ➜ Power BI

02 – Clean Column Names (Clean & Analyse Pipeline)
---------------------------------------------------

This is the second step in my data cleaning and analysis pipeline. After inspecting raw Excel files (Step 1), we now clean the data by standardizing column names and removing empty or duplicated rows — preparing the dataset for structured transformation and export.

What This Does
--------------

This script:
- Loads the Excel file used in Step 1 (`sample_input.xlsx`)
- Standardizes column names (lowercase, trimmed, symbols removed, spaces → underscores)
- Removes rows that are completely empty
- Removes fully duplicated rows

It then saves a cleaned version of the data to a new file: `cleaned_output.xlsx`

---

Files Included
--------------

| File                | Purpose                                               |
|---------------------|-------------------------------------------------------|
| clean_columns.py    | Python script to clean and export the Excel file      |
| cleaned_output.xlsx | Auto-generated cleaned Excel file (after running)     |

> Uses the input file from: `../01-read-inspect/sample_input.xlsx`

---

How to Use
----------

1) (Optional) Set up a virtual environment

Windows (CMD or PowerShell)
    python -m venv .venv
    .venv\Scripts\activate

macOS/Linux (bash/zsh)
    python3 -m venv .venv
    source .venv/bin/activate

---

2) Install the required packages

    pip install pandas openpyxl

---

3) Prepare your files

- Make sure you have already completed Step 1.
- Your Excel file should be in `01-read-inspect/sample_input.xlsx`
- `clean_columns.py` should be located in `02-clean-columns/`

---

4) Run the script

The script has no arguments — it expects the input Excel file to exist in the `01-read-inspect/` folder.

---

4.1) Terminal / Command Prompt

    python 02-clean-columns/clean_columns.py

---

4.2) VS Code

    1. Open `clean_columns.py`
    2. Click ▶️ Run
    3. The script will load the file automatically and save `cleaned_output.xlsx` in the same folder

---

4.3) Jupyter Notebook

    !python 02-clean-columns/clean_columns.py

---

4.4) PyCharm

    1. Open the project folder in PyCharm
    2. Right-click `clean_columns.py` → Run
    3. Output file will appear in the same folder

---

Why This Matters
----------------

Cleaning your data early prevents downstream issues — and column name consistency is essential for merging, analysis, and automation. This step sets the stage for structured transformation and database loading.

---

Next
-----

Export the cleaned data to SQLite for structured querying and Power BI connection.
