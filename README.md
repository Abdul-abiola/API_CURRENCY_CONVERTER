# Project Description

Here’s a complete README.md you can use 👇

 Currency Converter using API

A simple Python project that converts currency values in real time using a public exchange rate API (like ExchangeRate-API or Open Exchange Rates).

## Features

Convert between any two global currencies (e.g., USD → NGN)

Fetch live exchange rates using a free API

Input amount and currencies dynamically

Error handling for invalid inputs or API issues

 ### Technologies Used

Python 3

Requests library (for API calls)

JSON (for parsing API data)

Installation

Clone this repository

git clone https://github.com/yourusername/currency-converter-api.git
cd currency-converter-api


Install dependencies

pip install -r requirements.txt


Create a free API key
You can get one from:

https://www.exchangerate-api.com

 Usage Example
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "Error fetching data."

    rate = data["conversion_rates"].get(to_currency.upper())
    if rate is None:
        return f"Currency '{to_currency}' not found."

    converted_amount = rate * amount
    return f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}"

### Example usage
print(convert_currency(10, "USD", "NGN"))

 requirements.txt
requests

 Error Handling

Handles invalid currency codes

Handles API connection errors

Handles missing or expired API keys

###  Example Output
10 USD = 14600.25 NGN
