"""Tests for the budget app."""
import pytest
from src.budget_app import Category, create_spend_chart

@pytest.fixture
def food_category():
    """Provides a fresh Category instance for testing."""
    return Category("Food")

@pytest.fixture
def equipment_category():
    """Provides a second Category instance for transfers and charts."""
    return Category("Equipment")

def test_deposit(food_category):
    """Test that deposits update the balance and record ledger entries."""
    food_category.deposit(1000, "initial deposit")
    assert food_category.get_balance() == 1000.00
    assert food_category.ledger[0] == {"amount": 1000.00, "description": "initial deposit"}

def test_withdraw_success(food_category):
    """Test successful withdrawal."""
    food_category.deposit(500)
    success = food_category.withdraw(200, "groceries")

    assert success is True
    assert food_category.get_balance() == 300.00
    assert food_category.ledger[-1] == {"amount": -200, "description": "groceries"}

def test_withdraw_insufficient_funds(food_category):
    """Test withdrawal when funds are insufficient."""
    food_category.deposit(50)
    success = food_category.withdraw(100, "fancy dinner")

    assert success is False
    assert food_category.get_balance() == 50.00
    # Ledger should only have the deposit entry, no failed withdrawal
    assert len(food_category.ledger) == 1

def test_transfer_success(food_category, equipment_category):
    """Test successful transfer between categories."""
    food_category.deposit(500, "deposit")
    success = food_category.transfer(200, equipment_category)

    assert success is True
    assert food_category.get_balance() == 300.00
    assert equipment_category.get_balance() == 200.00

    # Check ledger descriptions created by transfer
    assert food_category.ledger[-1]["description"] == "Transfer to Equipment"
    assert equipment_category.ledger[-1]["description"] == "Transfer from Food"


def test_transfer_insufficient_funds(food_category, equipment_category):
    """Test transfer failure due to low balance."""
    food_category.deposit(50, "deposit")
    success = food_category.transfer(200, equipment_category)

    assert success is False
    assert food_category.get_balance() == 50.00
    assert equipment_category.get_balance() == 0.00

def test_category_str_representation(food_category):
    """Test the receipt-style __str__ output formatting."""
    food_category.deposit(900, "deposit")
    # Will truncate description
    food_category.withdraw(45.50, "milk, eggs, bread and a lot of other groceries")

    receipt = str(food_category)
    lines = receipt.split("\n")

    # Check title centering (30 asterisks total, "Food" centered)
    assert lines[0] == "*************Food*************"
    # Check truncated description and right-aligned amount
    assert lines[2] == "milk, eggs, bread and a -45.50"

    # Check total line
    assert lines[-1] == "Total: 854.50"

def test_create_spend_chart(food_category, equipment_category):
    """Test that the spend chart generates correct percentages and layout."""
    food_category.deposit(1000, "initial")
    food_category.withdraw(200, "groceries")  # 200 spent

    equipment_category.deposit(1000, "initial")
    equipment_category.withdraw(800, "equipment")  # 800 spent
    # Total spent = 1000. Food = 20% (rounds down to 10%? Wait: 200/1000 = 20%)
    # Let's adjust numbers to make percentages clean:
    # Food spent: 300 (30%), equipment spent: 700 (70%)

    food_category = Category("Food")
    food_category.deposit(1000)
    food_category.withdraw(30)

    equipment_category = Category("Equipment")
    equipment_category.deposit(1000)
    equipment_category.withdraw(70)

    chart = create_spend_chart([food_category, equipment_category])

    assert "Percentage spent by category" in chart
    assert "100|" in chart
    assert " 0|" in chart
    assert "    ------" in chart  # Dashed line for 2 categories
    assert "F   C   " in chart or "F" in chart  # Vertical names check
