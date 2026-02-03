#Define the database schema as a Python class using SQLAlchemy
#this way we'll be able to interact with the database Pythonically
#without writing raw SQL queries
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import declarative_base
#define the default class from which subsequent classes will inherit
Base = declarative_base

#define database schema
class GeneExpression(Base):
    __tablename__ = "gene_expression"
    gene_id = Column(String, primary_key=False)
    sample_id = Column(String, primary_key=False)
    TPM = Column(Float)
