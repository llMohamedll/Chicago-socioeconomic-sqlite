Chicago Socioeconomic SQLite Analysis

## Overview
This project demonstrates SQL database operations using Python, including database creation, complex queries, joins, aggregations, and integration with pandas for analysis.

## Original Notebooks (4)
- `DB0201EN-Week3-1-3-SQLmagic-SQlite-v2.ipynb`
- `DB0201EN-Week3-1-4-Analyzing-SQLite-v2.ipynb`
- `DB0201EN-Week4-1-1-RealDataPractice-v5-sqlite-Learner-v2(Edited).ipynb`
- `Week4-Insert-Update-SQLite-v2.ipynb`

## Key Skills Demonstrated
- SQLite database creation and management
- SQL queries: SELECT, WHERE, ORDER BY, GROUP BY, HAVING
- JOIN operations (INNER, LEFT)
- CRUD operations (CREATE, READ, UPDATE, DELETE)
- pandas `read_sql_query()` integration
- Statistical analysis and visualization

## How to Run
```bash
pip install pandas numpy matplotlib seaborn
python main.py
```

## Outputs
- `chicago_analysis.png` - Socioeconomic correlation analysis
- `chicago_sql_analysis.png` - SQL query results visualization

## Key Findings
- Strong negative correlation between per capita income and hardship index
- Unemployment rate positively correlates with hardship index
- SQL + pandas enables powerful analytical workflows
