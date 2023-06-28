import boto3
from datetime import date, datetime, timedelta,timezone
import csv
import os
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def access_key_age_fun():

	Iam_report = {}

	client = boto3.client('iam', region_name="eu-central-1", aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")

	List_IAM_users = client.list_users()
	#print (List_IAM_users['Users'])

	for i in List_IAM_users['Users']:
		Iam_Users = i['UserName']

		Access_Key = client.list_access_keys(UserName= Iam_Users)
		for j in Access_Key['AccessKeyMetadata']:
		    IAM_users_createddate = j['CreateDate']


		current_date = datetime.now(timezone.utc)
		#print(current_date)

		age = (current_date - IAM_users_createddate).days
		#print(Iam_Users, age)

		if (age >= 0):
			#print(Iam_Users, age)
			Iam_report["Username"] = Iam_Users
			Iam_report["Age"] = age
			Iam_report["Created_date"] = IAM_users_createddate
			writer.writerow(Iam_report)

def sending_email_asreport(file_name):
	SENDER = "gangula.ravik@gmail.com"
	RECIPIENT = "gangula.ravik@gmail.com"
	SUBJECT = "Accesskey 150 Age Data"
	ATTACHMENT = file_name
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h3>Hi All</h3>
	<p>Please see the attached file for a list of Accesskey those are created 2 5days ago.</p>
	</body>
	</html>
	"""
	CHARSET = "utf-8"
	client = boto3.client('ses')
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT
	
	msg_body = MIMEMultipart('alternative')
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        }
	    ) 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])

def main():
	fieldnames = ["Username", "Age", "Created_date"]
	file_name = "Iam_report.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		access_key_age_fun(writer)
		sending_email_asreport(file_name)
	main()



 