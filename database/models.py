from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, TIMESTAMP
from sqlalchemy.sql import func

Base = declarative_base()


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float, nullable=False)

    category = Column(String(100), nullable=False)

    description = Column(String(255))

    expense_date = Column(Date, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )