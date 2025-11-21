📦 Price Tracer Application

A Python-based Price Tracking Application that monitors product prices from e-commerce websites (Amazon, Flipkart, etc.).
It performs:

✔ Web Scraping
✔ Price Extraction
✔ Product Information Fetching
✔ API Integration (Optional)

This project allows users to enter a product URL and fetch:

Product Name

Current Price

Product Image

Product Link

🧩 Features
🔍 Web Scraping

Extracts product details from:

Amazon.in

Flipkart.com

📊 Price Monitoring (extendable)

Can be extended to:

Track price changes

Store price history

Trigger alerts

🛠 Built With

Python

BeautifulSoup4

Requests

Fake-UserAgent

🏗 Project Structure
price-tracer/
│
├── scraper.py
├── test_scraper.py
├── README.md
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourname/price-tracer.git
cd price-tracer

2️⃣ Install Dependencies
pip install -r requirements.txt

📄 requirements.txt
requests
beautifulsoup4
fake-useragent

🧩 Web Scraping Module (scraper.py)

This module contains functions to scrape:

Amazon product pages

Flipkart product pages

Highlights:

Detects website from URL

Uses strong headers to bypass bot detection

Extracts title, price, and image

Supports wrong or blocked pages

Returns clean JSON data

🚀 Usage
Run the test script
python test_scraper.py


Enter a product URL:

https://www.amazon.in/Nothing-Phone-3a-Black-128GB/dp/B0DZTNWWDH

Expected Output
{
  "site": "Amazon",
  "name": "Nothing Phone 3a (Black, 128GB)",
  "price": 24999.0,
  "image": "https://m.media-amazon.com/images/xxxx.jpg",
  "url": "https://www.amazon.in/..."
}


If Amazon blocks the scraper, the response will be:

{ "error": "Unable to fetch page" }

🛠 API Integration (Optional)

Use this in Django/Flask route:

from scraper import scrape_product

def api_scraper(request):
    url = request.GET.get("url")
    data = scrape_product(url)
    return JsonResponse(data)


API Call Example:

/api/scrape/?url=https://www.amazon.in/product

🧪 Supported Websites
Website	Status
Amazon	✔ Supported
Flipkart	✔ Supported
Myntra	✖ Not Yet
Ajio	✖ Not Yet

More sites can be added.

📌 Limitations

Amazon frequently updates HTML structure

Amazon blocks scrapers sometimes

Web scraping is slower than using API services

Requires strong user-agent headers

🚀 Future Enhancements

✔ Price history graph
✔ Daily price tracker
✔ Email/WhatsApp alerts
✔ Django REST API backend
✔ React frontend dashboard
✔ Selenium/Playwright-based scraper (100% detection-proof)

🤝 Contributing

Pull requests are welcome.
For major changes, open an issue first to discuss what you’d like to modify.

📜 License

This project is open-source under the MIT License.

If you want, I can also generate:

✅ README with screenshots
✅ Django version README
✅ Flask version README
✅ Full project code with frontend
