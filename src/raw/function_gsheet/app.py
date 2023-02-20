import json
import boto3
import requests
import pandas as pd
from datetime import datetime, timezone
from botocore.exceptions import ClientError
from io import StringIO # python3; python2: BytesIO 

def build_sheet_url(sheet_id, sheet_name):
    # return f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid={sheet_id}'
    return f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

def upload_data_to_s3(bucket, df):

    current_datetime = datetime.now()
    
    filename = f"{current_datetime.strftime('%s')}"
    path = f'gsheet/{current_datetime.date()}/{filename}.csv'
    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    # Upload JSON String to an S3 Object
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(name=bucket)
    s3_bucket.put_object(
        Key=path,
        Body=csv_buffer.getvalue()
    )

def lambda_handler(event, context):

    # get parameters from event
    sheet_id = event['SHEET_ID']
    sheet_name = event['SHEET_NAME']

    sheet_url = build_sheet_url(sheet_id, sheet_name)
    df = pd.read_csv(sheet_url, index=False)

    upload_data_to_s3('datalake-xpe-raw', df)

    return {
        'statusCode': 200,
        'body': f'New checkpoint: Okay.'
    }