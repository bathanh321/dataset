import pandas as pd

csv_file_path = 'honda_sell_data.csv'

df = pd.read_csv(csv_file_path)

# Select products have 5 star Rating
selected_rows = df[df["Consumer_Rating"] == 5.0]

print(selected_rows)
