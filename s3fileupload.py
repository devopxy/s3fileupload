import boto3
from botocore.exceptions import NoCredentialsError

#In production a better secret management is required
Access_key='ChangeThis:SandboxAccessKey'
secret_key='ChangeThis:SandboxSecretKey'

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=Access_key,
                      aws_secret_access_key=secret_key)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

#File path can be passed through a  config file or commandline parameter
uploaded = upload_to_aws('ChangeThis:File2BeUploaded', 'sandboxbucket', 'second_file')
