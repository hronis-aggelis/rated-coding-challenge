import datetime

import pandas as pd

from pycoingecko import CoinGeckoAPI
from sqlalchemy import create_engine


# I can do something better here like pass index etc and check a smaller subset in each iteration, but for 5k the difference is minimal
def find_eth(x, market_chart_subset):
    for i in range(len(market_chart_subset) - 1):
        if market_chart_subset[i][0] < x.utc_timestamp < market_chart_subset[i + 1][0]:
            return market_chart_subset[i][1]

def main():
    df = pd.read_csv("./ethereum_txs.csv")
    df = df.sort_values("block_number").reset_index()
    df['gas_cost_in_gwei'] = df['receipt_gas_used'] * (df['gas_price'] * 1e-09)

    df_grouped = df.groupby('block_number', sort=False).count().reset_index()
    df_grouped['utc_timestamp'] = df_grouped.apply(lambda x: datetime.datetime.now() + datetime.timedelta(seconds=13 * int(x.name)), axis=1)

    df_merged = df.merge(df_grouped[["block_number", "utc_timestamp"]], left_on='block_number', right_on="block_number", how='left')

    # normalize utc_timestamp to get values for all entries
    df_merged['utc_timestamp'] = df_merged['utc_timestamp'] - pd.Timedelta(days=1)

    cg = CoinGeckoAPI()
    market_chart = cg.get_coin_market_chart_by_id('ethereum', 'usd', 1, interval='5 minutes')

    # select values in needed time range
    market_chart_subset = [[datetime.datetime.utcfromtimestamp(i[0]/1000), i[1]] for i in market_chart['prices'] 
                        if datetime.datetime.utcfromtimestamp(i[0]/1000) > df_merged["utc_timestamp"][0] - pd.Timedelta(minutes=5) and 
                        datetime.datetime.utcfromtimestamp(i[0]/1000) < df_merged["utc_timestamp"][4999] + pd.Timedelta(minutes=5)]


    df_merged['eth_price'] = df_merged.apply(lambda x: find_eth(x, market_chart_subset), axis=1)



    # remove input in order to populate database from dataframe
    df_merged = df_merged.drop('input', axis=1)
    df_merged = df_merged.drop('index', axis=1)

    # create engine to connect to database
    engine = create_engine('mysql+mysqldb://root:password@0.0.0.0:3306/rated', echo = False)
    df_merged.to_sql(con=engine, name='transactions', if_exists='replace')

if __name__ == "__main__":
    main()