import requests
import os
from subprocess import run
import json
import subprocess

def create_block(dataa):
	headers = {
		  'Content-type': 'application/json',
	}
	data = '{"data" :' + dataa + '}'
	response = requests.post('http://localhost:3001/mineBlock', headers=headers, data=data)
	
def create_peer():
	headers = {
		  'Content-type': 'application/json',
	}

	data = '{"peer" : "ws://localhost:6001"}'

	response = requests.post('http://localhost:3001/addPeer', headers=headers, data=data)
	
	
while(input("Press q (quit) to stop ") != 'q'):
	if(input("Add block? Press y ") == 'y'):
		create_block(input("data "))
	else:
		create_peer()
	if(input("Get blockchain? Press y ") == 'y'):
			#res = os.system('curl http://localhost:3001/blocks')
			output = subprocess.check_output(["curl", "http://localhost:3001/blocks"])
			output = json.loads(output.decode('utf-8'))
			print(json.dumps(output, sort_keys = True, indent = 4))
			
	if(input("Get peers? Press y ") == 'y'):
			output = subprocess.check_output(["curl", "http://localhost:3001/peers"])
			output = json.loads(output.decode('utf-8'))
			print(json.dumps(output, sort_keys = True, indent = 4))

			

