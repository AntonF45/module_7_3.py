# Задача "Найдёт везде":
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            all_words[file_name] = self._get_words_from_file(file_name)
        return all_words

    def _get_words_from_file(self, file_name):
        words = []
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                line = self._clean_line(line)
                words += line.split()
        return words

    def _clean_line(self, line):
        for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
            line = line.replace(char, ' ')
        return line

    def find(self, word):
        found_in_files = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                found_in_files[name] = words.index(word.lower()) + 1
        return found_in_files

    def count(self, word):
        counting_words_in_a_file = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            counter = 0
            for w in words:
                if word.lower() == w.lower():
                    counter += 1
            counting_words_in_a_file[name] = counter
            return counting_words_in_a_file


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
