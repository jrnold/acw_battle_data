# Imports packages I need for script
# Generally I try to follow the https://google.github.io/styleguide/pyguide.html
import argparse
import csv
import json
import os
import requests
import sys
import os.path as path

# Need a comment on why this is necessary
# Wikipedia API requires clients to identify themselves
# https://www.mediawiki.org/wiki/API:Main_page
# It will reject queries that use a generic user-agent
USER_AGENT = 'https://github.com/jrnold/acw_battle_data; jeffrey.arnold@gmail.com'
# TODO: It may be better to set the user-agent from a config file

def download_battle(battle, dst):
	"""
	Download Wikipedia page for one battle to destination
	"""
	WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"
	# split URL into parameters (largely because it is easier to read)
	# Having this as a separate function is easier to debug and test
	params = {
		'action': 'query',
		'titles': battle,
		'prop': 'revisions',
		# https://www.mediawiki.org/wiki/API:Revisions
		# Content + unique revision ID and timestamp
		'rvprop': '|'.join(('content', 'ids', 'timestamp')),
		'format': 'json'
	}
	dstfile = path.join(dst, '%s.json' % battle)
	# Explain why the USER
	headers = {'user-agent': USER_AGENT}
	# check if file exists and do not download if it download_all_battle
	# useful if the script breaks in the middle of a download cycle
	if not path.exists(dstfile):
		# use 'wb' since we want to write, and we don't need or want python to mess with the
		# end of line characters (the b is for binary)
		r = requests.get(WIKIPEDIA_API_URL, headers = headers, params = params)
		# check if this was successful by checking the error Code
		if r.status_code == 200:
			with open(dstfile, 'wb') as f:
				# When a script has side effects like writing to files, I like to put some messages
				# A more robust way would have logging and verbosity/quiet options, but that's not really necessary
				print("Writing %s to %s" % (battle, dstfile))
				# instead of converting JSON -> python, and python -> json
				# dump the raw contents to a file.
				f.write(r.content)
		else:
			print("ERROR: %s had status code %s " % (r.url, r.status_code))
	else:
		print("%s already exists. Nothing downloaded." % dstfile)


def get_battle_titles(src):
	with open(src, 'r') as f:
		reader = csv.DictReader(f)
		# This is an example of a python list comprehension
		# See http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
		data = [row['wikipedia_title'] for row in reader]
	return data

def download_all_battles(dst, rootdir):
	try:
		os.makedirs(dst)
		print("Created directory %s" % dst)
	# if the directory exists, then catch the error and ignore it
	except os.error as e:
		pass
	battlefile = path.join(rootdir, 'rawdata', 'nps_combined', 'battles_to_wiki.csv')
	battlelist = get_battle_titles(battlefile)
	# Iterates through list, getting data and writing each to its own .json file
	for battle in battlelist:
		download_battle(battle, dst)
	# This may have been done better by combining titles, I don't know what
	# the

def main(args):
	# I use the main function only to parse command line arguments
	# Argparse https://docs.python.org/3/library/argparse.html is used to
	# parse command line arguments. This is also a nice way to make a self documenting
	# script.
	parser = argparse.ArgumentParser(description = "Download full texts of the English Wikipedia pages of battles in CWSAC")
	parser.add_argument('dst', metavar = "DST", nargs = 1,
						help = "Destination directory to save the files to")
	parser.add_argument('rootdir', metavar = "ROOTDIR", nargs = 1,
						help = "Root directory of the ACW Battles project")
	pargs = parser.parse_args(args)
	download_all_battles(pargs.dst[0], pargs.rootdir[0])

if __name__ == "__main__":
	# if __name__ = "__main__" is only run if the script is run directly
	# it will not run if the script is loaded via import
	#
	# sys.argv contains the command-line arguments
	main(sys.argv[1:])
