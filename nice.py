# def reverse(lst):
# 	lst.reverse() 
# 	return lst
# def maxPairs(rel):
# 	list=[]
# 	count=0 
# 	i=0
# 	while i<len(rel):
# 		j=i+1
# 		while j<len(rel):
# 			diff=r[i]-r[j]
# 			#if diff==min_d:
# 				#list.append(r[i])
# 				#list.append(r[j])
# 			list.append(diff)
# #				count+=1
# 			j+=1
# 		i+=1 
# 	print(max(list))		
# p=eval(input(''))
# r=[]
# n=[int(k) for k in input().split()]
# for i in range(len(n)):
# 	r.append(n[i])
# #min_d=eval(input(''))
# rel=reverse(r)
# maxPairs(rel)
class Difference:
    def __init__(self, a):
        self.elements = a
        self.l=[]
        self.maximumDifference=None
    def computeDifference(self):
        i=0
        while i<len(self.elements):
            j=i+1
            while j<len(self.elements):
                diff=self.elements[i]-self.elements[j]
                num=abs(diff)
                self.l.append(num)
                j+=1
            i+=1
        self.maximumDifference=max(self.l)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)