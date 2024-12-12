n = int(input())
x = -1
while n > 0:
    y = n % 10 
    if y < x:
        print("NO")
        break
    x = y
    n //= 10
else:
    print("YES")