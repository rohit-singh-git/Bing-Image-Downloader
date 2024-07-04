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
