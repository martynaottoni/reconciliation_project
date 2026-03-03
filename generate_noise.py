import pandas as pd
import numpy as np

try:
    df = pd.read_csv('oms_orders_placed.csv', encoding='latin1')
    print(f"Data loaded correctly using latin1 encoding. Loaded {len(df)} rows.")
except:
    df = pd.read_csv('oms_orders_placed.csv', encoding='cp1252')
    print(f"Data loaded using cp1252 encoding. Loaded {len(df)} rows.")