# Из списка: ['Валентин','Петр','Анна','Евгений','Константин','Валерия','Юлия']
# получить новый список, в котором длина слов не превышает 5 символов.

list_1 = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
new_list = (i for i in list_1  if len(i) <= 5 )
print(f'Новый список: {list(new_list)}')
