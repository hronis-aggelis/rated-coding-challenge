# main.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routers import transactions
from db import database

app = FastAPI()
app.include_router(transactions.router)


@app.exception_handler(Exception)
async def api_error_handler(
    request: Request,
    exc
) -> JSONResponse:
    """
    Handle any exception that might
    crash the application.
    """

    return JSONResponse(
        content={"message": exc.message, "details": exc.details},
        status_code=400
    )

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
