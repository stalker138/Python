'''
Created on 21 авг. 2018 г.

@author: Stalker
'''

from urllib.request import urlretrieve

import requests

url = "https://public.bybit.com/spot/DASHUSDT/DASHUSDT_2023-01-01.csv.gz"

file = urlretrieve(url)

text = requests.get(url)
print()

