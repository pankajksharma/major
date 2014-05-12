from model_tester import ModelTester

mt = ModelTester('test.csv', 'tf-idf-full.csv', 'global-full.csv')
mt.test()
mt.write("output")

# from knn import KNN

# knn = KNN('tf-idf.csv')

# f=open('/home/om/Desktop/test.csv')

# for i in range(10):
# 	knd = knn.find_knn(f.readline())
# 	# for doc in knd:
# 	# 	print doc.split()[0],
# 	# print
# f.close()
