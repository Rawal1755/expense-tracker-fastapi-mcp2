from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


ALLOWED_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Other",
]


class ExpenseCreate(BaseModel):
    user_id: str = Field(min_length=1)
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    category: str
    description: str | None = Field(default=None, max_length=255)
    expense_date: date


class ExpenseResponse(BaseModel):
    id: int
    user_id: str
    amount: Decimal
    category: str
    description: str | None
    expense_date: date

    model_config = {
        "from_attributes": True
    }


class ExpenseDeleteRequest(BaseModel):
    expense_ids: list[int] = Field(min_length=1)


class ExpenseDeleteResponse(BaseModel):
    user_id: str
    deleted_expense_ids: list[int]
    deleted_count: int


class ExpenseSummary(BaseModel):
    user_id: str
    total_spending: Decimal
    total_expenses: int
    category_breakdown: dict[str, Decimal]