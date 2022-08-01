# transactions.py
import typing
import json

from fastapi import APIRouter
from fastapi import Query
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

# from ..schemas import transactions_response
# from .. import db
from schemas import transactions_response
import db


router = APIRouter()


@router.get("/transactions/{hash}")
async def index(
    request: Request,
    hash: str = Query(...)
):

    result = await db.queries.get_trans_from_hash(hash)
    
    transaction_response_obj: typing.Optional[transactions_response.TransactionsResponse] = None

    try:
        if result:
            transaction_response_obj = transactions_response.TransactionsResponse(**result)
    except ValidationError as e:
        return  JSONResponse(
            content={'body': json.dumps(e.errors())},
            status_code=400
        )

    return JSONResponse(
        content=transaction_response_obj.dict(by_alias=True) 
        if transaction_response_obj else {"message": "invalid hash"},
        status_code=200
    )

import sqlalchemy
sqlalchemy.engine.row.Row