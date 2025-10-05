from consts import ROOMS
from utils import *
def move_player(game_state: dict, direction) -> str:
    current_room = game_state['current_room']
    if (new_room := ROOMS[current_room]["exits"].get(direction)):
        return new_room
    else:
        return False
    
def show_inventory(game_state):
    print(game_state['player_inventory'])

def get_input(prompt: str):
    try:
        return prompt
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 