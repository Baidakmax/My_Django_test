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


coin_list = []
date_list = []
price_list = []
dict_of_coins = currency_crypto()
for key, value in dict_of_coins.items():
    coin_list.append(key)
    price_list.append(value[0])
    date_list.append(value[1])
dict_of_all_coins = {}
dict_of_all_coins["coins"] = coin_list
dict_of_all_coins['price'] = price_list
dict_of_all_coins['date'] = date_list













df = pd.DataFrame(dict_of_all_coins)
# Transpose the DataFrame to flip the table


# Rename the columns of the transposed DataFrame
# df_flipped.columns = ['Coin', 'Date', "Price"]
file_path = 'coins_crypto.xlsx'
df.to_excel(file_path, index=False)
print(f'Data saved to {file_path}')







