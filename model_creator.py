import json

class ModelCreator(object):
	def __init__(self, tf_idf_file):
		self._doc = open(tf_idf_file)

	def create(self, out_dir='model/'):
		while True:
			line = self._doc.readline()
			if not line:
				break
			parts = line.split()
			if len(parts) < 2:
				break
			labels, features = parts[0].split(','), parts[1:]

			for label in labels:
				try:
					fp = open(out_dir+str(label)+'.json')
					label_model = json.load(fp)
					fp.close()
				except:
					label_model = {}

				for feature in features:
					f,w = feature.split(':')
					w = float(w)
					try:
						label_model[f] += w
					except KeyError:
						label_model[f]  = w

				fp = open(out_dir+str(label)+'.json', 'w')
				json.dump(label_model, fp)
				fp.close()

