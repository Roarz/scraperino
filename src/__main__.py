from sendCharInfo import check_player
import time, sys, os

def main():
    while True:
        check_player("Arkaykos Slayer")
        check_player("Young Kodak")
        check_player("Excail Oz")
        check_player("Azxkhar Te Pekea")
        break
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