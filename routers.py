from fastapi import APIRouter, HTTPException
from models import DepositRequest
from services import calculate_deposit


router = APIRouter()


@router.post("/calculate")
def calculate_deposit_endpoint(deposit: DepositRequest):
    try:
        result = calculate_deposit(deposit.date, deposit.periods, deposit.amount, float(deposit.rate))
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

