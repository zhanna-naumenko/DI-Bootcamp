import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import pandas as pd

url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/critics:certified_fresh~sort:popular'

req = Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
)
response = urlopen(req)
html_content = response.read()
response.close()
soup_tomato = BeautifulSoup(html_content, 'html.parser')


driver = webdriver.Chrome()
# options.add_argument('--headless')  # Run Chrome in headless mode
driver.get(url)
get_source = driver.page_source
print(get_source)
# print(soup_tomato.prettify())
print("----------------------------")
print(soup_tomato.title.get_text())

titles = soup_tomato.find_all('span', class_='p--small')
titles_list = [title.text.strip() for title in titles]
print("----------------------------")
print(titles_list)

release_dates = soup_tomato.find_all('span', class_="smaller")
dates_list = [date.text.strip()[7:] for date in release_dates]
print("----------------------------")
print(dates_list)

scores = soup_tomato.find_all('score-pairs-deprecated', {'audiencesentiment': 'positive', 'criticssentiment': 'positive', 'criticscertified': ''})
# print(scores)
audience_scores = []
for score in scores:
    audience_score = score['audiencescore']
    audience_scores.append(audience_score)
print("----------------------------")
print(audience_scores)

# print(len(titles_list[:len(audience_scores)]))
# print(len(dates_list))
# print(len(audience_scores))

dict_movies = {"Movie Name": titles_list[:len(audience_scores)], "Date of release": release_dates[:len(audience_scores)], "Score": audience_scores}
data_movies = pd.DataFrame(dict_movies)
print(data_movies)