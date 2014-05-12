import re, os

class KNN(object):
	def __init__(self, tf_idf_file, n=5):
		self._doc = open(tf_idf_file)
		self._n = n
		self.get_docs()

	def get_docs(self):
		cats = []
		docs = []
		c=0

		for o in os.listdir('model/'):
			cats.append(o.split('.')[0])
		while True:
			if c% 10000 == 0 : print c 
			line = self._doc.readline()
			if not line:
				break
			parts = line.split()
			if len(parts) <= 2:
				continue
			labels, features = parts[0].split(','), ' '.join(parts)		
				
			for i in labels :
				if i in cats:
					docs.append(features)
			c=c+1
			
			if c % 2000 == 0 :
				files = open("calculateddata.json",'w')
				files.write(str(docs))
				files.close()

		open("calculateddata.json",'w').write(docs)
		self._docs = docs
		


	def find_knn(self, doc):
		self._doc.seek(0)
		cos_distances = {}
		doc_features = re.findall(r'\d+:\d+\.\d+', doc)
		for fil in os.listdir('model/'):
			doc2 = json.read()
		for doc in self._docs:
			labels, features = parts[0].split(','), ' '.join(parts[1:])			
			features = re.findall(r'\d+:\d+\.\d+', features)
			if len(features) < 1:
				continue
			cos_distances[str(labels)] = self._cos_distance(doc_features, features)
		# cos_distances[]
		#   while True:
		# 	line = self._doc.readline()
		# 	if not line:
		# 		break
		# 	features = re.findall(r'\d+:\d+\.\d+', line)
		# 	if len(features) < 1:
		# 		continue
		# 	cos_distances[line] = self._cos_distance(doc_features, features)
		scd = sorted(cos_distances, key=cos_distances.get)
		sv = cos_distances.values()
		sv.sort()
		scd.reverse()
		# print sv[:self._n]
		top_cats = []
		for line in scd[:self._n]:
			cats = line.split()[0].split(',')
			top_cats += cats
		return top_cats

	def _cos_distance(self, doc1, doc2):
		sqt_sum1 = 0.0
		sqt_sum2 = 0.0
		pro_sum = 0.0
		terms1 = {}
		terms2 = {}
		for d in doc1:
			f,w = d.split(':')
			w = float(w)
			sqt_sum1 += w*w
			terms1[f] = w

		for d in doc2:
			f,w = d.split(':')
			w = float(w)
			sqt_sum2 += w*w
			terms2[f] = w

		# print sqt_sum1, sqt_sum2
		for t in terms1:
			if terms2.has_key(t):
				pro_sum += terms1[t]*terms2[t]
		return pro_sum / ((sqt_sum1**0.5)*(sqt_sum2**0.5)+1)
