import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from mcp.server.fastmcp import FastMCP

from expense_mcp.tools.expense_tools import record_expense

mcp = FastMCP("Expense Tracker")


@mcp.tool()
def add_expense_tool(
    user_id: str,
    amount: float,
    category: str,
    description: str,
    expense_date: str
):
    """
    Add an expense to the database.

    expense_date format:
    YYYY-MM-DD
    """

    return record_expense(
    user_id=user_id,
    amount=amount,
    category=category,
    description=description,
    expense_date=expense_date
    )


@mcp.tool()
def get_expenses_tool(
    user_id: str,
    categories: list[str] = []
):
    """
    Fetch expenses from the database.

    Optional:
    - categories filter
    """

    from expense_mcp.tools.expense_tools import fetch_expenses

    return fetch_expenses(
    user_id=user_id,
    categories=categories
    )



@mcp.tool()
def expense_summary_tool(user_id: str):
    """
    Get overall expense analytics summary
    for a specific user.
    """

    from expense_mcp.tools.expense_tools import (
        fetch_expense_summary
    )

    return fetch_expense_summary(
        user_id=user_id
    )




@mcp.tool()
def delete_expenses_tool(
    user_id: str,
    expense_ids: list[int]
):
    """
    Delete one or multiple expenses
    belonging to a specific user.
    """

    from expense_mcp.tools.expense_tools import (
        remove_expenses
    )

    return remove_expenses(
        user_id=user_id,
        expense_ids=expense_ids
    )

app = mcp

