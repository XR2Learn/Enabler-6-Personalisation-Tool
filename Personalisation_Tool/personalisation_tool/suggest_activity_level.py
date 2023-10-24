# Your Python code here
import redis
import json
from conf import REDIS_PORT, REDIS_HOST


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

    def recommend_level(self, emotions, user_level, activity_level, id_previous_activity):
        event_type = 'next_activity_level'
        event_data = {
            'id': id_previous_activity,
            'next_activity_level': 1
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
        print(
            self.recommend_level(self.emotions_session, self.user_level, self.activity_level, self.id_current_activity))
        self.emotions_session = []
        self.id_current_activity = None
        self.user_level = None
        self.activity_level = None
        print(message['data'])

    def handle_emotion(self, message):
        if self.id_current_activity is not None:
            message_dict = self._decode_message_to_dict(message['data'])
            self.emotions_session.append(message_dict['emotion'])
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
