import json
import time

from conf import (
    EMOTION_EVENT_TYPE,
    START_ACTIVITY_EVENT_TYPE,
    END_ACTIVITY_EVENT_TYPE,
    NEXT_ACTIVITY_LEVEL_EVENT_TYPE,
    DEBUG_CONSIDERED_EMOTIONS_EVENT_TYPE
)


class PubSub():
    def __init__(self, redis_cli, socket_app):
        self.redis_cli = redis_cli
        self.socket_app = socket_app
        self.socket_app.pub_sub = self

        self.sub_event_types = {
            NEXT_ACTIVITY_LEVEL_EVENT_TYPE: self.handle_next_activity_level,
            DEBUG_CONSIDERED_EMOTIONS_EVENT_TYPE: self.handle_debug_next_activity_level
        }
        self.pubsub = self.redis_cli.pubsub()
        self.pubsub.subscribe(**self.sub_event_types)

    # def subscribe_suggested_activity_level(self):
    #     self.pubsub.subscribe(**self.sub_event_types)
    #     self.sub_thread = self.pubsub.run_in_thread(sleep_time=0.001)

    # def run_old(self):
    #     self.subscribe_suggested_activity_level()
    #     event_type = START_ACTIVITY_EVENT_TYPE
    #     event_data = {
    #         'id': 0,
    #         'user_level': 0,  # 0 is beginner
    #         'activity_level': 0  # 0 is easy
    #     }
    #     print(self.publish_simulated_activity_session(event_type, event_data))

    #     for i in range(5):
    #         event_type = EMOTION_EVENT_TYPE
    #         event_data = {
    #             'emotion': i % 3,  # 1 is flow
    #         }
    #         print(self.publish_simulated_activity_session(event_type, event_data))
    #         time.sleep(2)

    #     event_type = END_ACTIVITY_EVENT_TYPE
    #     event_data = {
    #         'id': 0,
    #         'timestamp': time.time()  # 1 is flow
    #     }
    #     print(self.publish_simulated_activity_session(event_type, event_data))

    def publish_msg_to_redis(self, event_type, event_data):
        json_message = json.dumps(event_data)
        result = self.redis_cli.publish(event_type, json_message)
        return result

    def decode_message_data(self, message):
        return json.loads(message['data'].decode('utf-8'))

    def handle_next_activity_level(self, message):
        data = self.decode_message_data(message)
        # print(f'Handling "{NEXT_ACTIVITY_LEVEL_EVENT_TYPE}": {data} \n will emit this to socket app. {self.count}')
        self.socket_app.emit(
            NEXT_ACTIVITY_LEVEL_EVENT_TYPE,
            {
                'data': data,
            }
        )

    def handle_debug_next_activity_level(self, message):
        data = self.decode_message_data(message)

        self.socket_app.emit(
            DEBUG_CONSIDERED_EMOTIONS_EVENT_TYPE,
            {
                'data': data,
            }
        )

    def process_sub_messages(self):
        msgs = self.pubsub.get_message()

        # self.sub_thread = self.pubsub.run_in_thread(sleep_time=0.001)

        # self.sub_thread.stop()
