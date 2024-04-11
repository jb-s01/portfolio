import requests
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def get_ticker_metadata(ticker):
    """
    Fetches metadata for a given ticker symbol from the Tiingo API using an API key from a .env file.

    Parameters:
    - ticker: The ticker symbol for which to fetch metadata.

    Returns:
    - A dictionary containing the metadata for the requested ticker.
    """
    # Retrieve the API key from environment variables
    api_key = os.getenv('TIINGO_API_KEY')
    
    # The URL for the Tiingo metadata endpoint
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}"
    
    # Headers to include in the request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}'
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and return it
        return response.json()
    else:
        # Handle errors (e.g., ticker not found, authentication issues)
        return {'error': f'Failed to fetch data for {ticker}. HTTP Status Code: {response.status_code}'}

# Example usage:
# ticker = 'AAPL'
# metadata = get_ticker_metadata(ticker)
# print(metadata)

def get_hist_eod_px(ticker, start_date, end_date):
    """
    Fetches End-of-Day (EOD) stock prices for a given ticker symbol from the Tiingo API,
    using the API key loaded from a .env file, and returns the data as a pandas DataFrame.

    Parameters:
    - ticker: The ticker symbol for which to fetch EOD stock prices.
    - start_date: The start date for the price data in the format YYYY-MM-DD.
    - end_date: The end date for the price data in the format YYYY-MM-DD.

    Returns:
    - A pandas DataFrame containing the EOD stock prices for the requested ticker and date range.
    """
    # Retrieve the API key from environment variables
    api_key = os.getenv('TIINGO_API_KEY')
    
    # The URL for fetching EOD stock prices from Tiingo
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
    
    # Parameters to include in the request
    params = {
        'startDate': start_date,
        'endDate': end_date,
        'format': 'json',
    }
    
    # Headers to include in the request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}'
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Convert the JSON data to a pandas DataFrame
        df = pd.DataFrame(data)
        return df
    else:
        # Handle errors (e.g., ticker not found, incorrect dates, authentication issues)
        error_message = f'Failed to fetch EOD prices for {ticker}. HTTP Status Code: {response.status_code}'
        return pd.DataFrame({'error': [error_message]})

# Example usage:
ticker = 'AAPL'
start_date = '2024-01-01'
end_date = '2024-04-10'
eod_prices_df = get_hist_eod_px(ticker, start_date, end_date)
print(eod_prices_df.tail())
