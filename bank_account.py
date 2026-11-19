class BankAccount:
    bank_name = "BOG"
    total_accounts = 0

    def __init__(self, owner: str, card_type: str, balance: float = 0.0):
        self.owner = owner
        self.card_type = card_type
        self.balance = balance
        BankAccount.total_accounts += 1

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("ბალანსი არ შეიძლება იყოს უარყოფითი!")
        self.__balance = float(value)

    @balance.deleter
    def balance(self):
        print(f"ბალანსი განულდა ანგარიშზე: {self.owner}")
        self.__balance = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("შესატანი თანხა უნდა იყოს დადებითი!")
        self.balance += amount
        print(f"[{self.bank_name}] +{amount:.2f} ლარი ჩაირიცხა. ახალი ბალანსი: {self.balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("გასატანი თანხა უნდა იყოს დადებითი!")
        if amount > self.balance:
            print(f"[{self.bank_name}] არასაკმარისი თანხა! მიმდინარე ბალანსი: {self.balance:.2f}")
            return False
        self.balance -= amount
        print(f"[{self.bank_name}] -{amount:.2f} ლარი გაიტანეთ. ახალი ბალანსი: {self.balance:.2f}")
        return True

    @classmethod
    def set_bank_name(cls, new_name: str):
        if not new_name.strip():
            raise ValueError("ბანკის სახელი არ შეიძლება იყოს ცარიელი!")
        cls.bank_name = new_name.strip()

    @classmethod
    def get_bank_summary(cls) -> str:
        return f"ბანკი: {cls.bank_name} | სულ ანგარიშები: {cls.total_accounts}"

    @staticmethod
    def calculate_tax(amount: float, tax_rate: float = 0.18) -> float:
        if amount < 0 or tax_rate < 0:
            raise ValueError("თანხა და განაკვეთი არ შეიძლება იყოს უარყოფითი!")
        return round(amount * tax_rate, 2)