

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
sign_of_user_dict = dict()
sign_of_computer_dict = dict()
buttons_list_dict = dict()
win_size_dict = dict()
first_dict = dict()

name = 'Tester'
num_strok = 4
num_stolbets = 3
count_pobeda = 1
sign_of_user = 'X'
sign_of_computer = 'O'
buttons_list = ['', 'O', '', '', 'X', '', 'X', '', '']
win_size = 50
first = 0

num_strok_dict[str(name)] = num_strok
num_stolbets_dict[str(name)] = num_stolbets
count_pobeda_dict[str(name)] = count_pobeda
sign_of_user_dict[str(name)] = sign_of_user
sign_of_computer_dict[str(name)] = sign_of_computer
buttons_list_dict[str(name)] = buttons_list
win_size_dict[str(name)] = win_size
first_dict[str(name)] = first

with open("savegam", "wb") as f:
    pickle.dump(num_strok_dict, f)
    pickle.dump(num_stolbets_dict, f)
    pickle.dump(count_pobeda_dict, f)
    pickle.dump(sign_of_user_dict, f)
    pickle.dump(sign_of_computer_dict, f)
    pickle.dump(buttons_list_dict, f)
    pickle.dump(win_size_dict, f)
    pickle.dump(first_dict, f)
