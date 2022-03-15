from treelist import TreeList

a = TreeList([1, 2, 3, 3, 3, 4, 5, 7, 8])

print(f"a[{a.leftmost(lambda x: x > 3)}] > 3")

print(a)
for i in range(1, 8 + 1):
  print(f"{i} => {a.bisect_left(i)} .. {a.bisect_right(i)}")
