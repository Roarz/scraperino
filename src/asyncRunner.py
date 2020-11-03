from sendCharInfo import send_player
from onlineList import get_online_list, filter_players
from charInfo import response_to_player
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

failedUrls = []
async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                player = response_to_player(resp)
                players.append(player)
                send_player(player)
                #print("Successfully got url {} with response of length {}.".format(url, player.name))
    except AttributeError as ae:
        print("attr err to get url {} due to {}.".format(url, ae.__class__))
        failedUrls.append(url)
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def chunk_in_chunks(chunks, *do):
    for x in range(0, len(chunks)):
        for y in chunks[x]:
            print(y)
        
async def main(urls, amount):
    ret = await asyncio.gather(*[get(url) for url in urls])
    print("{} urls parsed".format(len(ret)))
    for f in failedUrls:
        print("failed url: %s" % f)
    failed = await asyncio.gather(*[get(url.lower()) for url in failedUrls])
    print("{} failed ones".format(len(failed)))

def addRequests(targets):
    for t in targets:
        req = char_to_url(t.name)
        urls.append(req)
        print(req)

players = []
urls = []
onlineList = get_online_list("Wintera")
targets = filter_players(onlineList, minLvl=30, maxLvl=300)
addRequests(targets)
amount = len(urls)
print("total targets: %s" % amount)


groupSize = 50
start = time.time()
urlChunks = list(chunks(urls, groupSize))

for i in range(0, len(urlChunks)):
    asyncio.run(main(urlChunks[i], 1))
    print("done group: ", i+1, " of ", len(urlChunks))
    time.sleep(2)

end = time.time()



print("")
print("Took {} seconds to pull {} characters.".format(end - start, amount))
print("")