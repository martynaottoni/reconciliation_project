import pandas as pd
import numpy as np

try:
    df = pd.read_csv('oms_orders_placed.csv', encoding='latin1')
    print(f"Data loaded correctly using latin1 encoding. Loaded {len(df)} rows.")
except:
    df = pd.read_csv('oms_orders_placed.csv', encoding='cp1252')
    print(f"Data loaded using cp1252 encoding. Loaded {len(df)} rows.")
    
#duplicates adding
n_duplicates = 500
old_rows_count = len(df)

duplicates = df.sample(n= n_duplicates)
df = pd.concat([df, duplicates], ignore_index=True)
print(f"{n_duplicates} duplicates added. From {old_rows_count} to {len(df)}. ")

#date format change
df.loc[0:10, 'InvoiceDate'] = 'ERR_DATE_2024'
print("Added date format errors.")

#spaces in customerID 
df['CustomerID'] = df['CustomerID'].astype(str)
idx_to_space = df.sample(n=2000).index
df.loc[idx_to_space, 'CustomerID'] = df.loc[idx_to_space, 'CustomerID'] + " "
print("Added hidden spaces in CustomerID.")

#prices modification
n_mismatched_prices = 1000
mismatch_indices = df.sample(n=n_mismatched_prices).index
df.loc[mismatch_indices, 'UnitPrice'] = df.loc[mismatch_indices, 'UnitPrice'] + 0.01
print(f"Mismatched prices created in {n_mismatched_prices} rows (added 0.01 to UnitPrice).")

#data gaps
df.loc[df.sample(n=1000).index, 'UnitPrice'] = np.nan
print("Deleted 1000 values in UnitPrice column.")

#new file save
output_file = 'wms_shipped_units.csv'
df.to_csv(output_file, index=False, encoding='utf-8')

