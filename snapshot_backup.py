import boto3

#client = boto3.client('ec2', region_name="eu-central-1", aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")

#response = client.create_snapshot(VolumeId='vol-086bdbf410ea62095')
#print(response['SnapshotId'])
#snapshotid = response['SnapshotId']
#print(snapshotid)

#response1 = client.copy_snapshot(SourceRegion='eu-central-1', SourceSnapshotId='snap-0feaa7c11c9ce57a7', DestinationRegion='eu-west-2', Description='This is my copied snapshot')
#print(response1)


source_client = boto3.client('ec2', region_name='eu-central-1', aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")
destination_client = boto3.client('ec2', region_name='eu-west-2', aws_access_key_id="AKIA2DKHECY5FOVEFLU3",  aws_secret_access_key="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")

response = destination_client.copy_snapshot(
    SourceSnapshotId='snap-0feaa7c11c9ce57a7',
    SourceRegion='eu-central-1',
    DestinationRegion='eu-west-2')

new_snapshot_id = response['SnapshotId']

response1 = destination_client.describe_snapshots(SnapshotIds=[new_snapshot_id])
status = response['SnapshotId']
#print(status)
