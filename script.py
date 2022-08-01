import pandas as pd
import pytz
from pycoingecko import CoinGeckoAPI()


pao=df.groupby('block_number', sort=False).count().reset_index()
pao['utc_timestamp'] = pao.apply(lambda x: datetime.datetime.now() + datetime.timedelta(seconds=13 * int(x.name)), axis=1)
pao2 = pao["block_number", "utc_timestamp"]
df2.merge(pao2, left_on='block_number', right_on="block_number", how='left')



pao = cg.get_coin_market_chart_by_id('ethereum', 'usd', 1, interval='5 minutes')