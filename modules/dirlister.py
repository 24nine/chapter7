#!/usr/bin/python

import os

def run(**args):
	print "[*] in module dirlister"
	files = os.listdir(".")

	return str(files)


