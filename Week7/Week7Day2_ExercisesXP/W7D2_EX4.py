from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import pandas as pd
import re

url = 'https://www.bbc.com/culture/style'

req = Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
)
response = urlopen(req)
html_content = response.read()
response.close()
soup_bbc = BeautifulSoup(html_content, 'html.parser')


driver = webdriver.Chrome()
# options.add_argument('--headless')  # Run Chrome in headless mode
driver.get(url)
get_source = driver.page_source
print(get_source)
# print(soup_bbc.prettify())
print("----------------------------")
print(soup_bbc.title.get_text())

# get titles

titles = soup_bbc.find_all("h2", class_="sc-4fedabc7-3 zTZri")
titles_list = [title.text.strip() for title in titles]
print(titles_list)


dates_starting_with_2024 = []

links_with_dates = soup_bbc.find_all('a', href=re.compile(r'/2024\d{4}'))

for link in links_with_dates:
    href = link['href']
    match = re.search(r'2024\d{4}', href)
    if match:
        dates_starting_with_2024.append(match.group())

print(dates_starting_with_2024)

dict_bbs = {"Title": titles_list, "Date of the Title": dates_starting_with_2024[:len(titles_list)]}

data_bbc = pd.DataFrame(dict_bbs)
# print(data_bbc)

data_bbc["Date of the Title"] = pd.to_datetime(data_bbc["Date of the Title"])

data_bbc['Publication Month'] = data_bbc['Date of the Title'].dt.month_name()
print(data_bbc)
