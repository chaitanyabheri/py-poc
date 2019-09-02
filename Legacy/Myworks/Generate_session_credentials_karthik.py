import boto3
from boto.sts import STSConnection
from boto.s3.connection import S3Connection
from boto3 import client


# Prompt for MFA time-based one-time password (TOTP)
mfa_TOTP = raw_input("Enter the MFA code: ")

# The calls to AWS STS GetSessionToken must be signed with the access key ID and secret
# access key of an IAM user. The credentials can be in environment variables or in
# a configuration file and will be discovered automatically
# by the STSConnection() function. For more information, see the Python SDK
# documentation: http://boto.readthedocs.org/en/latest/boto_config_tut.html

sts_connection = STSConnection(aws_access_key_id="AKIAJEGDPRSEOJMV46ZA", aws_secret_access_key="RHrGRGJrpb8mWAq6zRXTwmX1TmvjfQZTOevPatg9")

# Use the appropriate device ID (serial number for hardware device or ARN for virtual device).
# Replace ACCOUNT-NUMBER-WITHOUT-HYPHENS and MFA-DEVICE-ID with appropriate values.

tempCredentials = sts_connection.get_session_token(
    duration=2800,
    mfa_serial_number="arn:aws:iam::186502235371:mfa/sthathamsetty",
    mfa_token=mfa_TOTP
)

print (tempCredentials.access_key)
print (tempCredentials.secret_key)
print ("\n"+tempCredentials.session_token)

sts_connection1 = STSConnection(aws_access_key_id=tempCredentials.access_key, aws_secret_access_key=tempCredentials.secret_key, security_token=tempCredentials.session_token)


# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumedRoleObject = sts_connection1.assume_role(
    role_arn="arn:aws:iam::981284651061:role/CredibilityDataDevPowerUserCrossAccountSignin",
    role_session_name="session"
)

# From the response that contains the assumed role, get the temporary
# credentials that can be used to make subsequent API calls
#credentials = assumedRoleObject


s3_connection = S3Connection(
    aws_access_key_id=assumedRoleObject.credentials.access_key,
    aws_secret_access_key=assumedRoleObject.credentials.secret_key,
    security_token=assumedRoleObject.credentials.session_token,
    is_secure=False
)
bucket = s3_connection.get_bucket("capzones-dev")
for key in bucket.list():
    print (key.name.encode('utf-8'))


print (assumedRoleObject.credentials.access_key+"\n")
print (assumedRoleObject.credentials.secret_key+"\n")
print (assumedRoleObject.credentials.session_token)