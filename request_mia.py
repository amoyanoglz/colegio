import json
import requests

# urlData = 'https://api.coinbase.com/v2/exchange-rates?currency=EUR'
urlData = 'https://randomuser.me/api/?results=' + input("Cuantos quieres? ")

webURL = requests.get(urlData)

posts = webURL.json()
print(posts)
