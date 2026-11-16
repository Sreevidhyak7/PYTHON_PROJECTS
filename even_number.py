counter = 0

limit = int(input("Enter limit: "))
while counter != limit:
    counter += 1
    if counter%2 == 1:
        continue
    print(counter