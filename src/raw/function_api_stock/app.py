import json
import boto3
import requests
from datetime import datetime, timezone
from botocore.exceptions import ClientError

def upload_data_to_s3(bucket, json_data):

    current_datetime = datetime.now()
    
    filename = f"{current_datetime.strftime('%s')}"
    path = f'api_stock/{current_datetime.date()}/{filename}.json'
    # Upload JSON String to an S3 Object
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(name=bucket)
    s3_bucket.put_object(
        Key=path,
        Body=json.dumps(json_data)
    )

def lambda_handler(event, context):

    # get parameters from event
    symbol_name = event['symbol']
    function_name = event['function']
    apikey = event['apikey']

    url = f'https://www.alphavantage.co/query?function={function_name}&symbol={symbol_name}&apikey={apikey}'
    r = requests.get(url)

    upload_data_to_s3('datalake-xpe-raw', r.json())

    return {
        'statusCode': 200,
        'body': f'New checkpoint: Okay.'
    }