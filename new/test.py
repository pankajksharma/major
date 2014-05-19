import json, re
from iterate import * 

def get_Thresholds():
	thres = []
	file = open("results/threshold.csv")
	for i in xrange(0, 1000):
		line = float(file.readline())
		if i  % 50 == 0:
			thres.append(line)
	return thres

def True_or_false(top_labels,labels):
	lis = []
	for i in labels:
		if i in top_labels:
			lis.append(i)
	if len(lis) > 0 :
		return "True"
	else :
		return "False"


def cos_dis(obj1, obj2):
	num = 0.0
	sq1 = 0.0
	sq2 = 0.0
	for k,v in obj1.iteritems():
		try:
			num += v*obj2[k]
		except:
			pass
		sq1 += v*v
	for v in obj2.values():
		sq2 += v*v
	return num/((sq1**0.5)*(sq2**0.5))

def generate(threshold):
	fi=open('model-iterated.json', 'r')
	models = json.loads(fi.read())
	fi.close()
	fi = open('test-exp1.svm')
	fresult = open("results/"+str(threshold)+".csv","w")
	c = 0
	true_count = 0 
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
		#print top_labels[:n], labels
		# line_no , True 
		# break
		string = True_or_false(top_labels[:n], labels)
		if string == "True" : 
			true_count+=1
		if c % 1000 == 0 :
			print c
		stri=""+str(c)+","+string+"\n"
		fresult.write(stri)
		c+=1

	fresult.close()
	return float((true_count*100)/c)

n = 10

#n = int(raw_input())
#threshold = float(raw_input())
file = open("accuracy","w")
threshold  = get_Thresholds()
for th in threshold : 
	iterate_model(flaot(n))
	m=generate("threshold"+str(n))
	print "Accuracy is : ",m
	file.write(str(m)+","+str(th)+"\n")
file.close()