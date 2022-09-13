innout_dict = {'doubledouble': 3.45, 'hamburger' : 2.10, 'cheeseburger' : 2.40, 'frenchfries': 1.60,
'dblcombo': 6.70, 'hamcombo': 5.35, 'cheesecombo': 5.65,
'smalldrink': 1.50, 'mediumdrink': 1.65, 'largedrink': 1.85, 'xlargedrink': 2.05,
'milkshake': 2.15, 'milk': 0.99, 'coffee':1.35,
'3x3': 4.45, '4x4': 5.50, 'animalfries': 3.40}

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
        print('last person owes ' + str(round(counter, 2)))
        break
    if ret == ' ':
        counter = counter*1.0725
        print('this person owes ' + str(round(counter, 2)))
        counter = 0
    else:
        counter += innout_dict.get(keyboard_dict.get(ret))