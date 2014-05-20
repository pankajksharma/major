f = open('out','r')
l1 = []
i= 1.0
p1 = ['Iteration','Accuracy',]
l1.append(p1)
while True:
	p1 =[]
	try :
    		l = f.readline()
    		p=l.split(" ")
		p1.append(float(i))
		p1.append(float(p[0])*100)
		
		l1.append(p1)
		i = i + 1
    		l = f.readline()
	except : 
		break
	if i > 41 :
		break
	print i
	
print l1




