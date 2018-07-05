from Heap import Heap

H = Heap()

H.add(10)
H.add(15)
H.add(17)
H.add(20)
H.add(8)
H.add(9)


print(H.peek() == 8)
H.poll()
print(H.peek() == 9)
H.poll()
print(H.peek() == 10)
H.poll()
print(H.peek() == 15)
