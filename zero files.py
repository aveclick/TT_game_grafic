"""""

import pickle


# нулевой файл saveever
num_strok_dict = dict()
num_stolbets_dict = dict()
count_pobeda_dict = dict()
win_size_dict = dict()

name = 'Tester'
num_strok = 4
num_stolbets = 3
count_pobeda = 1
win_size = 100

num_strok_dict[str(name)] = num_strok
num_stolbets_dict[str(name)] = num_stolbets
count_pobeda_dict[str(name)] = count_pobeda
win_size_dict[str(name)] = win_size

with open("saveever", "wb") as f:
    pickle.dump(num_strok_dict, f)
    pickle.dump(num_stolbets_dict, f)
    pickle.dump(count_pobeda_dict, f)
    pickle.dump(win_size_dict, f)
# нулевой файл saveres
games_dict = dict()
wins_dict = dict()
lose_dict = dict()
tie_dict = dict()

name = 'Tester'
games = 0
wins = 0
lose = 0
tie = 0

games_dict[str(name)] = games
wins_dict[str(name)] = wins
lose_dict[str(name)] = lose
tie_dict[str(name)] = tie

with open("saveres", "wb") as f:
    pickle.dump(games_dict, f)
    pickle.dump(wins_dict, f)
    pickle.dump(lose_dict, f)
    pickle.dump(tie_dict, f)

# нулевой файл savegam
import pickle
num_strok_dict = dict()
num_stolbets_dict = dict()
count_pobeda_dict = dict()
up_me_dict = dict()
sign_of_user_dict = dict()
sign_of_computer_dict = dict()
array_game_dict = dict()

name = 'Tester'
num_strok = 4
num_stolbets = 3
count_pobeda = 1
up_me = '+'
sign_of_user = 'X'
sign_of_computer = 'O'
array_game = [[" " for j in range(num_stolbets)] for i in range(num_strok)]


num_strok_dict[str(name)] = num_strok
num_stolbets_dict[str(name)] = num_stolbets
count_pobeda_dict[str(name)] = count_pobeda
up_me_dict[str(name)] = up_me
sign_of_user_dict[str(name)] = sign_of_user
sign_of_computer_dict[str(name)] = sign_of_computer
array_game_dict[str(name)] = array_game

with open("savegam", "wb") as f:
    pickle.dump(num_strok_dict, f)
    pickle.dump(num_stolbets_dict, f)
    pickle.dump(count_pobeda_dict, f)
    pickle.dump(up_me_dict, f)
    pickle.dump(sign_of_user_dict, f)
    pickle.dump(sign_of_computer_dict, f)
    pickle.dump(array_game_dict, f)
"""