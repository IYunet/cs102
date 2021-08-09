import typing as tp
from collections import defaultdict
from math import log
from statistics import mean


class NaiveBayesClassifier:
    def __init__(self, a=1e-5):
        self.d = 0
        self.words_counter: tp.Dict[str, int] = defaultdict(int)
        self.classified_words: tp.Dict[tp.Tuple[str, str], int] = defaultdict(int)
        self.classes: tp.Dict[str, float] = defaultdict(int)
        self.a = a

    def fit(self, X, y):
        """Fit Naive Bayes classifier according to titles, labels"""

        for xi, yi in zip(X, y):
            self.classes[yi] += 1
            for word in xi.split():
                self.words_counter[word] += 1
                self.classified_words[word, yi] += 1

        for c in self.classes:
            self.classes[c] /= len(X)

        self.d = len(self.words_counter)

    def log_wi_c(self, cls, word):
        """Calculate log of probability of P(Wi|C)"""
        return log(
            (self.classified_words[word, cls] + self.a)
            / (self.words_counter[word] + self.a * self.d)
        )

    def class_probability(self, cls, feature):
        """Calculate log of probability"""
        return log(self.classes[cls]) + sum(self.log_wi_c(cls, w) for w in feature.split())

    def predict(self, feature):
        """Perform classification for one feature"""
        assert len(self.classes) > 0
        return str(max(self.classes.keys(), key=lambda c: self.class_probability(c, feature)))

    def get_predictions(self, X):
        """Perform classification on an array of test vectors X"""
        return [self.predict(feature) for feature in X]

    def score(self, X, y):
        """Returns the mean accuracy on the given test data and labels"""
        predicted = self.get_predictions(X)
        return mean(pred == actual for pred, actual in zip(predicted, y))
