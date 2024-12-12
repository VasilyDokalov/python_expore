n=int(input())
x=0
cnt=0
y=1
z=n%10
firstN=n
while firstN>=10:
    firstN//=10
while n>0:
    x+=(n%10)
    y*=(n%10)
    cnt+=1
    n//=10
print(x)
print(cnt)
print(y)
print(x/cnt)
print(firstN)
print(firstN+z)