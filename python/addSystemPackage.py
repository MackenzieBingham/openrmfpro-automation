import requests
from requests.structures import CaseInsensitiveDict

# Assign the API variables that are needed within the request's URL

APIname = "systempackage" # Constant for this particular API
AppKey = "applicationKey=degthatuploader"  # "degthatuploader is an example application key - replace it.
SystemKey = "aspireninetest"
data = "title=MyPackage&systemKey=mykeywithlowercaseletters&description=This+is+my+description&confidentiality=10&integrity=10&availability=10&fedrampLevel=10&packageType=10&systemType=Business+System&pocName=My+First+and+Last&pocPhone=8003456789 &pocEmail=info@soteriasoft.com&addUserToSystemPackage=true&acronym=TBD"

# Assign the request headers for this particular API
headers = CaseInsensitiveDict() # Does not change
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer s.xxxxxxxxxxxxxxxxxxxxxxx"
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Build the API URL in order to make the request

url = ("http://192.168.13.114:8080/api/external/"+APIname+"/?"+ AppKey)

# Make the API request
resp = requests.post(url, headers=headers, data=data)

# print to the screen the status code (i.e. 200, 400, 404, etc)
print(resp.status_code)
#print(resp.json)
print(resp.text)
