a = [5, 2, 4, 6, 1, 3]
j = 2
for j in range(len(a)):
    key = a[j]
    i = j-1
    while i>0 and a[i] < key:
        a[i+1] = a[i]
        i = i-1
    a[i+1] = key
    print(a)
