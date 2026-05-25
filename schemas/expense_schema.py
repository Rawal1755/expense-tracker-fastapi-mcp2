from pydantic import BaseModel
from typing import Optional
from datetime import date


ALLOWED_CATEGORIES = [
    "Food", "Transport", "Housing", "Healthcare",
    "Entertainment", "Shopping", "Education", "Utilities", "Other"
]


# TODO: Implement ExpenseCreate schema with validation
class ExpenseCreate(BaseModel):
    pass


# TODO: Implement ExpenseUpdate schema (all fields optional)
class ExpenseUpdate(BaseModel):
    pass


# TODO: Implement ExpenseResponse schema
class ExpenseResponse(BaseModel):
    pass


# TODO: Implement ExpenseSummary schema
class ExpenseSummary(BaseModel):
    pass
