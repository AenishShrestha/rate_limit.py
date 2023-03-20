import streamlit as st


import redis
import time

redis_client = redis.Redis(host='localhost', port=8501)

def rate_limit(key, limit, period):
    now = int(time.time())
    requests = redis_client.incr(key)
    redis_client.expireat(key, now + period)

    if requests > limit:
        raise Exception('Too Many Requests')






rate_limit('my_ip', 5, 60)
st.write('okay')
