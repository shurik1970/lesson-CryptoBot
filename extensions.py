import requests
import json
from config import keys

import requests
import json

from config import keys



class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}\n<Введите правильные данные>')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {quote}\n <Введите правильные данные>')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {base}\n<Введите правильные данные>')
        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionException(f'Невозможно обработать валюту {famount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base