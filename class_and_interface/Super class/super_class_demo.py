class MyBaseClass :
    def __init__(self, value):
        self.value = value

class TimesSevencorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class GoodWay(TimesSevencorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)

if __name__ == "__main__" :
    goodWay = GoodWay(3)
    assert(goodWay.value, 84)
