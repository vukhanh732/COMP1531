import json
import operator
import pickle

data = pickle.load(open("shapecolour.p", "rb"))

common = {}
for d in data:
    key = d['colour'] + '|' + d['shape']
    if key not in common:
        common[key] = 0
    common[key] += 1

colour, shape = (max(common.items(), key=operator.itemgetter(1))[0]).split('|')

new = {
    "mostCommon" : {
        "colour" : colour,
        "shape" : shape,
    },
    "rawData" : data,
}

with open("processed.json", "w") as write_file:
    json.dump(new, write_file)
