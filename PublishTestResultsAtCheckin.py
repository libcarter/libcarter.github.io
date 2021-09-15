import csv
from datetime import datetime

#final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<current run time>]]

#C:\Users\Libby\Downloads\Ex_Files_Scripting_for_Testers\Ex_Files_Scripting_for_Testers\Exercise Files\02_02\end\readInData_solution.py

results_data = []
with open('TestResultsTable.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        results_data.append(row)

#column_chart_data = [["Test Date","Test Name","Pass","Fail"]]
#table_data = [["Test Date","Test Name","Pass","Fail"]]
column_chart_data = [["Test Name","Pass","Fail"]]
table_data = [["Test Name","Pass","Fail"]]
#timing_data looks like this 
#[['Test Name', 'Latest Run Time', 'Average Run Time'], ['Test 1', '193', '60'], ['Test 2', '79', '15']] 

tPass = 0
tFail = 0

#tail()
for row in results_data[-4:]: #this is the second row in the timing_data list
    #test_name = row[0] #this is the first element in the row, i.e. the zeroth element
    #if not row[1] or not row[2]: #this is referencing the 1st, 2nd element in the row
    #    continue                 #this is looking for empty rows/fields they will be skipped
    #current_run_time = float(row[1])
    #avg_run_time = float(row[2])
    #diff_from_avg = avg_run_time - current_run_time
    #tDate = row[2]
    tName = row[0]
    tResult = row[4]
    if tResult == "Pass":
      tPass = 1
      tFail = 0
    else:
      tPass = 0
      tFail = 1
    column_chart_data.append([tName,tPass,tFail])
    table_data.append([tName,tPass,tFail])

    

from string import Template

#//template is a string class for supporting $-substitutions
#//function created to draw the chart..paste data into function
#//substitute hard coded data (sub header $labels and data $data)

html_string = Template("""<html> 
                                 

<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {   
      var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.
        var options = {
        title: '$title'
      };


    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data, options);
   
  }
</script>
</head>
<body>
<div id="chart_div" style="width:800; height:600">
</div>
</body>
</html>""")

chart_heading_str = 'Test Results as of:    ' + datetime.now().strftime("%m/%d/%Y %H:%M")


chart_data_str = ''                   #create a string
for row in column_chart_data[1:]:     #using the data file we created earlier
    chart_data_str += '%s,\n'%row     #%s will substitue in the string, \n is a new line
#insert each row into the string
#print(column_chart_data[0])
#print(chart_data_str)

completed_html = html_string.substitute(title=chart_heading_str,labels=column_chart_data[0],
data=chart_data_str)
#substitute the data we have into the string with labels and data

with open('column_chart.html','w') as f:  #w is "write"
    f.write(completed_html)


