# def lists(a):
#     b = [i for i in a if i % 2 == 0]
#     c = [i for i in a if i % 2 != 0]
#     summa = map(sum,zip(b,c))
#     print(b)
#     print(c)
#     print(list(summa))
# a = [8, 4, 5, 6, 78, 1, 2]
# sq = lists(a)

# a = [8, 4, 5, 6, 78, 1, 2]
# b = list(i for i in a if i%2 == 0)
# c = list(i for i in a if i%2 != 0)
# print(list(b))
# print(list(c))
# summa = sum(a,b)
# print(summa)

# a = [1, 2, 3, 4,6]
# b = [1, 2, 3, 12]
#
# # обработка
# c = map(sum, zip(a + [0,]*(len(b)-len(a)), b + [0,]*(len(a)-len(b))))
#
# # вывод результата
# print(list(c))


# a = [15, 4, 6 , 3, 2, 3, 15]
#
# b = [i for i in a if i%2 == 0]
# c = [i for i in a if i%2 != 0]
# summa = map(sum, zip(b + [0,] * (len(c)-len(b)), c + [0,] * (len(b)-len(c))))
# min_elem = min(map(sum, zip(b + [0,] * (len(c)-len(b)), c + [0,] * (len(b)-len(c)))))
# print(f'Последовательность: {a}')
# print(f'Четные элементы: {b}')
# print(f'Нечетные элементы: {c}')
# print(f'Суммирование соответствующих элементов: {list(summa)}')
# print(f'Минимальный элемент полученной последовательности: {min_elem}')






