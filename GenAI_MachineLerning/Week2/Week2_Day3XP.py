
from func import add
import string
import random
import datetime
from faker import Faker


# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"Currency ('{self.currency}', {self.amount})"

    def __int__(self):
        return int(self.amount)

    def __add__(self, other: "Currency | int | float"):
        if isinstance(other, (int, float)):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        raise TypeError("the type is not correct")

    def __iadd__(self, other: "Currency | int | float"):
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        raise TypeError("the type is not correct")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)       # '5 dollars'
print(int(c1))  # 5
print(repr(c1)) # 'Currency(dollar, 5)
print(c1 + 5)   # 10
print(c1 + c2)  # 15
print(c1)       # 5 dollars
c1 += 5
print(c1)       # 10 dollars
c1 += c2
print(c1)       # 20 dollars
# print(c1 + c3)  # TypeError: Cannot add between Currency type <dollar> and <shekel>

# Exercise 2: Import

add(5, 10)

# Exercise 3: String module

string_upper_lower = string.ascii_letters
print(string_upper_lower)
new_string = ""
for _ in range(5):
    new_string += random.choice(string_upper_lower)

print(new_string)

# Exercise 4: Current Date

def show_todays_date():
    print(datetime.date.today())

show_todays_date()

# Exercise 5: Amount of time left until January 1st
def days_left_till_january():
    today = datetime.date.today()
    next_year = today.year + 1
    next_january = datetime.date(next_year, 1, 1)
    return f"Till next January first remains: {next_january - today}"

print(days_left_till_january())

# Exercise 6: Birthday and minutes
def minutes_of_your_life(birth_date):
    birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d %H:%M:%S")
    birth_date = datetime.datetime(birth_date.year, birth_date.month, birth_date.day, birth_date.hour, birth_date.minute, birth_date.second)
    today = datetime.datetime.today()
    difference = today - birth_date
    total_minutes = int(difference.total_seconds() / 60)
    return f"You lived {total_minutes:,} minutes"

user_birth_date = input("Please enter your birthday date in format (Example: 2026-02-24 17:09:00): ")
print(minutes_of_your_life(user_birth_date))

# Exercise 7: Faker Module
fake = Faker()

users_list = []

def adding_user(num_of_users):
    for user in range(num_of_users):
        user_info = {}
        user_info["name"] = fake.name()
        user_info["address"] = fake.address()
        user_info["language_code"] = fake.language_code()
        users_list.append(user_info)

adding_user(num_of_users=5)
print(users_list)


