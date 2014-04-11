import re

class KNN(object):
	def __init__(self, tf_idf_file, n=5):
		self._doc = open(tf_idf_file)
		self._n = n

	def find_knn(self, doc):
		self._doc.seek(0)
		cos_distances = {}
		doc_features = re.findall(r'\d+:\d+\.\d+', doc)
		while True:
			line = self._doc.readline()
			if not line:
				break
			features = re.findall(r'\d+:\d+\.\d+', line)
			if len(features) < 1:
				continue
			cos_distances[line] = self._cos_distance(doc_features, features)
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
