import json
from operator import itemgetter
with open("sample-geochart-2.html") as f:
    htmlstr = f.read()
with open("data-hold/intl-jobcount.json") as f:
    data = json.loads(f.read())

sorteddata = sorted(data, key = itemgetter(1), reverse = True)

#filter out countries with less than 1 jobs
filtereddata = []
for d in sorteddata:
	if(d[1] >= 1):
		filtereddata.append(d)

# Chart all countries
chartdata = [['Country', 'Jobs']]
chartdata.extend(filtereddata)

# include all the countries
tablerows = []
for d in filtereddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)
#
with open("2-8.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(chartdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)