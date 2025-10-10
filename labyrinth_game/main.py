from .consts import ROOMS, ITEMS, COLORS
from .player_actions import get_input, move_player, take_item
from .utils import *


game_state = {
    'player_inventory': list(),     # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False,         # Значения окончания игры
    'steps_taken': 0,           # Количество шагов
}


def process_command(game_state: dict, cmd: str):
    tokenized = cmd.split()
    match tokenized[0]:
        case "go"|"cd":
            if new_room := (move_player(game_state, tokenized[1])):
                print(new_room)
                return ("current_room", new_room)
            else:
                print("Такого выхода в этой комнате нет!")
        case "info":
            pass
        case "inventory" | "e":
            print(f"{COLORS["BLUE"]}Инвентарь:", ", ".join(game_state["player_inventory"]),f"{COLORS["WHITE"]}")
        case "use":
            if tokenized[1] in game_state["player_inventory"]:
                result = ITEMS.get(tokenized[1])
                if result:
                    print(result)
                    if result == "treasure_key":
                        return win_condition(game_state)
        case "info":
            describe_current_room(game_state)
        case "take" | "tk":
            item = take_item(game_state,tokenized[1])
            if item:
                if item not in game_state["player_inventory"]:
                    ROOMS[game_state["current_room"]]["items"].remove(item)
                    print(f"{COLORS["GREEN"]}Вы подняли {item}!{COLORS["WHITE"]}")
                    return "player_inventory", item
            else:
                print("Такого предмета нет в этой комнате!")
        case "quit" | "q":
            print("Выход из игры")
            game_state['game_over'] = True
        case _:
            print(f"{COLORS["RED"]}Неизвестная команда{COLORS["WHITE"]}")

    return False, False
def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    while (not game_state["game_over"]):
        game_state["steps_taken"] += 1

        describe_current_room(game_state)
        key, value = process_command(game_state,get_input(input(">>>")))
        if key and value:
            if key == "player_inventory":
                game_state[key].append(value)
                continue
            game_state[key] = value
        elif not key and value == "win":
            print("Вы нашли клад!")
            print(f"Всего шагов,{game_state["steps_taken"]}")
            game_state["game_over"] = True

if __name__ == "__main__":
    main()