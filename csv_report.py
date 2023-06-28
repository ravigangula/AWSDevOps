import boto3
import csv

def Instance_fun(writer):
	client = boto3.client('ec2', region_name="eu-central-1", aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")

	empty_dict_hari = {}

	list_instance_var = client.describe_instances()

	for i in list_instance_var['Reservations']:
		for j in i['Instances']:
			
			empty_dict_hari["AMI_ID"] = j['ImageId']
			empty_dict_hari["InstanceId"] = j['InstanceId']
			empty_dict_hari["Created_date"] = j['LaunchTime']

			writer.writerow(empty_dict_hari)

			print ("CSV has been generator and stored in same location")

def main():
	fieldnames = ["AMI_ID","InstanceId","Created_date"]
	file_name = "empty_dict_hari.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		Instance_fun(writer)

main()