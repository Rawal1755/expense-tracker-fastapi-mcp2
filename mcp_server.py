from mcp.server.fastmcp import FastMCP

from expense_mcp.tools.expense_tools import record_expense

mcp = FastMCP("Expense Tracker")


@mcp.tool()
def add_expense_tool(
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
        amount=amount,
        category=category,
        description=description,
        expense_date=expense_date
    )


@mcp.tool()
def get_expenses_tool(categories: list[str] = None):
    """
    Fetch expenses from the database.

    Optional:
    - categories filter
    """

    from expense_mcp.tools.expense_tools import fetch_expenses

    return fetch_expenses(categories=categories)



@mcp.tool()
def expense_summary_tool():
    """
    Get overall expense analytics summary.
    """

    from expense_mcp.tools.expense_tools import (
        fetch_expense_summary
    )

    return fetch_expense_summary()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")


