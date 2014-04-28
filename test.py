from model_tester import ModelTester

mt = ModelTester('tr.csv', 'tf-idf.csv', 'global.csv')
mt.test()

# from knn import KNN

# knn = KNN('tf-idf.csv')

# f=open('/home/om/Desktop/test.csv')

# for i in range(10):
# 	knd = knn.find_knn(f.readline())
# 	# for doc in knd:
# 	# 	print doc.split()[0],
# 	# print
# f.close()
