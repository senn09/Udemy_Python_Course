import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Alpha Vantage API Key
AV_API_KEY = "W79TRVDTSNYPJSKF"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
av_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': AV_API_KEY
}

av_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(av_url, params=av_parameters)
data = r.json()["Time Series (Daily)"]
data_iter_keys = iter(data)

recent_key = next(data_iter_keys)
previous_key = next(data_iter_keys)
recent_open = float(data[recent_key]["1. open"])
previous_close = float(data[previous_key]["4. close"])

stock_change = recent_open - previous_close
print(stock_change)


# for item in data:
#     print(item)

# today = data_list[0]
# yesterday = data_list[1]

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
