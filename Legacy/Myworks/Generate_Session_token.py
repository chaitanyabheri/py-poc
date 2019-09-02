
Credentials ={
        "AccessKeyId": "ASIA6I6I7QA23QCPM772",
        "SecretAccessKey": "jGXCWFxVbkdfOzJCspUtprx/fkLN/D7PyAH1Gq3n",
        "SessionToken": "FQoGZXIvYXdzEAcaDKHCbynBX0/t7tBgaiLvAR9TT6/T0foIvp1SIFRcyuTZN2001Jal1x271L52QkeF2iScNDwNDsuNE4Z/HP0FIUYVMpjWQ90m1YUMN05MSevuxjJ4+6amLgT0VBSeAowELtPukxDRDjnLcMm5pQDCZFMgrTvwHiG2TrvEPzxv/aPdjMyIutjodEdmvUTwVrlWtBKQPGIr/6cZWnyj3iAUJZu2Aajw2EJeaLf70Z1f/WBfDUamhOIerhIbffGChsNwpX6YmOmlOpw5DvEon9qYc+QRl/ExHCUb5zg95MzygsB/BsF/s1lkJoS8MYiMdJXvEr4Nc/2OOxuOE5fOiz2kKKPgveIF",
        "Expiration": "2019-01-28T22:12:03Z"
              }

AWS_ACCESS_KEY_ID = Credentials['AccessKeyId']
AWS_SECRET_ACCEESS_KEY = Credentials['SecretAccessKey']
AWS_SESSION_TOKEN = Credentials['SessionToken']

print ('\n======== Session Credentials ==============')

print ('AccessKey\n\t',AWS_ACCESS_KEY_ID)
print('SecretKey\n\t',AWS_SECRET_ACCEESS_KEY)
print('SessionToken\n\t', AWS_SESSION_TOKEN)

print ('asd')