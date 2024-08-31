from pydantic import BaseModel, Field


class DepositRequest(BaseModel):
    date: str = Field(..., pattern=r"\d{2}\.\d{2}\.\d{4}", description="Дата заявки")
    periods: int = Field(..., ge=1, le=60, description="Количество месяцев по вкладу")
    amount: int = Field(..., ge=10_000, le=3_000_000, description="Сумма вклада")
    rate: float = Field(..., ge=1, le=8, description="Процент по вкладу")
