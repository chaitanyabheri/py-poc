import boto3
import os
import math

from boto_connection import s3_client
from boto_connection import s3_resource

s3_c = s3_client()
s3_r = s3_resource()



string1 = 'red'

string2 = 'yellow'

num1 = 1
num2 = 10

if num1 == num2:
    print ('numbers are equal')
elif num1 < num2:
    print ('num1 is less than num2')
else:
    print ('case did not fit')

if True:
    print ('Hello')


 callable(D)

buckets_metadata = s3_c.list_buckets()

print('\nBuckets Metadata---\n', buckets_metadata)

print('\n======= For Loop for s3 buckets ===========')

for header in buckets_metadata:
    print(header)

bucket_list=  [bucket['Name'] for bucket in buckets_metadata['Buckets']]

print('\nBucketList--\n', bucket_list)

print('\nBuckets--\n')
list = []
for bucket in buckets_metadata['Buckets']:

    #print (bucket['Name'])

    list.append(bucket['Name'])

print (list)


