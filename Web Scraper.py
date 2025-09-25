import requests
from bs4 import BeautifulSoup # pyright: ignore[reportMissingImports]
import os

def scrape_news_headlines(url, output_file='headlines.txt'):
    """
    Scrapes news headlines from a given URL and saves them to a text file.

    Args:
        url (str): The URL of the news website to scrape.
        output_file (str): The name of the file to save the headlines to.
    """
    try:
        # Step 1: Fetch the HTML content
        print(f"Fetching content from {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Step 2: Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Parsing HTML content...")

        # Find all <h2> or other relevant headline tags.
        # This part may need to be adjusted based on the specific website's HTML structure.
        # A common practice is to inspect the page to find the correct tag and class.
        headlines = soup.find_all(['h2', 'h1', 'h3'])
        
        # Extract the text from each headline tag
        extracted_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

        if not extracted_headlines:
            print("No headlines found. The selector might be incorrect.")
            return

        # Step 3: Save the headlines to a .txt file
        with open(output_file, 'w', encoding='utf-8') as f:
            for headline in extracted_headlines:
                f.write(headline + '\n')
        
        print(f"\nSuccessfully scraped {len(extracted_headlines)} headlines.")
        print(f"Headlines saved to {os.path.abspath(output_file)}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the actual URL of the news website you want to scrape
    news_url = 'https://www.bbc.com/news'
    scrape_news_headlines(news_url)