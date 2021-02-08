# HOME WORKS
list_ = [1]
for i in list_:
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
    list_.append(i)

