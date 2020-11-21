import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
      self.in_result = []
      self.pre_result = []
      self.post_result = []
      self.n = int(sys.stdin.readline())
      self.key = [0 for i in range(self.n)]
      self.left = [0 for i in range(self.n)]
      self.right = [0 for i in range(self.n)]
      for i in range(self.n):
          [a, b, c] = map(int, sys.stdin.readline().split())
          self.key[i] = a
          self.left[i] = b
          self.right[i] = c

  def inOrder(self, i=0):
    if self.left[i] != -1:
        self.inOrder(self.left[i])
    self.in_result.append(self.key[i])
    if self.right[i] != -1:
        self.inOrder(self.right[i])
    return self.in_result

  def preOrder(self, i=0):
    self.pre_result.append(self.key[i])
    if self.left[i] != -1:
        self.preOrder(self.left[i])
    if self.right[i] != -1:
        self.preOrder(self.right[i])
    return self.pre_result

  def postOrder(self, i=0):
    if self.left[i] != -1:
        self.postOrder(self.left[i])
    if self.right[i] != -1:
        self.postOrder(self.right[i])
    self.post_result.append(self.key[i])
    return self.post_result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
