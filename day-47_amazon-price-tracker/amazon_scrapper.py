import requests
from bs4 import BeautifulSoup

class Amazon_Scrapper:

    def __init__(self):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en",
            "Priority": "u=0, i",
            "Sec-Ch-Ua": "\"Brave\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        }
        practice_url = "https://appbrewery.github.io/instant_pot/"
        self.url = "https://www.amazon.ca/Instant-Electric-Pressure-Sterilizer-Stainless/dp/B00FLYWNYQ/ref=sr_1_5?sr=8-5"
        response = requests.get(self.url, headers=header)

        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.prettify())

        # grab price and format to a float
        self.price = float(soup.find(class_="a-offscreen").getText().replace("$",""))
        self.itemName = soup.find(id="productTitle").getText()

    def getPrice(self):
        return self.price

    def getItemName(self):
        return self.itemName

    def getItemLink(self):
        return self.url

# a = Amazon_Scrapper()
# print(a.getItemName().replace("  ", "").strip())
# print(a.getPrice())