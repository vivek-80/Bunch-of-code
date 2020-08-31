# problem link:
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
import array as arr
def socks_marchent(n,ar):
	counter=0
	for i in range(n):
		for j in range(i+1,n):
			if ar[i]>ar[j]:
				temp=ar[i]
				ar[i]=ar[j]
				ar[j]=temp
#	for i in range(n):
#		print(ar[i],end='')
	i=0
	while i<n:
		j=i+1
		while j<n:
			if ar[i]==ar[j]:
				counter+=1
				break
			else:
				j-=1
				break
			j+=1
		i=j+1
	return counter
ar=arr.array('i',[])
x=eval(input('Enter no.'))
#for i in range(x):
	#n=eval(input())
n=[int(k) for k in input().split()]
for p in range(len(n)):
	ar.append(n[p])
pair=socks_marchent(x,ar)
print(pair)