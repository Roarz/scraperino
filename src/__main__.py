from sendCharInfo import check_player, get_player_obj
from onlineList import get_online_list, filter_players
import time, sys, os

def main():
    while True:
        #check_player("Wizard of Fiery")
        onlineList = get_online_list("Wintera")
        targets = filter_players(onlineList, minLvl=40, maxLvl=50)
        for target in targets:
            start_time = time.time()            
            check_player(target.name)

            end_time = time.time()
            time_lapsed = end_time - start_time

            print("target: (%s)" % target.name, " in: (%s) seconds" % time_convert(time_lapsed))
        break

def time_convert(sec):
    sec = sec % 60
    return ("Time Lapsed = {0} secs".format(sec))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)