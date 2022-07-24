# python3


class Heap:
    def __init__(self, data):
        self.data =  data
        self.swap_operation = []
        self.size = len(data)


    @staticmethod
    def parent(i):
        return (i+1) // 2

    @staticmethod
    def left_child(i):
        return 2*i+1

    @staticmethod
    def right_child(i):
        return 2*(i + 1)


    def shift_up(self, i):
        while i > 0 and self.data[Heap.parent(i)] >= self.data[i] :
            self.data[Heap.parent(i)] , self.data[i] = self.data[i], self.data[Heap.parent(i)]
            self.swap_operation.append((i, Heap.parent(i)))
            i = Heap.parent(i)


    def shift_down(self, i):
        min_index = i
        l = Heap.left_child(i)
        if l < self.size and self.data[l] < self.data[min_index]:
            min_index = l

        r = Heap.right_child(i)

        if r < self.size and self.data[r] < self.data[min_index]:
            min_index = r

        if i != min_index :
            self.swap_operation.append((i, min_index))
            self.data[min_index], self.data[i] = self.data[i], self.data[min_index]
            self.shift_down(min_index)

    def build_heap(self):

        n = self.size
        for i in range(n//2-1, -1, -1 ):
            self.shift_down(i)
        return self


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    heap = Heap(data)
    swaps = heap.build_heap().swap_operation
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()