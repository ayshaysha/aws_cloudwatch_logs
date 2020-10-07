# aws_cloudwatch_logs

Title: AWS Cloudwatch Logs Uploader

Cloud Provider: Amazon Web Service (AWS)

Platform: AWS Lambda

Script Language: Python

Script Compatibility: Python 3.6


Purpose:

Python Function to get AWS Cloudwatch Logs through Lambda and uploads it to S3


Elements and Explanation:

It uses Python Library Boto3 to get Cloudwatch logs and uploads it to S3 which can be processed later


Parameters:

1. Bucket Name 


Deployment Process:

1. Create Lamda Function.

2. Copy Code in the Code Editor Area.

3. Set Bucket Policy to give access to Lambda and Cloudwatch.

4. Execute the Lambda.
