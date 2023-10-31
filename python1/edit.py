import pandas as pd
import numpy as np

csv_file_path = 'honda_sell_data.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

df['Price'] = np.random.randint(15000, 50000, size=len(df))

df.to_csv(csv_file_path, index=False)