from .consts import (
    ROOMS, COLORS, REAL_DIGIT, LONG_DIGIT, COMMANDS, MAX_CMD_LENGTH
)
from math import floor, sin

def random_event(num: int, game_state: dict):
    """Мэтчинг событий по числу"""
    match num:
        case 0:
            print("Вы нашли монетку")
            return ""
        case 1:
            ...
        case 2:
            ...

def rusty_key_checker(game_state) -> bool|None:
    """Проверка ключа для treasure_room"""
    return "rusty_key" in game_state["player_inventory"]
            

def win_condition(game_state):
    """Проверка условия победы"""
    if (game_state["current_room"] == "treasure_room" and 
        "treasure_key" in game_state["player_inventory"]):
        return False, "win" 
    return False, False

def attempt_open_treasure(answer,user_input):
    if is_solved(user_input, answer):
        ROOMS["treasure_room"]['puzzle'] = list()
        print(f"{COLORS['GREEN']}Загадка решена успешно!{COLORS['WHITE']}")  
        return False, "win"

def is_solved(user_input: str,answer: str) -> bool:
    return True if user_input == answer else False

def solving(answer, current_room_name, user_input):
    """решение загадок"""
    print("Ваш ввод:", user_input)
    if current_room_name == "treasure_room":
        return attempt_open_treasure(answer,user_input)
    if is_solved(user_input, answer):
        ROOMS[current_room_name]['puzzle'] = list()
        print(f"{COLORS['GREEN']}Загадка решена успешно!{COLORS['WHITE']}") 
        return False, "solved"
    
    print("Ответ неверен, попробуйте еще раз")
    return False, False

def puzzle_repr(room):
    """показывает загадку в терминале при наличии"""
    puzzle = room.get('puzzle')
    if puzzle:
        print(f"{COLORS['RED']}Обнаружена загадка! Чтобы дать ответ, напишите `solve ответ`:{COLORS['WHITE']}")
        print(puzzle[0])
    else:
        print("Загадки тут нет!")
        
def exits_repr(room: dict):
    """Показывает выходы"""
    return ", ".join([f"на {k} в {v}" for k,v in room["exits"].items()])

def items_repr(room: dict):
    """Показывает предметы в комнате"""
    return ", ".join([f"{i}" for i in room['items']]) if room['items'] else "не обнаружены"

def room_repr(room: dict, name: str) -> str:
    """Описывает помещение"""
    return f"""
Вы в помещении {COLORS["GREEN"]}{name}{COLORS["WHITE"]}
> Выходы:      
    {exits_repr(room)}
> Предметы: 
    {items_repr(room)}"""

def describe_current_room(game_state: dict) -> None:
    """Вывод информации о комнате в консоль"""
    current_room_name = game_state.get('current_room')
    current_room_global_info = ROOMS.get(current_room_name)
    if current_room_name:
        print(room_repr(current_room_global_info, current_room_name))
        puzzle_repr(current_room_global_info)

def pseudo_random(seed, modulo=3):
    """Генератор рандома"""
    sin_val = sin(REAL_DIGIT * seed) * LONG_DIGIT
    int_part= sin_val - floor(sin_val) 
    return floor(int_part * modulo)



def show_help():
    print(f"\n{COLORS['GREEN']}Команды:{COLORS['WHITE']}\n")
    commands: list = list()
    for cmd, descr in COMMANDS.items():
        commands.append(f"{cmd} {' ' * (MAX_CMD_LENGTH - len(cmd))} {descr}")
    joined = ";\n".join(commands)
    print(joined)
