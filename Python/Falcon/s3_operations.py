import boto3
import os
from pathlib import Path

from boto_connection import s3_client
from boto_connection import s3_resource



print ('\n======= Print Operations ===========\n')
s3_c = s3_client()
s3_r = s3_resource()

#list buckets

rslt = s3_c.list_buckets()


buckets = [bucket['Name'] for bucket in rslt['Buckets']]

print('\nBuckets list -\n', buckets)


#Create bucket
bucket_name = 'dbcc-inbound'


class Solution:
    @staticmethod

    def create_bucket(bucket_name):
       s3_c.create_bucket(Bucket=bucket_name)

    def get_s3_keys(bucket_name):
        keys = []
        s3_c.list_objects_v2(Bucket=bucket_name)
        return  (keys)

    def upload_small_file(self):
        file_path = os.path.dirname(__file__) + '/DAILY_PAYDR_201903090748.TXT'
        return s3_client().upload_file(file_path, bucket_name, 'DAILY_PAYDR_201903090748.TXT')



rslt = s3_c.list_buckets()


buckets = [bucket['Name'] for bucket in rslt['Buckets']]


if bucket_name in buckets:
    print ('Bucket exits')
else:
    print('Bucket does not exists')
    Solution.create_bucket(bucket_name)
    print('Bucket Created')


res =  s3_c.list_objects_v2(Bucket=bucket_name)

for obj in res['Contents']:
    print ('Bucket objects -', obj['Key'])

#file_path = os.path.dirname(__file__) + '/test.PNG'
#print(file_path)
#s3_c.upload_file(file_path, bucket_name, 'DAILY_PAYDR_201903090748.TXT')


data_folder = Path("ae01-win-ftp/DataFeeds_Dworks_1/Inbound/DailyPaydexScore/")
#file_to_open = data_folder / "DAILY_PAYDR_201903090748.TXT"

#f = open(file_to_open)

#print(f.read())

os.listdir("//ae01-win-ftp/DataFeeds_Dworks_1/")


#open("smb://ae01-win-ftp/DataFeeds_Dworks_1/Inbound/DailyPaydexScore/DAILY_PAYDR_201903090748.TXT", "r")

