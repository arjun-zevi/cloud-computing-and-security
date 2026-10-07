# Program 10: Deploy a static web application using S3 on AWS and secure it with signed URLs


## Aim
To host a static website on Amazon S3, serve it through CloudFront and secure access with signed URLs.

## Prerequisites
- AWS account; (for signed URLs) `pip install boto3` and `aws configure`

## Repository contents
```
10-s3-static-website-signed-url/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/bucket_policy_from_manual.json
├── src/bucket_policy_public_read.json
├── src/error.html
├── src/generate_signed_url.py
├── src/index.html
├── src/styles.css
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. **S3** > **Create bucket**: choose region and name; for the public website, untick *Block all public access*; Create.
2. Bucket > **Properties** > **Static website hosting** > Edit > enable, index document `index.html`, error document `error.html`.
3. **Permissions** > **Bucket policy** > paste `src/bucket_policy_public_read.json` (replace `BUCKET_NAME`).
4. **Upload** `index.html`, `styles.css`, `error.html`; open the S3 static website URL.
5. **CloudFront** > **Create distribution**: origin domain = S3 website endpoint (without `https://`); *Redirect HTTP to HTTPS*; Create. Open the distribution domain name.
6. **Signed URL:** keep the objects private (re-enable Block Public Access, remove the public policy) and run
   `python src/generate_signed_url.py <bucket> index.html 300` - the printed URL works only for 300 seconds.
7. Delete the resources afterwards to avoid charges.

## Expected output
The website opens on the CloudFront domain; the pre-signed URL opens the private object until it expires.


## Result
The static website was deployed on S3/CloudFront and access was secured with signed URLs.

