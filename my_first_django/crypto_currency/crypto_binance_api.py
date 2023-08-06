import requests
import pandas as pd
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from datetime import datetime
from openpyxl.workbook import Workbook



api_key = '8MG5BsyO2ecCoRYKtZrXSUvXr7biEG4KNJB62Pv1o9H6VmT8nEnk9IZVAL55zCYi'
api_secret = 'QaETTULrqEmSvG6lhj3n51Z9D0y00I8rAKDwwOAzx1VJis736AyEKPeRDOGnfado'
client = Client(api_key, api_secret)
list_coins = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'WAVESUSDT', 'NEARUSDT',
              'CAKEUSDT', "MATICUSDT", "ATOMUSDT", "APTUSDT", "DOGEUSDT"]

def currency_crypto():
    dict_cur = {}
    for item in list_coins:
        price_coin = client.get_avg_price(symbol=item)
        price = price_coin['price']
        now = datetime.now()
        dict_cur[item] = [round(float(price), 3), now.strftime("%Y-%m-%d %H:%M:%S")]


    return dict_cur

print(currency_crypto())
dict_of_coins = currency_crypto()


df = pd.DataFrame(dict_of_coins)
file_path = 'coins_crypto.xlsx'
df.to_excel(file_path, index=False)
print(f'Data saved to {file_path}')







