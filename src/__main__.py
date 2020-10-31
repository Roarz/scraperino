from sendCharInfo import check_player
import time, sys, os

def main():
    while True:
        check_player("Arkaykos Slayer")
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)