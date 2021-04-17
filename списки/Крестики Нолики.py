def draf_board(board):
    for i in range(3):
        print(board[i * 3], board[1 + i * 3], board[2 + i * 3])


def play(xo):
    correct = False
    while not correct:
        answer = input(f"Куда поставим {xo} ? ")
        try:
            answer = int(answer)
        except:
            print("Не корректный ввод, вы уверенны, что ввели число?")
            continue
        if answer >= 1 and answer <= 9:
            if str(board[answer - 1]) != "X" and str(board[answer - 1]) != "0":
                board[answer - 1] = xo
                correct = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9")


def chek_win(board):
    win_coords = ((0, 1, 2), (1, 4, 7), (2, 5, 8), (0, 3, 6), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6))
    for coord in win_coords:
        if board[coord[0]] == board[coord[1]] == board[coord[2]]:
            return board[coord[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draf_board(board)
        if counter % 2 == 0:
            play("X")
        else:
            play("0")
        counter += 1
        if counter > 4:
            if str(chek_win(board)) != "False":
                print(chek_win(board), "Winner")
                win = True
                break
        if counter == 9:
            print("ничья")
            win = True
            break



board = list(range(1, 10))
main(board)


