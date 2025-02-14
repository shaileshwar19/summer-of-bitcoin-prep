import requests
import matplotlib.pyplot as plt
from datetime import datetime

def get_historical_data():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    response = requests.get(url)
    data = response.json()["bpi"]
    
    dates = list(data.keys())
    prices = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker="o", linestyle="-", color="b", label="BTC Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Bitcoin Price Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

get_historical_data()
