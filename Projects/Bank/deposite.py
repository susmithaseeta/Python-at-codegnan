# Deposite function defination
def deposite(account : int, deposite_amount : int):
        users[account]['balance'] += deposite_amount
        return f"{deposite_amount} Deposite successful and Courrent balance is{users[account]['balance']}"