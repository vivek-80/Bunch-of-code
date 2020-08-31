# birth_day cake candle:
def max_blow(h):
	return max(h)
def compare(h,b):
	count=0
	i=0
	while i<len(h): 
		if h[i]==b:
			count+=1
		i+=1
	return count
no_candle=eval(input(''))
h=[]
n=[int(k) for k in input().split()]
for i in range(len(n)):
	h.append(n[i])
blow=max_blow(h)
blowed_out=compare(h,blow)
print(blowed_out)
