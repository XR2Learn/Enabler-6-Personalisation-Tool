import unittest

import redis

from personalisation_tool.conf import REDIS_HOST, REDIS_PORT
from personalisation_tool.suggest_activity_level import PersonalisationTool


class PersonalisationToolTestCase(unittest.TestCase):
    def setUp(self):
        self.redis_cli = redis.Redis(port=REDIS_PORT, host=REDIS_HOST)
        self.personalisation_tool = PersonalisationTool(self.redis_cli)

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
