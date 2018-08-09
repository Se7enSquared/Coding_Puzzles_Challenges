a = []
for i in range(0, 5):
    for j in range(0, 5):
        a.append(j * j + i)
        print(a[j], end='')
    print(a[i])