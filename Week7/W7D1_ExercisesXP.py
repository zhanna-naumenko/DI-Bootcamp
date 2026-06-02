from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import datetime
from urllib.request import Request, urlopen
import random

# Exercise 1
with open('sport.html', 'r') as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

print("Title:", soup.title.get_text())

paragraphs = soup.find_all("p")
print("\nParagraphs")
for p in paragraphs:
    print(p.get_text())

links = soup.find_all("a")
print("\nLinks")
for val in links:
    print(val.get_text())

# Exercise 2

response = requests.get("https://en.wikipedia.org/robots.txt")
test = response.text
print("robots.txt for http://www.wikipedia.org/")
print("===================================================")
print(test)

# Exercise 3

url = 'https://en.wikipedia.org/wiki/Main_Page'
response_1 = urlopen(url)
html_welcome = response_1.read()
# print(html_welcome)
soup_welcome = BeautifulSoup(html_welcome, 'html.parser')
# print(soup_welcome.prettify())
titles = soup_welcome.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])
for title in titles:
    print(title)

# Exercise 4

def get_title(url):
    response = urlopen(url)
    html_response = response.read()
    soup_html = BeautifulSoup(html_response, 'html.parser')
    html_title = soup_html.title.get_text()
    if html_title == None:
        print("There is no Title")
    else:
        print(f"Title: {html_title}")

get_title('https://en.wikipedia.org/wiki/Main_Page')
get_title('https://octopus.developers.institute/courses/')

# Exercise 5
url = "https://www.cisa.gov/news-events/cybersecurity-advisories"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
alerts_div = soup.find('div', class_='view-content')
current_year = datetime.datetime.now().year
alerts_count = 0
if alerts_div:
    alerts = alerts_div.find_all('div', class_='views-row')
    for alert in alerts:
        # Extract the date of the alert
        date_string = alert.find('div', class_='field field-name-field-advisory-date field-type-datetime field-label-hidden').text.strip()
        date = datetime.datetime.strptime(date_string, '%m/%d/%Y').date()
        # Check if the alert is issued in the current year
        if date.year == current_year:
            alerts_count += 1
print(f"Number of security alerts issued by US-CERT in {current_year}: {alerts_count}")


# Exercise 6
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
# Create a request object with a user-agent header
req = Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
)
# Use urlopen to open the URL
response = urlopen(req)
# Read the content from the response
html_content = response.read()
# Close the response
response.close()
# Parse the HTML content using BeautifulSoup
soup_imdb = BeautifulSoup(html_content, 'html.parser')
print("\n", soup_imdb.title.get_text())

# titles of the movie
title_elements = soup_imdb.find_all('h3', class_='ipc-title__text')
# print(title_elements)
# titels in the list
titles = [title.text.strip() for title in title_elements]
# print(titles)
# print 10 random movie titles
random_indices = random.sample(range(1, 251), k=10)
for idx in random_indices:
    print(titles[idx - 1])

print('______')
# find years
year_elements = soup_imdb.find_all('div', class_='feoqjK')
# print(year_elements[0].get_text()[0:4])
# print(year_elements[0].find_all("span")[0].get_text())

# all years in list
years = [year.text.strip() for year in year_elements]
# print 10 random years
random_years = random.sample(years, k=min(10, len(years)))
for year in random_years:
    print(year[0:4])

