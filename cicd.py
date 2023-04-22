import boto3
import json

ec2 = boto3.resource('ec2',region_name='us-east-1')
for instance in ec2.instances.all():
     data = ["id: "+str(instance.id), "platform: "+str(instance.platform), "type: "+str(instance.instance_type),"ip: "+ str(instance.public_ip_address),"imageId: " +str(instance.image.id),"state: "+ str(instance.state),"tags: "+ str(instance.tags[0])]
     print(
          json.dumps(data,indent=4,sort_keys=True)
     )
