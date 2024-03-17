import requests
from pymongo import MongoClient

# MongoDB connection details
client = MongoClient("mongodb+srv://asghar76555:cPoYYQf11I97sPUn@cluster0.2cx362r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Check if the database exists, create it if it doesn't
db_name = "databaseName"
if db_name not in client.list_database_names():
    db = client[db_name]
    print(f"Database '{db_name}' created.")
else:
    db = client[db_name]
    print(f"Database '{db_name}' already exists.")

# Financial Modeling Prep API key
api_key = '4ffea23194ffaea828e2f42946ed00ee'
symbols = ['XAUUSD', 'USDJPY', 'GBPUSD', 'EURUSD']

# Function to save data to MongoDB
def save_to_mongodb(data, collection_name):
    collection = db[collection_name]
    collection.insert_many(data)
    print(f"Data saved to MongoDB collection: {collection_name}")

# Real-time Quotes
def get_real_time_quotes():
    quotes = []
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        quotes.extend(data)
    save_to_mongodb(quotes, 'real_time_quotes')

# Historical Price Data
def get_historical_price_data():
    historical_data = []
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        historical_data.extend(data['historical'])
    save_to_mongodb(historical_data, 'historical_price_data')

# Economic Calendar
def get_economic_calendar():
    url = f"https://financialmodelingprep.com/api/v3/economic_calendar?apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    save_to_mongodb(data, 'economic_calendar')

# Main function
def main():
    get_real_time_quotes()
    get_historical_price_data()
    get_economic_calendar()

if __name__ == '__main__':
    main()