from bank_account import BankAccount
from savings_account import SavingsAccount
from credit_account import CreditAccount


if __name__ == "__main__":
    savings = SavingsAccount("გიორგი", "Visa Gold", balance=500, interest_rate=0.05, withdrawal_fee=3.0)
    credit = CreditAccount("ნინო", "Mastercard Credit", balance=200, credit_limit=2000)

    savings.apply_interest()
    savings.withdraw(100)

    credit.withdraw(1500)
    credit.withdraw(1000)

    print("გადასახადი 1000 ლარზე:", BankAccount.calculate_tax(1000))
    print(BankAccount.get_bank_summary())