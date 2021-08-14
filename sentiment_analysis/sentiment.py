

POSITIVE = 'Positive'
NEGATIVE = 'Negative'
NEUTRAL = 'Neutral'


class SentimentBuilder:

    @staticmethod
    def from_polarity(polarity: float):
        if polarity > 0:
            return PositiveSentiment(polarity)
        if polarity < 0:
            return NegativeSentiment(polarity)
        return NeutralSentiment(polarity)

    @staticmethod
    def from_sentiment(sentiment: str):
        if sentiment is POSITIVE:
            return PositiveSentiment()
        if sentiment is NEGATIVE:
            return NegativeSentiment()
        return NeutralSentiment()


class Sentiment:
    SENTIMENT = None

    def __init__(self, polarity: float = None):
        self.polarity = polarity

    def __repr__(self):
        if self.polarity:
            return f"{self.polarity:.5f}, {self.SENTIMENT}"
        return self.SENTIMENT


class PositiveSentiment(Sentiment):
    SENTIMENT = POSITIVE


class NegativeSentiment(Sentiment):
    SENTIMENT = NEGATIVE


class NeutralSentiment(Sentiment):
    SENTIMENT = NEUTRAL
