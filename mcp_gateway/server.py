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
    convert_currency,
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
    IMPORTANT: amount must always be in INR (Indian Rupees).
    If user provides amount in any other currency, use
    convert_currency_tool first to convert to INR.
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



@mcp.tool()
def convert_currency_tool(
    amount: float,
    from_currency: str,
    to_currency: str,
):
    """
    Convert an amount from one currency to another using live exchange rates.
    Always use this tool first if the user mentions an amount in any currency
    other than INR before calling add_expense_tool.
    Example: if user says '10 dollars', convert USD to INR first, 
    then use the converted_amount to add the expense.
    """
    return convert_currency(
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency,
    )