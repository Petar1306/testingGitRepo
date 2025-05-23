import requests


def convert_currencies(currency):
    api_key = '53b7bb339000b9554865a0a5'

    url = f"https://v6.exchangerate-api.com/v6/{'53b7bb339000b9554865a0a5'}/latest/GBP"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        conversion_rate = data['conversion_rates']['BGN']
        bgn = currency * conversion_rate

        return f'{bgn:.3f}'
    else:
        return 'Error fetching exchange rate'


currency_value = int(input())
bgn = convert_currencies(currency_value)
print(f'{currency_value} British pounds is equal to {bgn} Bulgarian leva.')
