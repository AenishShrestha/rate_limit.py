import redis
import streamlit as st
import requests

# r = redis.Redis(host='35.201.127.49', db=0)

# r = redis.Redis()

# # Get the host and port of the Streamlit app
# host, port = st.server.server_address

# # Print the host
# print("Host:", host)

# def get_public_ip():
#     response = requests.get("https://api.ipify.org/")
#     return response.text

# ip_address = get_public_ip()

# st.write(ip_address)

# def is_rate_limited(user_id):
#     key = f"rate_limit:{user_id}"
#     # Increment the counter for the user
#     r.incr(key)
#     # Set the TTL for the counter to 1 hour
#     r.expire(key, 3600)
#     # Check if the user has made more than 100 requests in the last hour
#     return r.get(key) > 5

# if is_rate_limited(ip_address):
#     st.write("You have exceeded the rate limit.")
# else:
#     st.write("OK")
    
    
    
from flask import Flask, request
from limits import RateLimitItem, parse_many
from limits.storage import MemoryStorage
from limits.strategies import MovingWindowRateLimiter

# Set up the rate limiter
limiter = MovingWindowRateLimiter(MemoryStorage())
rate_limit = parse_many("3/hour")

def is_rate_limited(ip_address):
    for limit in rate_limit:
        if not limiter.hit(RateLimitItem(limit, ip_address)):
            return True
    return False

    client_ip = request.remote_addr

    if is_rate_limited(client_ip):
        return "Too many requests. Please try again later.", 429

    return "Hello, you are not rate limited!"



