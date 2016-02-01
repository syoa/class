#!/usr/bin/python

import json
import yaml


my_list = range (8)
my_list.append('whatever')
my_list.append({})
my_list[-1]
my_list[-1]['ip_addr'] = '10.10.10.10'
my_list[-1]['cable'] = 'ethernet'
print my_list


#dump to yaml
with open("my_list.yml", "w") as f:
	f.write(yaml.dump(my_list, default_flow_style=False))

#reading from yaml

with open("my_list.yml") as f:
	new_list = yaml.load(f)
	print new_list

#dump to json

with open("my_list.json", "w") as f:
	json.dump(my_list, f)

#read from json

with open("my_list.json") as f:
	new_list1 = json.load(f)
	print new_list1
