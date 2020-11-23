import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
      self.result = []
      self.index_check = []
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
    self.index_check.append(i)
    if self.right[i] != -1:
        self.inOrder(self.right[i])
    return self.result


def IsBinarySearchTree(A, index_check, right_child):
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return False
        if A[i] == A[i-1]:
            if right_child[index_check[i-1]] != index_check[i]:
                if index_check[i] >= index_check[i-1]:
                    continue
                return False
    return True


def main():
    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
        print("CORRECT")
        return
    in_order_traversal = tree.inOrder()
    if IsBinarySearchTree(in_order_traversal, tree.index_check, tree.right) == False:
        print("INCORRECT")
    else:
        print("CORRECT")

threading.Thread(target=main).start()
