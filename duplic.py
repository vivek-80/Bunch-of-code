# This program find Duplicate Element in array :
def find_duplicate(arr):
	count=0
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]==arr[j]:
				return arr[i]
print('Enter The Element :',end=' ')
arr=[int(x) for x in input().split()]
ar=find_duplicate(arr)
print('Duplicate Element is %d'%(ar))





