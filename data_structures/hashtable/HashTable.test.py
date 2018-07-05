from HashTable import HashTable

H = HashTable()
H.insert('hello', 'goodbye')
H.insert('f', 'g')

hello = H.get('hello')
g = H.get('f')

print(hello)
print(g)

H.remove('hello')
hello = H.get('hello')
print(hello)