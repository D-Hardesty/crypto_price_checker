from pycoingecko import CoinGeckoAPI
import pandas as pd
from datetime import datetime

cg = CoinGeckoAPI()

# read the CSV file into a DataFrame
df = pd.read_csv("coins.csv")

# get the current date and time
now = datetime.now()
dt_date = now.strftime("%m/%d/%Y")
dt_time = now.strftime("%H:%M:%S")

# create the first entry in the list with date and time
coin_list = [{'coin': dt_time, 'price': dt_date}]

# get a list of coin IDs from the DataFrame
coin_ids = df['coin'].str.lower().tolist()

# request coin prices from CoinGecko for all coins
try:
    coin_data = cg.get_price(ids=coin_ids, vs_currencies='usd')
except Exception as e:
    print(f"Error fetching prices: {e}")
    coin_data = {}

# iterate through the DataFrame and populate the coin_list with prices
for index, row in df.iterrows():
    coin = row['coin'].lower()
    price = coin_data.get(coin, {}).get('usd', 'NA')

    coin_list.append({'coin': coin, 'price': price})
    print(coin)

# create a DataFrame from the updated coin_list
price_df = pd.DataFrame(coin_list)

# save the DataFrame to a CSV file
price_df.to_csv('crypto_prices.csv', mode="w", index=False)
