import boto3
import json

credential={}

with open('/Users/mbheri/Desktop/aws-dev/session-token/session_token.rtf' ,'r') as file:
    credential =json.load(file)
access_key =credential['AccessKeyId']
secret_key =credential['SecretAccessKey']
session_token =credential['SessionToken']

sts_client = boto3.client('sts',
                          aws_access_key_id = access_key,
                          aws_secret_access_key = secret_key,
                          aws_session_token=session_token,
                          region_name = 'us-west-2'
                          )



assumedRoleObject = sts_client.assume_role(
    RoleArn="arn:aws:iam::981284651061:role/CredibilityDataDevPowerUserCrossAccountSignin",
    RoleSessionName="Session",
    DurationSeconds=3600,
    TokenCode='444178',
    SerialNumber='arn:aws:iam::186502235371:mfa/bherim'
)

del assumedRoleObject['Credentials']['Expiration']

with open ('/Users/mbheri/Desktop/aws-dev/session-token/session_token.rtf' ,'w+') as f:
    json.dump(assumedRoleObject['Credentials'] ,f)






