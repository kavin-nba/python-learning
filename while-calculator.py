print("the options are + - * / // ** % == != > < ")
while True:
    operator = input('operator: ')
    if operator == 'exit':
        print("program exit")
        break
    number1 = int(input('first num: '))
    number2 = int(input('second num: '))
    if operator == '+':
        print(number1 + number2)
    elif operator == '-':
        print(number1 - number2)
    elif operator == '*':
        print(number1 * number2)
    elif operator == '/':
        print(number1 / number2)
    elif operator == '//':
        print(number1 // number2)
    elif operator == '**':
        print(number1 ** number2)
    elif operator == '%':
        print(number1 % number2)
    elif operator == '==':
        print("num1 is equal to num2")
    elif operator == '!=':
        print("num1 is not equal to num2")
    elif operator == '>':
        if number1 > number2:
            print("num1 is greater than num2")
        else:
            print("num1 is not greater than num2")
    elif operator == '<':
        if number1 < number2:
            print("num1 is is lesser than num2")
    # elif operator == 'exit':
    #     print("program exit")
    #     break
    else:
        print("wrong operator")