from datetime import date

from database.connection import SessionLocal
from database.models import Expense


ALLOWED_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Other"
]


def add_expense(
    amount: float,
    category: str,
    description: str,
    expense_date: date
):
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"Invalid category. Allowed categories: {ALLOWED_CATEGORIES}"
        )

    db = SessionLocal()

    new_expense = Expense(
        amount=amount,
        category=category,
        description=description,
        expense_date=expense_date
    )

    db.add(new_expense)

    db.commit()

    db.refresh(new_expense)

    db.close()

    return new_expense



def get_expenses(categories=None):
    db = SessionLocal()

    query = db.query(Expense)

    if categories:
        query = query.filter(
            Expense.category.in_(categories)
        )

    expenses = query.all()

    db.close()

    return expenses



def get_expense_summary():
    db = SessionLocal()

    expenses = db.query(Expense).all()

    total_spending = 0

    category_breakdown = {}

    for expense in expenses:
        total_spending += expense.amount

        if expense.category not in category_breakdown:
            category_breakdown[expense.category] = 0

        category_breakdown[expense.category] += expense.amount

    total_expenses = len(expenses)

    db.close()

    return {
        "total_spending": total_spending,
        "total_expenses": total_expenses,
        "category_breakdown": category_breakdown
    }