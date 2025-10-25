# APIs = Application programming interface
# How to use api
# Building currency converter system
import requests 
# print(dir(requests))
api_key = "da7d876320d8d8689db39072"
# https://v6.exchangerate-api.com/v6/da7d876320d8d8689db39072/latest/USD
base_url =  f"https://v6.exchangerate-api.com/v6/{api_key}/latest"
def convert(from_currency, to_currency, amount):
    url = f"{base_url}/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error, currency could not be converted")
        return None
    
    data = response.json()
    if data["result"] != "success":
        print("Error getting the conversion rates")
        return None
    
    rate = data["conversion_rates"][to_currency]
    try:
        return rate * amount
    except TypeError:
        print("can't add numbers and words")
     

def run():
    print("currency converter")
    from_currency = input("enter the currency you want to convert to e.g USD: ").upper()
    To_currency = input("enter the currency you want to convert to e.g NGN: ").upper()
    name = input("Enter your full name: ")
    try:
        amount = float(input("enter the amount: "))
    except ValueError:
        print("Invalid amount format, amount should be digit")
        return 
    result = convert(from_currency,To_currency,amount)
    
    if result is not None:
        if To_currency == "NGN":
            code = "Naira"
        elif To_currency == "USD":
            code = "Dollars"
        elif To_currency == "GBP ":
            code =  "Pounds"   
        elif To_currency == "EUR":
            code = "Euro"
        elif To_currency == "AED":
            code = "American dollars" 
                       

        print(f"{name}, conversion of {amount}{from_currency} to {code} is {result}")

        # print(f"{name}, conversion of {amount}{from_currency} to {To_currency} = {result}")





run()



