import boto3
import collections
import time; time.time()

def lambda_handler(event,context):
	s3_object = boto3.client('logs', region_name='us-east-2')

	response = s3_object.create_export_task(
		taskName='export to S3',
		logGroupName=('/aws/lambda/YOUR_LOG_GROUP_NAME'),
		logStreamNamePrefix='default',
		fromTime=456858943000,
		to=5655086899000,
		destination='YOUR_S3_BUCKET_ARN',
		destinationPrefix='default'
	)
	print(response)
