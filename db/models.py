from sqlalchemy import Column, DateTime, Float, String, Integer, Table, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


transactions = Table(
    "transactions",
    Base.metadata,
    Column("hash", String(255), primary_key=True, autoincrement=False),
    Column("nonce", Integer),
    Column("transaction_index", Integer),
    Column("from_address", String(255)),
    Column("to_address", String(255)),
    Column("value", BIGINT),
    Column("gas", Integer),
    Column("gas_price", Integer),
    Column("receipt_cumulative_gas_used", Integer),
    Column("receipt_gas_used", Integer),
    Column("receipt_contract_address", String(255)),
    Column("receipt_root", String(255)),
    Column("receipt_status", Integer),
    Column("block_number", Integer),
    Column("block_hash", String(255)),
    Column("max_fee_per_gas", BIGINT),
    Column("max_priority_fee_per_gas", BIGINT),
    Column("transaction_type", Integer),
    Column("receipt_effective_gas_price", BIGINT),
    Column("gas_cost_in_gwei", Float),
    Column("utc_timestamp", DateTime),
    Column("eth_price", Float),
)