COLORS = {
  "WHITE": "\033[0m",
  "BLUE":  "\033[34m",
  "GREEN":"\033[32m",
  "RED": "\033[31m"
}

ITEMS = {
  "torch": "🔥стало светлее!🔥",
  "sword": "🗡️так намного увереннее!🗡️",
  "bronze_box": "добавлен 'rusty_key'",
  "rusty_key":  "ключ получен!"
}

SPESIAL_ITEMS = {
  "bronze box": "get rusty_key"
}

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта...',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
          'exits': {'west': 'entrance'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')
    },
        'armory': {
          'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
          'exits': {'south': 'library', "west":"secret_passage"},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
          'exits': {'south': 'hall'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это 5!-4!)', '96')
    },
      'secret_passage': {
        'description': 'Узкий, пыльный тоннель, освещенный тусклым свечением мхов на стенах. Воздух спертый.',
        'exits': {'north': 'garden', 'east': 'armory'},
        'items': ['old_bone'],
        'puzzle': None
    },
    'garden': {
        'description': 'Заброшенный подземный сад. Призрачные светящиеся грибы освещают каменные грядки, где когда-то росли странные растения.',
        'exits': {'west': 'secret_passage', 'south': 'treasure_room', 'north': 'observatory'},
        'items': ['glowing_mushroom'],
        'puzzle': ('Сколько лисьтьев у квадра семилистника', '49')
    },
    'observatory': {
        'description': 'Круглая комната с разбитым куполом, через который видно каменный потолок пещеры. В центре стоит древний телескоп, направленный в ложное небо.',
        'exits': {'south': 'garden'},
        'items': ['treasure_key'],
        'puzzle': ('Телескоп показывает созвездие. На табличке выбито: "Сколько звезд в Малой Медведице?" (ответ цифрой)', '7')
    }
}
