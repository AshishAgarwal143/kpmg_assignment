# Challenge #2
# We need to write code that will query the meta data of an instance within AWS or Azure or GCP
# and provide a json formatted output.
# The choice of language and implementation is up to you.
# Bonus Points
# The code allows for a particular data key to be retrieved individually
# Hints
# · Aws Documentation (https://docs.aws.amazon.com/)
# · Azure Documentation (https://docs.microsoft.com/en-us/azure/?product=featured)
# · Google Documentation (https://cloud.google.com/docs)

from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'bustling-tree-383805'  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'us-west4-b'  # TODO: Update placeholder value.

# Name of the instance resource to return.
instance = 'team3-r61c'  # TODO: Update placeholder value.

request = service.instances().get(project=project, zone=zone, instance=instance)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)

val = input("Enter the key you want to see the data for: ")
print("Inputed value:",val)

def checkKey(dic, key):
    if key in dic.keys():
        print("value =", dic[key])
    else:
        print("provided key not present")

checkKey(response,val)    
