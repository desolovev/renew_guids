#!/usr/bin/env python3

import json
import re
import uuid
import os
import sys

def new_guids():
	try:
	    abs_path = sys.argv[1]
	except (NameError, IndexError):
	    raise NameError('specify abs path to the file')

	head_tail_abs_path = os.path.split(abs_path)
	head_abs_path = head_tail_abs_path[0]
	reg = r'[A-Za-z\d]{8}-[A-Za-z\d]{4}-[A-Za-z\d]{4}-[A-Za-z\d]{4}-[A-Za-z\d]{12}'

	with open(abs_path, 'r') as f:
		data = json.load(f)
		dstr = str(data)
		guid_orig = re.findall(reg, dstr)	
		for go in guid_orig:
			dstr = dstr.replace(go, str(uuid.uuid5(uuid.NAMESPACE_DNS, go)))
		new_file_name = re.search(reg, dstr)
		new_file_name = new_file_name.group(0)
		data = eval(dstr)
		new_file_abs_path = head_abs_path + '/' + new_file_name + '.json'
		
	if os.path.exists(abs_path):
		os.remove(abs_path)

	with open(new_file_abs_path, 'w', encoding='utf8') as f:
		json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)

	print(new_file_abs_path)

if __name__ == '__main__':
	new_guids()