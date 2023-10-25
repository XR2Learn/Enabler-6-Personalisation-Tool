from decouple import config

REDIS_ADDRESS = config('REDIS_ADDRESS', default='localhost')
REDIS_PORT = config('REDIS_PORT', default='6379')

EMOTION_EVENT_TYPE =  config('EMOTION_EVENT_TYPE', default='emotion')
START_ACTIVITY_EVENT_TYPE =  config('START_ACTIVITY_EVENT_TYPE', default='start_activity')
END_ACTIVITY_EVENT_TYPE =  config('END_ACTIVITY_EVENT_TYPE', default='end_activity')
NEXT_ACTIVITY_LEVEL_EVENT_TYPE =  config('NEXT_ACTIVITY_LEVEL_EVENT_TYPE', default='next_activity_level')

