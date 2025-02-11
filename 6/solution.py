import yfinance as yf
import pandas as pd
import requests
from typing import List
import time
def get_nasdaq_symbols() -> List[str]:
    """
    Fetches list of NASDAQ symbols from NASDAQ trader website.
    Returns:
        List[str]: List of NASDAQ stock symbols
    """
    try:
        # Get NASDAQ listed symbols
        url = "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt"
        df = pd.read_csv(url, sep="|")
        # Extract symbols and filter out test symbols
        symbols = df['Symbol'].tolist()
        # Remove any test symbols (usually contain '$' or '.')
        symbols = [sym for sym in symbols if not any(c in sym for c in ['$', '.'])]
        return symbols[:-1]  # Remove last item which is usually file creation time
    except Exception as e:
        print(f"Error fetching NASDAQ symbols: {e}")
        return []
def get_stock_price(symbol: str) -> float:
    """
    Gets the current stock price for a given symbol.
    Args:
        symbol (str): Stock symbol
    Returns:
        float: Current stock price or None if error
    """
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return info.get('regularMarketPrice', None)
    except Exception:
        return None
def get_nasdaq_equities_filtered() -> pd.DataFrame:
    """
    Returns DataFrame containing symbols and prices of NASDAQ equities under 10 dollars.
    Returns:
        pd.DataFrame: DataFrame containing symbols and prices of equities under 10 dollars.
    """
    # Get NASDAQ symbols
    symbols = get_nasdaq_symbols()
    # Initialize lists to store results
    filtered_symbols = []
    filtered_prices = []
    # Process symbols in batches to avoid rate limiting
    batch_size = 100
    for i in range(0, len(symbols), batch_size):
        batch = symbols[i:i + batch_size]
        # Get prices for batch
        for symbol in batch:
            price = get_stock_price(symbol)
            # Add to filtered lists if price is valid and under $10
            if price is not None and price < 10:
                filtered_symbols.append(symbol)
                filtered_prices.append(price)
        # Add small delay to avoid hitting rate limits
        time.sleep(1)
    # Create DataFrame from filtered data
    df = pd.DataFrame({
        'Symbol': filtered_symbols,
        'Price': filtered_prices
    })
    # Sort by price
    df = df.sort_values('Price')
    return df
if __name__ == "__main__":
    print("Fetching NASDAQ equities under $10...")
    df = get_nasdaq_equities_filtered()
    print("\nResults:")
    print(df)
    print(f"\nTotal stocks found: {len(df)}")