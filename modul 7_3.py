class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        lst = ' '
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punctuation:
                        line = line.replace(i, ' ')
                lst = lst + line
            all_words.update({self.file_names: lst.split()})
        return all_words

    def find(self, word):
        my_dict = {}
        for self.file_names, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    my_dict.update({self.file_names: i + 1})
                    return my_dict

    def count(self, word):
        my_dict = {}
        for self.file_names, words in self.get_all_words().items():
            my_dict.update({self.file_names: words.count(word.lower())})
            return my_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('mother_goose.txt')
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
