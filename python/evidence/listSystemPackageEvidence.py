# list the system package Evidence records, all 4 types
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/evidence/?applicationKey={applicationKey}&general=true&checklist=true&statement=true&poam=true
# ex: python3 listSystemPackageEvidence.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/evidence/?general=true&checklist=true&statement=true&poam=true&applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))