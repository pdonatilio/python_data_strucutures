#Linked List with Python
class Node:
	def __init__(self,label):
		self.label = label
		self.next  = None

	def getLabel(self):
		return self.label

	def setlabel(self, label):
		self.label = label

	def getNext(self):
		return self.next

	def setNext(self,next):
		self.next = next

class LinkedList:	
	def __init__(self):
		self.first    = None
		self.last     = None
		self.len_list = 0

	def push(self, label, index):
		if index >= 0:
			#create a new node
			node = Node(label)
			
			if self.empty(): #verify if the list is empty
				self.first = node
				self.last  = node
			elif index == 0: #insert at the begining of list
				node.setNext(self.first)
				self.first = node
			elif index >= self.len_list: #insert at the final of list
				self.last.setNext(node)
				self.last = node
			else: #insert at the middle of list
				prev_node  = self.first
				curr_node  = self.first.getNext()
				curr_index = 1

				while curr_node != None:
					if curr_index ==  index: #find the index we lloking for
						node.setNext(curr_node) #set the node in the position determinated
						prev_node.setNext(node) # set this node at the next node in prev node

					prev_node = curr_node
					curr_node = curr_node.getNext()
					curr_index += 1

			#update the list size
			self.len_list += 1

	def pop(self,index):
		if not self.empty() and index >= 0 and index <self.len_list:
			flag_remove = False

			if self.first.getNext() == None: #have one element in list
				self.first  = None
				self.last   = None
				flag_remove = True
			elif index == 0: #Have more than one element and you need remove the first element
				self.first  = self.first.getNext()
				flag_remove = True
			else: #have more than one element and you need remove in the middle
				prev_node  = self.first
				curr_node  = self.first.getNext()
				curr_index = 1

				while curr_node != None:
					if index == curr_index: #Finde the item
						prev_node.setNext(curr_node.getNext())
						curr_node.setNext = None
						flag_remove       = True
						break

					prev_node  = curr_node
					curr_node  = curr_node.getNext()
					curr_index += 1

			if flag_remove:
				self.len_list -= 1

	def empty(self):
		if self.first == None:
			return True
		return False

	def lenght(self):
		return self.len_list

	def show(self):
		curr_node = self.first
		while curr_node != None:
			print(curr_node.getLabel(), end=' ')
			curr_node = curr_node.getNext()
		print('')

the_list = LinkedList()

#insert
the_list.push('Paulo',0)
the_list.push('Vivi',1)
the_list.show()

the_list.push('Alexandre',2)
the_list.push('Laerson',3)
the_list.show()

the_list.push('Dani',2)
the_list.show()

the_list.push('Dudu',3)
the_list.show()

print(the_list.lenght())

#Delete
the_list.pop(0)
the_list.show()

the_list.pop(2)
the_list.show()

the_list.pop(3)
the_list.show()

print(the_list.lenght())