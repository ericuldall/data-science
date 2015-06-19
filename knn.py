#!/usr/bin/python
import sys
import importlib.machinery
loader = importlib.machinery.SourceFileLoader("algo", "/var/python/ga/data-science/lib/algo.py")
algo = loader.load_module().Algo()
algo.loadTrainingSet('/var/python/ga/dat-la-07/hw/hw1-athletes.clean.csv', 
    [
        {'index': 2, 'name': 'age', 'type': 'float'},
        {'index': 3, 'name': 'height', 'type': 'float'},
        {'index': 4, 'name': 'weight', 'type': 'float'},   
        #{'index': 5, 'name': 'sex', 'type': 'float', 'conversion': [{'from': 'F', 'to': 0},{'from':'M', 'to': 1}]},
        #{'index': 8, 'name': 'gold', 'type': 'float'}, 
        #{'index': 9, 'name': 'bronze', 'type': 'float'}, 
        #{'index': 10, 'name': 'silver', 'type': 'float'}, 
        {'index': 12, 'name': 'sport', 'type': 'string'}
    ]
)

args = []
for arg in sys.argv[1::1]:
    args.append(float(arg))

algo.loadTestSet(args)

avgs = {}
for neighbor in algo.getKNearestNeighbor(3):
    if neighbor[3] in avgs:
        avgs[neighbor[3]] += 1
    else:
        avgs[neighbor[3]] = 1

top_votes=0
top_voted=""

for key, val in avgs.items():
    if val > top_votes:
        top_votes = val
        top_voted = key

print(top_voted)
