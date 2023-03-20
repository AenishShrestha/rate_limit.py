import redis
import streamlit as st
import requests

r = redis.Redis(host='localhost', port=6379, db=0)



def get_public_ip():
    response = requests.get("https://api.ipify.org/")
    return response.text

ip_address = get_public_ip()

st.write(ip_address)

# def is_rate_limited(user_id):
#     key = f"rate_limit:{user_id}"
#     # Increment the counter for the user
#     r.incr(key)
#     # Set the TTL for the counter to 1 hour
#     r.expire(key, 3600)
#     # Check if the user has made more than 100 requests in the last hour
#     return r.get(key) > 100

# if is_rate_limited(ip_address):
#     st.write("You have exceeded the rate limit.")
# else:
#     st.write("OK")
