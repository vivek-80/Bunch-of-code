# def min_op(lst1,thre,d):
# 	lst2=[]
# 	count=0
# 	re=[]
# 	for i in range(len(lst1)):
# 		z=lst1[i]//d
# 		re.append(z)
# 	print(re)
# lst=[]
# x=int(input())
# for i in range(x):
# 	e=int(input())
# 	lst.append(e)
# thre=int(input())
# d=int(input())
# min_op(lst,thre,d)
# Python3 program to find minimum  
# operations needed to equalize an array. 
  
# Returns minimum operations needed  
# to equalize an array. 
def minOperations(arr, n): 
  
    # Compute sum of array elements 
    sum = 0
    for i in range(0,n): 
        sum += arr[i] 
  
    # If average of array is not integer, 
    # then it is not possible to equalize 
    if sum % n != 0: 
        return -1
  
    # Compute sum of absolute differences 
    # between array elements and average 
    # or equalized value 
    diff_sum = 0
    eq = sum / n 
    for i in range(0, n): 
        diff_sum += abs(arr[i] - eq) 
  
    return int(diff_sum / 2) 
  
# Driver code 
arr = [1,2,3,4,5] 
n = len(arr)  
print(minOperations(arr, n))