import boto3
# boto3.client= low level em python
#boto3.resource= high level em python
s3api = boto3.client("s3", region_name="us-east-1")
bucket_name = "annaheloisa12042004"

s3api.create_bucket(Bucket = bucket_name)
print("bucket criado com sucesso...")