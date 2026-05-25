# Expense Tracker MCP

A Model Context Protocol (MCP) server for tracking personal expenses, built with Python, SQLAlchemy, and FastMCP.

## Project Structure

```
expense-tracker-mcp2/
├── mcp/
│   ├── server.py            # FastMCP server & tool registration
│   └── tools/
│       └── expense_tools.py # Raw tool functions (called by server)
│
├── services/
│   └── expense_service.py   # Business logic layer
│
├── database/
│   ├── connection.py        # SQLAlchemy engine & session
│   └── models.py            # ORM models
│
├── schemas/
│   └── expense_schema.py    # Pydantic request/response schemas
│
├── .env                     # Environment variables
├── requirements.txt
└── README.md
```

## Setup

### 1. Install dependencies

```bash
cd expense-tracker-mcp2
pip install -r requirements.txt
```

### 2. Configure environment

Edit `.env` to set your database URL. Defaults to SQLite:

```
DATABASE_URL=sqlite:///./expenses.db
```

### 3. Run the MCP server

```bash
python mcp/server.py
```

The database tables are created automatically on first run.

## MCP Tools

| Tool | Description |
|------|-------------|
| `tool_add_expense` | Add a new expense |
| `tool_list_expenses` | List expenses with optional filters |
| `tool_update_expense` | Update an expense by ID |
| `tool_delete_expense` | Delete an expense by ID |
| `tool_summarize_expenses` | Summarize totals grouped by category |

## Expense Categories

`Food`, `Transport`, `Housing`, `Healthcare`, `Entertainment`, `Shopping`, `Education`, `Utilities`, `Other`

## Example Usage (via MCP client)

```python
# Add an expense
tool_add_expense(title="Lunch", amount=250.0, category="Food", date="2026-05-24")

# List this month's expenses
tool_list_expenses(start_date="2026-05-01", end_date="2026-05-31")

# Summarize by category
tool_summarize_expenses(start_date="2026-05-01", end_date="2026-05-31")
```

## Connecting to Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "expense-tracker": {
      "command": "python",
      "args": ["/path/to/expense-tracker-mcp2/mcp/server.py"]
    }
  }
}
```
