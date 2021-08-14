from sentiment_analyser import TextBlobSentimentAnalyser

if __name__ == '__main__':
    document = "I think bitcoin will lose a huge amount of value in the long run.".lower()
    analyser = TextBlobSentimentAnalyser()
    print(analyser.get_polarity_string(document))
