from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import requests

url = 'https://www.inmotionhosting.com/'

response = requests.get(url)
driver = webdriver.Chrome()
# options.add_argument('--headless')  # Run Chrome in headless mode
driver.get(url)
# get_source = driver.page_source
# print(get_source)

wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
pop_up = driver.find_element(By.ID, 'onetrust-close-btn-container')
pop_up.click()

print("Information for the 1st Plan")
# Find the element by link text
parent_div = driver.find_element(By.XPATH, '//*[@id="home-rostrum-3"]/div/div/div[1]')
parent_div.click()
# make a soup
page_source = driver.page_source
soup_plans = BeautifulSoup(page_source, 'html.parser')
# get titles from first plan
titles_plan1 = soup_plans.find_all('h3', class_='h3 imh-rostrum-card-title')
titles_list_plan1 = [title.text.strip() for title in titles_plan1]
print(titles_list_plan1)
# get costs from first plan
cost_plan1 = soup_plans.find_all('div', class_='imh-rostrum-starting-at-price-discounted')
cost_list_plan1 = [val.text.strip()[1:5] for val in cost_plan1]
print(cost_list_plan1)
# get features from first plan
features_plan1 = soup_plans.find_all("td")
features_list_plan1 = [feature.text.strip() for feature in features_plan1]
print(features_list_plan1)
# back to the main page
driver.back()

print("_____________________________")
print("Information for the 2nd Plan")
# go to the second plan
parent_div = driver.find_element(By.XPATH, '//*[@id="home-rostrum-3"]/div/div/div[2]')
parent_div.click()

# make a soup
page_source = driver.page_source
soup_plans = BeautifulSoup(page_source, 'html.parser')
# get titles from second plan
titles_plan2 = soup_plans.find_all('h3', class_='h3 imh-rostrum-card-title')
titles_list_plan2 = [title.text.strip() for title in titles_plan2]
print(titles_list_plan2)
# get costs from second plan
cost_plan2 = soup_plans.find_all('div', class_='imh-rostrum-starting-at-price-discounted')
cost_list_plan2 = [val.text.strip()[1:5] for val in cost_plan2]
print(cost_list_plan2)
# get features from second plan
features_plan2 = soup_plans.find_all("h3", class_='heading')
features_list_plan2 = [feature.text.strip() for feature in features_plan2]
print(features_list_plan2)
# back to the main page
driver.back()


print("_____________________________")
print("Information for the 3rd Plan")
# go to the third plan
parent_div = driver.find_element(By.XPATH, '//*[@id="home-rostrum-3"]/div/div/div[3]')
parent_div.click()

# make a soup
page_source = driver.page_source
soup_plans = BeautifulSoup(page_source, 'html.parser')
# get titles from third plan
titles_plan3 = soup_plans.find_all('h3', class_='h3 imh-rostrum-card-title')
titles_list_plan3 = [title.text.strip() for title in titles_plan3]
print(titles_list_plan3)
# get costs from third plan
cost_plan3 = soup_plans.find_all('div', class_='imh-rostrum-starting-at-price-discounted')
cost_list_plan3 = [val.text.strip()[1:5] for val in cost_plan3]
print(cost_list_plan3)
# get features from third plan
features_plan3 = soup_plans.find_all("td")
features_list_plan3 = [feature.text.strip() for feature in features_plan3]
print(features_list_plan3)
# back to the main page
driver.back()


print("_____________________________")
print("Information for the 4th Plan")
# go to the fourth plan
parent_div = driver.find_element(By.XPATH, '//*[@id="home-rostrum-3"]/div/div/div[4]')
parent_div.click()
# make a soup
page_source = driver.page_source
soup_plans = BeautifulSoup(page_source, 'html.parser')
# get titles from fourth plan
titles_plan4 = soup_plans.find_all('h3', class_='h3 imh-rostrum-card-title')
titles_list_plan4 = [title.text.strip() for title in titles_plan4]
print(titles_list_plan4)
# get costs from fourth plan
cost_plan4 = soup_plans.find_all('div', class_='imh-rostrum-starting-at-price-discounted')
cost_list_plan4 = [val.text.strip()[1:5] for val in cost_plan4]
print(cost_list_plan4)
# get features from fourth plan
features_plan4 = soup_plans.find_all("td")
features_list_plan4 = [feature.text.strip() for feature in features_plan4]
print(features_list_plan4)
# back to the main page
driver.back()

print("_____________________________")
print("Information for the 5th Plan")
# go to the fifth plan
parent_div = driver.find_element(By.XPATH, '//*[@id="home-rostrum-3"]/div/div/div[5]')
parent_div.click()
# make a soup
page_source = driver.page_source
soup_plans = BeautifulSoup(page_source, 'html.parser')
# get titles from fifth plan
titles_plan5 = soup_plans.find_all('h3', class_='imh-rostrum-card-title')
titles_list_plan5 = [title.text.strip() for title in titles_plan5]
print(titles_list_plan5)
# get costs from fifth plan
cost_plan5 = soup_plans.find_all('div', class_='imh-rostrum-starting-at-price-discounted')
cost_list_plan5 = [val.text.strip()[1:5] for val in cost_plan5]
print(cost_list_plan5)
# get features from fifth plan
features_plan4 = soup_plans.find_all("td")
features_list_plan4 = [feature.text.strip() for feature in features_plan4]
print(features_list_plan4)
# back to the main page
driver.back()

driver.quit()


