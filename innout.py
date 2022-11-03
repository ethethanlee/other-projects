innout_dict = {'doubledouble': 4.85, 'hamburger' : 3.05, 'cheeseburger' : 3.40, 'frenchfries': 2.10,
'dblcombo': 8.95, 'hamcombo': 7.15, 'cheesecombo': 7.50,
'smalldrink': 1.85, 'mediumdrink': 2.00, 'largedrink': 2.20, 'xlargedrink': 2.40,
'milkshake': 2.75, 'milk': 0.99, 'coffee':1.25,
'3x3': .0, '4x4': .0, 'animalfries': .0}

keyboard_dict = {
'q': 'doubledouble', 'w': 'hamburger', 'e': 'cheeseburger', 'r': 'frenchfries', 
'qq': '3x3', 'ww': '4x4', 'ee': 'animalfries', 'rr': 'milkshake', 
'qqq': 'smalldrink', 'www': 'mediumdrink', 'eee': 'largedrink', 'rrr': 'xlargedrink', 
'qqqq': 'dblcombo', 'wwww': 'hamcombo', 'eeee': 'cheesecombo', 
'qqqqq': 'milk', 'eeeee': 'coffee'}
counter = 0.0
while True:
    ret = input('value: ')
    if ret == 'p':
        counter = counter*1.0725
        print('last person owes ' + str(round(counter, 2)))
        break
    if ret == ' ':
        counter = counter*1.0725
        print('this person owes ' + str(round(counter, 2)))
        counter = 0
    else:
        counter += innout_dict.get(keyboard_dict.get(ret))