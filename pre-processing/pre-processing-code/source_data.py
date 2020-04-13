import os
import pandas as pd
import boto3

def source_dataset(s3_bucket, new_s3_key):

    source_data = 'https://data.cdc.gov/resource/hc4f-j6nb.csv'
    file_name = 'provisional-death-counts-covid-19-nchs.csv'

    df = pd.read_csv(source_data, index_col=None)

    df.to_csv('/tmp/' + file_name, index=False)

    s3 = boto3.client('s3')
    s3.upload_file('/tmp/' + file_name, s3_bucket, new_s3_key + file_name)