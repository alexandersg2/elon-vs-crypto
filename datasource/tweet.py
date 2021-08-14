from dataclasses import dataclass
from datetime import datetime

from sentiment_analysis.sentiment import Sentiment


@dataclass
class Tweet:
    author: str
    post: str
    posted_at: datetime
    sentiment: Sentiment
