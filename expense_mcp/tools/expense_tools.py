from datetime import date

from services.expense_service import (
    add_expense,
    get_expenses,
    get_expense_summary
)


def record_expense(
    amount: float,
    category: str,
    description: str,
    expense_date: str
):
    parsed_date = date.fromisoformat(expense_date)

    expense = add_expense(
        amount=amount,
        category=category,
        description=description,
        expense_date=parsed_date
    )

    return {
        "message": "Expense added successfully",
        "expense_id": expense.id,
        "amount": expense.amount,
        "category": expense.category,
        "description": expense.description,
        "expense_date": str(expense.expense_date)
    }


def fetch_expenses(categories=None):
    expenses = get_expenses(categories=categories)

    formatted_expenses = []

    for expense in expenses:
        formatted_expenses.append({
            "id": expense.id,
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "expense_date": str(expense.expense_date)
        })

    return formatted_expenses


def fetch_expense_summary():
    summary = get_expense_summary()

    return summary