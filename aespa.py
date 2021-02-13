import random
import sys

# словарь для добавления x или 0
g_d = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

rand = random.choice([2, 4, 6, 8])
game_list = []  # список чтобы понимать какие места заняты
x_or_o_2 = ""  # переменная для ПК
game_count = 1  # Переменная счетчик чтобы понимать чей ход
# кортеж победных ходов
WIN = {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {1, 5, 9}
# кортеж для юзера
user_set = set()
# кортеж для пк
pk_set = set()
# опасные позиции при который игра попадает в ничью
draw = {1, 9}, {3, 7}, {1, 6}, {3, 4}, {6, 8}, {2, 5, 9}, {4, 5, 9}, {7, 6}, {1, 6, 8}, {1, 8}, {3, 8}, {5, 9}, {1, 3,
                                                                                                                 8}


# функция начало игры
def start():
    global x_or_o, x_or_o_2
    x_or_o_2 = ""
    with open("../game.txt", "w") as f:
        f.close()
    x_or_o = input("Введи чем хочешь играть: ")
    if x_or_o == "x" or x_or_o == "0":
        if x_or_o == "x":
            x_or_o_2 = "0"
        else:
            x_or_o_2 = "x"
    else:
        start()


# функция определения победителя
def win_game():
    for win in WIN:
        win = list(win)
        if g_d[win[0]] == g_d[win[1]] == g_d[win[2]] != " ":
            wins = g_d[win[0]]
            return wins


# функция бота блокировка хадов и выйгрыша
def bot():
    num = 0

    global game_count

    if g_d[5] == " ":
        g_d[5] = x_or_o_2
        num = 1
        game_list.append(5)
    for i in g_d:
        if g_d[i] == x_or_o_2:
            pk_set.add(i)
        if g_d[i] == x_or_o:
            user_set.add(i)
    # for m in draw:
    if user_set == draw[-2]:
        r = random.choice([3, 7])
        g_d[r] = x_or_o_2
        game_list.append(r)
        game_count += 1
        return
    elif g_d[2] != " " and user_set == draw[-1]:
        r = random.choice([7, 9])
        g_d[r] = x_or_o_2
        game_list.append(r)
        game_count += 1
        return
    elif user_set == draw[-4]:
        g_d[7] = x_or_o_2
        game_list.append(7)
        game_count += 1
        return
    elif user_set == draw[-3]:
        g_d[9] = x_or_o_2
        game_list.append(9)
        game_count += 1
        return
    elif user_set == draw[2]:
        g_d[3] = x_or_o_2
        game_list.append(3)
        game_count += 1
        return
    elif user_set == draw[3]:
        g_d[1] = x_or_o_2
        game_list.append(1)
        game_count += 1
        return
    elif user_set == draw[4]:
        g_d[9] = x_or_o_2
        game_list.append(9)
        game_count += 1
        return
    elif g_d[8] != " " and user_set == draw[5]:
        ra = random.choice([7, 3, 6, 4])
        g_d[ra] = x_or_o_2
        game_list.append(ra)
        game_count += 1
        return
    elif g_d[2] != " " and user_set == draw[6]:
        g_d[6] = x_or_o_2
        game_count += 1
        return
    elif user_set == draw[7]:
        d = random.choice([8, 2])
        g_d[d] = x_or_o_2
        game_list.append(d)
        game_count += 1
        return
    elif user_set == draw[8]:
        d = random.choice([3, 7])
        g_d[d] = x_or_o_2
        game_list.append(d)
        game_count += 1
        return
    elif user_set == draw[0] or user_set == draw[1]:
        g_d[rand] = x_or_o_2
        game_list.append(rand)
        game_count += 1
        return

    for x in WIN:
        pk_ = x - pk_set
        user_ = x - user_set
        pk_ = list(pk_)
        user_ = list(user_)
        if pk_[0] not in game_list and len(pk_) == 1:
            hod_list = list(pk_)
            game_list.append(hod_list[0])
            g_d[hod_list[0]] = x_or_o_2
            num = 1
            break
        elif user_[0] not in game_list and len(user_) == 1:
            hod_list = list(user_)
            game_list.append(hod_list[0])
            g_d[hod_list[0]] = x_or_o_2
            num = 1
            break
    if num == 0:
        for l in [1, 3, 7, 9]:
            if g_d[l] == " ":
                g_d[l] = x_or_o_2
                game_list.append(l)
            break
    c = 0
    l_g_d = []
    for g in g_d:
        if g_d[g] == " ":
            c += 1
            l_g_d.append(g)
    if c == 2:
        r_ = random.choice(l_g_d)
        g_d[r_] = x_or_o_2
        game_list.append(r_)
    game_count += 1
    return


# функция хода пользователя и валидности его ввода
def user():
    global game_count, user_1
    try:
        user_1 = int(input("enter 1: "))
        if user_1 in [i for i in range(1, 9 + 1)]:
            if user_1 not in game_list:
                game_count += 1
                game_list.append(user_1)
                g_d[user_1] = x_or_o
                print(game_count)
                win_game()
                return
            else:
                print("Это место уже занято")
                user()
        else:
            print("диапазон чисел от 1 до 9")
            user()
    except ValueError:
        print("Введи число!!!")
        user()


# главная функция для показа game_cart и запуска всей игры
def inputs_():
    global user_1, game_cart
    start()
    while True:

        game_cart = f"""
                                [ {g_d[1]} | {g_d[2]} | {g_d[3]} ]   
                                [ {g_d[4]} | {g_d[5]} | {g_d[6]} ]   
                                [ {g_d[7]} | {g_d[8]} | {g_d[9]} ] 
                            """
        if win_game() in ["0", "x"]:
            print(f"WIN: {win_game()}")
            print(game_cart)
            with open("../game.txt", "a", encoding="UTF-8") as f:
                f.write(game_cart)
            sys.exit()
        print(game_cart)
        with open("../game.txt", "a", encoding="UTF-8") as f:
            f.write(game_cart)
        if game_count == 11:
            print("ничья")
            sys.exit()
        if game_count % 2 != 0:
            user()
        if game_count % 2 == 0:
            bot()
    # print(game_count)
    # print(game_list)


# запуск игры
inputs_()