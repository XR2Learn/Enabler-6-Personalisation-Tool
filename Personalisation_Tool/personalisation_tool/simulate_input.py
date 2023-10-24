import redis
import json
from personalisation_tool.conf import REDIS_HOST, REDIS_PORT


def publish_input(redis_cli, event_type, event_data):
    json_message = json.dumps(event_data)
    redis_cli.publish(event_type, json_message)


if __name__ == '__main__':
    redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    event_type = 'start_activity'
    event_data = {
        'user_level': 0,  # 0 is beginner
        'activity_level': 0  # 0 is easy
    }
    publish_input(redis_cli, event_type, event_data)
