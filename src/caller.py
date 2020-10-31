from charInfo import get_player_info_table, parse_char_stats, display_player_info
import time

def print_player_info(playerName):
    playerInfo = get_player_info_table(playerName)
    player = parse_char_stats(playerInfo)
    display_player_info(player)
    #time.sleep(1)

print_player_info("Excail Oz")
print_player_info("Azxkhar Te Pekea")
print_player_info("Young Kodak")
