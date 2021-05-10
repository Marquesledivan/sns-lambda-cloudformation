#!/usr/local/bin/python3
"""
version 1.0 Author: Ledivan B. Marques
            Email:	ledivan_bernardo@yahoo.com.br
"""
import json
import boto3

message = { "Key": "Ledivan", "Value": "Bernardo" }
client = boto3.client('sns')

response = client.publish(
    TopicArn='arn:aws:sns:us-east-1:43484260222223:ledivan_teste',
    Message=json.dumps(message),
    Subject='test',
)


if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
     print('Sucess!!!')