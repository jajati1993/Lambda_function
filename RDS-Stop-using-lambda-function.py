import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')
    rds.delete_db_instance(DBInstanceIdentifier='mydbinstance', 
                           SkipFinalSnapshot=True)
    return 'Deleted RDS instance successfully'