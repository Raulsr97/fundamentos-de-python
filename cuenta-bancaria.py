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
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se ha retirado {amount}. saldo actual {self.balance}')
            else:
                print('No se puede retirar porque no tienes suficiente dinero en tu cuenta')
        else: print('No se puede retirar, cuenta inactiva')

    def deactivate_account(self):
        self.is_active = False
        print('La cuenta ha sido desactivada')
        
    def activate_account(self):
        self.activate = True
        print('La cuenta ha sido activada')


account1 = BankAccount('Raul', 4000)
account2 = BankAccount('Crsitiano', 10000)

#   Llamada a los métodos

account1.deposit(200)
account2.deposit(1000)

account1.deactivate_account()
account1.deposit(100)

account2.withdrawal(5000)

account1.activate_account()
account1.withdrawal(10000)
