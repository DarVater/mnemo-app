source_by_top = {
    'Город': 'topic_town',
    'Дом': 'home',
    'Еда': 'food',
    'Природа': 'nature',
    'Человек': 'human',

    'Отношения': 'relations',
    'Транспорт': 'vehicle',
    'Животные': 'Animals',
    'Спорт': 'Sport',
    'Цвета': 'Colors',

    'Работа': 'Work',
    'Профессии': 'Professions',
    'Изучение': 'learning',
    'Развлечения': 'Entertainment',
    'Время': 'clock',

    'Календарь': 'Calendar',
    'Одежда': 'Clothing',
    'Хобби': 'Hobby',
    'Другое': 'Other',
    'Указатели': 'Pointers',

    'Восклицание': 'Exclamation',
    'союзы': 'unions',
    'числа': 'numbers',
    'Предлог': 'preposition',
    'Наречие': 'Adverb',

    'Наличия': 'Availability',
    'Операции': 'Operations',
    'Общения': 'Communication',
    'Стадии': 'Stages',
    'Мышления': 'Thinking',

    'Движения': 'Movements',
    'Другие глаголы': 'Other_verbs',
    'Эмоции': 'Emotions',
    'Абстрактные': 'Abstract',
    'На глаз': 'Approximately',

    'Состояние': 'Condition',
    'Качества': 'Qualities',
    'Местоимения': 'Pronouns',
}

words_by_lvl = {'ru': {
    'Город': {'area': 'район', 'building': 'здание', 'cafe': 'кафе', 'city': 'город (большой)', 'hospital': 'больница',
              'hotel': 'гостиница', 'police': 'полиция', 'post': 'почта', 'street': 'улица', 'taxi': 'такси',
              'library': 'библиотека', 'map': 'карта', 'museum': 'музей', 'park': 'парк', 'pool': 'бассейн',
              'restaurant': 'ресторан', 'school': 'школа', 'station': 'станция',
              'store': 'магазин', 'supermarket': 'супермаркет', 'town': 'город', 'university': 'университет',
              'market': 'рынок', 'money': 'деньги', 'shop': 'магазин', 'yard': 'двор',
              'traffic': 'движение', 'front': 'перед', 'mall': 'торговый центр', 'neighborhood': 'район'},

    'Дом': {'apartment': 'квартира', 'bathroom': 'ванная комната', 'bath': 'ванна', 'bedroom': 'спальня',
            'door': 'дверь', 'house': 'дом(тип жилья)', 'kitchen': 'кухня', 'room': 'комната',
            'shower': 'душ', 'toilet': 'туалет', 'floor': 'пол', 'chair': 'стул', 'picture': 'картина',
            'painting': 'картина (красками)', 'window': 'окно', 'home': 'дом (где живем)',
            'book': 'книга', 'table': 'стол', 'cup': 'чашка', 'bottle': 'бутылка', 'glass': 'стакан', 'wall': 'стена',
            'box': 'коробка', 'piano': 'пианино', 'radio': 'радио',
            'computer': 'компьютер', 'address': 'адрес', 'bed': 'кровать', 'garden': 'сад', 'key': 'ключ',
            'letter': 'письмо', 'neighbor': 'сосед', 'newspaper': 'газета'},

    'Еда': {'bread': 'хлеб', 'butter': 'масло', 'cake': 'торт', 'cheese': 'сыр', 'chocolate': 'шоколад',
            'coffee': 'кофе', 'carrot': 'морковь', 'onion': 'лук', 'cooking': 'готовка', 'pepper': 'перец',
            'food': 'еда', 'fruit': 'фрукт', 'ice cream': 'мороженое', 'juice': 'сок', 'meat': 'мясо', 'milk': 'молоко',
            'potato': 'картофель', 'drink': 'напиток', 'wine': 'вино',
            'rice': 'рис', 'salad': 'салат', 'salt': 'соль', 'sandwich': 'бутерброд', 'soup': 'суп', 'sugar': 'сахар',
            'tea': 'чай', 'tomato': 'помидор', 'vegetable': 'овощ',
            'apple': 'яблоко', 'banana': 'банан', 'breakfast': 'завтрак', 'meal': 'мука грубого помола', 'menu': 'меню',
            'beer': 'пиво', 'orange': 'апельсин', 'dinner': 'обед',
            'dish': 'блюдо', 'egg': 'яйцо', 'lunch': 'обед'},

    'Природа': {'air': 'воздух', 'cold': 'холод', 'rain': 'дождь', 'shower': 'ливень', 'snow': 'снег',
                'weather': 'погода', 'fire': 'огонь', 'water': 'вода', 'geography': 'география', 'tree': 'дерево',
                'beach': 'пляж', 'island': 'остров', 'mountain': 'гора', 'ocean': 'океан', 'river': 'река',
                'glass': 'стекло', 'paper': 'бумага', 'pencil': 'карандаш', 'ice': 'лёд', 'sound': 'звук',
                'space': 'пространство', 'star': 'звезда', 'sun': 'Солнце', 'flower': 'цветок',
                'plant': 'растение', 'land': 'земля', 'light': 'свет', 'thing': 'предмет', 'world': 'мир'},

    'Человек': {'arm': 'рука', 'back': 'спина', 'body': 'тело', 'face': 'лицо', 'hair': 'волосы', 'age': 'возраст',
                'hand': 'рука (кисть)', 'head': 'голова', 'health': 'здоровье', 'person': 'человек (личность)',
                'man': 'человек (обычно мужчина)', 'mouth': 'рот', 'nose': 'нос', 'woman': 'женщина', 'ear': 'ухо',
                'foot': 'ступня', 'eye': 'глаз', 'tooth': 'зуб', 'people': 'люди', 'teenager': 'подросток',
                'adult': 'взрослый', 'baby': 'младенец', 'boy': 'мальчик', 'child': 'ребенок', 'love': 'люблю',
                'girl': 'девочка', 'leg': 'нога', 'life': 'жизнь'},

    'Отношения': {'cousin': 'двоюродная сестра/брат', 'brother': 'брат', 'daughter': 'дочь', 'family': 'семья',
                  'boyfriend': 'парень', 'girl friend': 'подруга', 'husband': 'муж', 'wife': 'жена', 'aunt': 'тётя',
                  'father': 'папа', 'grandfather': 'дедушка', 'grandmother': 'бабушка', 'mother': 'мама',
                  'sister': 'сестра', 'son': 'сын', 'uncle': 'дядя', 'parent': 'родитель', 'friend': 'друг',
                  'grandparent': 'бабушка и дедушка',
                  },

    ###################### Достатоыно

    'Транспорт': {'bike': 'велосипед', 'boat': 'лодка', 'bus': 'автобус', 'car': 'автомобиль', 'road': 'дорога',
                  'train': 'поезд', 'truck': 'грузовой автомобиль', 'boot': 'багажник',
                  'vacation': 'отпуск', 'airport': 'аэропорт', 'flight': 'рейс', 'passport': 'паспорт', 'way': 'путь',
                  'course': 'курс', 'ticket': 'билет', 'information': 'справочное бро',
                  'bag': 'сумка', 'machine': 'машина (механизм)'},

    'Животные': {'animal': 'животное', 'elephant': 'слон', 'horse': 'лошадь', 'lion': 'лев', 'mouse': 'мышь',
                 'pig': 'свинья', 'bird': 'птица', 'kind': 'вид', 'sheep': 'овца',
                 'fish': 'рыба', 'snake': 'змея', 'cat': 'Кот', 'chicken': 'курица', 'cow': 'корова', 'dog': 'собака',
                 'farm': 'ферма'},

    'Спорт': {'baseball': 'бейсбол', 'basketball': 'баскетбол', 'football': 'футбол', 'sport': 'спорт',
              'swimming': 'плавание', 'tennis': 'теннис', 'club': 'клюшка',
              'gym': 'гимнастический зал', 'team': 'команда', 'game': 'игра', 'ball': 'мяч', 'fall': 'падение',
              'match': 'матч'},

    'Цвета': {'black': 'черный', 'blue': 'синий', 'brown': 'коричневый', 'cream': 'кремовый', 'orange': 'оранжевый',
              'pink': 'розовый', 'purple': 'фиолетовый', 'white': 'белый', 'paint': 'краска', 'red': 'красный',
              'yellow': 'желтый', 'gray': 'серый', 'color': 'цвет', 'green': 'зеленый', 'blond': 'блондин'},

    'Работа': {'office': 'офис', 'partner': 'партнер', 'art': 'искусство', 'article': 'статья', 'problem': 'проблема',
               'project': 'проект', 'bank': 'банк', 'business': 'бизнес', 'form': 'бланк', 'career': 'карьера',
               'cent': 'цент', 'change': 'сдача', 'chart': 'диаграмма', 'company': 'компания', 'pound': 'фунт',
               'product': 'продукт', 'conversation': 'беседа', 'cost': 'стоимость', 'customer': 'клиент',
               'dollar': 'доллар', 'euro': 'евро', 'job': 'работа (регулярная)', 'work': 'работа (объем)',
               'report': 'отчет', 'result': 'результат', 'mistake': 'ошибка', 'routine': 'рутина', 'science': 'наука',
               'visitor': 'посетитель'},

    'Профессии': {'actor': 'актер', 'artist': 'художник', 'doctor': 'доктор,врач', 'driver': 'водитель',
                  'nurse': 'медсестра', 'policeman': 'полицейский', 'scientist': 'ученый', 'singer': 'певец',
                  'teacher': 'учитель', 'waiter': 'официант', 'writer': 'писатель', 'farmer': 'фермер',
                  'model': 'модель', 'worker': 'рабочий',
                  },

    'Изучение': {'break': 'перемена', 'rule': 'правило', 'subject': 'предмет', 'spelling': 'написание',
                 'classroom': 'класс', 'exam': 'экзамен', 'history': 'история', 'map': 'карта', 'pen': 'ручка',
                 'study': 'изучение', 'music': 'музыка', 'paper': 'бумага', 'pencil': 'карандаш', 'school': 'школа',
                 'student': 'студент', 'word': 'слово', 'geography': 'география', 'teacher': 'учитель',
                 'right': 'правильно', 'test': 'испытание', 'writing': 'письмо', 'lesson': 'урок (чему учат)',
                 'answer': 'отвечать', 'capital': 'столица', 'card': 'карточка', 'class': 'урок (предмет)',
                 'college': 'колледж', 'country': 'страна', 'question': 'вопрос', 'section': 'раздел',
                 'desk': 'стол (письменный)', 'dictionary': 'словарь', 'east': 'восток', 'example': 'пример',
                 'exercise': 'упражнение', 'homework': 'домашнее здание', 'page': 'страница', 'text': 'текст',
                 'title': 'заглавие', 'topic': 'тема'},

    'Развлечения': {'band': 'группа', 'concert': 'концерт', 'guitar': 'гитара', 'piano': 'пианино', 'song': 'песня',
                    'favorite': 'любимый', 'feeling': 'чувство', 'festival': 'фестиваль', 'phone': 'телефон',
                    'movie': 'фильм', 'order': 'порядок', 'play': 'играть', 'player': 'игрок', 'present': 'подарок',
                    'reader': 'читатель', 'walk': 'ходить', 'website': 'интернет сайт',
                    'show': 'шоу', 'television': 'телевидение', 'theater': 'театр',
                    'tourist': 'турист', 'video': 'видео', 'visit': 'посещать'},

    'Время': {'clock': 'часы (настенные)', 'day': 'день', 'future': 'будущее', 'hour': 'час', 'month': 'месяц',
              'time': 'время', 'date': 'дата', 'past': 'прошлое', 'watch': 'часы (наручные)', 'morning': 'утро',
              'afternoon': 'после полудня', 'beginning': 'начало', 'minute': 'минута', 'moment': 'момент',
              'evening': 'вечер', 'night': 'ночь', 'second': 'секунда', 'midnight': 'полночь', 'today': 'сегодня',
              'tomorrow': 'завтра', 'tonight': 'сегодня ночью', 'weekend': 'выходные дни', 'yesterday': 'вчера'},

    'Календарь': {'Sunday': 'воскресенье', 'Thursday': 'четверг', 'Tuesday': 'Вторник', 'Wednesday': 'среда',
                  'Saturday': 'суббота', 'Monday': 'понедельник', 'Friday': 'пятница', 'January': 'январь',
                  'February': 'февраль', 'March': 'март', 'April': 'апрель', 'May': 'май', 'June': 'июнь',
                  'July': 'июль', 'August': 'август', 'September': 'сентябрь', 'October': 'октябрь', 'year': 'год',
                  'age': 'эра', 'birthday': 'день рождения', 'date': 'дата', 'week': 'неделя', 'November': 'ноябрь',
                  'winter': 'зима', 'summer': 'лето', 'spring': 'весна', 'autumn': 'осень', 'December': 'декабрь',
                  },

    'Одежда': {'clothes': 'одежда', 'coat': 'пальто', 'hat': 'шляпа', 'jacket': 'куртка', 'jeans': 'джинсы',
               'shirt': 'рубашка', 'skirt': 'юбка', 'sweater': 'свитер', 'pants': 'штаны', 'shoe': 'обувь',
               't-shirt': 'футболка', 'umbrella': 'зонт', 'dress': 'платье'},

    'Хобби': {'photo': 'фотография', 'reading': 'чтение', 'shopping': 'шоппинг', 'call': 'вызов', 'sing': 'петь',
              'activity': 'мероприятий', 'advice': 'совет', 'blog': 'блог', 'photograph': 'фотография',
              'camera': 'камера', 'dancing': 'танцы', 'date': 'свидание', 'diet': 'диета', 'event': 'мероприятие',
              'fun': 'весело', 'guess': 'угадать', 'practice': 'упражняться', 'program': 'программа',
              'hobby': 'хобби', 'interest': 'интерес', 'language': 'язык', 'laugh': 'смех', 'meeting': 'встреча',
              'member': 'член', 'news': 'новости', 'note': 'примечание', 'reason': 'причина', 'story': 'история',
              'skill': 'навык', 'way': 'способ',
              'style': 'стиль', 'success': 'успех', 'travel': 'путешествовать', 'trip': 'путешествие',
              },

    'Другое': {'description': 'описание', 'object': 'объект', 'action': 'действие', 'anything': 'что-ибо',
               'detail': 'деталь', 'dialogue': 'диалог', 'difference': 'разница', 'opinion': 'мнение',
               'email': 'Эл.адрес', 'fact': 'факт', 'idea': 'идея', 'meaning': 'значение', 'message': 'сообщение',
               'phrase': 'фраза', 'plan': 'план', 'return': 'возврат', 'situation': 'ситуация', 'thanks': 'спасибо',
               'statement': 'утверждение', 'type': 'тип'},

    'Указатели': {'center': 'центр', 'end': 'конец', 'group': 'группа', 'half': 'половина', 'left': 'слева',
                  'line': 'линия', 'meter': 'метр', 'mile': 'миля', 'name': 'имя', 'pair': 'пара', 'part': 'часть',
                  'north': 'север', 'place': 'место', 'point': 'точка', 'quarter': 'четверть', 'right': 'право',
                  'stop': 'останавливаться', 'turn': 'поворот', 'south': 'юг', 'west': 'запад'},

    'Восклицание': {'bye': 'до свидания (не формально)', 'goodbye': 'до свидания', 'hello': 'привет', 'oh': 'ой',
                    'hey': 'привет (не формально)', 'hi': 'привет (повседневное)', 'no': 'нет', 'ok': 'в порядке',
                    'please': 'пожалуйста', 'sorry': 'простите', 'welcome': 'добро пожаловать', 'thanks': 'спасибо',
                    'well': 'хорошо', 'yeah': 'да (довольное)', 'yes': 'да (стандартное)',
                    },

    'союзы': {'and': 'и', 'because': 'так как', 'but': 'но', 'if': 'если', 'so': 'так', 'than': 'чем', 'that': 'что',
              'until': 'до тех пор пока', 'when': 'когда', 'where': 'где', 'or': 'или',
              },

    'числа': {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'four', 'five': 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'eleven': 'одиннадцать',
              'twelve': 'двенадцать', 'thirteen': 'тринадцать', 'fourteen': 'четырнадцать', 'fifteen': 'пятнадцать',
              'sixteen': 'шестнадцать', 'seventeen': 'семнадцать', 'eighteen': 'восемнадцать', 'last': 'последний',
              'nineteen': 'девятнадцать', 'twenty': 'двадцать', 'thirty': 'тридцать', 'forty': 'сорок',
              'fifty': 'пятьдесят', 'sixty': 'шестьдесят', 'seventy': 'семьдесят', 'eighty': 'восемьдесят',
              'ninety': 'девяносто', 'hundred': 'сто', 'thousand': 'тысяча', 'million': 'миллион',
              'first': 'первый', 'second': 'второй', 'third': 'третий', 'fourth': 'четвертый', 'fifth': 'пятый',
              },

    'Предлог': {'about': 'о', 'above': 'над', 'across': 'через', 'after': 'после', 'around': 'вокруг', 'as': 'в виде',
                'at': 'на', 'before': 'до (результат)', 'behind': 'позади', 'below': 'ниже (не скрыт)', 'by': 'по',
                'down': 'вниз', 'during': 'в течение', 'for': 'за', 'from': 'от', 'in': '(где?) в', 'into': '(куда?) в',
                'like': 'как (похоже)', 'near': 'возле', 'next to': 'рядом с', 'of': 'из (выделение)', 'over': 'над',
                'off': 'отсутствовать (у противоположностей)', 'on': 'на', 'opposite': 'напротив', 'out': 'из',
                'past': 'мимо', 'through': 'через', 'under': 'под', 'until': 'до (активность)', 'up': 'вверх по',
                'with': 'с', 'without': 'без', 'between': 'между',
                },

    'Наречие': {'about': 'об', 'above': 'выше', 'again': 'очередной раз', 'ago': 'тому назад', 'always': 'всегда',
                'also': 'также', 'away': 'далеко', 'back': 'назад', 'downstairs': 'вниз по лестнице', 'each': 'каждый',
                'early': 'рано', 'then': 'затем', 'else': 'еще', 'enough': 'достаточно', 'even': 'даже',
                'ever': 'когда-либо', 'far': 'далеко', 'fast': 'быстро (двигаться)', 'first': 'сначала',
                'hard': 'тяжело',
                'here': 'здесь', 'home': 'дома', 'how': 'как', 'however': 'однако', 'in': 'внутри', 'just': 'просто',
                'late': 'поздно', 'later': 'позже', 'long': 'долго', 'lot': 'много (менее формальным)',
                'maybe': 'может быть', 'more': 'более', 'most': 'наиболее', 'much': 'много (не можем сосчитать)',
                'near': 'около', 'never': 'никогда', 'next': 'следующий', 'still': 'все еще', 'not': 'нет',
                'now': 'теперь', 'o’clock': 'на часах', 'off': 'выключено', 'often': 'довольно часто', 'on': 'согласно',
                'once': 'однажды', 'only': 'только', 'out': 'вне', 'outside': 'снаружи', 'over': 'свыше',
                'pretty': 'симпатичная', 'probably': 'вероятно', 'quickly': 'быстро (за короткое время)',
                'quite': 'вполне', 'really': 'в самом деле', 'right': 'верно', 'same': 'так же', 'sometimes': 'иногда',
                'so': 'настолько', 'soon': 'скоро', 'there': 'там', 'through': 'благодаря', 'together': 'вместе',
                'too': 'тоже', 'twice': 'дважды', 'under': 'ниже (скрывает)', 'up': 'выше',
                'upstairs': 'вверх по лестнице', 'usually': 'обычно', 'very': 'очень', 'why': 'зачем',
                },

    'Наличия': {'add': 'добавлять', 'have': 'иметь', 'include': 'включать',
                        'join': 'присоединять/присоединяться', 'keep': 'держать/хранить',
                        'lose': 'терять', 'need': 'нуждаться/нужно', 'pay': 'платить',
                        'share': 'совместно иметь или владеть', 'spend': 'тратить',
                        'take': 'занимать/требовать (по времени)', 'want': 'нуждаться/хотеть'},
    'Операции': {'break': 'ломать/ломаться', 'change': 'изменять',
                         'clean': 'чистить', 'correct': 'исправлять',
                         'cut': 'резать', 'draw': 'тянуть', 'feel': 'ощупывать', 'fill': 'наполнять',
                         'find': 'находить', 'finish': 'завершать', 'go': 'работать', 'join': 'соединять',
                         'make': 'делать', 'meet': 'встретить', 'open': 'открывать',
                         'put': 'толкать (ядро)', 'run': 'работать/быть включенным',
                         'send': 'послать/бросить', 'stop': 'заделать', 'take': 'брать',
                         'use': 'использовать', 'wash': 'мыть', 'work': 'работать'},
    'Общения': {'agree': 'соглашаться', 'answer': 'отвечать', 'ask': 'спрашивать',
                        'back': 'поддерживать', 'buy': 'покупать', 'call': 'призывать',
                        'explain': 'объяснять', 'get': 'получать',
                        'give': 'давать', 'help': 'помогать', 'let': 'сдавать внаем',
                        'meet': 'встречаться', 'order': 'приказывать', 'say': 'сказать',
                        'see': 'посещать', 'sell': 'продавать', 'show': 'показывать',
                        'speak': 'говорить (с кем)', 'talk': 'разговаривать',
                        'tell': 'сказать', 'turn': 'обращаться', 'welcome ': 'приветствовать '},
    'Стадии': {'arrive': 'появиться/подвернуться', 'become': 'наступать, приближаться',
                        'begin': 'начинать/начинаться', 'break': 'прерывать', 'change': 'становиться',
                        'complete': 'заканчивать', 'create': 'создавать', 'cut': 'резко прекращать',
                        'end': 'заканчивать/заканчиваться', 'finish': 'заканчивать/заканчиваться',
                        'grow': 'становиться', 'start': 'начинать/начинаться', 'stop': 'прекращать',
                        'turn': 'становиться'},
    'Движения': {'arrive': 'прибывать', 'come': 'приходить', 'drive': 'двигать/гнать/ехать',
                 'fly': 'проноситься/лететь', 'follow': 'следовать', 'get': 'прибывать/достигать',
                 'go': 'двигаться (идти, ехать)', 'leave': 'отправляться/покидать',
                 'move': 'двигать/двигаться', 'run': 'течь/бежать', 'stay': 'останавливать(ся) /находиться',
                 'stop': 'останавливать/останавливаться', 'take': 'захватывать',
                 'travel': 'путешествовать/двигаться', 'turn': 'поворачивать/сгибать'},
    'Мышления': {'believe': 'считать/думать', 'call': 'звать, называть', 'check': 'проверять',
                 'choose': 'выбирать', 'decide': 'принимать решение',
                 'describe': 'описывать', 'design': 'проектировать/моделировать',
                 'guess': 'предполагать', 'hear': 'слышать',
                 'imagine': 'создавать мысленный образ', 'know': 'знать/узнавать',
                 'learn': 'узнать', 'listen': 'слушать', 'look': 'смотреть',
                 'name': 'звать/давать имя', 'plan': 'планировать', 'see': 'видеть/смотреть',
                 'show': 'показывать, объяснять', 'study': 'изучать/анализировать',
                 'test': 'проверять/испытывать', 'think': 'думать', },
    'Другие глаголы': {'enjoy': 'наслаждаться', 'hope': 'надеяться', 'long': 'стремиться/очень хотеть',
                       'move': 'трогать', 'watch': 'следить ', 'put': 'класть', 'win': 'побеждать',
                       'become': 'быть к лицу/идти ', 'die': 'умирать', 'get': 'получать/зарабатывать ',
                       'have': 'есть', 'relax': 'расслабиться'},

    'Эмоции': {'afraid': 'испуганный', 'amazing': 'удивительный', 'angry': 'сердитый', 'beautiful': 'прекрасный',
               'awesome': 'потрясающие', 'boring': 'скучный', 'exciting': 'волнующий', 'fantastic': 'фантастический',
               'cold': 'холодный', 'fine': 'прекрасный', 'happy': 'счастливый', 'sad': 'грустный',
               'cool': 'хладнокровный', 'favorite': 'любимый'},

    'Абстрактные': {'common': 'обычный', 'complete': 'полный', 'few': 'немногие', 'free': 'свободный',
                    'correct': 'правильный', 'wrong': 'неправильный', 'most': 'самый',
                    'next': 'следующий', 'popular': 'популярный', 'positive': 'положительный', 'special': 'специальный',
                    'dear': 'дорогой (сердцу)', 'difficult': 'трудный', 'local': 'местный', 'possible': 'возможный',
                    'different': 'различный', 'negative': 'отрицательный', 'expensive': 'дорогой (Стоимость)'},

    'На глаз': {'better': 'более подходящий', 'best': 'лучший', 'great': 'великий', 'large': 'большой (количество)',
                'big': 'большой (значимость)', 'little': 'маленький (важность)', 'long': 'длинный', 'near': 'близкий',
                'cheap': 'дешевый', 'early': 'ранний', 'late': 'поздний', 'real': 'реальный', 'short': 'короткий',
                'small': 'маленький (размере)', 'dark': 'темный', 'tall': 'высокий'},

    'Состояние': {'busy': 'занятый (работой)', 'clean': 'чистый', 'final': 'окончательный', 'healthy ': 'здоровый',
                  'cool': 'прохладный', 'dirty': 'грязный', 'warm': 'теплый', 'young': 'молодой', 'well': 'здоровый',
                  'own': 'собственный', 'personal': 'личный', 'poor': 'бедный', 'ready': 'готовый', 'tired': 'усталый',
                  'modern': 'современный', 'sick': 'больной', 'terrible': 'ужасный', 'thirsty': 'жаждущий',
                  'new': 'новый', 'old': 'старый', 'open': 'открытый', 'perfect': 'совершенный', 'sorry': 'сожалеющий',
                  'fat': 'жирный', 'full': 'полный', 'hungry': 'голодный', 'married': 'женатый', 'rich': 'богатый',
                  'bad': 'плохой', 'friendly': 'дружеский', 'natural': 'естественный'},

    'Качества': {'false': 'фальшивый', 'dangerous': 'опасный', 'easy': 'легкий', 'hard': 'трудный', 'high': 'высокий',
                 'main': 'главный', 'nice': 'приятный', 'opposite': 'противоположный', 'wonderful': 'чудесный,',
                 'fast': 'быстрый', 'pretty': 'красивая', 'quiet': 'тихий', 'similar': 'похожий', 'slow': 'медленный',
                 'hot': 'горячий', 'strong': 'крепкий', 'sure': 'уверенный', 'true': 'истинный', 'useful': 'полезный',
                 'important': 'важный', 'interesting': 'интересный', 'same': 'одинаковый', 'smart': 'умный',
                 'delicious': 'очень вкусный', 'famous': 'знаменитый', 'funny': 'смешной', 'good': 'хороший'},

    'Местоимения': {'as': 'что', 'all': 'все', 'another': 'еще один', 'any': 'любой', 'anyone': 'кто-нибудь (один)',
                    'anything': 'что угодно', 'everybody': 'вся группа', 'everyone': 'каждый (из группы)', 'him': 'ему',
                    'everything': 'всё', 'every': 'каждый', 'he': 'он', 'she': 'она', 'her': 'её', 'nothing': 'ничего',
                    'no one': 'никто (письменный)', 'his': 'его', 'nobody': 'никто (разговорный)', 'one': 'некий',
                    'it': 'это', 'some': 'некоторые', 'somebody': 'кто-то (может быть знаком)', 'that': 'тот',
                    'us': 'нас',
                    'someone': 'кто-то (не знает человека)', 'something': 'что-нибудь', 'their': 'их', 'this': 'это',
                    'them': 'им', 'you': 'вы', 'yourself': 'себя',
                    'they': 'они', 'we': 'мы', 'what': 'какая', 'your': 'ваш', 'which': 'какой', 'who': 'кто',
                    'its': 'это', 'many': 'многие', 'me': 'меня', 'my': 'мой', 'other': 'другой', 'our': 'наш'},
}
}
