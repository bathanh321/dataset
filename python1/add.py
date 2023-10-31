import pandas as pd
import numpy as np

csv_file_path = 'honda_sell_data.csv'

df = pd.read_csv(csv_file_path, encoding='latin-1')

countries_in_southeast_asia = ["Vietnam", "Thailand", "Indonesia", "Malaysia", "Singapore", "Philippines", "Myanmar", "Cambodia", "Laos", "Brunei", "Timor-Leste"]

df['region'] = [" ".join(np.random.choice(countries_in_southeast_asia, np.random.randint(1))) for _ in range(len(df))]

# df = df.drop('region', axis=1)

df.to_csv('filtered_car.csv', index=False)