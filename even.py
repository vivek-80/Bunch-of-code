l=[]
def count(st):
	st2=''
	st3=''
	for i in st:
		for j in range(len(st)):
			if st[j]==i and j%2==0:
				st2+=i
	for i in st:
		for j in range(len(st)):
			if st[j]==i and j%2!=0:
				st3+=i
	l.append(st2+' '+st3)
final1=''
x=int(input())
for i in range(x):
	st=input()
	count(st)
for i in range(len(l)):
	print(l[i])



