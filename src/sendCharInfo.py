import pika
from charInfo import get_player_info_table, parse_char_stats, display_player_info
import time
import json
import jsonpickle
from json import JSONEncoder
import sys
import os

def get_player_obj(playerName):
    playerInfo = get_player_info_table(playerName)
    player = parse_char_stats(playerInfo)
    return player

def print_player_info(playerName):
    player = get_player_obj(playerName)
    display_player_info(player)

def save_player_json(player):
    print(player)

def check_player(player):
    print_player_info(player)
    lad = get_player_obj(player)
    channel.basic_publish(exchange='', routing_key='hello', body=jsonpickle.encode(lad, unpicklable=False))
    print("[x] Sent '%s'" % lad.name)

def main():
    channel.queue_declare(queue='hello')
    check_player("Arkaykos Slayer")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
            connection.close()
        except SystemExit:
            os._exit(0)
            connection.close()

