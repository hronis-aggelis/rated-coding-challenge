# Rated Coding Challenge

## Installation 
pip install -r requirements.txt

### Prerequisites

- msql running
- host: localhost, username: root, password: password, database name: rated

## Script
- Activate virtual-env
- run python script.py
- this will populate mysql db rated and create table transactions

## FastApi
- run uvicorn main:app --host 0.0.0.0 --port 80
- test request in postman: http://127.0.0.1:80/transactions/0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac8