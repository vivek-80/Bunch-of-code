# Left Rotation
import array as ar
def left_rotation(arr,rot,k):
	rot_count=0
#	while rot_count<rot:
#		temp=arr[len(arr)-1]
#		arr[len(arr)-1]=arr[0]
#		j=1
#		while j<=len(arr)-2:
#			arr[j-1]=arr[j]
#			j+=1
#		arr[len(arr)-2]=temp
#		rot_count+=1
#	for i in range(k):
#		print(arr[i],end=" ")
	while rot_count<rot:
		temp=arr[0]
		j=1
		while j<len(arr):
			arr[j-1]=arr[j]
			j+=1
		arr[len(arr)-1]=temp
		rot_count+=1
	for i in range(k):
		print(arr[i],end=" ")
arr=ar.array('i',[])
k,rot=[int(x) for x in input().split()]
n=[int(k) for k in input().split()]
for i in range(len(n)):
	arr.append(n[i])
#print('enter an left_rotation')
left_rotation(arr,rot,k)
