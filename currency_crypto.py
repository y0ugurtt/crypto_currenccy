#y0ugurt devlop
import asyncio
import requests

class Currency_crypto(object):
    def __init__(self, token):
        self.token = token

    def cryptocurrency_list(self):
        url = f'https://api.cryptorank.io/v1/currencies?api_key={self.token}'
        req = requests.get(url)
        wallet = req.json()
        name = wallet['data']
        lister = []
        for i in name:
            lister.append(f"id: {i['id']} = {i['name']}")
        return lister
    
    def cryptocurrency_data(self, crypto):
        url = f'https://api.cryptorank.io/v1/currencies/{crypto}?api_key={self.token}'
        req = requests.get(url)
        wallet = req.json()
        return wallet['data']['values']['USD']
    
    def currency_data(self):
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        return data['Valute']['USD']['Value']