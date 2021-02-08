white_figure_vert = int(input("Введите позицию белой фигуры по вертикали:"))
white_figure_gorz = int(input("Введите позицию белой фигуры по горизонтали:"))

black_figure_vert = int(input("Введите позицию черной фигуры по вертикали:"))
black_figure_gorz = int(input("Введите позицию черной фигуры по горизонтали:"))

move_vert = int(input("Куда идем по вертикали?:"))
move_gorz = int(input("Куда идем по горизонтали?:"))

which_figure = input("Какой фигурой ходим?:")

if which_figure == "Ладья":
    if move_vert == white_figure_vert or move_gorz == white_figure_gorz:
        if move_vert == black_figure_vert:
            print("Вы не можете ходить!")
    elif move_gorz == black_figure_gorz:
        print("Вы не можете ходить!")
    else:
        print("Вы вообще не можете туда ходить!")
else:
    print("ты тупой")


kon_hod = []

if which_figure == "Конь":
