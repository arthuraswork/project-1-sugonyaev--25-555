COLORS = {
  "WHITE": "\033[0m",
  "BLUE":  "\033[34m",
  "GREEN":"\033[32m",
  "RED": "\033[31m"
}

ITEMS = {
  "torch": "🔥стало светлее!🔥",
  "sword": "🗡️так намного увереннее!🗡️",
  "treasure_key": "с помощью ключа я смогу открыть сундук!",
  "rusty_key": "он подходит для двери в сокровищницу!"
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
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
          'exits': {'west': 'hall', 'north': 'treasure_room'},
          'items': ['rusty_key'],
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
        'puzzle': ('Сколько лисьтьев у квадратичного семилистника', '49')
    },
    'observatory': {
        'description': 'Круглая комната с разбитым куполом. В центре стоит древний телескоп.',
        'exits': {'south': 'garden', 'east': 'treasure_room'},
        'items': ['treasure_key'],
        'puzzle': ('Телескоп показывает созвездие. На табличке выбито: "Сколько звезд в Малой Медведице?" (ответ цифрой)', '7')
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
          'exits': {'west': 'observatory', 'south': 'trap_room'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код: (5!-4!)', '96')
    },
    'secret_passage': {
        'description': 'Узкий, пыльный тоннель, освещенный тусклым свечением мхов на стенах. Воздух спертый.',
        'exits': {'east': 'armory', 'west': 'library'},
        'items': ['old_bone'],
        'puzzle': None
    }
}