#!/usr/bin/env bash
# CLI equivalents of the console steps (optional). Replace the placeholders.
BUCKET=my-video-streaming-bucket-2026
REGION=us-east-1

# Step 1: private, versioned, encrypted bucket + upload test video
aws s3api create-bucket --bucket $BUCKET --region $REGION
aws s3api put-public-access-block --bucket $BUCKET \
  --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api put-bucket-versioning --bucket $BUCKET --versioning-configuration Status=Enabled
aws s3api put-bucket-encryption --bucket $BUCKET \
  --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'
aws s3 cp sample.mp4 s3://$BUCKET/sample.mp4

# Step 2 & 3: create the CloudFront distribution (with OAC) in the console,
# then attach cloudfront_bucket_policy.json to the bucket:
aws s3api put-bucket-policy --bucket $BUCKET --policy file://cloudfront_bucket_policy.json

# Step 4: test
curl -I https://<DISTRIBUTION_DOMAIN>.cloudfront.net/sample.mp4
