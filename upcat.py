import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('upcatpassers.csv', 'w'))
f.writerow(['Name', 'Campus', 'Course'])

for i in range(259):
	if i < 9:
		url = requests.get('https://upcat.up.edu.ph/results/page-00'+str(i+1)+'.html')
	elif i < 99:
		url = requests.get('https://upcat.up.edu.ph/results/page-0'+str(i+1)+'.html')
	else: 
		url = requests.get('https://upcat.up.edu.ph/results/page-'+str(i+1)+'.html')
	

	soup = BeautifulSoup(url.text, 'html.parser')

	textlist = soup.find(class_='table table-bordered table-hover')
	listitems = textlist.find_all('span')

	for x in range(0, len(listitems), 3):
		name = listitems[x].contents[0]
		campus = listitems[x+1].contents[0]
		course = listitems[x+2].contents[0]

		f.writerow([name, campus, course])
