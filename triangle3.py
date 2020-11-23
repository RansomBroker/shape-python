n = 5
for i in range(n):
    print(i+1, end=' ')
    for j in range(n-i):
        print(j+1, end=' ')
    print()