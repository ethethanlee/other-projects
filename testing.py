# Python3 code to demonstrate 
# swap of key and value
   
# initializing dictionary
d = {'doubledouble': 'q', 'hamburger' : 'w', 'cheeseburger' : 'e', 'frenchfries': 'r',
'3x3': 'qq', '4x4': 'ww', 'animalfries': 'ee', 'milkshake': 'rr', 
'smalldrink': 'qqq', 'mediumdrink': 'www', 'largedrink': 'eee', 'xlargedrink': 'rrr',
'dblcombo': 'qqqq', 'hamcombo': 'wwww', 'cheesecombo': 'eeee',
'milk': 'wwwww', 'coffee':'eeeee'
}
d_swap = {v: k for k, v in d.items()}
print(d_swap)