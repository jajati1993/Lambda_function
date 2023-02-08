import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Define the tag key and value to search for
    tag_key = '<Tag Key>'
    tag_value = '<Tag Value>'

    # Search for instances with the specified tag key and value
    instances = ec2.describe_instances(Filters=[{'Name': 'tag:' + tag_key, 'Values': [tag_value]}])
# Get the instance IDs of the instances with the specified tag
    instance_ids = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]
    
    # Stop the instances
    if len(instance_ids) > 0:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped instances: {instance_ids}')
    else:
        print('No instances with the specified tag found.')