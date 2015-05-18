import requests
# same code from problem 5
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
STATECODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
states = [['California', 'US-CA'], ['Florida','US-FL'], ['Maryland','MD'], ['New York', 'US-NY']]
list_of_states = []
list_of_states.append(["State", "Job Count"])
for s in states:
    atts = {'CountrySubdivision': s[0], 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    num_jobs = int(data['TotalJobs'])
    list_of_states.append([s[1],num_jobs])

htmlcode = """
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


htmlfile = open("1-8.html", "w")
htmlfile.write(htmlcode % list_of_states)
htmlfile.close()