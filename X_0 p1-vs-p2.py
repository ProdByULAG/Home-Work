Theline = {'1': '', '2': '', '3': '',
           '4': '', '5': '', '6': '',
           '7': '', '8': '', '9': ''}

TheLine_keys = []

for key in Theline:
    TheLine_keys.append(key)

def printLine(Line):
    print('___')
    print(Line['1'] + '|' + Line['2'] + '|' + Line['3'])
    print('___')
    print(Line['4'] + '|' + Line['5'] + '|' + Line['6'])
    print('___')
    print(Line['7'] + '|' + Line['8'] + '|' + Line['9'])

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printLine(Theline)
        print("Твой ход," + turn + ".Куда ходим?")

        move = input()

        if Theline[move] ==' ':
            Theline[move] = turn
            count += 1
        else:
            print("Это место занято.\nКуда ходим?")
            continue

        if count >=5:
            if Theline['1'] == Theline ['2'] == Theline['3'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['4'] == Theline ['5'] == Theline['6'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['7'] == Theline ['8'] == Theline['9'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['1'] == Theline ['5'] == Theline['9'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['3'] == Theline ['5'] == Theline['7'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['1'] == Theline ['4'] == Theline['7'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['2'] == Theline ['5'] == Theline['8'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break
            elif Theline['3'] == Theline ['6'] == Theline['9'] != ' ':
                printLine(Theline)
                print("\n Игра окончена. \n")
                print("****" + turn + "Победа. ****")
                break

        if count == 9:
            print("\n Игра окончена. \n")
            print("Ничья")

        if turn == 'x':
            turn = '0'
        else:
            turn = 'x'

    restart = input("Еще одну партию? Нажмите (y/n)")
    if restart == "y" or restart == "Y":
        for key in TheLine_keys:
            Theline[key] = " "

            game()


game()
