from collections import OrderedDict
import csv
import requests
import json
import sys
import time

#sys.stdout = open('logfile.txt', 'w')

with open('listOfNumbers.txt', 'r') as f:
	mylist = f.read().splitlines()
	for num in mylist:
		url = 'https://URL/adminapi/resource/' + num
		print num
		print url
		ext = num + ".json"

		try:
			with open(ext, 'r') as input_file:
				input_data = input_file.read()
				d = json.loads(input_data.decode('utf-8'), object_pairs_hook=OrderedDict)
		except IOError:
			print "File does not Exist"

		headers = {"content-type": "application/json"}

		try:
			r = requests.put(url, json=d, headers=headers, auth=("USERNAME", "PASSWORD"))
			print requests.Response()
			print r.status_code
			print r.text
			#time.sleep(.300)

		except requests.exceptions.HTTPError as err:
			print err
			sys.ext(1)
