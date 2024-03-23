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

# Function to predict Ethereum price, high, and low for future dates using Random Forest
def predict_prices_for_future_random_forest(date):
    # Preprocess input date provided by the user
    date = pd.to_datetime(date, dayfirst=True)
    year = date.year
    month = date.month
    day = date.day
    weekday = date.weekday()
    
    # Make prediction
    features_for_date = [[ethereum_data.iloc[-1]['Open'], ethereum_data.iloc[-1]['High'], ethereum_data.iloc[-1]['Low'], year, month, day, weekday]]
    predicted_price = random_forest_model.predict(features_for_date)[0]
    predicted_high = predicted_price + 100  # Example adjustment for high
    predicted_low = predicted_price - 100  # Example adjustment for low
    return predicted_price, predicted_high, predicted_low

# Function to predict Ethereum price, high, and low for future dates using Extra Trees
def predict_prices_for_future_extra_trees(date):
    # Preprocess input date provided by the user
    date = pd.to_datetime(date, dayfirst=True)
    year = date.year
    month = date.month
    day = date.day
    weekday = date.weekday()
    
    # Make prediction
    features_for_date = [[ethereum_data.iloc[-1]['Open'], ethereum_data.iloc[-1]['High'], ethereum_data.iloc[-1]['Low'], year, month, day, weekday]]
    predicted_price = extra_trees_model.predict(features_for_date)[0]
    predicted_high = predicted_price + 100  # Example adjustment for high
    predicted_low = predicted_price - 100  # Example adjustment for low
    return predicted_price, predicted_high, predicted_low

# # Get user input for the future date
# future_date = input("Enter the future date to predict (YYYY-MM-DD): ")

# # Predict Ethereum price, high, and low for the future date using Random Forest
# predicted_price_rf, predicted_high_rf, predicted_low_rf = predict_prices_for_future_random_forest(future_date)
# print("Predicted Ethereum price for", future_date, "using Random Forest is:", predicted_price_rf)
# print("Predicted Ethereum high for", future_date, "using Random Forest is:", predicted_high_rf)
# print("Predicted Ethereum low for", future_date, "using Random Forest is:", predicted_low_rf)

# # Predict Ethereum price, high, and low for the future date using Extra Trees
# predicted_price_et, predicted_high_et, predicted_low_et = predict_prices_for_future_extra_trees(future_date)
# print("Predicted Ethereum price for", future_date, "using Extra Trees is:", predicted_price_et)
# print("Predicted Ethereum high for", future_date, "using Extra Trees is:", predicted_high_et)
# print("Predicted Ethereum low for", future_date, "using Extra Trees is:", predicted_low_et)
