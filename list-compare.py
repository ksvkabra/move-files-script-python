import functools

l1 = [3, 2, 1, 4, 2]
l2 = [3, 2, 1, 4, 2]
l3 = [3, 2, 1, 4, 3]
l4 = [3, 342, 21321, 123, 7]
l5 = [3, 342, 21321, 123, 7]
l6 = [3, 2, 1, 43, 3]
l7 = [3, 2, 1, 4, 3]
l8 = l1.copy()

print(l1 == l2)  # True
print(l1 == l3)  # False
print(l3 == l2)  # False
print(l4 == l2)  # False
print(l5 == l2)  # False
print(l6 == l2)  # False
print(l7 == l3)  # True
print(l4 == l5)  # True
print(l1 == l8)  # True

for i, j in enumerate(l1[1:]):
    print(i, j)

if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, l1, l3), True):
    print("The lists l1 and l2 are the same")
else:
    print("The lists l1 and l2 are not the same")
