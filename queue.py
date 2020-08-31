class MyQueue:
    def __init__(self):
        self.queue=[]
    def peek(self):
        #if (self.is_empty()):
         #   return
        return self.queue[0]
    def pop(self):
        del self.queue[0]
    def put(self,item):
        self.queue.append(item)
queue = MyQueue()
l=[]
i=0
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    elif values[0]==3:
        temp=queue.peek()
        l.append(temp)
while i<len(l):
    print(l[i])
    i+=1