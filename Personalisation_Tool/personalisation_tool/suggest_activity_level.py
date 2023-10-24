# Your Python code here
import redis
from conf import MAIN_FOLDER, REDIS_PORT, REDIS_HOST


class PersonalisationTool:
    def __init__(self, redis_cli):
        self.redis_cli = redis_cli
        self.pubsub = self.redis_cli.pubsub()
        # self.sub_event_types = ['start_activity', 'end_activity', 'emotion']
        self.sub_event_types = {'start_activity': self.handle_start_activity,
                                'end_activity': self.handle_end_activity,
                                'emotion': self.handle_emotion}

    def recommend_level(self):
        return 1

    def run(self):
        self.pubsub.subscribe(**self.sub_event_types)
        for message in self.pubsub.listen():
            # print(message)
            pass

    def handle_start_activity(self, message):
        print(message['data'])

    def handle_end_activity(self, message):
        print(message['data'])

    def handle_emotion(self, message):
        print(message['data'])


if __name__ == '__main__':
    # call_component()
    redis_cli = redis.Redis(port=REDIS_PORT, host=REDIS_HOST)
    personalisation_tool = PersonalisationTool(redis_cli)
    personalisation_tool.run()
