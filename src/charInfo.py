import requests
import lxml
from bs4 import BeautifulSoup
import pyperclip
import re
from functions import list_contains_string, char_data_row
import module1
import asyncio
import aiohttp
import time

def get_player_info_table(playerName):
    res_str = re.sub(r"\s","+",playerName)
    requestString = "https://www.tibia.com/community/?subtopic=characters&name=%s" % res_str
    print("req string (%s)" % requestString)
    source = requests.get(requestString).text
    soup = BeautifulSoup(source,'lxml')
    charContainer = soup.find('div','BoxContent')
    return charContainer

def response_to_player(response):
    soup = BeautifulSoup(response,'lxml')
    charContainer = soup.find('div','BoxContent')
    player = parse_char_stats(charContainer)
    return player

def parse_char_stats(playerInfo):
    stats = playerInfo.find_all(char_data_row)
    results = {}
    deaths = {}
    player_information = ["Name:","Sex:","Vocation:","Level:","World:","Residence:","Last Login:"]

    for row in stats:
        col = row.findChildren("td")
        #print(row.contents)
        if len(col) == 2:
            #print(row)
            key = col[0].text
            val = col[1].text

            if list_contains_string(player_information, key):
                normalisedKey = re.search(r"(.*):", key)
                normalisedKey = normalisedKey.group(1)
                results[normalisedKey] = val

        if row.string == "Character Deaths":
            deathsRows = row.parent.findChildren("tr")
            #print("deaths count: ", len(deathsRows))
            for death in deathsRows:
                cols = death.findChildren("td")
                if len(cols) == 2:
                    deaths[cols[0].text] = cols[1].text
    
    player = module1.Player(results["Name"],results["Sex"],results["Vocation"],results["Level"],results["World"],results["Residence"],results["Last Login"])
    player.deaths = deaths

    return player

def display_player_info(player):
    print("player: ", player.name, player.level, player.lastLogin, len(player.deaths), "deaths")
    print("")
    for k in player.deaths.values():
        print(k)
    print("")
