# __init__.py

from fastapi import APIRouter

# from . import transactions
from routers import transactions

APIRouter().include_router(transactions.router)
