# Crypto Price Fetcher

This Python script fetches the current USD prices of multiple cryptocurrencies using the CoinGecko API and saves the results to a CSV file.

## Dependencies

- [pycoingecko](https://github.com/man-c/pycoingecko): Python wrapper for the CoinGecko API.
- [pandas](https://pandas.pydata.org/): Data manipulation library for Python.

## Usage

1. Install the required dependencies:

```bash
pip install pycoingecko pandas

2. Prepare a CSV file (coins.csv) with a column named "coin" containing the list of cryptocurrency names or IDs.

3. Run the script:

```bash  
python crypto_price_fetcher.py

##Notes
-If there are errors fetching prices for specific coins, check for spelling errors or incorrect IDs in the coins.csv file.

-The script uses the CoinGecko API, so an internet connection is required.

-Make sure to handle exceptions appropriately when running the script, especially if there are issues with the CoinGecko API request.
