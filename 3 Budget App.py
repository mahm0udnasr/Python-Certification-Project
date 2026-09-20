class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance()}"
        return title + items + total
    

def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total_spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent.append(total_spent)
    
    total_all = sum(spent)
    
    percentages = []
    for amount in spent:
        if total_all == 0:
            percentages.append(0)
        else:
            percentages.append(int((amount / total_all) * 100 // 10) * 10)
        
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"
    
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += f"{name[i]}  "
            else:
                res += "   "
        if i != max_len - 1:
            res += "\n"

    return res
