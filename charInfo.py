import requests
import lxml
from bs4 import BeautifulSoup
import pyperclip
import re
from functions import list_contains_string, char_data_row


def get_char_stats(characterName): 
    requestString = "https://www.tibia.com/community/?subtopic=characters&name=%s" % characterName
    source = requests.get(requestString).text
    soup = BeautifulSoup(source,'lxml')
    charContainer = soup.find('div','BoxContent')
    charInfo = charContainer.find_all(char_data_row)

    results = {}

    character_information = ["Name:","Sex:","Vocation:","Level:","World:","Residence:","Guild","Last Login:"]

    for row in charInfo:
        #print(x.nextSibling)
        col = row.findChildren("td")
        if len(col) > 1:
            #print(row)
            key = col[0].text
            val = col[1].text

            if list_contains_string(character_information, key):
                normalisedKey = re.search(r"(.*):", key)
                normalisedKey = normalisedKey.group(1)
                results[normalisedKey] = val
    
    return results

def get_deaths(characterName):
    charInfo = get_char_stats(characterName)
    print(charInfo["World"])
    print(charInfo["Name"])
    print(charInfo["Level"])

get_deaths("ya")
