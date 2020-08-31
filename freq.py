import array as arr
#def get_battery(event):
#	if event>0:
#		bc+=event
#	else:
#		bc-=event
#	return bc
bc=50
a=arr.array('i',[])
n=eval(input())
for i in range(n):
	ele=eval(input())
	a.append(ele)
for i in range(n):
	if bc>=100:
		
		if a[i]>0:
			bc+=a[i]
		else:
			bc+=a[i]
#for i in range(n):
#	fin=get_battery(a[i])
print(bc)