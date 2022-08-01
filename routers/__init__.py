# __init__.py

from fastapi import APIRouter

from routers import transactions

APIRouter().include_router(transactions.router)
