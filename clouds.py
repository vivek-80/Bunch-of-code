def jumping_onclouds(l):
	jump=0
	i=0
	while i<len(l)-1:
		j=i+1
		if l[i]==l[j]:
			if j==len(l)-1:
				jump+=1
				break
			if l[i]==l[j+1]:
				jump+=1
				j=j+1
			else:
				jump+=1
		elif l[i]!=l[j]:
			if l[i]==l[j+1]:
				jump+=1
				j=j+1
		i=j
	return jump
l=[]
k=eval(input())
n=[int(k) for k in input().split()]
for p in range(len(n)):
	l.append(n[p])
#for i in range(k):
#	x=eval(input())
#	l.append(x)
path=jumping_onclouds(l)
print(path)
