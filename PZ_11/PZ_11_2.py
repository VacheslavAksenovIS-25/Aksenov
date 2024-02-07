# Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно поставив последнюю строку между первой и второй.
try:
    t = 0
    d = 0
    for i in open('text18-1.txt', encoding= 'UTF-16'):
        print(i,end='')
        t+=1
        for j in i:
            if j.isupper():
                d += 1
    print(end = '\n')
    print(f'Количество букв в верхнем регистре: {d}')

    f1 = open('text18-1.txt', encoding= 'UTF-16')
    l = f1.readlines()
    l[6],l[1] = l[1],l[6]
    l[6],l[2] = l[2],l[6]
    l[6],l[3] = l[3],l[6]
    l[6],l[4] = l[4],l[6]
    l[6],l[5] = l[5],l[6]

    f1.close()
    f2 = open('text18-2.txt','w')
    f2.writelines(l)
    f2.close()
except ValueError:
    print('Данные неверны')