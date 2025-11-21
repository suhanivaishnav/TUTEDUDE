from scraper import scrape_product

url = input("Enter product URL: ")
data = scrape_product(url)
print(data)
