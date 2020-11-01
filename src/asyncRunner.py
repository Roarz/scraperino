from sendCharInfo import check_player, get_player_obj, send_player
from onlineList import get_online_list, filter_players
from charInfo import get_player_info_table, response_to_player
import time, sys, os
import asyncio
import requests
import re
import aiohttp

def time_convert(sec):
    sec = sec % 60
    return ("Time Lapsed = {0} secs".format(sec))

def char_to_url(playerName):
    res_str = re.sub(r"\s","+",playerName)
    requestString = "https://www.tibia.com/community/?subtopic=characters&name=%s" % res_str
    return requestString

async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                player = response_to_player(resp)
                players.append(player)
                send_player(player)
                #print("Successfully got url {} with response of length {}.".format(url, player.name))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def main(urls, amount):
    ret = await asyncio.gather(*[get(url) for url in urls])
    print("Finalized all. ret is a list of len {} outputs.".format(len(ret)))
    print("done")

def addRequests(targets):
    for t in targets:
        req = char_to_url(t.name)
        urls.append(req)
        print(req)

players = []
urls = []
onlineList = get_online_list("Wintera")
targets = filter_players(onlineList, minLvl=2, maxLvl=20)
addRequests(targets)

amount = len(urls)
print("total targets: %s" % amount)

start = time.time()
asyncio.run(main(urls, amount))
end = time.time()

print("")
print("Took {} seconds to pull {} characters.".format(end - start, amount))
print("")

time.sleep(10)