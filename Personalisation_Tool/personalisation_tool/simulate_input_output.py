import json
import time
from random import randint

import redis

from personalisation_tool.conf import REDIS_HOST, REDIS_PORT


class SimulateInputOutput:
    def __init__(self, redis_cli):
        self.redis_cli = redis_cli
        self.pubsub = self.redis_cli.pubsub()
        self.sub_event_types = {'next_activity_level': self.handle_next_activity_level,
                                'debug_considered_emotions': self.handle_debug_considered_emotions}

    def run(self):
        time.sleep(5)
        self.subscribe_suggested_activity_level()
        event_type = 'start_activity'
        event_data = {
            'id': 0,
            'user_level': 0,
            'activity_level': randint(0, 50) % 3
        }
        self.publish_simulated_activity_session(event_type, event_data)

        for i in range(6):
            value = randint(0, 50)
            event_type = 'emotion'
            event_data = {
                'emotion': value % 3,  # 1 is flow
            }
            print(self.publish_simulated_activity_session(event_type, event_data))
            time.sleep(2)

        event_type = 'end_activity'
        event_data = {
            'id': 0,
            'timestamp': time.time()  # 1 is flow
        }
        print(self.publish_simulated_activity_session(event_type, event_data))

        time.sleep(4)
        for i in range(3):
            value = randint(0, 50)
            event_type = 'emotion'
            event_data = {
                'emotion': value % 3,  # 1 is flow
            }
            print(self.publish_simulated_activity_session(event_type, event_data))
            time.sleep(2)

    def publish_simulated_activity_session(self, event_type, event_data):
        json_message = json.dumps(event_data)
        result = redis_cli.publish(event_type, json_message)
        return result

    def subscribe_suggested_activity_level(self):
        self.pubsub.subscribe(**self.sub_event_types)
        self.sub_thread = self.pubsub.run_in_thread(sleep_time=0.001)

    def handle_next_activity_level(self, message):
        print(message['data'])
        self.sub_thread.stop()

    def handle_debug_considered_emotions(self, message):
        print(message['data'])


if __name__ == '__main__':
    redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    simulate_input = SimulateInputOutput(redis_cli)
    for _ in range(3):
        simulate_input.run()
