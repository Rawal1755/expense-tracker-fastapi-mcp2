from datetime import date
from decimal import Decimal
from typing import Optional

from backend_api.database.connection import SessionLocal
from backend_api.database.models import Expense
from backend_api.schemas.expense_schema import ALLOWED_CATEGORIES


def add_expense(
    user_id: str,
    amount: Decimal,
    category: str,
    description: str | None,
    expense_date: date,
) -> Expense:
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"Invalid category. Allowed categories: {ALLOWED_CATEGORIES}"
        )

    new_expense = Expense(
        user_id=user_id,
        amount=amount,
        category=category,
        description=description,
        expense_date=expense_date,
    )

    with SessionLocal() as db:
        try:
            db.add(new_expense)
            db.commit()
            db.refresh(new_expense)
            return new_expense
        except Exception:
            db.rollback()
            raise


def get_expenses(
    user_id: str,
    categories: Optional[list[str]] = None,
) -> list[Expense]:
    with SessionLocal() as db:
        query = db.query(Expense).filter(
            Expense.user_id == user_id
        )

        if categories:
            query = query.filter(
                Expense.category.in_(categories)
            )

        return query.all()


def get_expense_summary(user_id: str) -> dict:
    with SessionLocal() as db:
        expenses = db.query(Expense).filter(
            Expense.user_id == user_id
        ).all()

    total_spending = Decimal("0.00")
    category_breakdown: dict[str, Decimal] = {}

    for expense in expenses:
        total_spending += expense.amount

        if expense.category not in category_breakdown:
            category_breakdown[expense.category] = Decimal("0.00")

        category_breakdown[expense.category] += expense.amount

    return {
        "user_id": user_id,
        "total_spending": total_spending,
        "total_expenses": len(expenses),
        "category_breakdown": category_breakdown,
    }


def delete_expenses(
    user_id: str,
    expense_ids: list[int],
) -> dict:
    with SessionLocal() as db:
        try:
            expenses = db.query(Expense).filter(
                Expense.user_id == user_id,
                Expense.id.in_(expense_ids),
            ).all()

            deleted_ids = [expense.id for expense in expenses]

            for expense in expenses:
                db.delete(expense)

            db.commit()
        except Exception:
            db.rollback()
            raise

    return {
        "user_id": user_id,
        "deleted_expense_ids": deleted_ids,
        "deleted_count": len(deleted_ids),
    }