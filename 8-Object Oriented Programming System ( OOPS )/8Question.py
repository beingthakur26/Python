# Question 1.
# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.


'''
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Debited Amount:", amount)

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Credited Amount:", amount)

    # print balance method
    def print_balance(self):
        print("Account Balance:", self.balance)


# Example usage
acc1 = Account(1000, 1234567890)
print("Account Number:", acc1.account_no)  # Account number is 1234567890
acc1.print_balance()  # Account balance is 1000
acc1.debit(100)  # Debit amount is 100
acc1.print_balance()  # Account balance after debit is 900
acc1.credit(200)  # Credit amount is 200
acc1.print_balance()  # Account balance after credit is 1100
'''

                    # OR

class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Debited Amount: {amount}") # Debited Amount: 1000
        print(f"New Balance after debit : {self.balance}") # New Balance after debit : 99000

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Credited Amount: {amount}") # Credited Amount: 2000
        print(f"New Balance after credit: {self.balance}") # New Balance after credit: 101000

    def get_balance(self):
        return self.balance 

acc1 = Account(100000, 1234567890)
print("Account Number:", acc1.account_no)  # Account number : 1234567890
print("Initial Balance:", acc1.balance)  # Initial balance : 100000
acc1.debit(1000)  
acc1.credit(2000)  

print("Final Balance:", acc1.get_balance())  # Final balance : 101000
