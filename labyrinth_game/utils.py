from .consts import ROOMS, COLORS


def win_condition(game_state):
    if game_state["current_room"] == "treasure_room":
        return False, "win "
    else: 
        return False, False

def is_solved(user_input: str,answer: str) -> bool:
    return True if user_input == answer else False

def solving(answer, current_room_name):
    while True:
        user_input = input(">s>")
        if is_solved(user_input,answer):
            ROOMS[current_room_name]['puzzle'] = list()
            print(f"{COLORS["GREEN"]}Загадка решена успешно!{COLORS["WHITE"]}")
            break
        else:
            print("Ответ неверен, попробуйте еще раз")


def puzzle_repr(room,current_room_name):
    puzzle = room.get('puzzle')
    if puzzle:
        print(f"{COLORS["RED"]}Обнаружена загадка, что пройти дальше, нужно ее решить:{COLORS["WHITE"]}")
        print(puzzle[0])
        solving(puzzle[1],current_room_name)
        
    else:
        print("Загадки тут нет!")
        

def exits_repr(room: dict):
    return ", ".join([f"на {k} в {v}" for k,v in room["exits"].items()])

def items_repr(room: dict):
    return ", ".join([f"{i}" for i in room['items']]) if room['items'] else "не обнаружены"

def room_repr(room: dict, name: str) -> str:
    return f"""
Вы в помещении {COLORS["GREEN"]}{name}{COLORS["WHITE"]}
> Выходы:      
    {exits_repr(room)}
> Предметы: 
    {items_repr(room)}"""

def describe_current_room(game_state: dict) -> None:
    current_room_name = game_state.get('current_room')
    current_room_global_info = ROOMS.get(current_room_name)
    if current_room_name:
        print(room_repr(current_room_global_info, current_room_name))
        puzzle_repr(current_room_global_info, current_room_name)