from .consts import ROOMS, ITEMS, COLORS
from .player_actions import get_input, move_player, take_item
from .utils import *


game_state = {
    'player_inventory': list(), # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False,         # Значения окончания игры
    'steps_taken': 0,           # Количество шагов
    'score': 0,                 # Очки
    'hp': 3                     # Здоровье
}

def process_command(game_state: dict, cmd: str):
    """командный интерпретатор команды по форме: (ключевое слово)(&|)[аргументы]"""
    tokenized = cmd.split()
    match tokenized[0]:
        case "tp":
            return "current_room", tokenized[1]
        case "solve":
            puzzle = ROOMS[game_state["current_room"]].get("puzzle")
            if puzzle:
                print(puzzle)
                return solving(puzzle[1],game_state["current_room"], " ".join(tokenized[1:]))
            
        case "north"|"south"|"east"|"west"|"go":
            if tokenized[0] == "go":
                new_room = (move_player(game_state, tokenized[1]))
                
            else:                
                new_room = (move_player(game_state, tokenized[0]))

            if new_room and new_room != "noRustyKey":
                game_state["steps_taken"] += 1
                print(new_room)
                return "current_room", new_room
            else:
                if not new_room:
                    print("Такого выхода в этой комнате нет!")
                else:
                    print("Дверь заперта!")
        case "inventory" | "e":
            print(f"{COLORS["BLUE"]}Инвентарь:", ", ".join(game_state["player_inventory"]),f"{COLORS["WHITE"]}")

        case "use":
            if tokenized[1] in game_state["player_inventory"]:
                result = ITEMS.get(tokenized[1])
                if result:
                    print(result)
                elif tokenized[1] == "bronze_box":
                    return "unboxing", "rusty_key"
                elif tokenized[1] == "treasure_key":
                    return win_condition(game_state)
                else:
                    print("Я не знаю что этоn предмет делает делает")

        case "look":
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

        case "help":
            show_help()

        case _:
            print(f"{COLORS["RED"]}Неизвестная команда{COLORS["WHITE"]}\nДля справки `help`")
    return False,False

def resulting(key,value):
    """Обработка результатов командного интерпретатора"""
    if key and value:
        if key in ["player_inventory","unboxing"]:
            if key == "unboxing":
                game_state["player_inventory"].remove("bronze_box")
                print("В ящике лежит ключ!")
            game_state["player_inventory"].append(value)

        if key == "current_room": 
            game_state[key] = value
    elif not key:
        if value == "win":
            print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
            print(f"Всего шагов,{game_state["steps_taken"]}")
            print(f"Заработано очков: {game_state["score"]-game_state["steps_taken"]}")
            game_state["game_over"] = True
        if value == 'solved':
            game_state["score"] += 5



def main():
    """Главный цикл"""
    print("Добро пожаловать в Лабиринт сокровищ!")
    while (not game_state["game_over"]):
        describe_current_room(game_state)
        if pseudo_random(game_state["steps_taken"]) == 1:
            random_event(pseudo_random(game_state["steps_taken"]),game_state)
        key, value = process_command(game_state,get_input(input(">>>")))
        resulting(key,value)
        
if __name__ == "__main__":
    main()
