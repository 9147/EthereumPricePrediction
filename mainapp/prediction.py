import pandas as pd
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor

# Load historical Ethereum price data
ethereum_data = pd.read_csv('Ethereum Historical Data.csv')

# Data preprocessing
ethereum_data['Date'] = pd.to_datetime(ethereum_data['Date'], dayfirst=True)
ethereum_data['Price'] = ethereum_data['Price'].str.replace(',', '').astype(float)
ethereum_data['Open'] = ethereum_data['Open'].str.replace(',', '').astype(float)
ethereum_data['High'] = ethereum_data['High'].str.replace(',', '').astype(float)
ethereum_data['Low'] = ethereum_data['Low'].str.replace(',', '').astype(float)

# Extract date features
ethereum_data['Year'] = ethereum_data['Date'].dt.year
ethereum_data['Month'] = ethereum_data['Date'].dt.month
ethereum_data['Day'] = ethereum_data['Date'].dt.day
ethereum_data['Weekday'] = ethereum_data['Date'].dt.weekday

# Split data into features (X) and target variable (y)
X = ethereum_data[['Open', 'High', 'Low', 'Year', 'Month', 'Day', 'Weekday']]  # Features
y = ethereum_data['Price']  # Target variable

# Train the Random Forest model using the entire dataset
random_forest_model = RandomForestRegressor()
random_forest_model.fit(X, y)

# Train the Extra Trees model using the entire dataset
extra_trees_model = ExtraTreesRegressor()
extra_trees_model.fit(X, y)

# Function to predict Ethereum price for future dates using Random Forest
def predict_price_for_future_random_forest(date):
    # Preprocess input date provided by the user
    date = pd.to_datetime(date, dayfirst=True)
    year = date.year
    month = date.month
    day = date.day
    weekday = date.weekday()
    
    # Make prediction
    features_for_date = [[ethereum_data.iloc[-1]['Open'], ethereum_data.iloc[-1]['High'], ethereum_data.iloc[-1]['Low'], year, month, day, weekday]]
    predicted_price = random_forest_model.predict(features_for_date)

    return predicted_price[0]

print(predict_price_for_future_random_forest('2022-01-01'))
