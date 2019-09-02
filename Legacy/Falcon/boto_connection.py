import boto3
import json



Credentials =      {
        "AccessKeyId": "ASIA6I6I7QA2X636UBFW",
        "SecretAccessKey": "QGOYkoahj1v8szcfoRKvmUkgssX+YM2vpAn1+g25",
        "SessionToken": "FQoGZXIvYXdzEJ7//////////wEaDBXsGS7CQCQO0dCD4iLvAR74H8TWVfDwMFAfLcPkj4Vgo85teocQjHMRe4zSeHkumTVvn0xhPQ8OSbN1IhQKoXxXp/BoKL0xWrLwuL11mzd8o+SVaVObOAtap0rXxSC10KbTF1DXUAsOc3RAWDp+KqPCYjBGT7UIGXSpT6Zd/TkcQHDu5K+jFITFfIhQrL1iDfBIHlBP8YNO/6f57pWp+sdkoXi5PIoWvBk/Zhx1i2wpDPtp4kmVMQwzYzoJC0XdI9Vh4CplVNajXN8BD5LuOp+X7V5u6hRyCdF/4MCJpjFK+NXYDr8z2hgYJWQyVhH9SmEG6SyPVT5hBkKxt50xKIiGwOQF",
        "Expiration": "2019-03-18T21:43:52Z"
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


