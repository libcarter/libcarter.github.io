
import requests
from datetime import datetime
import csv

# go to your favorite URL
# and Get ????
# every day at 8:00 AM Pacific
# capture the results 
# python "C:\Users\Libby\Desktop\Automation Testing\SimpleGet.py"

url = "http://api.nasa.gov/neo/rest/v1/feed?start_date=2015-13-07&end_date=2015-09-08&api_key=DEMO_KEY"

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
    result = "Fail"
    reason = "There was an error but the API returned status 200"
    note = "none"
    expected = "Verify api returned status 200 but no data"
    if dataList[0] == "activity":
      note = resultsToCheck["activity"]
      result = "Fail"
      reason = "The API returned status of 200 as expected"
      expected = "Verify api returned status 200 but no data"
else:
  result = "Pass"
  reason = "The API did not return status of 200" 
  note = "none"
  expected = "Verify api returned status 200 but no data"
  


#==== TEST_03 Verify api returned a status of 400
testname = "Test 03"
testTime = datetime.now().strftime("%H:%M")
testDt = datetime.now().strftime("%m/%d/%y")
TestResultsTable = [testname, expected, testDt, testTime, result, status, reason, note]
#print(TestResultsDetails)

with open('TestResultsTable.csv', 'a', newline='') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(TestResultsTable)
  







 # with open('eggs.csv', 'w', newline='') as csvfile:
    # spamwriter = csv.writer(csvfile, delimiter=' ',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# timing_data = []
# with open('TestTimingData.csv') as csv_file:
#     file_reader = csv.reader(csv_file)
#     for row in file_reader:
#         timing_data.append(row)



