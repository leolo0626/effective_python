def my_gen() :
    n = 1
    print("This is printed first")
    yield n
    n = 2
    print("This is printed second")
    yield n
    n = 3
    print("This is printed third")
    yield n

def PowTwoGen(max=0) :
    n = 0
    while n < max :
        yield 2**n
        n += 1

class PowTwo :
    def __init__(self, max):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        else :
            result = 2 ** self.n
            self.n += 1
            return result

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f"{self.name} is {self.age} years old"
if __name__ == "__main__":
    # a = my_gen()
    # print(next(a))

    # for i in PowTwoGen(3):
    #     print(i)

    # for i in PowTwo(3) :
    #     print(i)


    ages = [
        Employee("Corgi1", 3),
        Employee("Corgi2", 5),
        Employee("Corgi3", 10),
        Employee("Corgi4", 5),
        Employee("Corgi5", 6),
        Employee("Corgi6", 7)
    ]
    ages.sort()
    print(ages)
