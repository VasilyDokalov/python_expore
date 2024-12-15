# На вход программе подаются два натуральных числа(a< b). 
# Напишите программу, которая находит натуральное число из отрезка [a;b] (от a до b включительно) с максимальной суммой делителей.
# Если чисел с максимальной суммой делителей несколько, то искомым числом является наибольшее из них.
# Ваша программа должна выводить ответ в следующем формате:
# <число с максимальной суммой делителей> <сумма делителей этого числа>

a=int(input())
b=int(input())
max_sum = 0
result_num = 0
for num in range(a, b + 1):
    current_sum = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            current_sum += divisor
    if current_sum > max_sum or (current_sum == max_sum and num > result_num):
        max_sum = current_sum
        result_num = num

print(result_num, max_sum)
