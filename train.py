from model_creator import ModelCreator
from tf_idf import TfIdf

tf_idf = TfIdf('tr.csv')
tf_idf.tfidf('tr-idf.csv')
tf_idf.global_stats('global.csv')

mc = ModelCreator('tf-idf.csv')
mc.create()
#mt.test()
