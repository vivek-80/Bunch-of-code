#Here i'm solving swap program without using third variable :

def swap_without_third_var(a,b):
    b = b - a
    a = a + b
    b = a - b
    return a,b
l=[int(x) for x in input('Enter Two value :').split()]
swap=swap_without_third_var(l[0],l[1])
for i in swap:
    print(i,end=' ')

# brief: first go with second variable and then update it with second_var-first_var