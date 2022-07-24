# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderByIndex(self, i, result: []):
        #Left --> Root --> Right
        if self.left[i] != -1 :
            self.inOrderByIndex(self.left[i], result)
        result.append(self.key[i])
        if self.right[i] != -1:
            self.inOrderByIndex(self.right[i], result)

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inOrderByIndex(0, self.result)
        return self.result

    def preOrderByIndex(self, i, result:[]):
        #Root --> Left --> Right
        result.append(self.key[i])
        if self.left[i] != -1 :
            self.preOrderByIndex(self.left[i], result)
        if self.right[i] != -1:
            self.preOrderByIndex(self.right[i], result)

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preOrderByIndex(0, self.result)
        return self.result

    def postOrderByIndex(self, i, result:[]):
        # left --> right -- > root
        if self.left[i] != -1:
            self.postOrderByIndex(self.left[i], result)

        if self.right[i] != -1:
            self.postOrderByIndex(self.right[i], result)

        result.append(self.key[i])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postOrderByIndex(0, self.result)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()


'''
5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1

'''