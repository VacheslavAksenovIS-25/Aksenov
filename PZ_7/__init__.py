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
    input_str = "([]())"
    result = check_brackets(input_str)
    print(result)
except ValueError:
    print('Данные введены неверно')



def check(input_string):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for i, char in enumerate(input_string):
        if char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if not stack or stack[-1][0] != brackets[char]:
                return i + 1
            else:
                stack.pop()
    if stack:
        return stack[-1][1] + 1
    return 0
try:
   input_string = "[{()}]"
   result = check(input_string)
   print(result)
except ValueError:
    print('Данные введены неверно')