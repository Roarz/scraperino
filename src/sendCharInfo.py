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
    player = get_player_obj(player)
    send_player(player)

def send_player(player):
    channel.basic_publish(exchange='', routing_key='hello', body=jsonpickle.encode(player, unpicklable=False))
    print("[x] Sent '%s'" % player.name)
    #connection.close()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print("opening channel")

