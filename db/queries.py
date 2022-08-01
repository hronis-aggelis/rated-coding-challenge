# queries.py

import typing
import databases
import sqlalchemy
import json

# from .. import db
# from . import models
# from .. import errors
import db
from db import models
import errors

metadata = sqlalchemy.MetaData()


async def get_trans_from_hash(hash: str):
    try:
        query = models.transactions.select().with_only_columns([models.transactions.c.hash, models.transactions.c.from_address, models.transactions.c.to_address,
                                            models.transactions.c.block_number, models.transactions.c.utc_timestamp, models.transactions.c.gas_cost_in_gwei,
                                            models.transactions.c.eth_price]).where(models.transactions.c.hash == hash)
        return await db.database.fetch_one(query)
    except sqlalchemy.exc.SQLAlchemyError as sql_error:
        raise errors.db.DbError(details=str(sql_error))
