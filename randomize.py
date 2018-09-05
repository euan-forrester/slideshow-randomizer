#!/usr/bin/env python3

# Take a directory full of files and make a copy with the files named randomly. 
# Used to randomize a set of JPEGs for a slideshow.

import sys
from os import listdir, path, makedirs
from os.path import isfile, join
from shutil import copyfile, rmtree
from random import randint

if (len(sys.argv) < 3):
	print("Usage: randomize.py <input dir> <output dir>")
	sys.exit(0)

input_path = sys.argv[1]
output_path = sys.argv[2]

# Clean up the output directory so we can run this multiple times
try:
	rmtree(output_path)
except OSError as e: 
	pass

makedirs(output_path)

filenames = [f for f in listdir(input_path) if isfile(join(input_path, f))]

max_number = len(filenames) * 1000 # Leave some room for overlaps
num_digits = len(str(max_number))

for filename in filenames:
	old_filename, file_extension = path.splitext(filename)
	
	file_exists = True
	while (file_exists):
		new_filename = output_path + str(randint(0, max_number)).zfill(num_digits) + file_extension
		file_exists = path.exists(new_filename)

	copyfile(input_path + filename, new_filename)
	print("Copied %s -> %s" % (input_path + filename, new_filename))
