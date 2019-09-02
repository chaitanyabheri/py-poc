import pysftp


myHostname = "ftp.blackline.com"
myUsername = "Dandb"
myPassword = "d18JLJjk"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print
    "Connection succesfully stablished ... "

    # Switch to a remote directory
    sftp.cwd('/PROD/PHX_Extract')

    # Obtain structure of the remote directory '/var/www/vhosts'
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:
        print  ( attr.filename, attr)

# connection closed automatically at the end of the with-block



