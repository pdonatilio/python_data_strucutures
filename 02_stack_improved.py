#Stack improved in Python to performance
#FILO - First in Last Out

class Stack:
	#constructor
	def __init__(self):
		self.stack = []
		self.len_stack = 0

	#insert a element in a Stack
	def push(self, e):
		self.stack.append(e)
		self.len_stack += 1

	#remove the last element in a Stack
	def pop(self):
		if not self.empty():
			self.stack.pop(self.len_stack - 1)
			self.len_stack -= 1

	#Get the last element in a Stack
	def top(self):
		if not self.empty():
			return self.stack[-1]
		return None

	#Check if the Stack are empty
	def empty(self):
		if(self.len_stack == 0):
			return True
		return False

	#Get the size of the stack
	def lenght(self):
		return self.len_stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.empty())
print(s.lenght())

s.pop()
print(s.top())

s.pop()
print(s.top())

s.pop()
print(s.top())
print(s.empty())
print(s.lenght())