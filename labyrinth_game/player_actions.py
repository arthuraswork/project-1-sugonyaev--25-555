from .consts import ROOMS, COLORS, ITEMS
from .utils import  pseudo_random, random_event, rusty_key_checker,win_condition

def trigger_trap(game_state: dict) -> int|None:
    """Активирует ловушку в trap_room:"""
    if "torch" not in game_state["player_inventory"]:
        if not game_state["player_inventory"]:
            if pseudo_random(game_state["steps_taken"]) in [1,2]:
                damage = pseudo_random(game_state["steps_taken"], 9)
                if damage >= 5:
                    print(f"Сработала ловушка и вы получили ранение!")
                    return True
                print("Вы смогли увернуться!")
        else:
            lost_item = game_state["player_inventory"].pop()
            print(f"Сработала ловушка и вы потерялb {lost_item}")
    else:
        print("Вы вовремя заметили ловушку и обошли ее!")
    return None

def move_player(game_state: dict, direction) -> str|None:
    """Проверяет наличие выхода и возвращает новую комнату"""
    current_room = game_state['current_room']
    new_room = ROOMS[current_room]["exits"].get(direction)
    if new_room:
        if new_room == "treasure_room":
            if not rusty_key_checker(game_state):
                return "noRustyKey"
            else: 
                print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ")
        return new_room  

def use_item(game_state: dict, item_name: str):
    """Использование предмета в инвентаре"""
    item = item_name.lower()
    if item in game_state["player_inventory"]:
        result = ITEMS.get(item)
        if result:
            print(result)
        elif item == "bronze_box":
            return "unboxing", "rusty_key"
        elif item == "treasure_key":
            return win_condition(game_state)
        else:
            print("Неизвестно, как использовать этот предмет")
    else:
        print("У вас нет такого предмета!")
    return False,False


def show_inventory(game_state: dict) -> None:
    """Показывает инвентарь"""
    inventory_items = ", ".join(game_state["player_inventory"]) if game_state["player_inventory"] else "пусто"
    print(f"{COLORS['BLUE']}Инвентарь: {inventory_items}{COLORS['WHITE']}")

def take_item(game_state: dict, item_name: str) -> str|None:
    """Проверяет наличие предмета в комнате и возвращает"""
    item = item_name.lower()
    current_room = game_state['current_room']
    if item in ROOMS[current_room]['items']:
        return item

def get_input(prompt: str) -> str:
    """Предобработка ввода"""
    try:
        return prompt if prompt.strip() != "" else "null"
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 
