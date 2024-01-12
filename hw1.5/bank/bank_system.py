import json


def load_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

data = load_json('data.json')


def login(username, password):
    global account
    data = load_json('data.json')
    for info in data:
        if info['username'] == username and info['password'] == password:
            print('Succesfuly logged in')
            account = Account(username, info['money'], info['current_money'])

def register(username, password, money):
    data = {}

    data['username'] = username
    data['password'] = password
    data['money'] = money
    data['current_money'] = 0

    current_data = load_json('data.json')
    current_data.append(data)

    with open('data.json', 'w') as f:
        json.dump(current_data, f, indent=2)
    
    print("Account succesfuly created. Please type 'login' in the terminal.")


class Account():
    def __init__(self, username, account_money, current_money):
        self.username = username
        self.account_money = account_money
        self.current_money = current_money

    def update_account(self):
        current_data = {}
        current_data['username'] = self.username
        current_data['money'] = self.account_money
        current_data['current_money'] = self.current_money

        return current_data
    
    def withdraw(self, money):
        if money > self.account_money:
            return "Sorry, you do not have that amount."
        self.account_money -= money
        self.current_money += money


        with open('data.json', 'w') as f:
            json.dump(self.update_account, f, indent=2)

        return f'Current money - {self.current_money}; Account money - {self.account_money}'
    
        
    def deposit(self, money):
        if money > self.current_money:
            return "Sorry, you do not have that amount."
        self.account_money += money
        self.current_money -= money


        with open('data.json', 'w') as f:
            json.dump(self.update_account, f, indent=2)

        return f'Current money - {self.current_money}; Account money - {self.account_money}'

    def account_info(self):
        return f' Username - {self.username};\n Current money - {self.current_money};\n Account money - {self.account_money}'


while True:

    terminal = input('> ')

    if terminal == 'withdraw':
        print('Enter money to withdraw')
        terminal = int(input('> '))
        print(account.withdraw(terminal))

    if terminal == 'deposit':
        print('Enter money to deposit')
        terminal = int(input('> '))
        print(account.deposit(terminal))


    if terminal == 'login':
        print('Enter your username: ')
        username = input('> ')
        print('Enter your password: ')
        password = input('> ')
        login(username, password)


    if terminal == 'register':
        print('Enter username: ')
        username = input('> ')
        print('Enter password: ')
        password = input('> ')
        print('Enter desired money')
        money = int(input('> '))
        register(username, password, money)
    
    if terminal == 'info':
        print(account.account_info())

    
    if terminal in ['break', 'stop', 'exit']:
        break