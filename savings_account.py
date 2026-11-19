from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, card_type: str, balance: float = 0.0,
                 interest_rate: float = 0.05, withdrawal_fee: float = 2.0):
        super().__init__(owner, card_type, balance)
        self.interest_rate = interest_rate
        self.withdrawal_fee = withdrawal_fee

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"[Savings] დაერიცხა {interest:.2f} ლარი ({self.interest_rate * 100:.1f}%). ბალანსი: {self.balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("გასატანი თანხა უნდა იყოს დადებითი!")
        total_deduction = amount + self.withdrawal_fee
        if total_deduction > self.balance:
            print(
                f"[Savings] არასაკმარისი თანხა თანხისა და საკომისიოს ({self.withdrawal_fee:.2f} ლარი) დასაფარად! "
                f"ბალანსი: {self.balance:.2f}"
            )
            return False
        self.balance -= total_deduction
        print(
            f"[Savings] გატანილია {amount:.2f} ლარი + საკომისიო {self.withdrawal_fee:.2f} ლარი. "
            f"ახალი ბალანსი: {self.balance:.2f}"
        )
        return True