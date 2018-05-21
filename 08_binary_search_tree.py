#Binary Search Tree in Python

class Node:

  def __init__(self, label):
    self.label = label
    self.left  = None
    self.right = None

  def getLabel(self):
    return self.label

  def setLabel(self, label):
    self.label = label

  def getLeft(self):
    return self.left

  def setLeft(self, left):
    self.left = left

  def getRight(self):
    return self.right

  def setRight(self,right):
    self.right = right

class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self,label):
    node = Node(label) #create a new node

    if self.empty(): #if is the first node
      self.root = node
    else: # the tree is not empty, we use recursive methods to insert a new leaf
      dad_node = None
      curr_node = self.root

      while True:
        if curr_node != None:
          dad_node = curr_node
          if node.getLabel() < curr_node.getLabel(): #inform the direction to still search left or righ
            curr_node = curr_node.getLeft()
          else:
            curr_node = curr_node.getRight()
        else: #we find a leaf let's input the new one
          if node.getLabel() < dad_node.getLabel():
            dad_node.setLeft(node)
          else:
            dad_node.setRight(node)
          break

  def remove(self,label):
    '''
    There are three different situations
    1 - The node is a leaf: just set the dad pointer to Null
    2 - The node have one child: put the child of node in the Father's Pointer
    3 - The node have two children: Let us pray ;P Get the minor element of the subtree in right side
    '''
    
    dad_node = None
    curr_node = self.root

    while curr_node != None:
      if label ==curr_node.getLabel():

        #situation 1 - The node is a leaf
        if curr_node.getLeft() == None and curr_node.getRight() == None:
          if dad_node == None: #is the first element
            self.root == None
          elif dad_node.getLeft() == curr_node: #is the left child
            dad_node.setLeft(None)
          elif dad_node.getRight() == curr_node: #is the right child
            dad_node.setRight(None)

        #situation 2 - The node have one child
        elif (curr_node.getLeft() == None and curr_node.getRight() != None) \
          or (curr_node.getLeft() != None and curr_node.getRight() == None):

          if dad_node == None: #the node is a root
            if curr_node.getLeft() != None: #what the child side?
              self.root = curr_node.getLeft()
            else:
              self.root = curr_node.getRight()
          else:            
            if curr_node.getLeft() != None: #the curr_node child stay in left
              if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                dad_node.setLeft(curr_node.getLeft())
              else: 
                dad_node.setRight(curr_node.getLeft())
            else: #the curr_node child stay in right              
              if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                dad_node.setLeft(curr_node.getRight())
              else:
                dad_node.setRight(curr_node.getRight())

        #situation 3 - The node have two children
        elif curr_node.getLeft() != None and curr_node.getRight() != None:
          dad_smaller_node = curr_node
          smaller_node = curr_node.getRight()
          next_smaller = curr_node.getRight().getLeft()

          while next_smaller != None:
            dad_smaller_node = smaller_node
            smaller_node = next_smaller
            next_smaller = smaller_node.getLeft()

          if dad_node ==  None: #the node will be turn into root
            if self.root.getRight().getLabel() == smaller_node.getLabel():
              smaller_node.setLeft(self.root.getLeft())
            else:              
              if dad_smaller_node.getLeft() and dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
                dad_smaller_node.setLeft(None)
              else:
                dad_smaller_node.setRight(None)

              smaller_node.setLeft(curr_node.getLeft())
              smaller_node.setLeft(curr_node.getRight())

            #turn the smaller node into root
            self.root = smaller_node
          else: #the dad is not a root
            #the current_node is a child at the left side
            if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel(): 
              dad_node.setLeft(smaller_node)
            else:
              dad_node.setRight(smaller_node)

            #what the side about the smaller node? Avoiding the infinity circle of reference
            if dad_smaller_node.getLeft() and dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
              dad_smaller_node.setLeft(None)
            else:
              dad_smaller_node.setRight(None)

            #update the nodes about the smaller node
            smaller_node.setLeft(curr_node.getLeft())
            smaller_node.setRight(curr_node.getRight())
        
        break #get out of while

      #still searching
      dad_node = curr_node

      #choosing the side to do the next step
      if label < curr_node.getLabel(): #go left
        curr_node = curr_node.getLeft()
      else:
        curr_node = curr_node.getRight()

  def empty(self):
    if self.root == None:
      return True
    return False

  #pre-order show - first left elements
  def show(self, curr_node):
    if curr_node != None:
      print('%d' % curr_node.getLabel(), end=' ')
      self.show(curr_node.getLeft())
      self.show(curr_node.getRight())

  def getRoot(self):
    return self.root

t = BinarySearchTree()

t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.show(t.getRoot())
print('')

t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)
t.show(t.getRoot())
print('')

#removing leafs
t.remove(1)
t.show(t.getRoot())
print('')

t.remove(13)
t.show(t.getRoot())
print('')

#removing nodes with one child
t.remove(10)
t.show(t.getRoot())
print('')

#t.remove(14)
t.show(t.getRoot())
print('')

#remove nodes with two children
t.remove(6)
t.show(t.getRoot())
print('')

#remove the root
t.remove(8)
t.show(t.getRoot())
print('')