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




