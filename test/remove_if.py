from treelist import TreeList

a = TreeList(range(1, 9 + 1))

print(a)

a.remove_if(lambda x: x % 2 == 0)

print(a)