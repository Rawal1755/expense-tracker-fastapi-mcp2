from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Depends, Security
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(key: str = Security(api_key_header)):
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")

from backend_api.schemas.expense_schema import (
    ExpenseCreate,
    ExpenseDeleteRequest,
    ExpenseDeleteResponse,
    ExpenseResponse,
    ExpenseSummary,
)
from backend_api.services.expense_service import (
    add_expense,
    delete_expenses,
    get_expenses,
    get_expense_summary,
)


app = FastAPI(
    title="Expense Tracker REST API",
    description="REST API backend for the Expense Tracker MCP project",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "expense-tracker-api",
    }


@app.post("/expenses", response_model=ExpenseResponse, status_code=201, dependencies=[Depends(verify_api_key)])
def create_expense(expense: ExpenseCreate):
    try:
        return add_expense(
            user_id=expense.user_id,
            amount=expense.amount,
            category=expense.category,
            description=expense.description,
            expense_date=expense.expense_date,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@app.get(
    "/users/{user_id}/expenses",
    response_model=list[ExpenseResponse],dependencies=[Depends(verify_api_key)]
)
def list_expenses(
    user_id: str,
    categories: Optional[list[str]] = Query(default=None),
):
    return get_expenses(
        user_id=user_id,
        categories=categories,
    )


@app.get(
    "/users/{user_id}/expenses/summary",
    response_model=ExpenseSummary,dependencies=[Depends(verify_api_key)]
)
def expense_summary(user_id: str):
    return get_expense_summary(user_id=user_id)


@app.delete(
    "/users/{user_id}/expenses",
    response_model=ExpenseDeleteResponse,dependencies=[Depends(verify_api_key)]
)
def remove_expenses(
    user_id: str,
    request: ExpenseDeleteRequest,
):
    return delete_expenses(
        user_id=user_id,
        expense_ids=request.expense_ids,
    )
