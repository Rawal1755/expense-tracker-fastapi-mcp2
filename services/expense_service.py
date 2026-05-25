from datetime import date
from typing import Optional

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
    user_id: str,
    amount: float,
    category: str,
    description: str,
    expense_date: date
):
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"Invalid category. Allowed categories: {ALLOWED_CATEGORIES}"
        )

    new_expense = Expense(
        user_id=user_id,
        amount=amount,
        category=category,
        description=description,
        expense_date=expense_date
    )

    with SessionLocal() as db:
        try:
            db.add(new_expense)
            db.commit()
            db.refresh(new_expense)
        except Exception:
            db.rollback()
            raise

    return new_expense



def get_expenses(
    user_id: str,
    categories: Optional[list[str]] = None
):
    with SessionLocal() as db:
        query = db.query(Expense)

        query = query.filter(
            Expense.user_id == user_id
        )

        if categories:
            query = query.filter(
                Expense.category.in_(categories)
            )

        expenses = query.all()

    return expenses



def get_expense_summary(user_id):
    with SessionLocal() as db:
        expenses = db.query(Expense).filter(
            Expense.user_id == user_id
        ).all()

        total_spending = 0

        category_breakdown = {}

        for expense in expenses:
            total_spending += expense.amount

            if expense.category not in category_breakdown:
                category_breakdown[expense.category] = 0

            category_breakdown[expense.category] += expense.amount

        total_expenses = len(expenses)

    return {
        "user_id": user_id,
        "total_spending": total_spending,
        "total_expenses": total_expenses,
        "category_breakdown": category_breakdown
    }



def delete_expenses(
    user_id,
    expense_ids
):
    with SessionLocal() as db:
        try:
            expenses = db.query(Expense).filter(
                Expense.user_id == user_id,
                Expense.id.in_(expense_ids)
            ).all()

            deleted_count = len(expenses)

            for expense in expenses:
                db.delete(expense)

            db.commit()
        except Exception:
            db.rollback()
            raise

    return {
        "user_id": user_id,
        "deleted_expense_ids": expense_ids,
        "deleted_count": deleted_count
    }
