from model_creator import ModelCreator
from tf_idf import TfIdf

#tf_idf = TfIdf('train.csv')
#print 'train.csv'
#tf_idf.tfidf('tr-idf-full.csv')
#print 'TfIdf'
#tf_idf.global_stats('global-full.csv')
#print 'global-stats'
mc = ModelCreator('tf-idf-full.csv')
print 'model create'
mc.create()
#mt.test()