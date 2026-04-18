# #find union and  of 2 set
a = {1,2,3,4,5}
b = {3,4,5,6,7,8}
c = a.union(b)
print("This is the a union of two set")
print(c)
#Find the union of 3 set 
A = {5,12,52,0,8}
B = {2,5,1,9,8}
C = {4,5,6,0,10}
D = A.union(B,C)
print("This is the union of three set")
print(D)

#Intersection of set
#intersection of 2 set
E = {5,2,6,6,7,1}
F = {5,3,11}
G = a.intersection(b)
print("This is the intersection of two set")
print(G)
#intersection of 3 set
e = {5,2,4,6,7,1}
f = {5,3,11}
g = {4,5,12,2,1,0}
h = A.intersection(B,C)
print("This is the intersection of three set")
print(h)

# difference of set
ab = {23,5,1,12,4,6,7}
ad = {6,11,12,4,5,2,15,21,22,33}
ag = ab.difference(ad)
am = ad.difference(ab)
print("This is the difference of 2 set")
print(ag)
print(am)
#write a program to calculate symmetric difference of two set
Y = {12,2,0,3,8}
z = {15,10,12,3,6}
k = Y.difference(z)
j = z.difference(Y)
print("These are the differences of the two set")
print(k)
print(j)

st = {1,2,3,4,5,6,7,8,}
print(st)
print(len(st))
print(min(st))
print(max(st))


# 1. Prompt the user for the first set of numbers
input1 = input("Enter five numbers for set1 separated by space: ")
# Convert the string input into a set of integers
set1 = set(map(int, input1.split()))

# 2. Prompt the user for the second set of numbers
input2 = input("Enter five numbers for set2 separated by space: ")
# Convert the string input into a set of integers
set2 = set(map(int, input2.split()))

# 3. Print both sets
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

print("-" * 30)

# 4. Perform Set Operations
# Union: All unique elements from both sets
print(f"Union: {set1 | set2}")

# Intersection: Only elements present in both sets
print(f"Intersection: {set1 & set2}")

# Difference: Elements in set1 that are NOT in set2
print(f"Difference (set1 - set2): {set1 - set2}")

# Symmetric Difference: Elements in either set, but NOT in both
print(f"Symmetric Difference: {set1 ^ set2}")