#!/usr/bin/env python
import threading
from threading import Lock

import redis

from flask import Flask, request, jsonify, make_response, render_template

from flask_socketio import SocketIO, emit

# join_room, leave_room, \
#     close_room, rooms, disconnect

from pubsub import PubSub

from conf import (
    REDIS_HOST,
    REDIS_PORT,
    START_ACTIVITY_EVENT_TYPE,
    EMOTION_EVENT_TYPE,
    END_ACTIVITY_EVENT_TYPE,
    NEXT_ACTIVITY_LEVEL_EVENT_TYPE,
    DEBUG_CONSIDERED_EMOTIONS_EVENT_TYPE,
)


TEMPLATE_CONTEXT_CONFS = {
    'START_ACTIVITY_EVENT_TYPE': START_ACTIVITY_EVENT_TYPE,
    'END_ACTIVITY_EVENT_TYPE': END_ACTIVITY_EVENT_TYPE,
    'EMOTION_EVENT_TYPE': EMOTION_EVENT_TYPE,
    'NEXT_ACTIVITY_LEVEL_EVENT_TYPE': NEXT_ACTIVITY_LEVEL_EVENT_TYPE,
    'DEBUG_CONSIDERED_EMOTIONS_EVENT_TYPE': DEBUG_CONSIDERED_EMOTIONS_EVENT_TYPE,
}


async_mode = 'threading'

app = Flask(__name__, static_url_path="")
app.debug = True
app.config["SECRET_KEY"] = "very hidden secret!"
# app.use_reloader = False
socketio = SocketIO(app, async_mode=async_mode)


thread = None
thread_lock = Lock()


@app.route("/demo_enabler_six", methods=["get"])
def demo_enabler_six():
    context = TEMPLATE_CONTEXT_CONFS.copy()
    context['active_page'] = 'demo_enabler_six'
    return render_template("demos/enabler_six.html", **context)


@app.route("/")
def index():
    context = TEMPLATE_CONTEXT_CONFS.copy()
    return render_template("index.html", **context)


@socketio.on("connect")
def confirm_connect(auth):
    socketio.emit("ws_log", {"data": 'connected'})


@socketio.event
def pub_event(message):
    event_type = message['event_type']
    event_data = message['data']
    socketio.pub_sub.publish_msg_to_redis(event_type, event_data)


def background_thread():
    socketio.sleep(1)
    redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    pub_sub = PubSub(redis_cli=redis_cli, socket_app=socketio)
    while True:
        socketio.pub_sub.process_sub_messages()
        socketio.sleep(0.01)

def main():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    socketio.run(app, host="0.0.0.0", port=8000, allow_unsafe_werkzeug = True)



if __name__ == "__main__":
    main()
