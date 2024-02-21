"""
Retrieve credentials password for given username from AWS SecretsManager
"""
import json
import boto3

def get_credentials(secret_id: str, region_name: str) -> str:

    client = boto3.client('secretsmanager', region_name=region_name)
    response = client.get_secret_value(SecretId=secret_id)
    secrets_value = json.loads(response['SecretString'])

    return secrets_value