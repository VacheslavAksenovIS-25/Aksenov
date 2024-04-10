# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать
# количество фамилий
# Создать новый файл, в котором выполнить замену слова "роман" на слово "произведение"
import re
re1 = re.compile(r"\n(\w+)")
with open('writer.txt','r', encoding='utf-8') as file:
    text = file.read()
    reg1 = re1.findall(text)
    print(reg1)
    print(f'Количество фамилий: {len(reg1)}')

re2 = re.compile(r"\bроман\b", re.M)
f2 = open('writer2.txt', 'w')
reg2 = re.sub( re2,"произведение",text)
f2.writelines(reg2)
f2.close()
print('Замена слова "роман" на слово "произведение" осуществлена')















