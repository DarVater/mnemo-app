import json
from random import randint
import time

from kivy.storage.jsonstore import JsonStore
from word_by_topics import words_by_lvl

from language import Language

class Associator():
    def __init__(self):
        self.ru_nouns = []
        self.given_word = ''
        self.china_word = ''
        self.broken_versions = {}
        self.version_words = {}
        self.realization_time = ''
        self._start_time = {}
        self.sum_times = 0
        self.def_lvl = 0

    def start_t(self, name):
        self._start_time[name] = time.perf_counter()
        self.realization_time += f"\n{'    '*self.def_lvl} {name}"
        self.def_lvl += 1

    def stop_t(self, name):
        self.sum_times += time.perf_counter() - self._start_time[name]
        self.def_lvl -= 1
        self.realization_time += f"\n{'    '*self.def_lvl} {name} {round(time.perf_counter() - self._start_time[name],3)}"

    def load_dict(self, name: str):
        '''
        load dict from data file
        :param name:
        :return:
        '''
        self.start_t("load_dict"+name)
        with open(f'{name}.data', 'r') as file:
            ret = json.loads(file.read())
            self.stop_t("load_dict"+name)
            return ret

    def china_trans(self, word_trans: str) -> str:
        '''
        replace english transcription letter into russian
        :param word_trans:
        :return:
        '''
        self.start_t("china_trans")
        store = JsonStore(f'hello_{words_by_lvl["en_lvl"]}.json')
        lang = Language()
        lang.set_lang(store.get('user')['lang'])
        china_dict = self.load_dict(lang.title('FILE_CHINA_TRANS'))
        for compl in china_dict['complex']:
            word_trans = word_trans.replace(compl, china_dict['complex'][compl])
        for compl in china_dict['simple']:
            word_trans = word_trans.replace(compl, china_dict['simple'][compl])
        self.china_word = word_trans
        self.stop_t("china_trans")
        return word_trans

    def check_other_letters(self, letters_type: str):
        '''
        Function don`t allow all symbols but russian "г", "с"
        :param letters_type:
        :return:
        '''
        self.start_t("check_other_letters")
        for letter in letters_type:
            if letter not in ['г', 'с']:
                print(f"ERROR! Not expected letter '{letter}' !")
                raise "ERROR! Look last print()"
        self.stop_t("check_other_letters")

    def get_letters_type(self, china_word: str):
        """
        replace avery vowel letter to "г" and consonant to "с"
        :param china_word:
        :return:
        """
        self.start_t("get_letters_type")
        ru_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'і', 'е']
        ru_consonant = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч',
                        'ш', 'щ', 'ъ', 'ь']
        for vowel in ru_consonant:
            china_word = china_word.replace(vowel, 'с')
        for vowel in ru_vowels:
            china_word = china_word.replace(vowel, 'г')
        self.stop_t("get_letters_type")
        return china_word

    def random_change(self, syllables_version: str):
        '''
        random move lonely vowel or consonant to syllables
        :param syllables_version:
        :return:
        '''
        from_to = [['с[', '[С'],
                   [']с', 'С]'],
                   ['[Г][', '[Г'],
                   ['][Г]', 'Г]']]
        r_num = randint(0, len(from_to) - 1)
        syllables_version = syllables_version.replace(from_to[r_num][0], from_to[r_num][1], 1)
        return syllables_version

    def find_version(self, root_syllables: str) -> str:
        '''
        move single letters while put togather
        :param root_syllables:
        :return:
        '''
        syllables_version = root_syllables
        if ']с' in syllables_version or 'с[' in syllables_version or '[Г]' in syllables_version:
            while True:
                syllables_version = self.random_change(syllables_version)
                if 'с' not in syllables_version and '[Г]' not in syllables_version:
                    return syllables_version

    def find_all_version(self, root_syllables: str) -> dict:
        '''
        regenerate new version of letters connection
        :param root_syllables:
        :return:
        '''
        self.start_t("find_all_version")
        all_syllables_version = {}
        loos_try = 0
        while True:
            start_count_versions = len(all_syllables_version)
            syllables_version = self.find_version(root_syllables)
            all_syllables_version[syllables_version] = ''
            if len(all_syllables_version) == start_count_versions:
                loos_try += 1
            if loos_try > 15:
                break
        self.stop_t("find_all_version")
        return all_syllables_version

    def break_a_word_into_syllables(self, china_word: str):
        self.start_t("break_a_word_into_syllables")
        letters_type = self.get_letters_type(china_word)
        self.check_other_letters(letters_type)
        letters_type = letters_type.replace('сг', '[СГ]')
        root_syllables = letters_type.replace('г', '[Г]')
        all_syllables_version = self.find_all_version(root_syllables)
        self.stop_t("break_a_word_into_syllables")
        return all_syllables_version

    def collect_syllables(self, root_syllables: str):
        '''
        random connect syllables
        :param root_syllables:
        :return:
        '''
        row = root_syllables
        space_c = 0
        if '][' in root_syllables:
            for n in range(10):
                if '][' in row:
                    row = row.replace('][', str(n), 1)
                    space_c += 1
            row = row.replace(str(randint(0, space_c - 1)), '')
            for n in range(10):
                row = row.replace(str(n), '][')
        return row

    def collect_avery_syllables(self, all_syllables: dict) -> dict:
        '''
        collect avery syllables in different group
        :param all_syllables:
        :return:
        '''
        self.start_t("collect_avery_syllables")
        all_syllables_version = {}
        loos_try = 0
        while True:
            start_count_versions = len(all_syllables_version)
            for one_syllables in all_syllables:
                if type(one_syllables) != type(None):
                    collection_of_syllables = self.collect_syllables(one_syllables)
                    all_syllables_version[collection_of_syllables] = ''
            if len(all_syllables_version) == start_count_versions:
                loos_try += 1
            if loos_try > 10:
                break
        self.stop_t("collect_avery_syllables")
        return all_syllables_version

    def get_logic_like_syllables(self, syllables: str) -> list:
        """
        function count avery syllables in word
        :param syllables:
        :return:
        """
        syllables_logic = []
        if '][' in syllables:
            syllables_part = syllables.split('][')
            for part in syllables_part:
                clear_part = part.replace('[', '').replace(']', '')
                syllables_logic.append(len(clear_part))
        else:
            clear_part = syllables.replace('[', '').replace(']', '')
            syllables_logic.append(len(clear_part))

        return syllables_logic

    def make_syllables(self, word: str, syllables_logic: list) -> list:
        '''
        get first letter in word syllables_logic times
        :param word:
        :param syllables_logic:
        :return:
        '''
        word_like_syllables = []
        for logic_times in syllables_logic:
            word_part = ''
            for n in range(logic_times):
                word_part = f'{word_part}{word[n]}'
            word_like_syllables.append(word_part)
            word = word[logic_times::]
        return word_like_syllables

    def split_word_lake_all_syllables(self, word: str, all_syllables: dict) -> list:
        '''
        get word and make like syllables
        :param word:
        :param all_syllables:
        :return:
        '''

        broken_word = []
        for syllables in all_syllables.keys():
            syllables_logic = self.get_logic_like_syllables(syllables)
            word_like_syllables = self.make_syllables(word, syllables_logic)
            broken_word.append(word_like_syllables)
        return broken_word

    def compare_ane_known_word(self, ru_nouns: str, word_part: str) -> list:
        '''
        calculate sub string and wrong letters
        :param word_part:
        :param ru_nouns:
        :return:
        '''
        score = 0
        find_at_x = -1
        find_at_y = -1
        see_known_word = ru_nouns
        similar_letters = {'б': 'п',
                           'в': 'ф',
                           'г': 'к',
                           'д': 'т',
                           'з': 'с',
                           'ж': 'ш',
                           'п': 'б',
                           'ф': 'в',
                           'к': 'г',
                           'т': 'д',
                           'с': 'з',
                           'ш': 'ж',
                           'э': 'е',
                           'е': 'э',
                           }
        similar_scores = 0
        for x in range(len(word_part)):
            for y in range(len(ru_nouns)):
                if word_part[x] == ru_nouns[y]:
                    if find_at_x < x and find_at_y < y:
                        find_at_x = x
                        find_at_y = y
                        see_known_word = see_known_word[0:y] + see_known_word[y].upper() + see_known_word[(y + 1)::]
                        score += 1
                if ru_nouns[y] in similar_letters and word_part[x] == similar_letters[ru_nouns[y]]:
                    if find_at_x < x and find_at_y < y:
                        find_at_x = x
                        find_at_y = y
                        see_known_word = see_known_word[0:y] + see_known_word[y].upper() + see_known_word[(y + 1)::]
                        score += 1
                        similar_scores += 1
        up_l = 0
        miss_l = 0
        for l in see_known_word:
            if l.isupper():
                up_l += 1
            else:
                miss_l += 1
            if up_l == score:
                break
        return [score, miss_l + (similar_scores / 2), see_known_word]

    def get_best_version(self, all_word_parts: dict) -> list:
        self.start_t("get_best_version")
        # get best score versions plus miss letters to find the lowest
        race_participants = {}
        best_len = max(all_word_parts.keys())
        for burden in range(3):
            for version in all_word_parts[best_len - burden]:
                if version[0] + version[1] + burden * 2 in race_participants:
                    race_participants[version[0] + version[1] + burden * 2].append(version)
                else:
                    race_participants[version[0] + version[1] + burden * 2] = [version]

        # get best version and find the shorter
        tails_race = {}
        for best_words in sorted(race_participants.keys()):
            for version in race_participants[best_words]:
                tail = int((len(version[2]) - version[0] - version[1]) * 2)
                if tail not in tails_race:
                    tails_race[tail] = [version]
                else:
                    tails_race[tail].append(version)
            nn = 0
            for part in tails_race:
                nn += len(tails_race[part])
            if nn > 10:
                break

        best_versions = []
        for tail_l in range(max(tails_race.keys())):
            if tail_l in tails_race:
                if len(best_versions) < 10:
                    best_versions = best_versions + tails_race[tail_l]
        self.stop_t("get_best_version")
        return best_versions

    def get_words_of_broken_version(self, broken_word: str ) -> list:
        self.start_t("get_words_of_broken_version")
        all_compares = []
        if not self.ru_nouns:
            store = JsonStore(f'hello_{words_by_lvl["en_lvl"]}.json')
            lang = Language()
            lang.set_lang(store.get('user')['lang'])
            self.ru_nouns = self.load_dict(lang.title('FILE_NOUNS'))
        for word_part in broken_word:
            all_word_parts = {}
            self.start_t("get_words_of_broken_version # one word_part")
            for known_word in self.ru_nouns:
                compare_data = self.compare_ane_known_word(known_word, word_part)
                if compare_data[0] not in all_word_parts:
                    all_word_parts[compare_data[0]] = [compare_data]
                else:
                    all_word_parts[compare_data[0]].append(compare_data)
            self.stop_t("get_words_of_broken_version # one word_part")
            self.start_t("get_words_of_broken_version # append")
            all_compares.append(self.get_best_version(all_word_parts))
            self.stop_t("get_words_of_broken_version # append")
        self.stop_t("get_words_of_broken_version")
        return all_compares

    def find_broken_word_versions(self, china_word: str) -> dict:
        self.start_t("find_broken_word_versions")
        all_syllables = self.break_a_word_into_syllables(china_word)
        syllables_connections = self.collect_avery_syllables(all_syllables)
        all_syllables.update(syllables_connections)
        broken_word_version = self.split_word_lake_all_syllables(china_word, all_syllables)
        self.stop_t("find_broken_word_versions")
        return dict((zip([n for n in range(len(broken_word_version))], broken_word_version)))

    def get_broken_word(self, word):
        self.start_t("get_broken_word")
        word_trans_dict = self.load_dict('word_trans_dict')
        self.given_word = word.lower()
        if self.given_word in word_trans_dict:
            word_trans = word_trans_dict[self.given_word]
        else:
            self.given_word = word.lower()[0].upper() + word.lower()[1::]
            word_trans = word_trans_dict[self.given_word]
        self.china_trans(word_trans)
        self.broken_versions = self.find_broken_word_versions(self.china_word)
        self.stop_t("get_broken_word")
        return self.broken_versions

    def get_words_of_broken_of_all_version(self, broken_word_version: list) -> dict:
        self.start_t("get_words_of_broken_of_all_version")
        all_seem_word = {}
        for broken_word in broken_word_version:
            fined_seem_word = self.get_words_of_broken_version(broken_word )
            all_seem_word['|'.join(broken_word)] = fined_seem_word
        self.stop_t("get_words_of_broken_of_all_version")
        return all_seem_word


if __name__ == '__main__':
    ass = Associator()
    broken_word = ass.get_broken_word('house')
    for n in broken_word:
        print(f"{n}) {broken_word[n]}")
    print('Enter need version: ')
    answer = int(input())
    all_compares = ass.get_words_of_broken_version(broken_word[answer])
    for n in all_compares:
        print(n)
    with open('realization_time.txt', 'w') as file:
        file.write(ass.realization_time)

    print(ass.sum_times)


