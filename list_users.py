import boto3

client = boto3.client('iam', aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")

response = client.list_users()
#print (response['Users'])

for new_user in response['Users']:
	print(new_user['UserName'],new_user['CreateDate'])


