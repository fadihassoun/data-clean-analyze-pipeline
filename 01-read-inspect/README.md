Part of my workflow project: Excel ➜ Python ➜ SQLite ➜ Power BI

01 – Read & Inspect Excel (Clean & Analyse Pipeline)
---------------------------------------------------

This is the first step in my data cleaning and analysis pipeline: starting from raw Excel files, specifically with construction cost and time data, inspecting them, and preparing them for transformation.

What This Does
--------------

This script loads an Excel workbook, checks for:
- Data structure
- Data types
- Missing values

and then saves a clean summary as a markdown file (`summary.md`), so I can quickly assess what needs fixing in the next step.

---

Files Included
--------------

| File              | Purpose                                         |
|-------------------|-------------------------------------------------|
| load_excel.py     | Python script to inspect an Excel file and export a summary |
| sample_input.xlsx | Example dataset to test and explore             |
| summary.md        | Auto-generated report (after you run the script) |

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

    pip install pandas openpyxl tabulate

---

3) Prepare your files

Make sure your Excel file (e.g., sample_input.xlsx) is in the same folder as load_excel.py.

---

4) Run the script


Make sure your Excel file (e.g., sample_input.xlsx) and load_excel.py are in the same folder.

You can run the script either:

- **Without arguments** (the script will prompt you to type the filename), or  
- **With arguments** (you pass the filename when running)

---

4.1) Terminal / Command Prompt

- Without arguments (interactive prompt):

      python load_excel.py

- With argument (direct file path):

      python load_excel.py --file sample_input.xlsx

---

4.2) VS Code

- Without arguments:

  1. Open load_excel.py.  
  2. Click Run ▶️.  
  3. When prompted in the terminal, type the filename (e.g., sample_input.xlsx).

- With arguments (hardcoded):

  1. Add this before main():

         if __name__ == "__main__":
             import sys
             sys.argv = ["", "--file", "sample_input.xlsx"]
             main()

  2. Run the script.

---

4.3) Jupyter Notebook

- Without arguments:

      !python load_excel.py

  Enter filename when prompted.

- With arguments:

      !python load_excel.py --file sample_input.xlsx

---

4.4) PyCharm

- Without arguments:

  1. Open folder as PyCharm project.  
  2. Right-click load_excel.py → Run 'load_excel'.  
  3. Enter filename when prompted.

- With arguments:

  1. Go to Run > Edit Configurations.  
  2. Add `--file sample_input.xlsx` to Parameters.  
  3. Run the script.



Why This Matters
----------------

This is the foundation — before doing any cleaning, transformation, or analysis, I always inspect the shape and structure of the raw data. This gives me direction and prevents mistakes later.

---

Next

Clean column names and remove empty/duplicated/noisy rows.
