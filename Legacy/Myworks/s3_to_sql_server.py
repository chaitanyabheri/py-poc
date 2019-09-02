import boto3
import json
import os
from pathlib import Path


client=boto3.client('sts')
response=client.get_session_token(
                DurationSeconds=7200,
                SerialNumber='arn:aws:iam::186502235371:mfa/bherim',
                TokenCode='936672'
)
file = Path ('/Users/mbheri/Desktop/aws-dev/session-token/session_token.rtf')

if file.is_file():
    os.remove('/Users/mbheri/Desktop/aws-dev/session-token/session_token.rtf')

del response['Credentials']['Expiration']

data =response['Credentials']

print (data)

with open('/Users/mbheri/Desktop/aws-dev/session-token/session_token.rtf','w+') as file:
    json.dump(data,file)





