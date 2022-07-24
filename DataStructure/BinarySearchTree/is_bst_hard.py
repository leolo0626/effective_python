#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) == 0:
      return True
  return IsBinarySearchTreeByIndex(tree, 0, float("-inf"), float("inf"))


def IsBinarySearchTreeByIndex(tree, i, min_val, max_val):
    if i == -1:
        return True

    key, left_idx, right_idx = tree[i]
    if key < min_val:
        return False

    if key >= max_val:
        return False

    if left_idx == -1 and right_idx == -1:
        return True

    return IsBinarySearchTreeByIndex(tree, right_idx, key, max_val) and IsBinarySearchTreeByIndex(tree, left_idx,
                                                                                                  min_val, key)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()


'''
3
2 1 2
1 -1 -1
3 -1 -1
correct

3
1 1 2
2 -1 -1
3 -1 -1
Incorrect

5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1
correct

7
4 1 2
2 3 4
6 5 6
1 -1 -1
3 -1 -1
5 -1 -1
7 -1 -1
correct

4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1
Incorrect

3
2 1 2
2 -1 -1
3 -1 -1
Incorrect

3
2 1 2
1 -1 -1
2 -1 -1
correct

'''