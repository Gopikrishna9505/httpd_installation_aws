import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
sg_det = ec2.describe_instances(
  Filters =[
   {
    #'Name':"private-ip-address",
    #'Values':['192.168.12.173']
    'Name':'tag:Project',
    'Values' : ['data-mask-02']
   },
  ],
)
group_id = sg_det['Reservations'][0]['Instances'][0]['SecurityGroups'][0]['GroupId']

data = ec2.authorize_security_group_ingress(
   GroupID = group_id,
   IpPermisions=[
       { 'IpProtocol': 'tcp',
         'FromPort': 80,
         'ToPort': 80,
         'IpRanges': [{'CidrIp': '103.109.144.46'}]},
print("ingress rule is set to ", data)

