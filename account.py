class Account():
    def __init__(self, full_name, account_number, balance):
        self.__full_name = full_name
        self.__account_number = account_number
        self.__balance = balance

    @property
    def full_name(self):
        return self.__full_name

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @classmethod
    def from_csv_row(cls, row):
        return cls(row[0], row[1], row[2])

accounts = []
for line in open('accounts.csv'):
    accounts.append(Account.from_csv_row(line.split(',')))

accounts.pop(0)

print(accounts[0].full_name)
print(accounts[0].account_number)
print(accounts[0].balance)
print(accounts[1].full_name)
print(accounts[1].account_number)
print(accounts[1].balance)
print(accounts[2].full_name)
print(accounts[2].account_number)
print(accounts[2].balance)
