

class Language():
    def __init__(self, lang='ru'):
        self.language = lang
        self.title_by_language = {"ru": {"TITLE_BTN_NEXT": 'Следующий',
                                         "TITLE_NAME_ONLY_CHARACTERS": 'Имя только из букв',
                                         "TITLE_NAME_NOT_LONGER": 'Имя до 10 символов',
                                         "TITLE_HI_WHAT_ARE_YOUR_NAME": 'Привет! Как тебя зовут?',
                                         "TITLE_HOW_LOD_ARE_YOU": 'какого \nты года рождения?',
                                         "TITLE_YOU_ARE_FROM_THE_PAST": 'Ты из прошлого?',
                                         "TITLE_YOU_ARE_FROM_THE_FUTURE": 'Ты из будущего?',
                                         "TITLE_YOUR_MAIL": 'Твоя электронная почта?',
                                         "TITLE_DONT_LOOK_LIKE_REAL_MAIL": 'На настоящую почту не похоже!',
                                         "TITLE_WHAT_GENDER_ARE_YOU": 'Последний вопрос. Какого ты пола?',
                                         "TITLE_MALE": 'Мужской',
                                         "TITLE_FEMALE": 'Женский',
                                         },
                                  "ua": {"TITLE_BTN_NEXT": 'Наступний',
                                         "TITLE_NAME_ONLY_CHARACTERS": "Ім'я тільки з букв",
                                         "TITLE_NAME_NOT_LONGER": "Ім'я до 10 символів",
                                         "TITLE_HI_WHAT_ARE_YOUR_NAME": 'Вітаю! Як тебе звати?',
                                         "TITLE_HOW_LOD_ARE_YOU": 'якого \nти року народження?',
                                         "TITLE_YOU_ARE_FROM_THE_PAST": 'Ти з минулого?',
                                         "TITLE_YOU_ARE_FROM_THE_FUTURE": 'Ти з майбутнього?',
                                         "TITLE_YOUR_MAIL": 'Твоя електронна пошта?',
                                         "TITLE_DONT_LOOK_LIKE_REAL_MAIL": 'На справжню пошту не схоже!',
                                         "TITLE_WHAT_GENDER_ARE_YOU": 'Останнє питання. Якої ти статі?',
                                         "TITLE_MALE": 'Чоловічий',
                                         "TITLE_FEMALE": 'Жіночий',
                                         },
                                  }

    def title(self, title):
        return self.title_by_language[self.language][title]
