import json,re

def remove_out_liers(model, doc,threshold):
	for k,v in doc.iteritems():
		cos = cos_dis(model, {k:v})
		if cos not in lis : lis.append(cos)
		if cos < threshold:
			model[k] -= v
	return model

def write(lis):
	fi = open("threshold", "w")
	lis.sort()
	for i in lis:
		fi.write(str(i)+"\n")
	fi.close()

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


def iterate_model(n):
	fi = open("model.json", "r")
	models = json.loads(fi.read())
	fi.close()
	c = 0
	fi = open("train-exp1.svm", "r")
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
			model = models[label]
			doc = {}
			for feature in features:
				f,w = feature.split(':')
				doc[f] = float(w)

		model = remove_out_liers(model, doc,n)

		if c % 1000 == 0: 
			print c
			write(lis)
		c += 1
	fi.close()

	fi = open("data/model-iterated"+str(n)+".json", "w")
	json.dump(models, fi)
	fi.close()



