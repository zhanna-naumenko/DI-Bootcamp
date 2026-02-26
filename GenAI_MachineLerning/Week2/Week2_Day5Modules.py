import time
import requests


def time_of_request(url):
    start = time.time()
    file_path = 'downloaded_page.html'

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Open a local file in write mode ('w') with UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as f:
            # Write the text content of the response to the file
            f.write(response.text)

        print(f"Successfully downloaded the page to {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    end = time.time()
    return end - start
print(time_of_request("https://www.google.com/"))

# from pyowm.owm import OWM
# from pyowm.commons.exceptions import UnauthorizedError
#
# try:
#     owm = OWM('262029e6b9bd1f12dd5dc6ebb14b432b')
#     mgr = owm.weather_manager()
#     weather = mgr.weather_at_place('Tokyo,JP').weather
#     temp_kelvin = weather.temperature('kelvin')
#     temp_celsius = weather.temperature('celsius')
#     print("Min temp (K):", temp_kelvin['temp_min'])
#     print("Max temp (K):", temp_kelvin['temp_max'])
#     print("Min temp (°C):", temp_celsius['temp_min'])
#     print("Max temp (°C):", temp_celsius['temp_max'])
# except UnauthorizedError:
#     print("Invalid API Key! Check your key and try again.")

# my_list = [5, 4, 3]
#
# new_list = list(map(lambda x: x**2, my_list))
# print(new_list)
#
# a = [(0, 2), (4, 3), (9, 9), (10, -2)]
# a.sort(key=lambda x: x[1])
# print(a)
# new_a = list(sorted(map(lambda x:x[-1], a)))
# print(new_a)




