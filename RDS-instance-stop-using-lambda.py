import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')

    instances = rds.describe_db_instances()
    for instance in instances['DBInstances']:
        tags = rds.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])
        for tag in tags['TagList']:
            if tag['Key'] == 'AutoStop' and tag['Value'] == 'True':
                rds.stop_db_instance(DBInstanceIdentifier=instance['DBInstanceIdentifier'])
                print(f"Stopped RDS instance {instance['DBInstanceIdentifier']}")