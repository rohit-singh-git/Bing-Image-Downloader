<<<<<<< HEAD
import os
from random import choice
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import logging

# suppress logging
logging.getLogger("selenium").setLevel(logging.CRITICAL)

emojis = ["😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙",
          "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "🙂‍↕️", "😏", "😒", "🙂‍↔️"]


# Function to download an image from a URL
def download_image(url, folder_path, image_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        random_emoji = choice(emojis)
        print(f"Downloading {image_name} {random_emoji}")
        with open(os.path.join(folder_path, image_name), 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {image_name} from {url}: {e}")


def main(search_query, save_path):
    # Set up the WebDriver with headless mode and other options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")  # Suppress console logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Suppress DevTools listening message
    driver = webdriver.Chrome(options=options)

    try:
        # Open Bing Images search
        # driver.get(f'https://www.bing.com/images/search?q={search_query}')
        driver.get(f"https://www.bing.com/images/search?q={search_query}&qft=+filterui:imagesize-custom_170_100&form=IRFLTR&first=1")
        print(f"Searching images for {search_query}...")
        print("Be patient.😊")
        # Create a directory to save images
        path = os.path.join(save_path, search_query)
        if not os.path.exists(path):
            os.makedirs(path)

        # Scroll down to load more images
        for _ in range(15):
            try:
                # Wait until the "See more results" button is clickable
                btn = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#bop_container > div.mm_seemore > a'))
                )
                btn.click()
                time.sleep(2)  # Adjust the sleep time as needed after clicking
            except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
                pass  # If the button is not found or not interactable, just continue

            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(1)  # Adjust the sleep time as needed

        # Parse the page source and find image URLs
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        images = soup.find_all('img', {'class': 'mimg'})
        print(f"Found {len(images)} images.")

        # Download images
        for idx, img in enumerate(images):
            img_url = img.get('src') or img.get('data-src') or img.get('src2')
            if img_url:
                download_image(img_url, path, f'image_{idx + 1}.jpg')

    finally:
        # Close the browser
        driver.quit()

    print("Images downloaded successfully.")


if __name__ == "__main__":
    # Set up argument parser
    parser = ArgumentParser(description="Download images from Bing Images.")
    parser.add_argument("-s", "--search", type=str, required=True, help="Search query for images.")
    parser.add_argument("-d", "--destination", type=str, required=True, help="Destination folder to save images.")
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.search, args.destination)
=======
import os
from random import choice
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from bs4 import BeautifulSoup

emojis = ["😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙",
          "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "🙂‍↕️", "😏", "😒", "🙂‍↔️"]


# Function to download an image from a URL
def download_image(url, folder_path, image_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        random_emoji = choice(emojis)
        print(f"Downloading {image_name} {random_emoji}")
        with open(os.path.join(folder_path, image_name), 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {image_name} from {url}: {e}")


# Set up the WebDriver with headless mode and other options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

try:
    # Open Bing Images search
    query = input("Enter what you are looking for: ")
    driver.get(f'https://www.bing.com/images/search?q={query}')
    print(f"Searching images for {query}...")
    print("Be patient.😊")
    # Create a directory to save images
    folder_path = 'downloaded_images'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Scroll down to load more images
    for _ in range(15):
        try:
            # Wait until the "See more results" button is clickable
            btn = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#bop_container > div.mm_seemore > a'))
            )
            btn.click()
            time.sleep(2)  # Adjust the sleep time as needed after clicking
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
            pass  # If the button is not found or not interactable, just continue

        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)  # Adjust the sleep time as needed

    # Parse the page source and find image URLs
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    images = soup.find_all('img', {'class': 'mimg'})
    print(f"Found {len(images)} images.")

    # Download images
    for idx, img in enumerate(images):
        img_url = img.get('src') or img.get('data-src') or img.get('src2')
        if img_url:
            download_image(img_url, folder_path, f'image_{idx + 1}.jpg')

finally:
    # Close the browser
    driver.quit()

print("Images downloaded successfully.")
>>>>>>> 0abb1a290e269aa19a330d67a36e7c57404fbf1c
