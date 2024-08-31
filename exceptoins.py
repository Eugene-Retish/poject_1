# from main import app
# from fastapi import Request, HTTPException
# from fastapi.responses import JSONResponse


# @app.exception_handler(HTTPException)
# async def http_exception_handler(request: Request, exc: HTTPException):
#     if exc.status_code == 400:
#         return JSONResponse(
#             status_code=400,
#             content={"error": str(exc.detail)}
#         )
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"error": exc.detail},
#     )