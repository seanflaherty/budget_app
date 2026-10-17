"""Budget tracking app."""
from __future__ import annotations
class Category:
    """Class for budget item categories."""
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger: list[dict] = []

    def deposit(self, amount: float, description: str="") -> None:
        """Adds a entry (assumed to be positive) to the ledger."""
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: float, description: str="") -> bool:
        """Adds a negative (withdrawal) entry to the ledger."""
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self) -> float:
        """Returns the balance of the ledger."""
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount: float, destination: Category) -> bool:
        """Moves an amount to a different category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> float:
        """A helper method that returns True or False depending on the amount and balance."""
        return amount <= self.get_balance()

    def __str__(self) -> str:
        """Returns a formatted list of transactions."""
        # 30 asterisks total, with the category name centered
        title = f"{self.name:*^30}\n"
        items = ""

        for item in self.ledger:
            # Description left-aligned (max 23 chars),
            # amount right-aligned with 2 decimal places (max 7 chars)
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories: list) -> str:
    """Generates a percentage-based bar chart."""
    # Calculate withdrawals only.
    withdrawals = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        withdrawals.append(spent)

    total_spent = sum(withdrawals)

    # Percentages rounded DOWN to nearest 10.
    percentages = []
    for spent in withdrawals:
        if total_spent > 0:
            percentages.append(int((spent / total_spent) * 100) // 10 * 10)
        else:
            percentages.append(0)

    # Build the chart.
    chart = "Percentage spent by category\n"

    # Y-axis + bars
    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "|"
        for pct in percentages:
            if pct >= level:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"          # one space after the last bar group + newline

    # Horizontal line (4 spaces + 3 dashes per category + 1 extra dash)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        # 5 leading spaces
        chart += "     "
        for name in names:
            if i < len(name):
                # letter + two spaces
                chart += name[i] + "  "
            else:
                # three spaces if name is shorter
                chart += "   "
        # No extra characters; the two spaces after the last category
        # are already included by the loop above.
        if i < max_len - 1:
            chart += "\n"
        # The very last name line has no trailing newline

    return chart
