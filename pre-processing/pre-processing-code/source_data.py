import os
import boto3
import urllib.request

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://data.cdc.gov/api/views/hc4f-j6nb/rows'
	
	urllib.request.urlretrieve(
		source_dataset_url + '.csv', '/tmp/' + new_filename + '.csv')
	urllib.request.urlretrieve(
		source_dataset_url + '.json', '/tmp/' + new_filename + '.json')

	s3 = boto3.client('s3')
	folder = "/tmp"

	asset_list = []

	for filename in os.listdir(folder):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + filename)

		asset_list.append({'Bucket': s3_bucket, 'Key': new_s3_key + filename})

	return asset_list