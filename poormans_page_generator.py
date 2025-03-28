#!/usr/bin/env python

from pathlib import Path
from generate_bib import convert

import re
import subprocess


def create_homepage(pubtypes):
	# convert bibfile to html lists
	convert('franka.bib', pubtypes, format='html')

	# load files
	index = Path('index.html_template').read_text()

	for pubtype in pubtypes:
		reflist = Path(f'{pubtype}.html_part').read_text()
		index = index.replace(f'<object type="text/html" data="{pubtype}.html_part"></object>', reflist)

	# write 
	Path('index.html').write_text(index)

	# clean up
	for pubtype in pubtypes:
		Path(f'{pubtype}.html_part').unlink()

if __name__ == '__main__':
	# specify the categories
	pubtypes = ['preprint', 'publication', 'lecturenote', 'nonarchival', 'book']

	create_homepage(pubtypes)