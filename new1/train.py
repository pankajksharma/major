import numpy as np
import pandas as pd
import json,re,random
from sklearn.ensemble import RandomForestClassifier 
from sklearn.svm import SVC

def accuracy(tr, te):
	forest = RandomForestClassifier(100)
	forest.fit(tr[::, 1::], tr[::, 0])
	
	output = forest.predict(te[::, 1::])
	return np.sum(te[::, 0]==output) / float(len(te))

def accuracy_svc(tr, te):
	classifier = SVC()
	classifier.fit(tr[::, 1::], tr[::, 0])
	output = classifier.predict(te[::, 1::])
	return np.sum(te[::, 0]==output) / float(len(te))

def cos_dis(model, data):
	num = 0.0
	sq1 = 0.0
	sq2 = 0.0
	for k,v in model.iteritems():
		sq1 += v * v
		num += v * data[k]
		sq2 += data[k] * data[k]
	return (num/((sq1**0.5)*(sq2**0.5)))


def identify_outliers(ds, te):
	while True:
		#Create initial model
		models = {}
		for d in ds:
			k = int(d[0])
			if k not in models.keys():
				models[k] = {}
			# print d[0]
			model = models[k]
			for x in range(1, len(d[1:])):
				try:
					model[x] += int(d[x])
				except:
					model[x] = int(d[x])
		
		#Now try to find outliers
		ac_old = accuracy_svc(ds, te)
		coses = {}
		for d in range(len(ds)):
			model = int(ds[d][0])
			if model not in coses.keys():
				coses[model] = {}
			cos = coses[model]
			cos[d] = cos_dis(models[model], ds[d])
		for k,cos in coses.iteritems():
			most_diff = sorted(cos, key=cos.get)[0]
			# print k,most_diff, cos[most_diff]
			#Apply threshold funda here
			ds = np.delete(ds, most_diff, 0)
		print ds.shape
		ac_new = accuracy_svc(ds, te)
		print ac_old, ac_new
	return ds


def clean_data(df):
	df['Gender']=df['Sex'].map({'female': 0, 'male':1})
	median_ages = np.zeros((2,3))
	for i in range(2):
		for j in range(3):
			median_ages[i, j] = df[(df.Gender==i) & (df.Pclass==j+1)].Age.dropna().median()
	df['AgeFill'] = df['Age']
	for i in range(2):
		for j in range(3):
			df.loc[(df.Gender==i) & (df.Pclass==j+1) & (df.Age.isnull()), 'AgeFill'] = median_ages[i,j]

	df['FamilySize'] = df['SibSp'] + df['Parch']
	df = df.drop(['PassengerId', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked', 'Age'], axis=1) 
	median_fare=[0,0,0]
	for i in range(3):
		median_fare[i] = df[df.Pclass==i+1].Fare.dropna().median()
	for i in range(3):
		df.loc[ (df.Pclass==i+1) & (df.Fare.isnull()), 'Fare' ]	= median_fare[i]
	return df.values

def random_sample(ds, ratio=0.1):
	ds_len = len(ds)
	samples = []
	sample_counts = range(ds_len)
	for i in range(int(ratio*ds_len)):
		s = random.choice(sample_counts)
		sample_counts.remove(s)
		samples.append(ds[s])
	return np.asarray(samples)

tr=pd.read_csv('train.csv', header=0)
tr = clean_data(tr)

forest = RandomForestClassifier(100)

forest.fit(tr[::, 1::], tr[::, 0])

te = pd.read_csv('test.csv', header=0)
# tx = te.PassengerId.values
te = clean_data(te)
# print len(te)
# te = random_sample(te)
# print len(te)

# print type(te)

# output = forest.predict(te[::, 1::])
# print pd.crosstab(te[::, 0], output, rownames=["Actual"], colnames=["Pred"])

# print np.sum(te[::, 0]==output) / float(len(te))

# print tr
print accuracy_svc(tr,te)
print identify_outliers(tr,te)

# print output
# print 'PassengerId,Survived'
# for i in range(len(tx)):
# 	print '{0},{1}'.format(tx[i], int(output[i]))


# fi=open('train.csv', 'r')
# model = {}
# labels_occ = {}

# c  = 0
# while True:
# 	line = fi.readline()
# 	if not line:
# 		break
# 	parts = line.split()
# 	if len(parts) < 3:
# 		continue
# 	if re.findall(r'\d+:\d+\.\d+', str(parts[0])) != []:
# 		continue
# 	labels, features = parts[0].split(','), parts[1:]
# 	for label in labels:
# 		if not label in labels_occ.keys():
# 			labels_occ[label] = {}

# 		if not label in model.keys():
# 			model[label] = {}
# 		for feature in features:
# 			f,w = feature.split(':')
# 			try:
# 				model[label][f] += float(w)
# 			except:
# 				model[label][f] = float(w)
# 			try:
# 				labels_occ[label][f] += 1
# 			except:
# 				labels_occ[label][f] = 1


# for k,v in model.iteritems():
# 	for k1,v1 in v.iteritems():
# 		model[k][k1] /= labels_occ[k][k1]

# fi.close()
# f=open('model.json', 'w')
# json.dump(model, f)
# f.close()

