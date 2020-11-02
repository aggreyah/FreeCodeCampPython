class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        funds_available = self.check_funds(amount)
        if funds_available:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        available_amount = 0
        for item in self.ledger:
            available_amount += item["amount"]
        return available_amount

    def transfer(self, amount, other_category):
        funds_available = self.check_funds(amount)
        if funds_available:
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        my_string = f"{self.category}".center(30, "*")
        category_total = 0
        for item in self.ledger:
            category_total += item["amount"]
            item_description = item["description"]
            item_amount = item["amount"]
            formatted_amount = "{:.2f}".format(item_amount).rjust(7)
            if len(item_description) > 23:
                my_string += f"\n{item_description[0:23]}{formatted_amount}"
            else:
                format_item_desc = item_description.ljust(23)
                my_string += f"\n{format_item_desc}{formatted_amount}"
        formatted_category_total = "{:.2f}".format(category_total)
        my_string += f"\nTotal: {formatted_category_total}"
        return my_string


def create_spend_chart(categories):
    pass
