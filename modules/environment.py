#!/usr/bin/python

import os

def run(**args):
	print "[*] in module environmnent"
	return str(os.environ)