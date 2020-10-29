import sys
import threading


def constructTree(n, parents):
    nodes = [i for i in range(n)]
    children = [[] for node in nodes]
    root = int()
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)
    return root, children

def nodeHeight(i, parents, height):
    if parents[i] == -1:
        height[i] = 1
        return 1
    if height[i]:
        return height[i]
    height[i] = 1 + nodeHeight(parents[i], parents, height)
    return height[i]


def treeHeight(n, parents):
    height = [int() for i in range(n)]
    for i in range(n):
        if not height[i]:
            height[i] = nodeHeight(i, parents, height)
    return max(height)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(treeHeight(n,parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
