import redis
import time


def check_and_increment_connections(username):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    total_connections_key = f"user:{username}:total_connections"
    last_login_key = f"user:{username}:last_login"

    r.set(last_login_key, time.time())
    total_connections = r.get(total_connections_key)
    last_login_timestamp = r.get(last_login_key)

    if time.time() - float(last_login_timestamp) < 600:
        r.incr(total_connections_key)
    else:
        r.set(total_connections_key, 1)
        r.set(last_login_key, time.time())

    if total_connections is not None and int(total_connections) >= 10 and time.time() - float(last_login_timestamp) < 600:
        print("false")
    else:
        print("true")


check_and_increment_connections("Ugo")