import datetime

birthday_cake = """       ___i___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~"""

today = datetime.date.today()
print(today)

user_date_of_birth = input("Please enter the date of birth in the format DD/MM/YYYY: ")
birthday = datetime.datetime.strptime(user_date_of_birth, "%d/%m/%Y").date()
years = today.year - birthday.year

if (today.month, today.day) < (birthday.month, birthday.day):
    years -= 1
list_years = list(str(years))
num_of_candles = "i" * int(list_years[-1])
birthday_cake = birthday_cake.replace("___i___", f"___{num_of_candles}___")
print(birthday_cake)
