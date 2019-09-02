import boto3

from boto_connection import s3_client
from boto_connection import s3_resource



print ('\n======= Print Operations ===========\n')
s3_c = s3_client()
s3_r = s3_resource()

#list buckets

rslt = s3_c.list_buckets()

print (rslt)

print ('\nMetadata--\n', rslt['ResponseMetadata'])

print('\nBuckets--\n',rslt['Buckets'])


buckets = [bucket['Name'] for bucket in rslt['Buckets']]


print(buckets)

