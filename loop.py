#WHILE

i = 1
while i <= 5:
    print("hi")
    i += 1

#FOR
L = [1,2,3,4,5]

for i in L:
    print(i, end=" ")

print()

for i in range(0,5):
    print(L[i], end=" ")

print()

for i in range(len(L)):
    print(L[i], end=" ")