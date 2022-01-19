A = {1, 2, 3, 4, 7, 8}
B = {2, 4, 5, 6, 11, 12}
# Phép giao
print("A giao B: ", A & B)
print("A giao B: ", A.intersection(B))
#Phép hợp
print("A hợp B: ", A | B)
print("A hợp B: ", A.union(B))
# Phép trừ
print("A trừ B: ", A - B)
print("A trừ B: ", A.difference(B))
# Phương thức add()
A.add(9)
A.add(10)
print("A: ", A)