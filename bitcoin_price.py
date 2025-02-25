import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return f"Current Bitcoin Price: ${price}"

print(get_bitcoin_price())
