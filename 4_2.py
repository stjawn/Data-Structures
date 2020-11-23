import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
      self.result = []
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
    self.result.append(self.key[i])
    if self.right[i] != -1:
        self.inOrder(self.right[i])
    return self.result


def IsBinarySearchTree(A):
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return False
    return True


def main():
    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
        print("CORRECT")
        return
    in_order_traversal = tree.inOrder()
    if IsBinarySearchTree(in_order_traversal) == False:
        print("INCORRECT")
    else:
        print("CORRECT")

threading.Thread(target=main).start()
