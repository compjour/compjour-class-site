import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
STATECODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
names = requests.get(STATECODES_URL).json()
## Everything from 1-8 on is the same:
thelist = []
thelist.append(["State", "Job Count"])
for name, abbrev in names.items():
    print("Getting: ", name)
    atts = {'CountrySubdivision': name, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    label = "US-" + abbrev
    thelist.append([label, jobcount])



chartcode = """
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'};

        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));

        chart.draw(datatable, options);
      }
    </script>


      <div class="container">
        <h1 style="text-align:center">Hello chart</h1>
        <div id="mychart"></div>
      </div>
  </body>
</html>
"""



htmlfile = open("1-9.html", "w")
htmlfile.write(chartcode % thelist)
htmlfile.close()
