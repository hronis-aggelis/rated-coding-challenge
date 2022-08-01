import os
import re
import datetime

from unittest.mock import patch
from fastapi.testclient import TestClient


from main import app


client = TestClient(app)

def get_transaction(hash):
    return client.get(f"/transactions/{hash}")

@patch("db.queries.get_trans_from_hash", return_value={}) 
def test_get_transaction_invalid_hash(mock_get_trans_from_hash):
    response = get_transaction(hash='dummy_hash')
    assert response.json() == {"message":"invalid hash"}
    assert response.status_code == 200
    

@patch("db.queries.get_trans_from_hash", return_value={"hash": '0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac8',
                                                       "from_address": '0x0057be07beef5d9b4beb9e2d147906e83d1915c8',
                                                       "to_address": '0x8f26d7bab7a73309141a291525c965ecdea7bf42', "block_number": 15077724,
                                                       "utc_timestamp": datetime.datetime(2022, 7, 27, 16, 40, 21),
                                                       "gas_cost_in_gwei": 5977549.843268778, "eth_price": 1514.347700044128}) 
def test_get_transaction_success(mock_get_trans_from_hash):
    response = get_transaction(hash='0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac81')
    assert response.json() == {
                                "hash": "0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac8",
                                "fromAddress": "0x0057be07beef5d9b4beb9e2d147906e83d1915c8",
                                "toAddress": "0x8f26d7bab7a73309141a291525c965ecdea7bf42",
                                "blockNumber": "15077724",
                                "executedAt": "2022-07-27 16:40:21",
                                "gasUsed": 5977549.843268778,
                                "gasCostInDollars": 1514.347700044128
                            }
    assert response.status_code == 200
    
    
@patch("db.queries.get_trans_from_hash", return_value={"hash2": '0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac8',
                                                       "from_address": '0x0057be07beef5d9b4beb9e2d147906e83d1915c8',
                                                       "to_address": '0x8f26d7bab7a73309141a291525c965ecdea7bf42', "block_number": 15077724,
                                                       "utc_timestamp": datetime.datetime(2022, 7, 27, 16, 40, 21),
                                                       "gas_cost_in_gwei": 5977549.843268778, "eth_price": 1514.347700044128}) 
def test_get_transaction_validation_error(mock_get_trans_from_hash):
    response = get_transaction(hash='0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac81')
    assert response.json() == {'body': '[{"loc": ["hash"], "msg": "field required", "type": "value_error.missing"}]'}
    assert response.status_code == 400