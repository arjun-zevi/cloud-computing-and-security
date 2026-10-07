# Program 11: Create a video streaming service using S3 and CloudFront (with AWS Elemental MediaConvert / DRM)


## Aim
To build a video streaming service where videos are stored in a private S3 bucket and delivered through CloudFront.

## Prerequisites
- AWS account, a test `.mp4` video

## Repository contents
```
11-video-streaming-s3-cloudfront/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/aws_cli_commands.sh
├── src/cloudfront_bucket_policy.json
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. **S3** > Create bucket (globally unique name, region). Keep *Block all public access* ON, enable **Versioning** and default encryption **SSE-S3**. Upload a test `.mp4`.
2. **CloudFront** > Create distribution: origin = the bucket; **Origin access control (OAC)** - create control setting with defaults; viewer protocol *Redirect HTTP to HTTPS*; methods GET, HEAD; cache policy *CachingOptimized*; no WAF. Create.
3. Copy the policy offered in the banner (or use `src/cloudfront_bucket_policy.json`) into S3 > **Permissions > Bucket policy** > Save.
4. Wait until the distribution status is *Deployed*, copy the **Distribution domain name** and open `https://<domain>/<video-file>.mp4`.

## Expected output
The video plays in the browser through the CloudFront URL, while direct S3 access is denied.

## Result
A video streaming service was created using S3 and CloudFront.

