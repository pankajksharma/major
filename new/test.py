import json, re
from iterate import cos_dis

n = 10

fi=open('model.json', 'r')
models = json.loads(fi.read())
fi.close()

fi = open('train-exp1.svm')
c = 0
while True:
	line = fi.readline()
	if not line:
		break
	parts = line.split()
	if len(parts) < 3:
		continue
	if re.findall(r'\d+:\d+\.\d+', str(parts[0])) != []:
		labels, features = [], parts[:]
	else:
		labels, features = parts[0].split(','), parts[1:]
	doc = {}
	for feature in features:
		f,w = feature.split(':')
		doc[f] = float(w)

	coses = {}
	for label, model in models.iteritems():
		coses[label] = cos_dis(model, doc)
	# print coses

	top_labels = sorted(coses, key=coses.get)
	top_labels.reverse()
	print top_labels[:n], labels
	# break
