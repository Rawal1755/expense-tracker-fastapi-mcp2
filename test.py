from services.expense_service import add_expense
from datetime import date

expense = add_expense(
    amount=250,
    category="Food",
    description="Pizza",
    expense_date=date.today()
)

print("Expense added successfully!")

print(expense.id)
print(expense.amount)
print(expense.category)