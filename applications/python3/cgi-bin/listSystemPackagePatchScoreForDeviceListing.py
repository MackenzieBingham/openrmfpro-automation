#!/usr/bin/env python3
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from prettytable import PrettyTable
import myVariables
import html
import os
import urllib.parse

## get the query string. this gets passed to cgi scripts as the environment
## variable QUERY_STRING
query_string = os.environ['QUERY_STRING']

## convert the query string to a dictionary
arguments = urllib.parse.parse_qs(query_string)

url = myVariables.rootURL + "/api/external/systempackage/" + str(arguments["systemKey"][0]) + "/patchscore/devices/?applicationKey=" + myVariables.applicationKey

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + myVariables.bearerToken
# call the API
resp = requests.get(url, headers=headers)
json_object = json.loads(resp.text)
# make into a PrettyTable
deviceTable = PrettyTable(["Host Name", "Critical Open", "High Open", "Medium Open", "Low Open", "Info Open", "Version"])
# Just get the fields want
for element in json_object:  # iterate on each element of the list
    deviceTable.add_row([element['hostname'], element['totalCriticalOpen'],  element['totalHighOpen'],  element['totalMediumOpen'], element['totalLowOpen'], element['totalInfoOpen'], element['version']])
# call to make this an HTML table and put into a new variable
htmlCode = deviceTable.get_html_string(attributes={"class":"table"}, format=True)

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