import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

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

  def IsBinarySearchTree(self, i=0):
    global trigger
    if self.left[i] != -1:
        self.IsBinarySearchTree(self.left[i])
    self.result.append(self.key[i])
    print(self.result)
    trigger += 1
    if trigger > 1 and self.result[-1] < self.result[-2]:
        print('false')
        return False
    if self.right[i] != -1:
        self.IsBinarySearchTree(self.right[i])


trigger = 0
def main():
    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
        print("CORRECT")
        return
    # print(TreeOrders.IsBinarySearchTree(tree))
    if TreeOrders.IsBinarySearchTree(tree) == False:
        print("INCORRECT")
    else:
        print("CORRECT")

threading.Thread(target=main).start()
