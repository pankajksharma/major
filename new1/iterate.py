def cos_dis(obj1, obj2):
	num = 0.0
	sq1 = 0.0
	sq2 = 0.0
	for k,v in obj1.iteritems():
		try:
			num += v*obj2[k]
		except:
			pass
		sq1 += v*v
	for v in obj2.values():
		sq2 += v*v
	return num/((sq1**0.5)*(sq2**0.5))



