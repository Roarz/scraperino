import requests
import lxml
from bs4 import BeautifulSoup
import pyperclip
import re
from functions import list_contains_string, char_data_row, char_deaths_row
import module1

def character_info_table(characterName):
    requestString = "https://www.tibia.com/community/?subtopic=characters&name=%s" % characterName
    source = requests.get(requestString).text
    soup = BeautifulSoup(source,'lxml')
    charContainer = soup.find('div','BoxContent')
    return charContainer

def get_char_stats(charInfo):
    stats = charInfo.find_all(char_data_row)
    results = {}
    deaths = {}
    character_information = ["Name:","Sex:","Vocation:","Level:","World:","Residence:","Guild","Last Login:"]

    for row in stats:
        col = row.findChildren("td")
        #print(row.contents)
        if len(col) == 2:
            #print(row)
            key = col[0].text
            val = col[1].text

            if list_contains_string(character_information, key):
                normalisedKey = re.search(r"(.*):", key)
                normalisedKey = normalisedKey.group(1)
                results[normalisedKey] = val

        if row.string == "Character Deaths":
            deathsRows = row.parent.findChildren("tr")
            print("info: ", len(deathsRows))
            for death in deathsRows:
                cols = death.findChildren("td")
                if len(cols) == 2:
                    deaths[cols[0].text] = cols[1].text

    character = module1.Character(results["Name"],results["Sex"],results["Vocation"],results["Level"],results["World"],results["Residence"],results["Last Login"])
    character.deaths = deaths

    return character

def display_character_info(character):
    for k in char.deaths.values():
        print(k)
    print("")
    print("char: ", char.name, char.level, char.lastLogin, len(char.deaths), "deaths")


charName = "Cleitinho Tacaesside"
charInfo = character_info_table(charName)
char = get_char_stats(charInfo)
display_character_info(char)