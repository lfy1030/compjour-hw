import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def get_num_jobs(data):
	return data[1]

#sort list 
intl_sorted = sorted(intl_data, key = get_num_jobs, reverse=True)
print(intl_sorted)

#filter
for d in intl_sorted:
	if(d[1] > 10):
		print("%s,%s" % (d[0], d[1]))