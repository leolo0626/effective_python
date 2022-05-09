class Counter :
    def __init__(self):
        self.added = 0

    def __call__(self):
        # when the counter is executed then it will add the self.added + 1
        self.added += 1
        return 0

