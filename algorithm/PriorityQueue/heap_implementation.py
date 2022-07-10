
def parent(i):
    return i // 2

def left_child(i):
    return 2*i

def right_child(i):
    return 2*i+1

class Heap :
    def __init__(self, ls, max_size ):
        self.size = len(ls)
        self.max_size = max_size
        if self.max_size > self.size :
            self._list = ls + [0] *(self.max_size-self.size)
        else:
            self._list = ls
    #private function shift up
    def __shift_up(self, i):
        while i >= 1 and self._list[parent(i)] < self._list[i] :
            temp = self._list[i]
            self._list[i] = self._list[parent(i)]
            self._list[parent(i)] = temp
            i = parent(i)

    def __shift_down(self, i):
        max_index = i
        left = left_child(i)
        if left <= self.size and self._list[left] > self._list[max_index] :
            max_index = left
        right = right_child(i)
        if right <= self.size and self._list[right] > self._list[max_index]:
            max_index = right

        if i != max_index :
            temp = self._list[i]
            self._list[i] = self._list[max_index]
            self._list[max_index] = temp
            self.__shift_down(max_index)

    def insert(self, p):
        if self.size == self.max_size :
            raise Exception('Max Size is reached')

        self.size = self.size + 1
        self._list[self.size-1] = p
        self.__shift_up(self.size-1)

    def extract_max(self):
        result = self._list[0]
        self._list[0] = self._list[self.size-1]
        self.size = self.size -1
        self.__shift_down(0)
        return result

    def remove(self, i):
        self._list[i] = float('inf')
        self.__shift_up(i)
        self.extract_max()

    def change_priority(self, i, p):
        old_p = self._list[i]
        self._list[i] = p
        if p > old_p :
            self.__shift_up(i)
        else :
            self.__shift_down(i)

    def __repr__(self):
        return f"{self._list} and {self.size}"


if __name__ == "__main__" :
    heap = Heap([42, 29, 18, 14, 7, 18, 12, 11, 5], 15)
    print(heap.extract_max())
    print(heap)
    heap.insert(42)
    print(heap)
    heap.insert(19)
    print(heap)
    heap.remove(2)
    print(heap)
    heap.change_priority(2, 50)
    print(heap)

