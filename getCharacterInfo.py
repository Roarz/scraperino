import requests
import lxml
from bs4 import BeautifulSoup
import pyperclip
import re
from filterData import *

source = requests.get('https://www.tibia.com/community/?subtopic=characters&name=Asfgdf').text
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
            results[key] = val
            print(key, val)

        

print("done")