# Program 3: Create an EC2 instance in AWS (Amazon)


## Aim
To create an EC2 instance in AWS and connect to it using an SSH key pair.

## Prerequisites
- AWS account (free tier)
- A terminal with `ssh`

## Repository contents
```
03-ec2-instance-aws/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/connect_ssh.txt
├── src/launch_instance_cli_optional.sh
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Log in to the AWS console, open **Services > EC2**.
2. Click **Launch instance** and give the instance a name.
3. Select the **AMI** (operating system).
4. Keep instance type `t2.micro` (free-tier eligible) and the default storage (up to 30 GB EBS).
5. Keep default network settings; create/select a key pair.
6. Check everything is free-tier eligible and click **Launch instance**.
7. **Connect:** select the instance > **Connect** > copy the SSH command, open a terminal in the folder with the `.pem` file, and run it (see `src/connect_ssh.txt`).

## Expected output
After connecting, the shell prompt of the EC2 instance (`[ec2-user@ip-... ~]$`) is displayed.


## Result
An EC2 instance was created and accessed successfully through SSH.

## Notes
Stop/terminate the instance after the lab to avoid charges.
