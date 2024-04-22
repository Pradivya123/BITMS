#class Banking(Neon,Xpattern):
    email='prad34@gmail.com'
    
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
    'email':'prad34@gmail.com'
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
        
        
        
        
        
        
        
        
        
        
        
