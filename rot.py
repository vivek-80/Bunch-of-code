import array as arr;
def rotate(ar,n,no_rot,no_quer):
	count=0
	for i in range(n):
		for j in range(i+1,len(ar)):
			if no_rot>count:
				if j<=i+1:
					if j<len(ar):
						temp=ar[i]
						ar[i]=ar[j]
						ar[j]=temp
						count+=1
	for k in range(no_quer):
		m=eval(input())
		print(ar[m],end=' ')
	#print('\n{}'.format(count))
a=arr.array('i',[])
n=eval(input('Enter the size of array :'))
no_of_rotation=eval(input('Enter the element from which you have to begin:'))
no_of_queries=eval(input('the queries :'))
for i in range(n):
	ele=eval(input('Enter the element :'))
	a.append(ele)
rotate(a,n,no_of_rotation,no_of_queries)
for i in range(n):
	print(count)
 
	  
	 	
	 	
	 		
	 			
	 			
	 			
	 			
	 		
	 