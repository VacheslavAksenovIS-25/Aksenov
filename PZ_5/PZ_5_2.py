# Описать функцию PowerA234(параметры), вычисляющую вторую, третью и четвёртую
# степень числа A и возвращающую степени соответственно в переменные B, C и D.
# С помощью этой функции найти вторую, третью и четвёртую степень пяти данных чисел.
def PowerA234(A):
    B = A**2
    C = A**3
    D = A**4
    return B, C, D

try:
    print("Введите 5 целых чисел:")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    result1 = PowerA234(num1)
    result2 = PowerA234(num2)
    result3 = PowerA234(num3)
    result4 = PowerA234(num4)
    result5 = PowerA234(num5)

    print("Степени числа", num1, ":", result1)
    print("Степени числа", num2, ":", result2)
    print("Степени числа", num3, ":", result3)
    print("Степени числа", num4, ":", result4)
    print("Степени числа", num5, ":", result5)

except ValueError:
    print('Данные введены неверно')



