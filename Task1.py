# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

number_a = int(input("Enter number A: "))
number_b = int(input("Enter number B: "))

def funcial(number_a, number_b):
    if number_b == 0:
        return 1
    return number_a * funcial(number_a, number_b - 1)

print(funcial(number_a, number_b))