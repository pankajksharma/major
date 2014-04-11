
from tf_idf import TfIdf
from model_creator import ModelCreator

tf_idf = TfIdf('/home/om/Desktop/tr.csv')
tf_idf.tfidf('tf-idf.csv')
tf_idf.global_stats('global.csv')

mc = ModelCreator('tf-idf.csv')
mc.create()
