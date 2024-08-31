from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from routers import router as deposit_router


app = FastAPI(title="Deposit Calculation Service")

app.include_router(deposit_router)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 400:
        return JSONResponse(
            status_code=400,
            content={"error": str(exc.detail)}
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )