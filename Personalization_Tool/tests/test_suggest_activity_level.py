import unittest

import redis

from personalization_tool.conf import REDIS_HOST, REDIS_PORT
from personalization_tool.suggest_activity_level import PersonalizationTool


class PersonalisationToolTestCase(unittest.TestCase):
    def setUp(self):
        self.redis_cli = redis.Redis(port=REDIS_PORT, host=REDIS_HOST)
        self.personalisation_tool = PersonalizationTool(self.redis_cli)

    def tearDown(self):
        pass

    def test_calculate_recommended_level_should_stay_same_level(self):
        expected_activity_level = 1
        emotions = [1, 1, 0, 2]
        activity_level = 1
        recommended_level = self.personalisation_tool.calculate_recommended_level(emotions, activity_level)
        self.assertEqual(recommended_level, expected_activity_level)

    def test_calculate_recommended_level_should_increase_level(self):
        expected_activity_level = 2
        emotions = [1, 0, 0, 2]
        activity_level = 1
        recommended_level = self.personalisation_tool.calculate_recommended_level(emotions, activity_level)
        self.assertEqual(recommended_level, expected_activity_level)

    def test_calculate_recommended_level_should_decrease_level(self):
        expected_activity_level = 0
        emotions = [1, 2, 2, 2]
        activity_level = 1
        recommended_level = self.personalisation_tool.calculate_recommended_level(emotions, activity_level)
        self.assertEqual(recommended_level, expected_activity_level)

    def test_calculate_emotion_frequency(self):
        emotions = [1, 2, 2, 2, 0]
        emotion = 1
        frequency = self.personalisation_tool.get_emotion_frequency(emotions, emotion)
        self.assertEqual(frequency, 1 / 5 * 100)

    def test_calculate_recommended_level_should_decrease_level_intense(self):
        self.personalisation_tool.user_level = 0
        expected_activity_level = 0
        emotions = [1, 2, 2, 2]
        activity_level = 2
        recommended_level = self.personalisation_tool.calculate_recommended_level(emotions, activity_level)
        self.assertEqual(recommended_level, expected_activity_level)

    def test_calculate_recommended_level_should_increase_level_intense(self):
        self.personalisation_tool.user_level = 2
        expected_activity_level = 2
        emotions = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2]
        activity_level = 0
        recommended_level = self.personalisation_tool.calculate_recommended_level(emotions, activity_level)
        self.assertEqual(recommended_level, expected_activity_level)
