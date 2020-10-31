from charInfo import get_player_info_table, parse_char_stats, display_player_info
import time

def get_player_obj(playerName):
    playerInfo = get_player_info_table(playerName)
    player = parse_char_stats(playerInfo)
    return player

def print_player_info(playerName):
    player = get_player_obj(playerName)
    display_player_info(player)
    #time.sleep(1)

def save_player_json(player):
    print(player)

#print_player_info("Excail Oz")
#print_player_info("Azxkhar Te Pekea")
#print_player_info("Young Kodak")

#lad = get_player_obj("Young Kodak")
#save_player_json(lad)

