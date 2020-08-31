from itertools import compress
def pair(freq):
	we=[]
	result=[]
	for i in range(len(freq)):
		for j in range(freq[i]):
			we.append(i+1)
	for i in range(len(we)):
		for j in range(len(we)):
			result.append([we[j],we[j+1]])

	print(result) 
x=eval(input(''))
freq=[]
#weight=[]
for i in range(x):
	e=eval(input(''))
#	weight.append(i+1)
	freq.append(e)
print(freq)
pair(freq)
#print(weight)














#def rev_sentence(sentence):
#	words = sentence.split(' ')
#	reverse_sentence = ' '.join(reversed(words))
#	return reverse_sentence
#input="aWESOME is cODING"
#string=rev_sentence(input)
#print(string.swapcase()) 