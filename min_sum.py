# find min_sum and max_sum:
n=[int(k) for k in input().split()]
sum_1=sum_2=sum_3=sum_4=sum_5=0
for i in range(len(n)):
	if i==0:
		continue
	sum_1+=n[i]
for i in range(len(n)):
	if i==1:
		continue
	sum_2+=n[i]
for i in range(len(n)):
	if i==2:
		continue
	sum_3+=n[i]
for i in range(len(n)):
	if i==3:
		continue
	sum_4+=n[i]
for i in range(len(n)):
	if i==4:
		continue
	sum_5+=n[i]
print(min(sum_1,sum_2,sum_3,sum_4,sum_5),end=' ')
print(max(sum_1,sum_2,sum_3,sum_4,sum_5))

	





