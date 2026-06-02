import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/topics"

# fetch the content of the website
response = requests.get(url)
# print(response.text)

# the status code of the response
if response.status_code != 200:
    print("Failed to retrieve the HTML content. Status code:", response.status_code)
else:
    print(f"Status code: {response.status_code}")

# the first 100 characters
print("__________________________")
print("100 characters of the code:")
print(response.text[:100])

# Save the html code to a file named webpage.htm
# with open("webpage.html", "w", encoding="utf-8") as file:
#     file.write(response.text)

# parse the saved HTML with BeautifulSoup
with open("webpage.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

# print(soup.title.get_text())

# get titles
titles_of_topics = soup.find_all('p', class_='f3 lh-condensed mb-0 mt-1 Link--primary')
# print(titles_of_topics)
titles = [title.text.strip() for title in titles_of_topics]
# get descriptions
descrp_of_topics = soup.find_all('p', class_='f5 color-fg-muted mb-0 mt-1')
titles_discr = [description.text.strip() for description in descrp_of_topics]
# print title with description
print("__________________________")
print("\nTitles with descriptions")
index = 0
for val in range(len(titles_discr)):
    print("\n", titles[index])
    print(titles_discr[index])
    index += 1

# the length and content
print("__________________________")
print(f"\nThe length of the titles list: {len(titles)}")
print(f"\nThe length of the descriptions list: {len(titles_discr)}")

print("__________________________")
print("Content of the titles list:")
for title in titles:
    print(title)

print("__________________________")
print("Content of the descriptions list:")
for description in titles_discr:
    print(description)

# dictionary to structure the extracted data
dict_of_data = {'Title': titles, 'Description': titles_discr}

# convert this dictionary into a pandas DataFrame and print it
data = pd.DataFrame(dict_of_data)
print(data)