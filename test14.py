#Sets in python

l=[1,2,3,4,5,4,3,2,4,5,6]
a=set(l)
print(a)
k={1,2,3,4,5}
print(type(k))
print(dir(set()))
l={1,2,3}
m={2,3,4,5}
print(len(l))
print(len(m))
print(len(m))
for i in m:
  print(i)
l.add(1)
l.update([11,2,15])
print(l)
l.add(20)
print(l)
l.remove(20)
print(l)
l.discard(15)
print(l)
print(l|m)
a={1,2,3}
b={4,5,6,2}
print(a|b)
print(a.intersection(b))
print(a-b)
print(b-a)
print(dir(set()))
print(a.union(b))
print(a.intersection(b))
















