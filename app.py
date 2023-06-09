import redis
import streamlit as st
import requests

# r = redis.Redis(host='35.201.127.49', db=0)

# r = redis.Redis()

# # Get the host and port of the Streamlit app
# host, port = st.server.server_address

# # Print the host
# print("Host:", host)

def get_public_ip():
    response = requests.get("https://api.ipify.org/")
    return response.text

testip = get_public_ip()
ip_address = str(testip)

st.write(ip_address)

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
    
    
    
from limits import RateLimitItem, parse_many
from limits.storage import MemoryStorage
from limits.strategies import MovingWindowRateLimiter

# Set up the rate limiter
limiter = MovingWindowRateLimiter(MemoryStorage())
rate_limit = parse_many("3/hour")

def is_rate_limited(ip_address):
    for limit in rate_limit:
        if not limiter.hit(RateLimitItem(limit, ip_address)):
            st.write("OKAy")
            return True
    st.write("OKAy")
    return False

#     client_ip = ip_address

#     if is_rate_limited(client_ip):
#         st.write("Too many requests")
#         return "Too many requests. Please try again later.", 429

#     st.write("Hello")
#     return "Hello, you are not rate limited!"


is_rate_limited(ip_address)
