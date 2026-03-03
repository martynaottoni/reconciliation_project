import pandas as pd 

#data load

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        print(f"File {file_path} loaded correctly using latin1 encoding. Loaded {len(df)} rows.")
        return df
    except Exception:
        df = pd.read_csv(file_path, encoding='cp1252')
        print(f"File {file_path} loaded correctly using cp1252 encoding. Loaded {len(df)} rows.")
        return df
    
    
df_oms = load_data('oms_orders_placed.csv')
df_wms = load_data('wms_shipped_units.csv')