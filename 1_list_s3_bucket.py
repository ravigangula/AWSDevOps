import boto3

client = boto3.client('s3', aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")

response = client.list_buckets()
#print (response['Buckets'])

for new_bucket in response['Buckets']:
	print(new_bucket['Name'])
 