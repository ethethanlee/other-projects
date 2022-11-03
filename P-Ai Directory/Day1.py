import requests
import time
# Lv 1 Nuguri; WQWr9bDJEPMV2qBojfnZp6NmbRf03uPkWvKlxuDyKCwiv40KcB4JqFhEesWUWI9cxhDcayZRM2X8sQ = puuid

NEW_API_KEY = "RGAPI-baa3b759-cad6-4cc3-994f-5a8415ddbd5d"
# REGION = ""
# SUMMONER_NAME = ""


def get_input():
    global REGION
    global SUMMONER_NAME
    REGION = (str) (input("what REGION bro (all lower e.g. na1): "))
    SUMMONER_NAME = (str) (input("what ur name: "))
    return (REGION, SUMMONER_NAME)

def request_summoner_data (region, summoner_name):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + NEW_API_KEY
    response = requests.get(url)
    # print (response)
    return response.json()

def get_puuid():
    # REGION = (str) (input("what REGION bro (all lower e.g. na1): "))
    # SUMMONER_NAME = (str) (input("what ur name: "))

    response_JSON = request_summoner_data(REGION, SUMMONER_NAME)
    return response_JSON['puuid']

def get_soloq_match(num):
    if REGION == 'br1' or REGION == 'na1' or REGION == 'la1' or REGION == 'la2':
        the_region = 'americas'
    elif REGION == 'eun1' or REGION == 'euw1' or REGION == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'
    url = 'https://' + the_region + '.api.riotgames.com/lol/match/v5/matches/by-puuid/' + get_puuid() + '/ids?queue=420&type=ranked&start=0&count=50&api_key=' + NEW_API_KEY
    response = requests.get(url)
    our_response = response.json()
    match_ID = our_response[num] 
    return match_ID

def get_data_red(parameter, numb):
    if REGION == 'br1' or REGION == 'na1' or REGION == 'la1' or REGION == 'la2':
        the_region = 'americas'
    elif REGION == 'eun1' or REGION == 'euw1' or REGION == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'

    url = "https://" + the_region + ".api.riotgames.com/lol/match/v5/matches/" + get_soloq_match(numb) + "?api_key=" + NEW_API_KEY
    response = requests.get(url)
    our_response = response.json()
    number = 0
    for i in range(5,10):
        number = our_response['info']['participants'][i][parameter] + number
    return number

def get_data_blue(parameter, numb):
    if REGION == 'br1' or REGION == 'na1' or REGION == 'la1' or REGION == 'la2':
        the_region = 'americas'
    elif REGION == 'eun1' or REGION == 'euw1' or REGION == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'

    url = "https://" + the_region + ".api.riotgames.com/lol/match/v5/matches/" + get_soloq_match(numb) + "?api_key=" + NEW_API_KEY
    response = requests.get(url)
    our_response = response.json()
    number = 0
    for i in range(5):
        number = our_response['info']['participants'][i][parameter] + number
    return number

def game_length(numb):
    if REGION == 'br1' or REGION == 'na1' or REGION == 'la1' or REGION == 'la2':
        the_region = 'americas'
    elif REGION == 'eun1' or REGION == 'euw1' or REGION == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'

    url = "https://" + the_region + ".api.riotgames.com/lol/match/v5/matches/" + get_soloq_match(numb) + "?api_key=" + NEW_API_KEY
    response = requests.get(url)
    our_response = response.json()
    number = 0
    number = our_response['info']['participants'][1]["timePlayed"]
    return number

def winner(numb):
    if REGION == 'br1' or REGION == 'na1' or REGION == 'la1' or REGION == 'la2':
        the_region = 'americas'
    elif REGION == 'eun1' or REGION == 'euw1' or REGION == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'

    url = "https://" + the_region + ".api.riotgames.com/lol/match/v5/matches/" + get_soloq_match(numb) + "?api_key=" + NEW_API_KEY
    response = requests.get(url)
    our_response = response.json()
    win_variable = our_response['info']['teams'][1]["win"]
    if win_variable:
        return (0)
    else :
        return (1)

def num_kills_blue(numb):
    return get_data_blue("kills", numb)
def num_kills_red(numb):
    return get_data_red("kills", numb)
def assists_red(numb):
    return get_data_red("assists", numb)
def assists_blue(numb):
    return get_data_blue("assists", numb)
def gold_red(numb):
    return get_data_red("goldEarned", numb)
def gold_blue(numb):
    return get_data_blue("goldEarned", numb)

    


get_input()
print ("blue team kills: " + str(num_kills_blue(0)))
print ("red team kills: " + str(num_kills_red(0)))
print (gold_red(0))
print (gold_blue(0))
print (assists_red(0))
print (assists_blue(0))
print (game_length(0))
print (winner(0))

# import csv

# def CSV_Data():
#     with open('match_data.csv', mode='w') as csvfile:
#         csv_writer = csv.writer(csvfile, delimiter = ',' )
#         csv_writer.writerow(['num_kills_blue', 'num_kills_red', 'gold_red', 'gold_blue', 'assists_red', 'assists_blue', 'game_length', 'winner'])
#         for i in range(20):
#             csv_writer.writerow([num_kills_blue(i), num_kills_red(i), gold_red(i), gold_blue(i), assists_red(i), assists_blue(i), game_length(i), winner(i)])
#             time.sleep(10)
#         return csv_writer

# print (CSV_Data())