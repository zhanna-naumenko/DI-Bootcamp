from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from datetime import datetime, timedelta
import pandas as pd
import re

# url = 'https://weather.com/weather/tenday/l/Bat+Yam+Tel+Aviv+District+Israel?canonicalCityId=7a76e4913514e047dc4208b52fb5d5b5472cce97a8db848267f404c33bd6883c'
url = 'https://www.yr.no/en/forecast/daily-table/2-295548/Israel/Tel%20Aviv/Bat%20Yam'
req = Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
)
response = urlopen(req)
html_content = response.read()
response.close()
soup_weather = BeautifulSoup(html_content, 'html.parser')


driver = webdriver.Chrome()
# options.add_argument('--headless')  # Run Chrome in headless mode
driver.get(url)
get_source = driver.page_source
print(get_source)
# print(soup_bbc.prettify())
print("----------------------------")
print(soup_weather.title.get_text())

dates_weather = soup_weather.find_all('div', class_='daily-weather-list-item__date-and-warnings')
dates_weather_list = [dates.text.strip() for dates in dates_weather]
# print(dates_weather_list)

list_week_day = [dates.text.strip().split(" ")[0] for dates in dates_weather]
# print(list_week_day)
list_date = [dates.text.strip().split(" ")[1] for dates in dates_weather]
# print(list_date)
list_month = [dates.text.strip().split(" ")[-1] for dates in dates_weather]
# print(list_month)

tempr_weather = soup_weather.find_all('span', class_='text-3 text--color-primary text-tabular-nums text-weight-normal')
list_tempr_high = [temp.text.strip()[:3] for temp in tempr_weather]
list_tempr_low = [temp.text.strip()[-3:] for temp in tempr_weather]
# print(f'High: {list_tempr_high}')
# print(f'Low: {list_tempr_low}')

wind_speed = soup_weather.find_all('span', class_='wind daily-weather-list-item__wind-value')
list_wind = [wind.text.strip() for wind in wind_speed]
# print(list_wind)

data_weather = {'Day of the Week': list_week_day,
                'Date': list_date, 'Month': list_month,
                'High Temperature': list_tempr_high,
                'Low Temperature': list_tempr_low,
                'Wind Speed': list_wind}

weather_data = pd.DataFrame(data_weather)
print(weather_data)



