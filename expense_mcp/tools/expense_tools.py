from datetime import date
from typing import Optional

from services.expense_service import (
    add_expense,
    get_expenses,
    get_expense_summary,
    delete_expenses
)


def record_expense(
    user_id: str,
    amount: float,
    category: str,
    description: str,
    expense_date: str
):
    parsed_date = date.fromisoformat(expense_date)

    expense = add_expense(
    user_id=user_id,
    amount=amount,
    category=category,
    description=description,
    expense_date=parsed_date
    )

    return {
        "message": "Expense added successfully",
        "expense_id": expense.id,
        "user_id": expense.user_id,
        "amount": expense.amount,
        "category": expense.category,
        "description": expense.description,
        "expense_date": str(expense.expense_date)
    }


def fetch_expenses(
    user_id: str,
    categories: Optional[list[str]] = None
):
    expenses = get_expenses(
        user_id=user_id,
        categories=categories
    )

    formatted_expenses = []

    for expense in expenses:
        formatted_expenses.append({
            "id": expense.id,
            "user_id": expense.user_id,
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "expense_date": str(expense.expense_date)
        })

    return formatted_expenses


def fetch_expense_summary(user_id):
    summary = get_expense_summary(
        user_id=user_id
    )

    return summary



def remove_expenses(
    user_id,
    expense_ids
):
    result = delete_expenses(
        user_id=user_id,
        expense_ids=expense_ids
    )

    return result
