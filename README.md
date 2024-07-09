# Bing Images Downloader

A Python script to download images from Bing Images search.

## Features

- Scrape and download images from Bing Images search results.
- Save downloaded images to a specified folder.

## Requirements

- Python 3.x
- `requests` library
- `selenium` library
- `beautifulsoup4` library
- Chrome WebDriver

## Installation

1. Clone the repository or download the script.

2. Install the required Python libraries:
    ```sh
    pip install requests selenium beautifulsoup4
    ```
    or
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script with the following command:

```sh
python bing_image_downloader.py -s "search_query" -d "destination_folder"
