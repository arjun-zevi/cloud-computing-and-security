#!/usr/bin/env bash
# OPTIONAL: same as the console steps, using the AWS CLI. Replace the placeholders.
aws ec2 run-instances \
  --image-id <AMI_ID> \
  --instance-type t2.micro \
  --key-name YOUR_KEY \
  --security-group-ids <SG_ID> \
  --count 1 \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=lab-ec2}]'
