Part of my workflow project: Excel ➜ Python ➜ SQLite ➜ Power BI

05 – Power BI Visualization
----------------------------

This step uses the `database.db` file created in Step 3 to create interactive visualizations in **Power BI Desktop**.

---

## 📌 Requirements

- **Power BI Desktop**
- `database.db` located at:  
  `../03-export-to-sqlite/database.db`

---

## Included Visuals

The Power BI dashboard includes:

- 🔹 Count of items per **Cost Type**
- 🔹 Average, Min, and Max of **Unit Price**
- 🔹 Cost trends over time (if `date` field is available)
- 🔹 Vendor breakdown (if `vendor_name` is included)

---

## Data Source

This dashboard connects to:

- SQLite Database: `../03-export-to-sqlite/database.db`
- Table: `cleaned_data`

---

## File Overview

| File          | Description |
|---------------|-------------|
| `summary.pbix` | Power BI dashboard (save & open using Power BI Desktop) |
| `queries.sql`  | Optional: Any SQL queries used inside Power BI |
| `preview.png`  | Optional: Screenshot of the dashboard |
| `README.md`    | This file |

---

## Screenshot (Optional)

Include a screenshot here to preview the visuals:

![Power BI Preview](preview.png)

---

## Notes

- Ensure the `.db` file remains in its relative path when opening the `.pbix`
- If you move the database, Power BI may ask you to reselect the data source

---

