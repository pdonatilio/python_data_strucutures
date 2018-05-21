#Queue in Python
#FIFO - First in First Out

class Queue:
	#constructor
	def __init__(self):
		self.queue = []
		self.len_queue = 0

	#insert an element in queue
	def push(self, e):
		self.queue.append(e)
		self.len_queue += 1

	#remove the first element in queue
	def pop(self):
		if not self.empty():
			self.queue.pop(0)
			self.len_queue -= 1

	#Verify if the queue is empty
	def empty(self):
		if self.len_queue == 0:
			return True
		return False

	#get the size of the queue
	def length(self):
		return self.len_queue

	#get the first element in queue
	def front(self):
		if not self.empty():
			return self.queue[0]

q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.front())
print(q.empty())

q.pop()
print(q.front())

q.pop()
q.pop()
print(q.front())



