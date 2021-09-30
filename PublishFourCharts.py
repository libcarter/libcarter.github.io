import csv
from datetime import datetime
from datetime import timedelta
import pytz
timezone = pytz.timezone("America/Los_Angeles")


results_data = []
with open('TestResultsTable.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        results_data.append(row)

column_chart_data1 = [["Test Name","Pass","Fail"]]
table_data1 = [["Test Name","Pass","Fail"]]
column_chart_data2 = [["Test Results","Pass/Fail"]]
table_data2 = [["Test Results","Pass/Fail"]]
column_chart_data3 = []
#table_data3 = [["Date","Last 5 Results - Things To Do For Boredom"]]
column_chart_data4 = [["Date","Run Time"]]
table_data4 = [["Date","Run Time"]]

tPass = 0
tFail = 0

#CHART 1
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
    column_chart_data1.append([tName,tPass,tFail])
    table_data1.append([tName,tPass,tFail])
    

#CHART 2
tPassTest2 = 0
tFailTest2 = 0
totalPass = 0
totalFail = 0
temp_data1 = []
temp_data2 = []
for row in results_data[-16:]: #this is the second row in the timing_data list
    #test_name = row[0] #this is the first element in the row, i.e. the zeroth element
    #if not row[1] or not row[2]: #this is referencing the 1st, 2nd element in the row
    #    continue                 #this is looking for empty rows/fields they will be skipped
    #current_run_time = float(row[1])
    #avg_run_time = float(row[2])
    #diff_from_avg = avg_run_time - current_run_time
    #tDate = row[2]
    #tName = row[0]
    tResult = row[4]
    if tResult == "Pass":
      tPassTest2 = 1
      tFailTest2 = 0
      totalPass = totalPass + tPassTest2
      tNameP = "Pass"
      temp_data1 = ([tNameP,totalPass])
    else:
      tPassTest2 = 0
      tFailTest2 = 1 
      totalFail = totalFail + tFailTest2
      tNameF = "Fail"
      temp_data2 = ([tNameF,totalFail])
    

#[item[-1] for item in my_list]
for row in temp_data1[-1:]:
    column_chart_data2.append([tNameP,totalPass])

for row in temp_data2[-1:]:
    column_chart_data2.append([tNameF,totalFail])
    


#CHART 3
#tPassTest3 = 0
#tFailTest3 = 0


for row in results_data[-20:]: #this is the second row in the timing_data list
    #test_name = row[0] #this is the first element in the row, i.e. the zeroth element
    #if not row[1] or not row[2]: #this is referencing the 1st, 2nd element in the row
    #    continue                 #this is looking for empty rows/fields they will be skipped
    #current_run_time = float(row[1])
    #avg_run_time = float(row[2])
    #diff_from_avg = avg_run_time - current_run_time
    #tDate = row[2]
    tName = row[0]
    tDate = row[2]
    tResult = row[4]
    tBored = row[7]
    if tName == "Test 01":
      if tResult == "Pass":
         
         tSuggest = tBored
    else:
      continue

    column_chart_data3.append([tDate,tSuggest])
    #table_data3.append([tDate,tSuggest])

    #print(column_chart_data3)


#CHART 4
temp_table = []
runTime = 0
for row in results_data[-40:]: #this is the second row in the timing_data list
    #test_name = row[0] #this is the first element in the row, i.e. the zeroth element
    #if not row[1] or not row[2]: #this is referencing the 1st, 2nd element in the row
    #    continue                 #this is looking for empty rows/fields they will be skipped
    #current_run_time = float(row[1])
    #avg_run_time = float(row[2])
    #diff_from_avg = avg_run_time - current_run_time
    #tDate = row[2]
    tName = row[0]
    tDate = row[2]
    tResult = row[4]
    if tName == "Test 04":
      if tResult == "Pass":
        runTime = float(row[7])
      else: continue 
    else:
         continue
      
    column_chart_data4.append([tDate,runTime])
    table_data4.append([tDate,runTime])


from string import Template

#//template is a string class for supporting $-substitutions
#//function created to draw the chart..paste data into function
#//substitute hard coded data (sub header $labels and data $data)

html_string1 = Template("""<html> 
                                 

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


    var chart = new google.visualization.BarChart(document.getElementById('nw'));
      chart.draw(data, options);
   
  }
</script>
</head>
<body>
<style type="text/css">
html, body{width: 100%; height: 100%; padding: 2; margin: 0}
div{position: absolute; padding: 1px}
#nw{top: 0; left: 0; right: 50%; bottom: 50%}

</style>
<div id="nw" >
</div>
</body>
</html>""")

html_string2 = Template("""<html> 
                                 

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


    var chart = new google.visualization.PieChart(document.getElementById('ne'));
      chart.draw(data, options);
   
  }
</script>
</head>
<body>
<style type="text/css">
html, body{width: 100%; height: 100%; padding: 2; margin: 0}
div{position: absolute; padding: 1px}

#ne{top: 0; left: 50%; right: 0; bottom: 50%}

</style>
<div id="ne" >
</div>
</body>
</html>""")

html_string3 = Template("""<html> 
                                 

<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {'packages':['table']});
  google.charts.setOnLoadCallback(drawTable);
  function drawTable () {   
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Date');
      data.addColumn('string','Last 5 Results - Things To Do For Boredom');
      data.addRows([
      $data
      ]); 
  var table = new google.visualization.Table(document.getElementById('sw'));
  
  table.draw(data,{showRowNumber: true, width: '100%', height: '100%'});
    }
</script>
</head>
<body>
<style type="text/css">
html, body{width: 100%; height: 100%; padding: 2; margin: 0}
div{position: absolute; padding: 1px}

#sw{top: 53%; left: 3%; right: 49%; bottom: 0}

</style>
<div id="sw" >
</div>
</body>
</html>""")

html_string4 = Template("""<html> 
                                 

<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {   
      var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ]); // 'false' means that the first row contains labels, not data.
        var options = {
        title: '$title'
      };


    var chart = new google.visualization.LineChart(document.getElementById('se'));
      chart.draw(data, options);
   
  }
</script>
</head>
<body>
<style type="text/css">
html, body{width: 100%; height: 100%; padding: 2; margin: 0}
div{position: absolute; padding: 1px}

#se{ top: 50%; left: 50%; right: 0; bottom: 0}
</style>
<div id="se">
</div>
</body>
</html>""")

chart_heading_str1 = 'Last Test Results as of:    ' + datetime.now(timezone).strftime("%m/%d/%Y %H:%M")

chart_data_str1 = ''                   #create a string
for row in column_chart_data1[1:]:     #using the data file we created earlier
    chart_data_str1 += '%s,\n'%row     #%s will substitue in the string, \n is a new line

chart_heading_str2 = 'Combined Results Last 4 Test Runs as of:    ' + datetime.now(timezone).strftime("%m/%d/%Y %H:%M")

chart_data_str2 = ''                   #create a string
for row in column_chart_data2[1:]:     #using the data file we created earlier
    chart_data_str2 += '%s,\n'%row     #%s will substitue in the string, \n is a new line

#chart_heading_str3 = 'Chart #3 Results as of:    ' + datetime.now(timezone).strftime("%m/%d/%Y %H:%M")

chart_data_str3 = ''                   #create a string
for row in column_chart_data3[0:]:     #using the data file we created earlier
    chart_data_str3 += '%s,\n'%row     #%s will substitue in the string, \n is a new line

chart_heading_str4 = 'API Performance - Last 10 Results as of:    ' + datetime.now(timezone).strftime("%m/%d/%Y %H:%M")

chart_data_str4 = ''                   #create a string
for row in column_chart_data4[1:]:     #using the data file we created earlier
    chart_data_str4 += '%s,\n'%row     #%s will substitue in the string, \n is a new line

completed_html1 = html_string1.substitute(title=chart_heading_str1,labels=column_chart_data1[0],
data=chart_data_str1)

completed_html2 = html_string2.substitute(title=chart_heading_str2,labels=column_chart_data2[0],
data=chart_data_str2)

completed_html3 = html_string3.substitute(data=chart_data_str3)

completed_html4 = html_string4.substitute(title=chart_heading_str4,labels=column_chart_data4[0],
data=chart_data_str4)


#substitute the data we have into the string with labels and data

with open('FourCharts.html','w') as f:  #w is "write"
    f.write(completed_html1)
    f.write(completed_html2)
    f.write(completed_html3)
    f.write(completed_html4)

