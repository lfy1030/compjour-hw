import json
#opening the file
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())

#sorting the file
domestic_sorted = sorted(domestic_data)


#filter
for d in domestic_sorted:
	if(d[1] < 100):
		print("%s,%s" % (d[0], d[1]))