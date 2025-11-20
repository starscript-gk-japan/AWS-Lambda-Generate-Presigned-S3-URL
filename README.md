Lambda S3 Presigned URL Generator

This project demonstrates an AWS Lambda function that generates a presigned URL for an S3 object. The URL allows temporary access to download a file (valid for 24 hours).

Project Structure
project-root/
├─ README.md
├─ lambda/
│   ├─ generate_download_url.py   # Lambda function
│   └─ requirements.txt          # Dependencies (boto3, etc.)
├─ .gitignore
└─ LICENSE
Usage

Deploy the Lambda function in AWS.

Ensure the Lambda execution role has permission to s3:GetObject.

Invoke the Lambda function via AWS Console or API Gateway.

The function returns a JSON containing the presigned download_url.

Open the URL in a browser or use it in your application to download the file.

Notes

URL validity is set to 24 hours.

You can customize the bucket name and file key in generate_download_url.py.