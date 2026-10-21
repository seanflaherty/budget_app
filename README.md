# Python Budget App (`budget_app`)

> An object-oriented budget tracking application built in Python as part of the [freeCodeCamp](https://www.freecodecamp.org/) Python Certification curriculum.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Project Overview

This project implements a budget management system using Python's Object-Oriented Programming (OOP) principles. It allows users to create different budget categories (e.g., `Food`, `Clothing`, `Entertainment`), perform financial transactions (deposits, withdrawals, transfers), and visualize spending habits across categories via a formatted ASCII spend chart.

---

## ✨ Features

* **Category Management:** Instantly instantiate budget objects with specific category names.
* **Ledger Tracking:** Log deposits and withdrawals complete with optional transaction descriptions and monetary amounts.
* **Inter-Category Transfers:** Easily transfer funds between different budget category instances.
* **Balance Calculation:** Check current category balances dynamically based on total ledger entries.
* **Formatted Printing:** Display neat ASCII financial statements when printing category objects.
* **Spend Chart Generator:** Includes a standalone function `create_spend_chart` that generates a bar chart showing percentages spent per category.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.8** or higher installed:

```bash
python3 --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/seanflaherty/budget_app.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd budget_app
   ```

---

## 💡 Usage Example

Below is a quick demonstration of how to use the `Category` class and `create_spend_chart` function in your scripts:

```python
from budget import Category, create_spend_chart

# Create categories
food = Category("Food")
clothing = Category("Clothing")

# Perform operations
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(50, clothing)

clothing.withdraw(25.50, "t-shirt")

# Print category summary
print(food)

# Generate expenditure percentage chart
print(create_spend_chart([food, clothing]))
```

### Example Printed Output

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

---

## 🧪 Running Tests

To run the test suite with **pytest**, execute:

```bash
pytest
```

## 🛠️ Built With

* **Language:** [Python 3](https://www.python.org/)
* **Testing:** [pytest](https://docs.pytest.org/)
* **Platform:** [freeCodeCamp](https://www.freecodecamp.org/) Python Certification
* **Focus:** Object Oriented Programming with Python and Pytest.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.