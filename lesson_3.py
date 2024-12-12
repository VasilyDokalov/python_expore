n=int(input())
x=0
max1=0
min1=9
while n>=10:
    x=n%10
    if x>max1:
        max1=x
    if x<min1:
        min1=x        
    n=n//10
if n>max1:
    max1=n
if n<min1:
    min1=n
print('Максимальная цифра равна', max1)
print('Минимальная цифра равна', min1)



