import pandas as pd

csv_file_path = 'honda_sell_data.csv'

df = pd.read_csv(csv_file_path)

def evaluate_rating(row):
    if row['Consumer_Rating'] >= 3.0:
        return 'Positive'
    else:
        return 'Negative'

df['Evaluate_Rating'] = df.apply(evaluate_rating, axis=1)

print(df)