import json,re
fi=open('train-exp1.svm', 'r')
model = {}
labels_occ = {}
c  = 0
result = open("results/threshold","w")
while True:
	line = fi.readline()
	if not line:
		break
	parts = line.split()
	if len(parts) < 3:
		continue
	if re.findall(r'\d+:\d+\.\d+', str(parts[0])) != []:
		continue
	labels, features = parts[0].split(','), parts[1:]
	for label in labels:
		if not label in labels_occ.keys():
			labels_occ[label] = {}

		if not label in model.keys():
			model[label] = {}
		for feature in features:
			f,w = feature.split(':')
			try:
				model[label][f] += float(w)
			except:
				model[label][f] = float(w)
			try:
				labels_occ[label][f] += 1
			except:
				labels_occ[label][f] = 1

	if c % 1000 == 0: print c
	c += 1

# for k,v in model.iteritems():
# 	for k1,v1 in v.iteritems():
# 		model[k][k1] /= labels_occ[k][k1]

fi.close()
f=open('model.json', 'w')
json.dump(model, f)
f.close()

