from .consts import ROOMS
from .utils import describe_current_room
def move_player(game_state: dict, direction) -> str:
    current_room = game_state['current_room']
    if new_room := ROOMS[current_room]["exits"].get(direction):
        return new_room    
    return False
    
def show_inventory(game_state):
    print(game_state['player_inventory'])

def take_item(game_state, item_name):
    current_room = game_state['current_room']
    if item_name in ROOMS[current_room]['items']:
        return item_name
    return False


def get_input(prompt: str) -> str:
    try:
        return prompt if prompt != "" else "null"
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 