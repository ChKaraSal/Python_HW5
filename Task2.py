# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

number_a = int(input("Enter number A: "))
number_b = int(input("Enter number B: "))

def sum(number_a, number_b):
    if number_a == 0:
        return number_b
    else:
        return sum(number_a - 1, number_b + 1)

print(sum(number_a, number_b))