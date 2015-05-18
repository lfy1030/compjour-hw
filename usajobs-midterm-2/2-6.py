import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def get_num_jobs(data):
	return data[1]

#sort list 
intl_sorted = sorted(intl_data, key = get_num_jobs, reverse=True)

#filter
count = 0
total_jobs = 0
for d in intl_sorted:
	if(count < 10):
		print("%s,%s" % (d[0], d[1]))
	else:
		total_jobs += d[1]
	count += 1

print("Others,%s" % total_jobs)