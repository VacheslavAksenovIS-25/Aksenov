# Средствами языка Python сформировать текстовый документ (.txt), содержащий последовательность из
# целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего
# вида, предварительно выполнив обработку элементов:
# Исходные данные:
# Количество элементов:
# Отрицательные нечетные элементы:
# Сумма отрицательных нечетных элементов:
# Среднее арифметическое отрицательных нечетных элементов:
try:
    list = ['-99 6 12 -36 20 -45 100 -15']
    file = open('data.txt','w')
    file.writelines(list)
    file.close()

    file_2 = open('data_2.txt','w')
    file_2.write('Исходные данные: ')
    file_2.writelines(list)
    file_2.close

    file = open('data.txt')
    f = file.read()
    f = f.split()
    for i in range (len(f)):
        f[i] = int(f[i])
    file.close()

    file = open('data.txt')
    neg_odd = []
    sum_of_neg_odd = 0
    sr_ar = 0
    count = 0
    for i in range(len(f)):
        if f[i] < 0 and f[i] % 2 != 0:
            neg_odd.append(f[i])
            sum_of_neg_odd += f[i]
            count += 1
            sr_ar = sum_of_neg_odd // count

    file_2 = open('data_2.txt','a')
    file_2.write(f'\nКоличество элементов:  {len(f)}' 
                 f'\nОтрицательные нечетные числа: {neg_odd}'
                 f'\nСумма отрицательных нечетных чисел:  {sum_of_neg_odd}'
                 f'\nСреднее арифметическое отрицательных нечетных элементов: {sr_ar}')
    file_2.close()
except ValueError:
    print('Данные неверны')




