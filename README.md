# scraperino
scrape tibia.com to find char info

# structure:
Python console app scrape the website every so often. If it finds something interesting, pump it out over the messaging broker. Client app displays the messages from queue.

# plan
1. get website data 
2. prettify it
3. parse it
4. how to store values
5. how do I get new data
6. how do I update old data
7. how do I use the data
8. host it as a REST api or one which sends notifications

# next
1. pick criteria for players we are interested in
2. request for each of these players
3. every 30 seconds, check these players
4. optimise: if no deaths, skip as we dont care

# then:
1. optimise: caching (maybe not needed?)
