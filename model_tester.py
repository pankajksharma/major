import json, re
from knn import KNN
from math import log

class ModelTester(object):
	def __init__(self, test_file, trained_file, global_file):
		self._doc = open(test_file)
		self._stats = json.load(open(global_file))
		self._n = self._stats["N"]
		self._gf = self._stats["freq"]
		self._knn = KNN(trained_file)
		self.result = {}

	def test(self):
		c = 0 
		while True:
			line = self._doc.readline()
			if not line:
				break
			line = line.replace(', ', ',')
			parts = line.split()
			if parts < 2:
				raise ValueError
			labels, features = parts[0], ' '.join(parts[1:])
			tfidf = self.get_tfidf(features)
			top_cats = self._knn.find_knn(tfidf)
			#print top_cats
			print c 
			c =c +  1
			for i in top_cats:
				try :
					self.result[str(i)].append(line.replace('\n', ''))
				except : 
					self.result[str(i)] = []
					self.result[str(i)].append(line.replace('\n', ''))
				
	def write(self, output_file ) :
		fp = open(output_file+'.json', 'w')
		json.dump(self.result, fp)
		fp.close()		
			

	def get_tfidf(self, features):
		features = re.findall(r'\d+:\d+', features)
		fs = ""
		doc_sum = 0.0
		for f in features:
			# print f
			r,w = f.split(':')
			w = float(w)
			doc_sum += w
		
		for f in features:
			r,w = f.split(':')
			w = float(w)
			w /= doc_sum
			try:
				w *= log(self._n/(self._gf[r]+1))
			except KeyError:
				w *= log(self._n)
			fs += r+":"+str(w)+" "
		return fs
