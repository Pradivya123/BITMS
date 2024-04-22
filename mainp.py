class MagicalPrimeChecker:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def is_magical_prime(n):
        if MagicalPrimeChecker.is_prime(n):
            reverse_n = int(str(n)[::-1])
            return MagicalPrimeChecker.is_prime(reverse_n)
        return False

# Example usage:
number = int(input('Enter the number'))
prime_checker = MagicalPrimeChecker()
if prime_checker.is_magical_prime(number):
    print(number, "is a magical prime number.")
else:
    print(number, "is not a magical prime number.")
class Neon(MagicalPrimeChecker):
    def is_neon(n):
        square = n * n
        digit_sum = sum(int(digit) for digit in str(square))
        return digit_sum == n

# Example usage:
num = int(input("Enter a number to check if it's a neon number: "))
if Neon.is_neon(num):
    print(num, "is a neon number.")
else:
    print(num, "is not a neon number.")
class Xpattern(MagicalPrimeChecker):
    word = input('Enter the name')
    word_length = len(word)

    for i in range(word_length):
        for j in range(word_length):
            if i == j or i == word_length - j - 1:
                print(word[i], end="")
            else:
                print(" ", end="")
        print()
class Reverse(MagicalPrimeChecker):
    def reverse_string(input_string):
        return input_string[::-1]

# Example usage:
    original_string =input('enter the word')
    reversed_string = reverse_string(original_string)
    print(reversed_string)
class Banking(Neon,Xpattern):
    email='pradivya005@gmail.com'
    def withdraw(account, amount):
        if amount>account['balance']:
            print('Insufficient funds')
        else:
            uemail=input('enter the email')
        if email==uemail:
            account['balance']-=amount
            account['transactions'].append(f"withdrawal: ${amount}")
            print(f"withdrawal successful.Remaining balance:${account['balance']}")
        else:
            print('not eligible')
    def deposit(account, amount):
        uemail=input('enter the email')
        if email==uemail:
            account['balance']+=amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful.Remaining balance:${account['balance']}")
        else:
            print('not eligible')
    def check_balance(account):
        return account['balance']
    def get_transaction_history(account):
        return account['transactions']

account={
    'balance':1000,
    'transactions':[],
    'email':'pradivya005@gmail.com'
    }
choices={
    '1':deposit,
    '2':withdraw,
    '3':check_balance,
    '4':get_transaction_history
    }
while True:
    print('1.Deposit')
    print('2.Withdraw')
    print('3.check balance')
    print('4.transaction history')
    print('5.exit')
    choice=input('Enter your choice:')
    if choice=='5':
        print('exiting program.')
        break
    if choice in choices:
        if choice=='1' or choice=='2':
            amount=float(input('Enter amount:'))
            choices[choice](account, amount)
        else:
            print(choices[choice](account))
    else:
        print("Invalid choice. please try again")
        
        
        
        
        
        