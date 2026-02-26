from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import requests
import csv

url = 'https://www.bbc.com/weather/293397'

response = requests.get(url)
driver = webdriver.Chrome()
# options.add_argument('--headless')  # Run Chrome in headless mode
driver.get(url)
# get_source = driver.page_source
# print(get_source)


# click to the day button
parent_div = driver.find_element(By.XPATH, '//*[@id="daylink-1"]')
parent_div.click()

# make a soup
page_source = driver.page_source
soup_weather = BeautifulSoup(page_source, 'html.parser')

# get the information about the day
day_of_week = soup_weather.find_all('span', class_='wr-date__long')
list_day_of_week = [day.text.strip().split('\xa0') for day in day_of_week]

list_days = []
list_dates = []
list_months = []
for index in list_day_of_week:
    list_days.append(index[0])
    list_dates.append(index[1])
    list_months.append(index[2])

print("_______________________")
# printing the list of the days of the week
print(f'Days of the Week: {list_days}')
# printing the list of the dates
print(f'Dates: {list_dates}')
# printing the list of the months
print(f'Months: {list_months}')

# get the information about the temperatures
inf_temp = soup_weather.find_all('span', class_='wr-value--temperature--c')
# get the list of all temperature of the day
list_all_temp = [temp.text.strip() for temp in inf_temp]
# get the temperature of needed days
list_of_temp = list_all_temp[1:(len(list_months) * 2) +1]

# get the list of high temperature of the day
high_temperature = list_of_temp[1::2]
# get the list of low temperature of the day
low_temperature = list_of_temp[::2]

print("_______________________")
print(f"High Temperature: {high_temperature}")
print(f"Low Temperature: {low_temperature}")


# get condition of the day
conditions = soup_weather.find_all('div', class_='wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque')
list_cond = [cond.text.strip() for cond in conditions]
print("_______________________")
print(list_cond)

# Hourly information
hour_button = driver.find_element(By.XPATH, '//*[@id="wr-forecast"]/div[4]/div/div[1]/div[2]/div/div/div/div[2]/ol/li[1]/button')
hour_button.click()

page_source = driver.page_source
soup_weather = BeautifulSoup(page_source, 'html.parser')

# get list of the hours
time_of_day = soup_weather.find_all('span', class_='wr-time-slot-primary__time')
list_time = [time.text.strip() for time in time_of_day]
print("_______________________")
print(list_time)


index = 1

# get dict of the humidity of all 13 days hourly
humidity_dict = {}
# get dict of the pressure of all 13 days hourly
pressure_dict = {}
# get dict of the visibility of all 13 days hourly
visibility_dict = {}

# a for loop to go through all od the days on the website page to take the data
for index in range(1, 14):
    parent_div = driver.find_element(By.XPATH, f'//*[@id="daylink-{index}"]')
    parent_div.click()
    hour_button = driver.find_element(By.XPATH, '//*[@id="wr-forecast"]/div[4]/div/div[1]/div[2]/div/div/div/div[2]/ol/li[1]/button')
    hour_button.click()

    page_source = driver.page_source
    soup_weather = BeautifulSoup(page_source, 'html.parser')

    information_hourly = soup_weather.find_all('dd', class_='wr-time-slot-secondary__value gel-long-primer-bold')
    list_information = [inf.text.strip() for inf in information_hourly]

    humidity_dict[f'list_humidity_day{index}'] = []
    pressure_dict[f'list_pressure_day{index}'] = []
    visibility_dict[f'list_visibility_day{index}'] = []

    for item in list_information:
        if item.endswith('%'):
            humidity_dict[f'list_humidity_day{index}'].append(item)
        elif item.endswith('mb'):
            pressure_dict[f'list_pressure_day{index}'].append(item)
        else:
            visibility_dict[f'list_visibility_day{index}'].append(item)
    index += 1

print("_______________________")
print(f"Humidity dict: {humidity_dict}")
print(f"Pressure dict: {pressure_dict}")
print(f"Visibility dict: {visibility_dict}")


# a dictionary of the all information by days
dict_days = {'Day of the Week': list_days, 'Date': list_dates,
             'Month': list_months, 'High Temperature': high_temperature,
             'Low Temperature': low_temperature, 'Conditions': list_cond[1:]}
days_data = pd.DataFrame(dict_days)
print("_______________________")
print(days_data)

hourly_data = pd.DataFrame(index=list_time)

list_of_dates = [f"{date} {month}" for date, month in zip(list_dates, list_months)]
print("_______________________")
print(list_of_dates)

# Add columns from dictionaries
for key, value in humidity_dict.items():
    hourly_data[key] = value

for key, value in pressure_dict.items():
    hourly_data[key] = value

for key, value in visibility_dict.items():
    hourly_data[key] = value

# create a dictionary to rename the columns
column_names_mapping = {}

for date in list_of_dates:
    day = date.split()[0]
    month = date.split()[1]
    day_index = list_of_dates.index(date) + 1
    key_humidity = f'list_humidity_day{day_index}'
    key_pressure = f'list_pressure_day{day_index}'
    key_visibility = f'list_visibility_day{day_index}'
    column_names_mapping[key_humidity] = f'Humidity {date}'
    column_names_mapping[key_pressure] = f'Pressure {date}'
    column_names_mapping[key_visibility] = f'Visibility {date}'

hourly_data.rename(columns=column_names_mapping, inplace=True)
print("_______________________")
print(hourly_data)


# save days_data to CSV
days_data.to_csv('days_data.csv', index=False)
# save hourly_data to CSV
hourly_data.to_csv('hourly_data.csv')