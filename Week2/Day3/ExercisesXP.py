import string
import random
from datetime import datetime, timedelta
from datetime import date
from faker import Faker

#Exercise 1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        '''Print the attributes as a string'''
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        '''get an integer from attribute amount'''
        return self.amount

    def __repr__(self):
        return self.__str__()


    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                sum = self.amount + other.amount
                return sum
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            sum_num = self.amount + other
            return sum_num

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount

        elif isinstance(other, int):
            self.amount += other

        else:
            raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        return self






c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
#str
print(f"Printing object as a string {str(c1)}")

#int
print(f"Printing object as a integer {int(c1)}")

#repr
print(f"Representation {repr(c4)}")

#add num
print(f"Object + Number: {c3 + 35}")

#add amount from one currency to another
print(f"Object + Object: {c1 + c2}")
c4 += c2
print(f"Object += Object: {c4}")
c1 += 7
print(f"Number += Object: {c1}")

#Exercise 2
#func.py file and exercise_one.py

#Exercise 3

user_length = int(input("Please enter the length of the string: "))

gen_string = ""
index = 0
while index <= (user_length - 1):
    gen_string += random.choice(string.ascii_letters)
    index += 1
print(gen_string)

#Exercise 4

def current_date():
    today = date.today()
    print(f"Today's date: {today}")

current_date()

#Exercise 5

def time_to_New_Year():
    today = datetime.today()
    new_year = datetime(2025, 1, 1)
    days_left = new_year - today
    print(f"The 1st of January is in {days_left} hours")

time_to_New_Year()

#Exercise 6

def get_minutes_of_live():
    '''displays a message stating how many minutes the user lived in his life'''
    date_of_birth = input("Please write the date of your Birthday in format yyyy m d: ")
    list_of_data = list(date_of_birth.split(" "))
    if len(list_of_data[0]) != 4 or len(list_of_data[1]) != 2 or len(list_of_data[-1]) != 2:
        print("Not correct input")
    else:
        birth_date = datetime(int(list_of_data[0]), int(list_of_data[1]), int(list_of_data[-1]))
        today_data = datetime.today()
        difference = today_data - birth_date
        difference_in_seconds = difference.total_seconds()
        minutes = divmod(difference_in_seconds, 60)[0]
        print(f"{minutes} minutes you lived in this life.")

get_minutes_of_live()

#Exercise 7

fake = Faker()
users = []
def add_user_inf():
    user = {"name": fake.name(), "adress": fake.address(), "language_code": fake.language_code}
    users.append(user)

for _ in range(4):
    add_user_inf()

for user in users:
    print(user)



