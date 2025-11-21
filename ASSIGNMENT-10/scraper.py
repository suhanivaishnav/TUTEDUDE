import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

def fetch_html(url):
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.in/",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("ERROR:", e)
        return None


def scrape_amazon(url):
    html = fetch_html(url)
    if not html:
        return {"error": "Unable to fetch page"}

    soup = BeautifulSoup(html, "html.parser")

    # Multiple selectors for title
    title = (
        soup.find("span", id="productTitle")
        or soup.find("span", {"class": "a-size-large product-title-word-break"})
    )
    title = title.get_text().strip() if title else None

    # Price selectors
    price = (
        soup.find("span", {"class": "a-price-whole"})
        or soup.find("span", {"class": "a-offscreen"})
    )
    price = price.get_text().replace("₹", "").replace(",", "").strip() if price else None

    # Image selectors
    image = soup.find("img", {"id": "landingImage"})
    if image:
        image = image.get("src")
    else:
        img_tag = soup.find("img", {"data-old-hires": True})
        image = img_tag["data-old-hires"] if img_tag else None

    return {
        "site": "Amazon",
        "name": title,
        "price": float(price) if price else None,
        "image": image,
        "url": url,
    }


def scrape_product(url):
    if "amazon" in url:
        return scrape_amazon(url)
    return {"error": "Website not supported"}
