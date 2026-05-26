import sys
import os
from typing import Optional

sys.path.insert(0, os.path.dirname(__file__))

from fastmcp import FastMCP

from tools.expense_tools import (
    fetch_expenses,
    fetch_expense_summary,
    record_expense,
    remove_expenses,
)


mcp = FastMCP("Expense Tracker REST Gateway")


@mcp.tool()
def add_expense_tool(
    user_id: str,
    amount: float,
    category: str,
    description: str | None,
    expense_date: str,
):
    """
    Add an expense through the Expense Tracker REST API.

    expense_date must use YYYY-MM-DD format.
    Allowed categories: Food, Transport, Shopping, Bills,
    Entertainment, Other.
    """
    return record_expense(
        user_id=user_id,
        amount=amount,
        category=category,
        description=description,
        expense_date=expense_date,
    )


@mcp.tool()
def get_expenses_tool(
    user_id: str,
    categories: Optional[list[str]] = None,
):
    """
    Fetch expenses for a user through the Expense Tracker REST API.

    categories is optional and can contain one or more allowed categories.
    """
    return fetch_expenses(
        user_id=user_id,
        categories=categories,
    )


@mcp.tool()
def expense_summary_tool(user_id: str):
    """
    Get overall expense analytics for a user through the REST API.
    """
    return fetch_expense_summary(user_id=user_id)


@mcp.tool()
def delete_expenses_tool(
    user_id: str,
    expense_ids: list[int],
):
    """
    Delete one or multiple expenses for a user through the REST API.
    """
    return remove_expenses(
        user_id=user_id,
        expense_ids=expense_ids,
    )