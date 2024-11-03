class BankAccount:    
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False
    
class BankAccountProxy:
    def __init__(self, bank_account):
        self._bank_account = bank_account

    def deposit(self, amount):
        self._bank_account.deposit(amount)

    def get_balance(self):
        return self._bank_account.get_balance()
    
    def withdraw(self, amount):
        if amount > 10000:
            print("You need manager approval for withdrawals over 10000")
            return False
        else:
            return self._bank_account.withdraw(amount)
        
my_account = BankAccount(15000) 
my_account_proxy = BankAccountProxy(my_account) 

result = my_account_proxy.withdraw(500)

if result:
    print(f"Withdrawal successful. Balance is now {my_account_proxy.get_balance()}")
else:
    print("Withdrawal not possible")
        
result = my_account_proxy.withdraw(12000)

if result:
    print(f"Withdrawal successful. Balance is now {my_account_proxy.get_balance()}")
else:
    print("Withdrawal not possible")
    print(f"{my_account_proxy.get_balance()}")


    