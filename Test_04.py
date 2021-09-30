
import requests
from datetime import datetime
import csv

# go to your favorite URL
# and simple GET
# every day at 8:00 AM Pacific
# collect results 
# python "C:\Users\Libby\Desktop\Automation Testing\Test 04.py"

url = "https://www.boredapi.com/api/activity?type=relaxation"

# GET
startTime = datetime.now()
response = requests.get(url)
status = response.status_code
resultsToCheck = (response.json())
howLong = response.elapsed
TestResultsDetails = []
dataList = []
endTime = datetime.now()
timeElapsed = (endTime - startTime)




for each_key in resultsToCheck.keys():
  dataList.append(each_key)



if status == 200:
  if dataList[0] == "error":
    result = "Pass"
    reason = "There was an error but the API returned status 200"
    note = "none"
    expected = "There was an error but api returned results in less than 3 seconds"
  elif dataList[0] == "activity":
    if timeElapsed.seconds <= 3:   
      #note = resultsToCheck["activity"]
      note = timeElapsed.microseconds / 1000000
      result = "Pass"
      reason = "The API returned status of 200 in less than 3 seconds"
      expected = "Verify api returned status 200 in less than 3 seconds"
    else:
      result = "Fail"
      reason = "The API took longer than 3 seconds to return data" 
      note = "none"
      expected = "Verify api returned status 200 but no data in less than 3 seconds"
else:
  result = "Fail"
  reason = "The API did not return status of 200" 
  note = "none"
  expected = "Verify api returned status 200 but no data in less than 3 seconds"
  


#==== TEST_04 Verify api returned valid result, status 200 in less than 3 seconds
testname = "Test 04"
testTime = datetime.now().strftime("%H:%M")
testDt = datetime.now().strftime("%m/%d/%y")
TestResultsTable = [testname, expected, testDt, testTime, result, status, reason, note]
#print(TestResultsDetails)

with open('TestResultsTable.csv', 'a', newline='') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(TestResultsTable)
  



