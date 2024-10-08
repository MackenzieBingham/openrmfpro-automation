#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html

url = myVariables.rootURL + "/api/external/approvedpps/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken

resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)

ppsTable = PrettyTable(["Title", "Key"])

for element in json_object:
    ppsTable.add_row([element['systemTitle'], element['systemKey']])    
# call to make this an HTML table and put into a new variable
htmlCode = ppsTable.get_html_string(attributes={"class":"table"}, format=True)

htmlCode = html.unescape(htmlCode)
# print out the HTML fully page
print(
"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>"""
)
print(htmlCode)
print(
"""\
</body>
</html>"""
)