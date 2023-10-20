import math


# Код с третьего семинара ААА по Python
# 1
class CountVectorizer:

    def __init__(self):
        self.all_terms = []

    def fit_transform(self, corpus):
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
        return self.all_terms


# 2
def tf_transform(count_matrix):
    tf_matrix = []
    for vector in count_matrix:
        freq_counter = []
        lenght = sum(vector)
        for value in vector:
            freq_counter.append(round(value / lenght, 3))
        tf_matrix.append(freq_counter)
    return tf_matrix


# 3
def idf_transform(count_matrix):
    idf_matrix = []
    for i in range(len(count_matrix[0])):
        value = round(math.log((len(count_matrix)+1) /
                               (column_summator(i, count_matrix)+1)), 1) + 1
        idf_matrix.append(value)
    return idf_matrix


def column_summator(col, count_matrix):
    count = 0
    for row in range(len(count_matrix)):
        if count_matrix[row][col]:
            count += 1
    return count


# 4
class TfidfTransformer:

    @staticmethod
    def fit_transform(count_matrix):
        tfidf_matrix = []
        idf = idf_transform(count_matrix)
        for vector in count_matrix:
            tf = tf_transform([vector])
            tfidf_matrix.append([round(x * y, 3) for x, y in zip(idf, tf[0])])
        return tfidf_matrix


# 5
class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self._vectorizer = TfidfTransformer

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._vectorizer.fit_transform(count_matrix)
