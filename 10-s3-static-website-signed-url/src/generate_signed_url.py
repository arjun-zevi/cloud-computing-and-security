"""Create a time-limited pre-signed URL for a private S3 object.
Usage: python generate_signed_url.py <bucket> <key> [expires_seconds]
Needs: pip install boto3 and AWS credentials configured (aws configure)."""
import sys
import boto3
from botocore.client import Config

bucket, key = sys.argv[1], sys.argv[2]
expires = int(sys.argv[3]) if len(sys.argv) > 3 else 300

s3 = boto3.client("s3", config=Config(signature_version="s3v4"))
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket, "Key": key},
    ExpiresIn=expires,
)
print(f"Signed URL (valid {expires}s):\n{url}")
