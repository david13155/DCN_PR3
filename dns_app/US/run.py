from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

# Endpoint to get the current time in US/Eastern timezone
@app.route('/time')
def get_time():
    eastern_time = datetime.now(pytz.timezone("US/Eastern"))
    formatted_time = eastern_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
