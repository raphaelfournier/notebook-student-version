import json
import re
import sys
import os
import pickle
from copy import deepcopy

EXCLUSION_KEYWORDS = ['exclude', 'excluded', 'solution']
STUDENT_SUFFIX="students"

filename = sys.argv[1]
basename, ext = os.path.splitext(filename)
outname = basename + "-" + STUDENT_SUFFIX + ext

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Import the notebook in memory
with open(filename) as f:
    data = json.load(f)

copy = {'cells': []}

for key in data:
    if key != 'cells':
        copy[key] = data[key]

for j, cell in enumerate(data['cells']):
    tags = cell.get('metadata', {}).get('tags', [])
    if intersection(tags, EXCLUSION_KEYWORDS) != []:
        continue

    # Let's proceed for cells that are not excluded
    cell_copy = deepcopy(cell)
    copy['cells'].append(cell_copy)

with open(outname, 'w') as f:
        json.dump(copy, f)
        print(outname+" written")
