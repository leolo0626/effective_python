# python3
''''
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213

8
find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0

'''
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for query in queries:
        if query.type == 'add' :
            contacts[query.number] = query.name
        elif query.type == 'find':
            if query.number in contacts :
                result.append(contacts[query.number])
            else:
                result.append("not found")
        elif query.type == 'del':
            if query.number in contacts :
                del contacts[query.number]
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

