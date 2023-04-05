from bs4 import BeautifulSoup
import requests


def get_currency(from_currency, to_currency):
    url = f"https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1"
    content = requests.get(url).text
    # providing the markup and features to BeautifulSoup constructor
    soup = BeautifulSoup(content, "html.parser")
    # finding element by it class, then extract the text and get the number only
    rate = soup.find("span", class_="ccOutputRslt").get_text()[:-4]
    return float(rate)


print(get_currency("EUR", "USD"))