import re, json
from math import log

class TfIdf(object):
	def __init__(self, file):
		self.doc = open(file)
		self._no_of_docs = 0.0
		self._global_freq = {}

	def tfidf(self, out_file_name):
		self._fill_global_stats()		
		self._save_tf_idf(out_file_name)

	def global_stats(self, out_file_name=None):
		if out_file_name:
			f = open(out_file_name, 'w')
			json.dump({"N":self._no_of_docs, "freq":self._global_freq}, f)
			f.close()
		return self._no_of_docs, self._global_freq

	def _fill_global_stats(self):
		c = 0 
		while True:
			line = self.doc.readline()
			if not line:
				break
			self._no_of_docs += 1
			features = re.findall(r'\d+:\d+', line)
			for feature in features:
				f,w = feature.split(':')
				try:
					self._global_freq[f] += 1
				except KeyError:
					self._global_freq[f] = 1
			if c %10000 == 0 : print c 
			c=c+1

			
	def _save_tf_idf(self, out_file_name):
		of = open(out_file_name, 'w')
		self.doc.seek(0)
		c = 0 
		while True:
			line = self.doc.readline()
			if not line:
				break
			parts = line.split()
			if len(parts) <= 1:
				continue
			c+=1
			out_line = self._get_out_line(parts)
			of.write(out_line)
			if c % 10000 == 0 : print c 
		of.close()

	def _get_out_line(self, parts):
			labels = []
			features = {}
			weights_sum = 0.0
			for p in parts:
				if ':' not in p:
					p = p.replace(',', '').strip()
					labels.append(p)
				else:
					f,v = p.strip().split(':')
					weights_sum += int(v)
					features[f] = int(v)

			for f in features:		
				features[f] /= weights_sum
				features[f] *= (log(self._no_of_docs/(self._global_freq[f]+1)))

			labels.sort()
			all_labels = ','.join(labels)

			s_features = features.keys()
			s_features.sort()

			all_features = ' '
			for sf in s_features:
				all_features += sf+':'+str(features[sf])+' '
			return all_labels+all_features+'\n'
