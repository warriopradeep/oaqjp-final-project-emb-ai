import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_joy(self):
        dominant_emo = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual('	joy', dominant_emo)

    def test_emotion_anger(self):
        dominant_emo = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual('	anger', dominant_emo)

    def test_emotion_disgust(self):
        dominant_emo = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual('disgust', dominant_emo)

    def test_emotion_sadness(self):
        dominant_emo = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual('sadness', dominant_emo)

    def test_emotion_fear(self):
        dominant_emo = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual('fear', dominant_emo)


if __name__ == "__main__":
    unittest.main()