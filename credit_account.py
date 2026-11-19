from bank_account import BankAccount


class CreditAccount(BankAccount):
    def __init__(self, owner: str, card_type: str, balance: float = 0.0, credit_limit: float = 2000.0):
        super().__init__(owner, card_type, balance)
        if credit_limit < 0:
            raise ValueError("საკრედიტო ლიმიტი არ შეიძლება იყოს უარყოფითი!")
        self.credit_limit = float(credit_limit)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("გასატანი თანხა უნდა იყოს დადებითი!")

        available_funds = self.balance + self.credit_limit
        if amount > available_funds:
            print(
                f"[Credit] საკრედიტო ლიმიტი ამოიწურა! მაქსიმალური ხელმისაწვდომი თანხა: {available_funds:.2f} ლარი"
            )
            return False

        self._BankAccount__balance -= amount
        print(
            f"[Credit] გატანილია {amount:.2f} ლარი. "
            f"მიმდინარე ბალანსი: {self._BankAccount__balance:.2f} ლარი (ლიმიტი: {self.credit_limit:.2f})"
        )
        return True