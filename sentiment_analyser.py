from typing import Tuple, List

import nltk

from nltk import NLTKWordTokenizer
from nltk.downloader import Downloader
from nltk.corpus import stopwords
from nltk.stem import (
    SnowballStemmer,
    WordNetLemmatizer,
)
from textblob import TextBlob


class TextBlobSentimentAnalyser:
    def __init__(self):
        self._init_nltk_data()
        self.stop_words = stopwords.words('english')
        self.stemmer = SnowballStemmer('english', ignore_stopwords=True)
        self.lemmatizer = WordNetLemmatizer()
        self.tokenizer = NLTKWordTokenizer()

    @staticmethod
    def _init_nltk_data() -> None:
        nltk_downloader = Downloader()
        if not nltk_downloader.is_installed('stopwords'):
            nltk.download('stopwords')
        if not nltk_downloader.is_installed('wordnet'):
            nltk.download('wordnet')

    def _tokenize(self, document: str) -> List[str]:
        return self.tokenizer.tokenize(document)

    def _lemmatize(self, tokenized_document: List[str]) -> List[str]:
        return [
            self.lemmatizer.lemmatize(word) for word in tokenized_document
            if word not in self.stop_words
        ]

    def _stem(self, words: List[str]) -> str:
        return ' '.join([self.stemmer.stem(word) for word in words])

    @staticmethod
    def _analyse_sentiment(document: str) -> Tuple[float, float]:
        analysis = TextBlob(document)
        return analysis.sentiment

    def _pre_process(self, document: str) -> str:
        tokenized_document = self._tokenize(document)
        lemmatized_document = self._lemmatize(tokenized_document)
        stemmed_document = self._stem(lemmatized_document)
        return stemmed_document

    def analyse(self, document: str) -> Tuple[float, float]:
        pre_processed_document = self._pre_process(document)
        return self._analyse_sentiment(pre_processed_document)

    def get_polarity(self, document: str) -> float:
        return self.analyse(document)[0]

    def get_polarity_string(self, document: str) -> str:
        polarity = self.get_polarity(document)
        msg = f'{polarity}, '
        if polarity > 0:
            msg += 'Positive'
        elif polarity < 0:
            msg += 'Negative'
        else:
            msg += 'Neutral'

        return msg
