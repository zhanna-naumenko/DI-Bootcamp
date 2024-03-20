import psycopg2
import requests
import random

conn = psycopg2.connect(database="PyCharm", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()

def fetch_random_countries(num_countries):
    url = f"https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        countries_data = response.json()
        random_countries = random.sample(countries_data, num_countries)
        return random_countries
    else:
        print("Failed to fetch countries data")
        return []

# Function to insert countries into the database
def insert_countries_into_db(countries):
    try:
        for country in countries:
            name = country.get('name').get('common')
            capital = country.get('capital')
            flag = country.get('flags')[0]
            subregion = country.get('subregion')
            population = country.get('population')
            cursor.execute("INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)", (name, capital, flag, subregion, population))
        conn.commit()
        print("Countries inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Main function
def main():
    num_countries = 10
    countries = fetch_random_countries(num_countries)
    insert_countries_into_db(countries)

if __name__ == "__main__":
    main()