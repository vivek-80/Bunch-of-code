#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Encryption problem of Hackerrank :
import math as m
def remove(string): 
    return "".join(string.split())
def encryp(str, k):
	l1=[]
	l2=[]
	for i in range(len(str)):
		if i %k == 0:
			sub = str[i:i+k]
			lst = []
			for j in sub:
				lst.append(j)
			l1.extend(lst)
	for i in range(k):
		if i!=0:
			print(' ',end='')
		for j in range(i,len(l1),k):
			print(l1[j],end='')
s = input()
st= remove(s)
l=len(st)
r=m.floor(m.sqrt(l))
c=m.ceil(m.sqrt(l))
encryp(st,c)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
