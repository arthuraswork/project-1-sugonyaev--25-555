#!/usr/bin/env python3

from .consts import COLORS, ROOMS, EVENT_WORKING_NUM
from .player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from .utils import (
    apply_event_results,
    describe_current_room,
    pseudo_random,
    show_help,
    solving,
    random_event
)

game_state = {
        'player_inventory': [],
        'current_room': 'entrance', 
        'game_over': False,
        'steps_taken': 0,
        'score': 0,
    }

def on_go_command(game_state: dict,direction: str):
    """Обработка команды перехода в другую комнату"""
    new_room = move_player(game_state, direction)
    if new_room and new_room != "TreasureNoRustyKey":
        game_state["steps_taken"] += 1
        return "current_room", new_room
    else:
        if not new_room:
            print("Такого выхода в этой комнате нет!")
        else:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше")
    return False,False


def on_take_command(game_state: dict, item:str):
    """Обработка команды взятия предмета"""
    found_item = take_item(game_state, item)
    if found_item:
        if found_item not in game_state["player_inventory"]:
            ROOMS[game_state["current_room"]]["items"].remove(found_item)
            print(f"{COLORS['GREEN']}Вы подняли {found_item}!{COLORS['WHITE']}")
            return "player_inventory", found_item
    else:
        print("Такого предмета нет в этой комнате!")
    return False, False

def process_command(game_state: dict, cmd: str):
    """Командный интерпретатор команды по форме: (ключевое слово)(&|)[аргументы]"""
    tokenized = cmd.split()
    if not tokenized:
        return False, False
        
    command = tokenized[0]

    match command:
    
        case "solve"|"s":
            puzzle = ROOMS[game_state["current_room"]].get("puzzle")
            if puzzle:
                print(puzzle[0])
                return solving(
                    puzzle[1], game_state["current_room"], 
                               " ".join(tokenized[1:])
                               )
            
        case "north"|"south"|"east"|"west"|"go":
            if command == "go":
                return on_go_command(game_state, direction=tokenized[1])
            else:
                return on_go_command(game_state, direction=command)
                    
        case "inventory" | "i":
            show_inventory(game_state)

        case "use"|"f":
            if len(tokenized) == 2:
                return use_item(game_state, tokenized[1])
            else:
                print("Укажите предмет для использования")
        case "look"|"ls":
            describe_current_room(game_state)

        case "take" | "tk":
            if len(tokenized) == 2:
                return on_take_command(game_state, tokenized[1])
            else:
                print("Укажите предмет для взятия")
        case "quit" | "q" | "c":
            print("Выход из игры")
            game_state['game_over'] = True

        case "help":
            show_help()

        case _:
            print(f"{COLORS['RED']}Неизвестная команда{COLORS['WHITE']}")
            print("Для справки введите 'help'")
            
    return False, False

def apply_command_result(key, value):
    """Обработка результатов командного интерпретатора"""
    if key and value:
        if key in ["player_inventory", "unboxing"]:
            if key == "unboxing":
                game_state["player_inventory"].remove("bronze_box")
                print("В ящике лежит ключ!")
            game_state["player_inventory"].append(value)

        if key == "current_room": 
            game_state[key] = value
            
    elif not key:
        if value == "win":
            print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
            print(f"Всего шагов: {game_state['steps_taken']}")
            final_score = game_state['score'] - game_state['steps_taken']
            print(f"Заработано очков: {final_score}")
            game_state["game_over"] = True
            
        if value == 'solved':
            game_state["score"] += 5
            print(f"{COLORS['GREEN']}Загадка решена! +5 очков{COLORS['WHITE']}")

def cmd_type(cmd):
    """Определяет тип команды и если go->вызывается ивент """
    tokenized = cmd.split()
    if tokenized[0] in ["north","south","east","west","go"]:
        return "go"
    return "other"

def main():
    """Главный цикл"""
    print("Добро пожаловать в Лабиринт сокровищ!")
    show_help()
    while not game_state["game_over"]:    
        cmd = get_input(input(">>> "))
        key, value = process_command(game_state, cmd)
        apply_command_result(key, value)
        if cmd_type(cmd) == "go":
            if pseudo_random(game_state["steps_taken"]) == EVENT_WORKING_NUM:
                event_result = random_event(
                    pseudo_random(
                        game_state["steps_taken"]
                        ), game_state)
                
                if apply_event_results(event_result,game_state) == "defeat":
                    break

if __name__ == "__main__":
    main()