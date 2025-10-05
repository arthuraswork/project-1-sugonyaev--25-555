from consts import ROOMS
def solving(game_state):
    if puzzle := ROOMS[game_state["current_room"]].get("puzzle"):
        print(f"Тут есть загадка! {puzzle[0]}")
        while True:
            
        
    else:
        return False

def room_representarion(room: dict, name: str) -> str:
    return f"""
Вы в помещении {name}
> Выходы:      
    {", ".join([f"на {k} в {v}" for k,v in room["exits"].items()])}
> Предметы: 
    {", ".join([f"{i}" for i in room['items']]) if room['items'] else "не обнаружены"}
> Загадки:
    {", ".join([f"{i}" for i in room['puzzle']]) if room['puzzle'] else "не обнаружены"}
"""
def describe_current_room(game_state: dict) -> str:
    current_room = game_state['current_room']
    print(room_representarion(ROOMS[current_room], current_room))