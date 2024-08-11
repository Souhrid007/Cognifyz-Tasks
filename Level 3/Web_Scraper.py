import requests
from bs4 import BeautifulSoup

def fetch_and_save_books(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        books = soup.find_all('article', class_='product_pod')

        with open(filename, 'w') as file:
            for book in books:
                title = book.find('h3').find('a')['title']
                price = book.find('p', class_='price_color').get_text(strip=True)

                file.write(f"Title: {title}\n")
                file.write(f"Price: {price}\n")
                file.write("\n")

        print(f"Data saved to {filename}")

    except requests.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


url = 'https://books.toscrape.com/'
filename = 'book_listings.txt'
fetch_and_save_books(url, filename)
