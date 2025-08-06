import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    bucket_name = 'lambda-access-bucket-dm'
    file_key = 'lambda-test.txt'
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        print("File content:", file_content)
        
        return {
            'statusCode': 200,
            'body': file_content
        }
        
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
