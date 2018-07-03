from Queue import Queue

S = Queue()
S.add(1)
S.add(2)
S.add(3)
S.add(4)


def print_all():
    while not S.empty():
        print(S.peek())
        S.pop()


print_all()