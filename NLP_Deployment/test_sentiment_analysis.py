from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        resp1 = sentiment_analyzer("I love working with Python")
        resp2 = sentiment_analyzer("I hate working with Pyhton")
        resp3 = sentiment_analyzer("I am neutral on Python")

        self.assertEqual(resp1["label"], "SENT_POSITIVE")
        self.assertEqual(resp2["label"], "SENT_NEGATIVE")
        self.assertEqual(resp3["label"], "SENT_NEUTRAL")


unittest.main()