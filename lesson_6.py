n=int(input())
x=n%10
while n>0:
    k=n%10
    if k!=x:
        print('NO')
        break
    n//=10
else:
    print('YES')