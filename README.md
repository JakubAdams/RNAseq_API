# FastAPI API to query a database of RNAseq data

## Setup

1. Clone repo:
   ```bash
   git clone https://github.com/JakubAdams/RNAseq_API.git
   cd app
2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run FastAPI
fastapi dev main.py
5. Run in browser
Open the URL provided by FastAPI and add "/expression" to the end.
Add optional query parameters to the path, for example
"/expression?gene_id=TP53&min_tpm=5&format=csv" to fetch all rows
with TP53 with TPM>=5 and export to CSV, ready for analysis
