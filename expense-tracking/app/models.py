from pydantic import BaseModel, field_validator
from datetime import date

class ExpenseModel(BaseModel):
    expense_date: date
    category: str
    amount: float
    description: str

   
    @field_validator('amount')
    def check_amount(cls, value):
        if value <= 0:                        # Check amount is positive and not zero
            raise ValueError("amount can not be zero or negative")
        return value