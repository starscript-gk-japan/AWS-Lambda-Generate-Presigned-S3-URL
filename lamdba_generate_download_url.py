import json
import boto3
import os

# S3 client
s3 = boto3.client("s3")

# Your S3 bucket and file name
BUCKET = "invoiceaijapantech"
KEY = "Download Your Application.zip"

def lambda_handler(event, context):
    try:
        # Generate a presigned URL (24 hours = 86400 seconds)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': BUCKET,
                'Key': KEY
            },
            ExpiresIn=86400  # 24 hours (seconds)
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"  # CORS permission
            },
            "body": json.dumps({"download_url": url})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }