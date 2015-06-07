from bs4 import BeautifulSoup
import requests
response = requests.get('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.xml')
soup = BeautifulSoup(response.text)
votes = soup.findAll("vote")
counter = 0
for v in votes:
	r_str = str(v.findAll("result")[0])
	result = r_str[8:len(r_str)-9]
	if(result == "Rejected"):
		yeas = v.findAll("yeas")
		y_num  = int(str(yeas[0])[6:len(yeas)-8])
		nays = v.findAll("nays")
		n_num = int(str(nays[0])[6:len(nays)-8])
		if(n_num - y_num < 5):
			counter += 1

print(counter)