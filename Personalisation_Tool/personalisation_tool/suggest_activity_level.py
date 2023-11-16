# Your Python code here
import json
from statistics import mode

import redis

from personalisation_tool.conf import REDIS_PORT, REDIS_HOST


class PersonalisationTool:
    def __init__(self, redis_cli):
        self.redis_cli = redis_cli
        self.pubsub = self.redis_cli.pubsub()
        self.sub_event_types = {'start_activity': self.handle_start_activity,
                                'end_activity': self.handle_end_activity,
                                'emotion': self.handle_emotion}
        self.id_current_activity = None
        self.user_level = None
        self.activity_level = None
        self.emotions_session = []

    def calculate_recommended_level(self, emotions, activity_level):
        if not emotions:
            return activity_level

        most_frequent_emotion = mode(emotions)
        print(f'Most prevalent emotion: {most_frequent_emotion}')

        if most_frequent_emotion == 0:
            next_activity_level = activity_level + 1 if activity_level < 2 else activity_level
        elif most_frequent_emotion == 1:
            next_activity_level = activity_level
        else:
            next_activity_level = activity_level - 1 if activity_level > 0 else activity_level

        return next_activity_level

    def publish_recommended_level(self, id_previous_activity, next_activity_level):
        event_type = 'next_activity_level'
        event_data = {
            'id': id_previous_activity,
            'next_activity_level': next_activity_level
        }
        json_message = json.dumps(event_data)
        result = redis_cli.publish(event_type, json_message)
        return result

    def run(self):
        self.pubsub.subscribe(**self.sub_event_types)
        # Keep listening for subscribed events
        for message in self.pubsub.listen():
            pass

    def handle_start_activity(self, message):
        message_dict = self._decode_message_to_dict(message['data'])
        self.id_current_activity = int(message_dict['id'])
        self.user_level = message_dict['user_level']
        self.activity_level = message_dict['activity_level']
        print('Starting Activity Session')
        print(message['data'])

    def handle_end_activity(self, message):
        print('Ending Activity Session')
        next_activity_level = self.calculate_recommended_level(self.emotions_session,
                                                               self.activity_level)
        self.publish_recommended_level(self.id_current_activity, next_activity_level)
        self.emotions_session = []
        self.id_current_activity = None
        self.user_level = None
        self.activity_level = None
        print(message['data'])

    def handle_emotion(self, message):
        if self.id_current_activity is not None:
            message_dict = self._decode_message_to_dict(message['data'])
            self.emotions_session.append(message_dict['emotion'])

        event_type = 'debug_considered_emotions'
        event_data = {
            'emotions_session': self.emotions_session
        }
        json_message = json.dumps(event_data)
        redis_cli.publish(event_type, json_message)

        print(message['data'])
        print(self.emotions_session)

    def _decode_message_to_dict(self, message):
        message_str = message.decode('utf-8')
        message_dict = json.loads(message_str)
        return message_dict


if __name__ == '__main__':
    redis_cli = redis.Redis(port=REDIS_PORT, host=REDIS_HOST)
    personalisation_tool = PersonalisationTool(redis_cli)
    personalisation_tool.run()
