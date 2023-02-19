import requests


def lambda_handler(event, context):

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)

    return {
        'statusCode': 200,
        'body': f'New checkpoint: Okay.'
    }