from .consts import ROOMS
from .utils import  pseudo_random, random_event, rusty_key_checker


def trigger_trap(game_state):
    if pseudo_random(game_state["steps_taken"]) in [1,2]:
        if "torch" not in game_state["player_inventory"]:
            damage = pseudo_random(game_state["steps_taken"])
            print("Сработала ловушка!")
            return damage
        else:
            print("Вы вовремя заметили ловушку и обошли ее!")



        

def move_player(game_state: dict, direction) -> tuple[str,str] | None:
    """Проверяет наличие выхода и возвращает новую комнату"""
    current_room = game_state['current_room']
    if new_room := ROOMS[current_room]["exits"].get(direction):
        if new_room == "treasure_room" and "rusty_key" not in game_state["player_inventory"]:
            return "noRustyKey"
        return new_room  
    
    

def show_inventory(game_state):
    """Показывает инвентарь"""
    print(game_state['player_inventory'])

def take_item(game_state, item_name):
    """Проверяет наличие предмета в комнате и возвращает"""
    current_room = game_state['current_room']
    if item_name in ROOMS[current_room]['items']:
        return item_name


def get_input(prompt: str) -> str:
    """Предобработка ввода"""
    try:
        return prompt if prompt != "" else "null"
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 
