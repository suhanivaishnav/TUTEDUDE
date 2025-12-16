from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Open website
driver.get("https://quotes.toscrape.com/")
time.sleep(3)

# Get all quotes
quotes = driver.find_elements(By.CLASS_NAME, "quote")

print("Quotes and Authors:\n")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f"{text} — {author}")

driver.quit()
