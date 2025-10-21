from .consts import ROOMS
from .utils import describe_current_room, pseudo_random, random_event


def trigger_trap():
    ...


def check_trigger(room, inventory):
    
    if room == "trap_room" and "torch" not in inventory:
        ...
    elif "sword" not in inventory:
        ...

def move_player(game_state: dict, direction) -> str:
    """Проверяет наличие выхода и возвращает новую комнату"""
    current_room = game_state['current_room']
    if new_room := ROOMS[current_room]["exits"].get(direction):
        check_trigger(game_state["current_room"], game_state["player_inventory"])
        return new_room    

        
    return False
    

def show_inventory(game_state):
    """Показывает инвентарь"""
    print(game_state['player_inventory'])

def take_item(game_state, item_name):
    """Проверяет наличие предмета в комнате и возвращает"""
    current_room = game_state['current_room']
    if item_name in ROOMS[current_room]['items']:
        return item_name
    return False


def get_input(prompt: str) -> str:
    """Предобработка ввода"""
    try:
        return prompt if prompt != "" else "null"
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 
