#Deque (Double-ended queue) in Python
#expanded o contracted in both sides

class Deque:
	
	def __init__(self):
		self.deque = []
		self.len = 0

	def empty(self):
		if self.len == 0:
			return True
		return False

	def push_front(self, e):
		self.deque.insert(0,e)
		self.len += 1

	def push_back(self, e):
		self.deque.insert(self.len,e)
		self.len += 1

	def pop_front(self):
		if not self.empty():
			self.deque.pop(0)
			self.len -= 1

	def pop_back(self):
		if not self.empty():
			self.deque.pop(self.len - 1)
			self.len -= 1

	def front(self):
		if not self.empty():
			return self.deque[0]
		return 0

	def back(self):
		if not self.empty():
			return self.deque[-1]
		return 0

	def show_deque(self):
		if not self.empty():
			for i in self.deque:
				print(i, end = ' ')
			print()
		else:
			print(None)
	
d = Deque()

d.push_front(10)
d.show_deque()

d.push_front(5)
d.show_deque()

d.push_back(20)
d.show_deque()

d.push_front(7)
d.show_deque()

d.push_back(40)
d.show_deque()

print(d.empty())
print("front item: %d" % d.front())
print("back item: %d" % d.back())

d.pop_back()
d.show_deque()

d.pop_front()
d.show_deque()

d.pop_back()
d.show_deque()

d.pop_front()
d.show_deque()

d.pop_front()
d.show_deque()

print(d.empty())
print("front item: %d" % d.front())
print("back item: %d" % d.back())
