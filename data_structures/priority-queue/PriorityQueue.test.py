from PriorityQueue import PriorityQueue

pq = PriorityQueue()

pq.add(10, 0)
pq.add(15, 1)
pq.add(17, 2)
pq.add(20, 3)
pq.add(8, 5)
pq.add(9, 18)


print(pq.peek() == 10)
pq.poll()
print(pq.peek() == 15)
pq.poll()
print(pq.peek() == 17)
pq.poll()
print(pq.peek() == 20)
