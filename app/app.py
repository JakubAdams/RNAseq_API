from fastapi import FastAPI, Depends, Query, Response
from sqlalchemy.orm import Session
from pydantic import BaseModel
import pandas as pd
import io

from database import SessionLocal, engine
from models import Base, GeneExpression

#create tables if they don't exist
Base.metadata.create_all(bind=engine)

#create an instance of the FastAPI class
app = FastAPI(title="RNA-seq expression API")

#dependency that gives us a database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#use a Pydantic model to define in what format FastAPI should
#return the data in the "responsemodel=" parameter
class Response(BaseModel):
    gene_id: str
    sample_id: str
    tpm: float

@app.get("/expression")
def get_expression(
    gene_id: str,
    sample_id: str | None = None,
    min_tpm: float | None = None,
    format: str = Query("json", regex="^(json|csv)$"),
    db: Session = Depends(get_db),
    response_model = Response
):
    #build query using SQLAlchemy (no raw SQL)
    query = db.query(GeneExpression).filter(GeneExpression.gene_id == gene_id)

    if sample_id:
        query = query.filter(GeneExpression.sample_id == sample_id)

    results = query.all()

    #convert to list of dicts
    data = [
        {
            "gene_id": r.gene_id,
            "sample_id": r.sample_id,
            "tpm": r.tpm,
        }
        for r in results
        if min_tpm is None or r.tpm >= min_tpm
    ]

    #CSV option
    if format == "csv":
        df = pd.DataFrame(data)
        buf = io.StringIO()
        df.to_csv(buf, index=False)

        return Response(
            content=buf.getvalue(),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=expression.csv"},
        )

    #default: JSON
    return {
        "gene_id": gene_id,
        "n_results": len(data),
        "results": data,
    }
