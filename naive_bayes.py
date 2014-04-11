import json,re

class NB(object):
	def __init__(self, top_cats, doc, max_cat_couts=5, model_dir='models/'):
		self._doc = doc
		self._top_cats = top_cats
		self._model_dir = model_dir
		self._max_cat_couts = max_cat_couts

	def apply(self):
		cats_prob = {}
		for cat in top_cats:
			prob = 0.0
			model = json.load(open(model_dir+str(cat)+'.json'))
			terms = re.findall(r'/d+:', self._doc)
			for term in terms:
				term = term.replace(':', '')
				try:
					prob += model[term]
				except:
					pass
			cats_prob[cat] = 