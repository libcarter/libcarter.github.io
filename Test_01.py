
import requests
from datetime import datetime
import csv

# go to your favorite URL
# and Get something
# every day at 8:00 AM Pacific
# capture result
# python "C:\Users\Libby\Desktop\Automation Testing\Test_01.py"


url = "http://www.boredapi.com/api/activity?type=relaxation"


# GET
response = requests.get(url)
status = response.status_code
resultsToCheck = (response.json())
howLong = response.elapsed
TestResultsDetails = []
dataList = []


for each_key in resultsToCheck.keys():
  dataList.append(each_key)


if status == 200:
  if dataList[0] == "error":
    result = "Pass"
    reason = "There was an error but the API returned status 200"
    note = "none"
    expected = "Verify API Returned status 200 with valid data"
  elif dataList[0] == "activity":
    note = resultsToCheck["activity"]
    result = "Pass"
    reason = "The API returned status of 200 as expected"
    expected = "Verify API Returned status 200 with valid data"
else:
  result = "Fail"
  reason = "The API did not return status of 200" 
  note = "none"
  expected = "Verify API Returned status 200 with valid data"
  


#==== TEST_01 Verify API Returned status 200 with valid data
testname = "Test 01"
testTime = datetime.now().strftime("%H:%M")
testDt = datetime.now().strftime("%m/%d/%y")
TestResultsTable = [testname, expected, testDt, testTime, result, status, reason, note]



with open('TestResultsTable.csv', 'a', newline='') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(TestResultsTable)
  
  



