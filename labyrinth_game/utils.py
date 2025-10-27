from math import floor, sin

from .consts import (
    COLORS,
    COMMANDS,
    DEATH_RANGE,
    LONG_DIGIT,
    MAX_CMD_LENGTH,
    MAX_RANGE,
    REAL_DIGIT,
    ROOMS,
    TRAP_TRIGGER_RANGE,
)


def random_event(num: int, game_state: dict):
    """Мэтчинг событий по числу"""
    match num:
        case 0:
            print("Вы нашли монетку!")
            return "coin"
        case 1:
            print("Вы слышите шорох")
            if "sword" in game_state["player_inventory"]:
                print("Вы отпугнули существо")
            return "sound"
        case 2:
            if game_state["current_room"] == "trap_room":
                result = trigger_trap(game_state)
                if result:
                    game_state["game_over"] = True                
                    return "defeat"


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
    """Реализует опцию решения загадки в сокровищнице"""
    if is_solved(user_input, answer):
        ROOMS["treasure_room"]['puzzle'] = list()
        print(f"{COLORS['GREEN']}Загадка решена успешно!{COLORS['WHITE']}")  
        return False, "win"

def is_solved(user_input: str,answer: str) -> bool:
    """Проверяет верно ли решение игрока"""
    if "|" in answer:
        variants = answer.split("|")
        if user_input in variants:
            return True
    return True if user_input == answer else False

def solving(answer, current_room_name, user_input):
    """Решение загадок"""
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
    """Показывает загадку в терминале при наличии"""
    puzzle = room.get('puzzle')
    if puzzle:
        print(
            f"""{COLORS['RED']}
Обнаружена загадка! Чтобы дать ответ, напишите `solve ответ`:
            {COLORS['WHITE']}"""
            )
        print(puzzle[0])
    else:
        print("Загадки тут нет!")
        
def exits_repr(room: dict):
    """Показывает выходы"""
    return ", ".join([f"на {k} в {v}" for k,v in room["exits"].items()])

def items_repr(room: dict):
    """Показывает предметы в комнате"""
    return ", ".join([f"{i}" for i in room['items']]) if room['items'] else "ничего нет"

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

def apply_event_results(result,game_state):
    """Применяет результаты ивента"""
    match result:
        case "coin":
            ROOMS[game_state["current_room"]]["items"].append(result)
            
def trigger_trap(game_state: dict) -> str|None:
    """Активирует ловушку в trap_room:"""
    if "torch" not in game_state["player_inventory"]:
        print("Ловушка активирована! Пол стал дрожать...")
        if not game_state["player_inventory"]:
            if pseudo_random(game_state["steps_taken"]) in TRAP_TRIGGER_RANGE:
                damage = pseudo_random(game_state["steps_taken"], MAX_RANGE)
                if damage >= DEATH_RANGE:
                    print("Сработала ловушка и вы получили ранение!")
                    return "defeat"
                print("Вы смогли увернуться!")
        else:
            lost_item = game_state["player_inventory"].pop()
            print(f"Сработала ловушка и вы потерялb {lost_item}")
    else:
        print("Вы вовремя заметили ловушку и обошли ее!")
    return None

def show_help():
    """Вывод команд"""
    print(f"\n{COLORS['GREEN']}Команды:{COLORS['WHITE']}\n")
    commands: list = list()
    for cmd, descr in COMMANDS.items():
        commands.append(f"{cmd}: {'.' * (MAX_CMD_LENGTH - len(cmd))} {descr}")
    joined = ";\n".join(commands)
    print(joined)
