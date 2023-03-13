import json
import boto3
import requests
from pytz import timezone
from datetime import datetime
from botocore.exceptions import ClientError

def upload_data_to_s3(bucket, symbol, json_data):

    current_datetime = datetime.now(timezone('America/Sao_Paulo'))
    
    path = f'api_stock/{current_datetime.date()}/{symbol}.json'
    print(path)
    # Upload JSON String to an S3 Object
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(name=bucket)
    s3_bucket.put_object(
        Key=path,
        Body=json.dumps(json_data)
    )

def lambda_handler(event, context):

    # get parameters from event
    symbols = event['symbol']
    function = event['function']
    apikey = event['apikey']
    interval = event['interval']

    for symbol in symbols:
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={apikey}'
        print(url)
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"
            print(r)
        upload_data_to_s3('datalake-xpe-raw', symbol, r.json())

    return {
        'statusCode': 200
    }