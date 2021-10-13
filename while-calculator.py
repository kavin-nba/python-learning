print("the options are + - * / // ** % == != > < ")
while True:
    a = int(input('first num: '))
    op = input('operator: ')
    c = int(input('second num: '))
    if op == '+':
        print(b + d)
    elif op == '-':
        print(b - d)
    elif op == '*':
        print(b * d)
    elif op == '/':
        print(b / d)
    elif op == '//':
        print(b // d)
    elif op == '**':
        print(b ** d)
    elif op == '%':
        print(b % d)
    elif op == '==':
        print("num1 is equal to num2")
    elif op == '!=':
        print("num1 is not equal to num2")
    elif op == '>':
        print("num1 is greater than num2")
    elif op == '<':
        print("num1 is is lesser than num2")
    q = input('do you want to continue?: ')
    if q == 'y':
        continue
    else:
        break