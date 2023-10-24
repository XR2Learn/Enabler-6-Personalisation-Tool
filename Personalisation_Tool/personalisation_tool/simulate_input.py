import time

import redis
import json
from personalisation_tool.conf import REDIS_HOST, REDIS_PORT


# def publish_input(redis_cli, event_type, event_data):
#     json_message = json.dumps(event_data)
#     result = redis_cli.publish(event_type, json_message)
#     return result
#
#
# def simulate_activity_session(redis_cli):
#     event_type = 'start_activity'
#     event_data = {
#         'user_level': 0,  # 0 is beginner
#         'activity_level': 0  # 0 is easy
#     }
#
#     print(publish_input(redis_cli, event_type, event_data))


class SimulateInput:
    def __init__(self, redis_cli):
        self.redis_cli = redis_cli

    def run(self):
        event_type = 'start_activity'
        event_data = {
            'id': 0,
            'user_level': 0,  # 0 is beginner
            'activity_level': 0  # 0 is easy
        }
        print(self.publish_simulated_activity_session(event_type, event_data))

        for i in range(10):
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


if __name__ == '__main__':
    redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    # simulate_activity_session(redis_cli)

    simulate_input = SimulateInput(redis_cli)
    simulate_input.run()
