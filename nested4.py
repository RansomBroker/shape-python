n = 5
spaces = n - 1
for i in range(5):
    print(i+1, end=" ")
    for j in range(spaces):
        print(' ', end=" ")

    spaces -= 1

    for k in range(0, i+1):
        print((k+n)-i, end=" ")

    print()
