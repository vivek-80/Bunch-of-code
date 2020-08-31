# Vowels are (a,e,i,o,u) :
# My vowel and consonant Finder Program :
def consonant(str):
	str1=''
	for j in str:
		if j not in ['a','e','i','o','u']:
			str1+=j
	return str1
def vowel_finder(str):
	count=0
	str1=' '
	a,e,i,o,u=True,True,True,True,True
	lst=[]
	for j in str:
		if j=='a' and a:
			count+=1
			a=False
			lst.append(j)
		elif j=='e' and e:
			count+=1
			e=False
			lst.append(j)
		elif j=='i' and i:
			count+=1
			i=False
			lst.append(j)
		elif j=='o' and o:
			count+=1
			o=False
			lst.append(j)
		elif j=='u' and u:
			count+=1
			u=False
			lst.append(j)
	return count,lst
s1=input('Enter Any String OR Name : ')
st=' '
con=consonant(s1)
x=len(con)
vowels,lst=vowel_finder(s1)
st1=st.join(lst)
print('\n')
print('******************************************')
print('Vowels in String are : {}'.format(st1))
print('******************************************')
print('No. of Vowels are : %d'%(vowels))
print('******************************************')
print('consonant in string are : %s'%(con))
print('******************************************')
print('No. of consonant in string are : %d'%(x))
print('******************************************')