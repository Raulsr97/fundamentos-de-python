class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

        def deposit(self, amount):
            if self.is_active:
                self.balance += amount
                print(f'Se ha depositado {amount}. Saldo actual {self.balance}')
            else: 
                print('No se puede depositar, cuenta inactiva')
            
        def withdrawal(self, amount):
            if self.is_active:
                self.balance -= amount
                print(f'Se ha retirado {amount}. saldo actual {self.balance}')
            else: print('No se puede depositar, cuenta inactiva')