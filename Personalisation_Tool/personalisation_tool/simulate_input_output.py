import time
import redis
import json
from personalisation_tool.conf import REDIS_HOST, REDIS_PORT


class SimulateInputOutput:
    def __init__(self, redis_cli):
        self.redis_cli = redis_cli
        self.pubsub = self.redis_cli.pubsub()
        self.sub_event_types = {'next_activity_level': self.handle_next_activity_level}

    def run(self):
        self.subscribe_suggested_activity_level()
        event_type = 'start_activity'
        event_data = {
            'id': 0,
            'user_level': 0,  # 0 is beginner
            'activity_level': 0  # 0 is easy
        }
        print(self.publish_simulated_activity_session(event_type, event_data))

        for i in range(5):
            event_type = 'emotion'
            event_data = {
                'emotion': i % 3,  # 1 is flow
            }
            print(self.publish_simulated_activity_session(event_type, event_data))
            time.sleep(2)

        event_type = 'end_activity'
        event_data = {
            'id': 0,
            'timestamp': time.time()  # 1 is flow
        }
        print(self.publish_simulated_activity_session(event_type, event_data))

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


if __name__ == '__main__':
    redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    simulate_input = SimulateInputOutput(redis_cli)
    simulate_input.run()
