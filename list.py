l = [1, 2, 3, 4]

l1 = [1, 6, 3, 8]
l2 = [5, 6, 1, 8]

print(l1+l2)

m1 = [1,2,3,4]
m2 = [5,6,7,8]
m = [l1,l2]     

print(m[0][3])


print(l1[0::2])
print(l1[::-1])
print(l1[-1])

print(len(l))
l.append(5)                  #just add 5 at end
l.insert(1,10)               #insert 10 at index 1
l.extend([55,66,77])         #add 55,66,77 at end 
print(l)
l.remove(3)                  #value 3 removed
l.pop(2)                     #value at index 2 removed

print(sum(l1))
print(max(l1))
print(min(l1))

l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l2.reverse()
print(l2)

print(l1.index(6))

l1 = [1, 6, 3, 8, 5, 9, 2]
del l1[0:3]
print(l1)