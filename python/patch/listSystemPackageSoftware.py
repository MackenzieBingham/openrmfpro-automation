# list software from the system package
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/software/?applicationKey={applicationKey}&devicename={hostname}
# ex: python3 listSystemPackageSoftware.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/software/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))