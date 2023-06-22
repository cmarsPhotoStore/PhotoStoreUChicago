import csv
import json
from pprint import pprint as pp
import argparse
from datetime import *

parser = argparse.ArgumentParser()
parser.add_argument('csv', help='csv')


args = parser.parse_args()


rows = []
with open(args.csv, encoding='utf-8', errors='ignore') as f:
	reader = csv.DictReader(f) 
	for row in reader:
		pp(row)
		if 'PhotoStore' not in row['Albums']:
			continue
		else:
			rows.append(row)

pp(len(rows))

keys = rows[0].keys()
with open('metadata_photostore_only.csv', 'w', newline='', errors='ignore', encoding='utf-8') as outfile:
	writer = csv.DictWriter(outfile, keys)
	writer.writeheader()
	writer.writerows(rows)