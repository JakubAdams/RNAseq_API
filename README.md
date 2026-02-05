# API to query a database of RNAseq data
This is an API to query a mock database of RNAseq gene expression data
(for example results from an 'abundance.tsv' file after running kallisto).
It allows the user to filter by gene, sample, TPM and export to CSV
(default is JSON), without directly interacting with the database itself
with SQL queries or navigating file paths in storage. It uses FastAPI and
SQLAlchemy to map database rows/columns to Python classes.
## Setup

1. Clone repo:
   ```bash
   git clone https://github.com/JakubAdams/RNAseq_API.git
   cd app
2. Create a virtual environment:
   ```python
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
3. Install dependencies:
`pip install -r requirements.txt`
4. Run FastAPI:
`fastapi dev main.py`
5. Open in browser:
Open the URL provided by FastAPI and add `"/expression"` to the end.
Add optional query parameters to the path, for example
`"/expression?gene_id=TP53&min_tpm=5&format=csv"` to fetch all rows
with the TP53 gene with TPM≥5 and export to CSV, ready for analysis. Visit
the interactive docs provided by FastAPI to try different queries.
