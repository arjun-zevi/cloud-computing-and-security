# Program 8: Deploy a dynamic web application on an EC2 instance on AWS


## Aim
To deploy a web application on an AWS EC2 instance using the Apache HTTP server.

## Prerequisites
- AWS account
- Amazon Linux EC2 instance with ports 22, 80 and 443 open

## Repository contents
```
08-dynamic-web-app-ec2/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/deploy_webserver.sh
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. EC2 > **Launch instance**; name `web-server`; AMI **Amazon Linux**; type `t3.micro`.
2. Create a new key pair (e.g. `kyp`) and download it.
3. Network settings: allow **SSH**, **HTTPS** and **HTTP** traffic. Keep storage/advanced defaults and **Launch**.
4. Select the instance > **Connect** > **EC2 Instance Connect** > **Connect**.
5. Run the commands in `src/deploy_webserver.sh` (install `httpd`, download the template, copy to `/var/www/html`, start the service).
6. Copy the instance's **Public IPv4 address**, paste it in a browser (`http://<ip>`).

## Expected output
The deployed website (Electric Xtra template) opens from the public IP of the instance.


## Result
The web application was deployed on an EC2 instance and accessed through its public IP.

## Notes
Use `http://` (not https) unless you have configured a certificate. Stop/terminate the instance after the lab.
