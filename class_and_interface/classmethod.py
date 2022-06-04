class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split("-"))
        date1 = cls(day, month, year)
        return date1

    def print_date(self):
        return f"{self.year}-{self.month}-{self.day}"


if __name__ == "__main__" :
    date2 = Date.from_string("06-12-2022")
    print(date2.print_date())
    print(Date(6,3,2013).print_date())
