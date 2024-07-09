class Account:
    def __init__(self, balance, account_num, name):
        self.balance = balance
        self.account_num = account_num
        self.name = name

    def Depo(self, depo):
        if depo <= 0:
            return "Error: Deposit can't be negative"
        if not isinstance(depo, int):
            return "Error: Deposit must be a whole number"
        self.balance = self.balance + depo
        return self.balance

    def With(self, wit):
        if wit <= 0:
            return "Error: Withdraw can't be negative"
        if wit > self.balance:
            return "Error: Withdraw can't be more than balance"
        if not isinstance(wit, int):
            return "Error: Withdraw must be a whole number"
        self.balance = self.balance - wit
        return self.balance

    def Print(self):
        return self.balance
