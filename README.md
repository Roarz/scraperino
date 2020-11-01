# scraperino
scrape tibia.com to find char info

# structure:
Python console app scrape the website every so often. If it finds something interesting, pump it out over the messaging broker. Client app displays the messages from queue.

# todo:
1. optimise: caching (maybe not needed?)
2. optimise: if no deaths, skip as we dont care
3. every 30 seconds, check these players
4. pick criteria for players we are interested in

