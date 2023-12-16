# Дана строка, содержащая латинские буквы и скобки трех видов : "()", "[]", "{}".
# Если скобки расставлены правильно(то есть каждой открывающей соответствует закрывающая скобка того же вида),
# то вывести число 0. В противном случае вывести или номер позиции, в которой расположена первая ошибочная скобка,
# или, если закрывающих скобок не хватает, число 1.

def check_brackets(s):
    stack = []
    for i, char in enumerate(s):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if not stack:
                return i + 1
            last, pos = stack.pop()
            if (char == ')' and last != '(') or (char == ']' and last != '[') or (char == '}' and last != '{'):
                return i + 1
    if stack:
        return stack[0][1] + 1
    return 0

try:
    input_str = "({[]})"
    result = check_brackets(input_str)
    print(result)
except ValueError:
    print('Данные введены неверно')