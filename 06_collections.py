#Using Deque with collections module in python

from collections import deque

d = deque()
d.append(1) #insert an iten in the right side of deque
d.appendleft(2) #insert an iten in the left side of deque
d.append(3)
d.appendleft(4)

for i in d:
	print(i,end=' ')
print()

d.pop()
for i in d:
	print(i,end=' ')
print()

d.popleft()
for i in d:
	print(i,end=' ')
print()

d.remove(1)
for i in d:
	print(i,end=' ')
print()

d.remove(2)
for i in d:
	print(i,end=' ')
print()