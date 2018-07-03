from LinkedList import LinkedList

L = LinkedList(0)
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.append(6)
L.append(7)
L.append(8)
L.append(9)


def print_all(x):
    current = x.head
    while current:
        print(current.data)
        current = current.next


print_all(L)
print("append 27")
L.append(27)
print_all(L)
print("delete 6")
L.delete(6)
print_all(L)
print("prepend 44")
L.prepend(44)
print_all(L)
