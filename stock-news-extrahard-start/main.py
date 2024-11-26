import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Alpha Vantage API Key
AV_API_KEY = ""

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
av_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': AV_API_KEY
}

av_url = 'https://www.alphavantage.co/query'
av_request = requests.get(av_url, params=av_parameters)
av_data = av_request.json()["Time Series (Daily)"]
av_data_list = [value for (key, value) in av_data.items()]

recent_close = float(av_data_list[0]["4. close"])
previous_close = float(av_data_list[1]["4. close"])

stock_change = ((recent_close - previous_close) / previous_close) * 100
print(f"{stock_change}%")




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# News API Key
NEWS_API_KEY = ""

news_parameters = {
    'q': 'telsa',
    'apiKey': NEWS_API_KEY
}

news_url = 'https://newsapi.org/v2/everything'
news_request = requests.get(news_url, params=news_parameters)
news_data = news_request.json()["articles"]



# if abs(stock_change) >= 5:
#     print(news_data)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

for i in range(3):
    print(news_data[i]["description"])
    if stock_change >= 0:
        direction = '🔺'
    else:
        direction = '🔻'

    body = f"""{STOCK}: {direction}{stock_change}
        Headline: {news_data[i]["title"]}
        Brief: {news_data[i]["description"]} 
        """
    print(body)

    message = client.messages \
        .create(
        body=body,
        from_='+',
        to='+'
    )
    print(message.status)


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
