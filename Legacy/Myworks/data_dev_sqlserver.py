import json
import pandas
import boto3
import io
import pyodbc
import pyspark

with open('/Users/mbheri/Desktop/aws-dev/session-token/session_token.rtf','r') as file:
    credentials=json.load(file)
AWS_ACCESS_KEY_ID=credentials['AccessKeyId']
AWS_SECRET_ACCEESS_KEY=credentials['SecretAccessKey']
AWS_SESSION_TOKEN=credentials['SessionToken']


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


data = s3_client().get_object(Bucket='dwstage-source-dev',Key='alerts365short/year=2018/dt=20180103/Alerts365Short_20180103.txt')

df = pandas.read_csv(io.BytesIO(data['Body'].read()))


print(df.head(2))

duns = df["Duns"]

#print(duns[2])

#sql=pyodbc.connect('DRIVER=/usr/local/lib/libtdsodbc.so;SERVER=test-wayne.cqvd0gbl7rg8.us-west-2.rds.amazonaws.com,1433;\
#DATABASE=test;UID=sa;PWD=sa_1234567')

conn=pyodbc.connect('DRIVER=/usr/local/lib/libtdsodbc.so;SERVER=ae-sql01-qa,1433;\
DATABASE=DWStage;UID=CREDIBILITY\mbheri;PWD=Chaitubharu@1904')

cursor = conn.cursor()
cursor.execute('select top 10 * from dwstage.datafeed.releaseconfig')
query = 'select top 10 * from dwstage.datafeed.releaseConfig'

#df = pandas.read_sql_query(query, conn)

#for row in cursor:
#   print(row)
#print(df.head(3))

#

res = cursor.execute('select ReleaseConfigId, DataFeedtype, IsActive from dwstage.datafeed.ReleaseConfig order by 1')

#Active data feedtypes
d = {}

for rec in res:
    #print(rec)

    if rec[2]==True:
       # print('Active Feeds: ', rec[1])
        if 'Active Feeds' not in d.keys():
            d['Active Feeds']=[rec[1]]
        else:
            d['Active Feeds'].append(rec[1])
    else:
        if 'InActive Feeds' not in d.keys():
            d['InActive Feeds']=[rec[1]]
        else:
            d['InActive Feeds'].append(rec[1])

print(d)
print(d['Active Feeds'])
print(d['InActive Feeds'])
'''

res = cursor.execute("select ProcessLogID, SourceSystem, DataFeedType, StageLoadStatusID, SourceName from Datafeed.S3Log ")

for rec in res:
    print(rec)

cursor.execute("INSERT INTO Datafeed.S3Log"
               "(SourceSystem, DataFeedType, StageLoadStatusID, SourceName)"
               "SELECT SourceSystem = 's3', DataFeedType = 'AlertsS3Test', StageLoadStatusID = 1, SourceName = 'test.file'"
               "")

res = cursor.execute("select ProcessLogID, SourceSystem, DataFeedType, StageLoadStatusID, SourceName from Datafeed.S3Log ")

conn.commit()




print(df.head(2))


AlertSQL = "select top 10 * from dwstage.DnbEvents.[tblAlerts365_poc]"

df = pandas.read_sql(AlertSQL, conn)

print(df)

for index,row in df.iterrows():
    if index <2:
        cursor.execute("INSERT INTO dwstage.DnbEvents.[tblAlerts365_poc] ([DunsNumber],[CreditRiskScore], [CompositeCreditRating], [PaydexScore], [SourceID], [DataFeedEffectiveDate])"
                   "values (?,?,?,?,?,?)",long(str(row[0]),row[1],row[2],row[3],1,20190401)

    conn.commit()

'''
