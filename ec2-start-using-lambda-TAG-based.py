import boto3

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    instances = ec2.describe_instances(Filters=[{"Name": "tag:TagName", "Values": ["TagValue"]}])
    instance_ids = [instance["InstanceId"] for instance in instances["Reservations"][0]["Instances"]]
    ec2.start_instances(InstanceIds=instance_ids)