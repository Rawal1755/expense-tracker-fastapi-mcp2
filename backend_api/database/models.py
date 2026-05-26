from sqlalchemy import Column, Date, Integer, Numeric, String, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    expense_date = Column(Date, nullable=False)
    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False,
    )