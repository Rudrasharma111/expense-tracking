import sys,os,pytest
from pydantic import ValidationError

# add the app directorysystem path so we  can import our Models
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from models import ExpenseModel

def test_valid_expense():
    expense = ExpenseModel(expense_date="2026-03-02", category="Food", amount=150.0, description="Pizza")
    assert expense.amount == 150.0

def test_invalid_negative_amount():
    with pytest.raises(ValidationError):
        ExpenseModel(expense_date="2026-03-02", category="Food", amount=-50.0, description="Error")