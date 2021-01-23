# HOME WORKS
N = 'y'
while N == 'y':
    num1 = int(input("Введите первое число"))
    o = (input("Введите операцию"))
    num2 = int(input("Введите второе число"))
    if o == '+':
        print(num1 + num2)
    elif o == '-':
        print(num1 - num2)
    elif o == '*':
        print(num1 * num2)
    elif o == '/':
        print(num1 / num2)
    elif o == '%':
        print(num1 % num2)
    elif o == '+-':
        print(num1 + - num2)
    else:
        print("Error")
        N = input("Введите 'y' чтобы продолжить, или любую клавишу чтобы завершить")

