from consts import ROOMS
from player_actions import get_input, move_player
from utils import *

game_state = {
    'player_inventory': [],     # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False,         # Значения окончания игры
    'steps_taken': 0,           # Количество шагов
}


def process_command(game_state: dict, cmd: str):
    tokenized = cmd.split()
    match tokenized[0]:
        case "go":
            if new_room := (move_player(game_state, tokenized[1])):
                print(new_room)
                return ("current_room", new_room)
            else:
                print("Такого выхода в этой комнате нет!")
                return ("current_room", game_state["current_room"])
def main():
    
    print("Добро пожаловать в Лабиринт сокровищ!")

    while (not game_state["game_over"]):
        game_state["steps_taken"] += 1

        describe_current_room(game_state)
        solve_puzzle(game_state)

        key, value = process_command(game_state,get_input(input(">>>")))
        if key & value:
            game_state[key] = value




if __name__ == "__main__":
    main()