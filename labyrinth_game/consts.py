COLORS = {
    "WHITE": "\033[0m",
    "BLUE": "\033[34m", 
    "GREEN": "\033[32m",
    "RED": "\033[31m"
}

REAL_DIGIT = 12.9898
LONG_DIGIT = 42123.234509
DEATH_RANGE = 5
MAX_RANGE = 9
TRAP_TRIGGER_RANGE = (1,2)
ITEMS = {
    "torch": "🔥 стало светлее! 🔥",
    "sword": "🗡️ так намного увереннее! 🗡️",
    "treasure_key": "С помощью ключа я смогу открыть сундук!",
    "rusty_key": "Он подходит для двери в сокровищницу!",
    "ancient_book": "0001+0010+0011+0100+1000",
    "bronze_box": "Небольшая бронзовая шкатулка с замочком",
    "glowing_mushroom": "Светящийся гриб, излучающий мягкий свет",
    "treasure_chest": "Большой сундук, прочно запертый на замок",
    "old_bone": "Старая кость неизвестного существа"
}

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта...',
        'exits': {'north': 'hall'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'east': 'trap_room', 'north': 'garden'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой', '10|десять')
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной полом. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'hall', 'north': 'treasure_room'},
        'items': [],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'кредит')
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library', 'east': 'garden'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'garden': {
        'description': 'Заброшенный подземный сад. Призрачные светящиеся грибы освещают каменные грядки.',
        'exits': {'south': 'hall', 'west': 'armory', 'north': 'observatory'},
        'items': ['glowing_mushroom'],
        'puzzle': ('Сколько листьев у квадратичного семилистника?', '49|сорок девять')
    },
    'observatory': {
        'description': 'Круглая комната с разбитым куполом. В центре стоит древний телескоп.',
        'exits': {'south': 'garden', 'east': 'treasure_room'},
        'items': ['treasure_key'],
        'puzzle': ('Телескоп показывает созвездие. На табличке выбито: "Сколько звезд в Малой Медведице?" (ответ цифрой)', '7|семь')
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        'exits': {'west': 'observatory', 'south': 'trap_room'},
        'items': ['treasure_chest'],
        'puzzle': ('Ответ в старой книге', '18|восемндцать')
    },
    'secret_passage': {
        'description': 'Узкий, пыльный тоннель, освещенный тусклым свечением мхов на стенах. Воздух спертый.',
        'exits': {'east': 'armory', 'west': 'library'},
        'items': ['old_bone','rusty_key'],
        'puzzle': None
    }
}
    
MAX_CMD_LENGTH = 24

COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "north|south|east|west": "перейти в направлении (краткая форма)",
    "look|ls": "осмотреть текущую комнату",
    "take <item>|tk|mv": "поднять предмет", 
    "use <item>|f": "использовать предмет из инвентаря",
    "inventory|i|cat": "показать инвентарь",
    "solve <answer>|s": "попытаться решить загадку в комнате",
    "quit|q|c": "выйти из игры",
    "help": "показать это сообщение"
}