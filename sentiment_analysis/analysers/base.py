from typing import Tuple


class SentimentAnalyser:
    def analyse(self, document: str) -> Tuple[float, float]:
        raise NotImplementedError("Subclasses of SentimentAnalyser must implement an analyse method.")

    def get_polarity(self, document: str) -> float:
        raise NotImplementedError("Subclasses of SentimentAnalyser must implement a get_polarity method.")

    def get_polarity_string(self, document: str) -> str:
        raise NotImplementedError("Subclasses of SentimentAnalyser must implement a get_polarity_string method.")
