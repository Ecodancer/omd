# Надеюсь, смысл задания понял правильно)))
class CountVectorizer:
    '''
    Класс для представления терм-документной матрицы.
    ========
    Атрибуты
    --------
    all_terms : list
        Список терминов.
    Методы
    ------
    fit_transform(self, corpus):
        Представляет все слова из списка текстов (corpus)
        в виде списка терминов.
        И для каждого текста
        выводит вектор, показывающий кол-во вхождений
        в него соответствующих терминов.
    '''

    def __init__(self):
        '''
        Пусть все термины хранятся в атрибуте.
        Почему бы и нет :)
        '''
        self.all_terms = []

    def fit_transform(self, corpus):
        '''
        Два раза проходимся по списку текстов (corpus).
        После 1-го прохода получаем список всех терминов (слов).
        За 2-ой проход уже получаем векторы для каждого текста.
        Кол-во проход можно уменьшить (наверное),
        но сложность остаётся O(n).
        '''
        full_split_text = (' '.join(corpus)).split()
        all_terms = set()
        for term in full_split_text:
            term = term.lower()
            all_terms.add(term)
        self.all_terms = list(all_terms)
        count_matrix = []
        for text in corpus:
            counter = dict.fromkeys(self.all_terms, 0)
            for term in text.split():
                term = term.lower()
                counter[term] += 1
            count_matrix.append(list(counter.values()))
        return count_matrix

    def get_feature_names(self):
        '''
        Возвращаем список хранящийся в атрибуте.
        '''
        return self.all_terms


if __name__ == '__main__':  # тесты
    corpus_1 = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    corpus_2 = ['a b b b a a b b', 'c c a c b c']

    vectorizer = CountVectorizer()
    count_matrix_1 = vectorizer.fit_transform(corpus_1)
    print(vectorizer.get_feature_names())
    print(count_matrix_1)
    print('=' * 20)

    count_matrix_2 = vectorizer.fit_transform(corpus_2)
    print(vectorizer.get_feature_names())
    print(count_matrix_2)
