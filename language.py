

class Language():
    def __init__(self, lang='ru'):
        self.language = lang
        self.title_by_language = {"ru": {"TITLE_BTN_NEXT": 'Следующий',
                                         "TITLE_NAME_ONLY_CHARACTERS": 'Имя только из букв',
                                         "TITLE_NAME_NOT_LONGER": 'Имя до 10 символов',
                                         "TITLE_HI_WHAT_ARE_YOUR_NAME": 'Привет! Как тебя зовут?',
                                         "TITLE_HOW_LOD_ARE_YOU": 'какого ты года рождения?',
                                         },
                                  "ua": {"TITLE_BTN_NEXT": 'Наступний',
                                         "TITLE_NAME_ONLY_CHARACTERS": "Ім'я тільки з букв",
                                         "TITLE_NAME_NOT_LONGER": "Ім'я до 10 символів",
                                         "TITLE_HI_WHAT_ARE_YOUR_NAME": 'Вітаю! Як тебе звати?',
                                         },
                                  }

    def title(self, title):
        return self.title_by_language[self.language][title]
