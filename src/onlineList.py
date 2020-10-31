import requests
import lxml
from bs4 import BeautifulSoup, SoupStrainer
import pyperclip
import re
from functions import list_contains_string, char_data_row
import module1

def online_player_record(css_class):
    return css_class is not None and (css_class=="Odd" or css_class=="Even")

def get_online_list(world):
    requestString = "https://www.tibia.com/community/?subtopic=worlds&world=%s&order=level_asc" % world
    source = requests.get(requestString).text
    rows = SoupStrainer(class_=online_player_record)
    soup = BeautifulSoup(source, "html.parser", parse_only=rows)
    return soup

def parse_online_player(row):
    props = []
    for element in row:
        props.append(element.text)
    player = module1.OnlinePlayer(props[0],props[1],props[2])
    return player

def filter_players(onlineList):
    playersList = []
    for row in onlineList:
        player = parse_online_player(row)
        if player.level > 100 and player.level < 250:
            #print(player.name, player.level, player.vocation)
            playersList.append(player)
    return playersList

onlineList = get_online_list("Wintera")
targets = filter_players(onlineList)
for t in targets:
    print(t.name, t.level, t.vocation)