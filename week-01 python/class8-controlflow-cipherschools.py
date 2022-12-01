n=9
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end=' ')
    print()