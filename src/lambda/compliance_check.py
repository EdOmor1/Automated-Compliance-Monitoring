import boto3

def lambda_handler(event, context):
    # Logic for compliance checks
    # Example: Check if S3 buckets have encryption enabled
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    non_compliant_buckets = []
    for bucket in response['Buckets']:
        bucket_encryption = s3.get_bucket_encryption(Bucket=bucket['Name'])
        if 'ServerSideEncryptionConfiguration' not in bucket_encryption:
            non_compliant_buckets.append(bucket['Name'])
    
    if non_compliant_buckets:
        notify_compliance_issue(non_compliant_buckets)
    else:
        print("All S3 buckets have encryption enabled.")

def notify_compliance_issue(non_compliant_buckets):
    # Logic to notify compliance issue via SNS
    sns = boto3.client('sns')
    topic_arn = 'YourSNSTopicARN'
    message = f"Non-compliant S3 buckets: {', '.join(non_compliant_buckets)}"
    
    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="Non-compliant S3 buckets found!"
    )
