import os
import time
import threading
import requests

RENDER_BASE = os.environ.get("RENDER_API_URL", "https://my-personal-website-t7tw.onrender.com")
RENDER_URL = os.environ.get("RENDER_HEALTH_URL", f"{RENDER_BASE.rstrip('/')}/health")
PING_INTERVAL = 300  # 5 minutes in seconds

def keep_alive_ping():
    """Send a ping to the health endpoint every 5 minutes"""
    while True:
        try:
            print(f"Sending keep-alive ping to {RENDER_URL}")
            response = requests.get(RENDER_URL)
            print(f"Ping response: {response.status_code}")
        except Exception as e:
            print(f"Ping error: {str(e)}")
        
        # Sleep for the ping interval
        time.sleep(PING_INTERVAL)

# Start the keep-alive thread when this module is imported
keep_alive_thread = threading.Thread(target=keep_alive_ping, daemon=True)
keep_alive_thread.start() 
