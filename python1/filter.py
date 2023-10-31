import pandas as pd;

csv_file_path = 'honda_sell_data.csv'

df = pd.read_csv(csv_file_path)

filtered_df = df[
    (df["Interior_Color"].notnull()) &
    (df["Exterior_Color"].notnull()) &
    (df["Performance_Rating"].notnull()) &
    (df["Value_For_Money_Rating"].notnull()) &
    (df["Exterior_Styling_Rating"].notnull()) &
    (df["Reliability_Rating"].notnull()) &
    (df["MPG"].notnull()) &
    (df["Mileage"].notnull()) &
    (df["State"].notnull()) &
    (df["Seller_Type"].notnull())
]

filtered_df.to_csv('honda_sell_data.csv', index=False)
