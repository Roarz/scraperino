from charInfo import get_player_info_table, parse_char_stats, display_player_info

playerName = "Cleitinho Tacaesside"
playerInfo = get_player_info_table(playerName)
player = parse_char_stats(playerInfo)
display_player_info(player)
