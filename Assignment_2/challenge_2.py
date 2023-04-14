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

import requests
import json

url = "http://localhost/metadata/myservices"
headers = {'Metadata': 'true'}
response = requests.get(url, headers=headers)
metadata = response.json()

json_output = json.dumps(metadata, indent=4)
print(json_output)
