import boto3
import json



Credentials =  {
        "AccessKeyId": "ASIA6I6I7QA2V64QQ4GI",
        "SecretAccessKey": "F4QvhFcptsdbe1bvZFXXC0cZLp+l3CU7Bzv7U4D8",
        "SessionToken": "FQoGZXIvYXdzELX//////////wEaDPnBp1CI8Klyj7EP0iLvAVuLM9h6njoZwwbuQg1eA7wAjV5tRwZDLyrYMmAkCbZw+XhirqXCJe+l8zQVgHMghuMAUQx1WVQHF+y/rUehS+dJ/v9nbCrJWwCnOcVQrS6RQmm3dj2Xe/yZHB3xqDzARRpiRzBvJ3hSH/1u+lL/evfmr5VrpcrIElSN1PwXjN7aaRB5azLPz4qCGr3puNlRrJbCY5cy9OJbKFle8zdAHyXe5nsKm6jX7VUQncOv0Z5xYghO+Lhd54bRuzXFU89R9DGMslDIMNKe87iTnTeqBgCnHYemrrFTaBUH46ntfVqS12YP36P8GgAjM2KAQtgEKO2wnOMF",
        "Expiration": "2019-02-15T20:52:13Z"
    }

AWS_ACCESS_KEY_ID = Credentials['AccessKeyId']
AWS_SECRET_ACCEESS_KEY = Credentials['SecretAccessKey']
AWS_SESSION_TOKEN = Credentials['SessionToken']

print ('\n======== Session Credentials ==============')

print ('AccessKey\n\t',AWS_ACCESS_KEY_ID)
print('SecretKey\n\t',AWS_SECRET_ACCEESS_KEY)
print('SessionToken\n\t', AWS_SESSION_TOKEN)


def s3_client():
    ''' creates s3 connection using boto3'''
    return boto3.client('s3',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCEESS_KEY,
                        aws_session_token = AWS_SESSION_TOKEN
                        )


def s3_resource():
    return boto3.resource('s3',
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCEESS_KEY,
                          aws_session_token=AWS_SESSION_TOKEN
                        )


def sns_client():
    return boto3.client('sns',
                        aws_access_key_id = AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = AWS_SECRET_ACCEESS_KEY,
                        aws_session_token = AWS_SESSION_TOKEN
                        )

def sqs_client():
    return boto3.client('sqs',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCEESS_KEY,
                        aws_session_token=AWS_SESSION_TOKEN
                        )

def athena_client():
    return  boto3.client('athena',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCEESS_KEY,
                        aws_session_token=AWS_SESSION_TOKEN
                        )


