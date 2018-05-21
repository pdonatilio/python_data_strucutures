#Stack in Python
#FILO - First in Last Out

class Stack: 
	def __init__(self):
		self.stack = []

	#insert a element in a Stack
	def push(self, e):
		self.stack.append(e)

	#remove the last element in a Stack
	def pop(self):
		if not self.empty():
			self.stack.pop(len(self.stack)-1)

	#Get the last element in a Stack
	def top(self):
		if not self.empty():
			return self.stack[-1]
		return None

	#Check if the Stack are empty
	def empty(self):
		if(len(self.stack) == 0):
			return True
		return False

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.empty())

s.pop()
print(s.top())

s.pop()
print(s.top())

s.pop()
print(s.top())
print(s.empty())