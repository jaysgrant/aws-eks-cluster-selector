import boto3
from botocore.exceptions import ClientError


def main():
    try:
        region = 'us-east-1'
        eks = boto3.client('eks', region)
        eks.list_clusters()
    except ClientError as e:
        print(e)


if __name__ == "__main__":
    main()
