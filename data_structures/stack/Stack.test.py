from Stack import Stack

S = Stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)


def print_all():
    while not S.empty():
        print(S.peek())
        S.pop()


print_all()