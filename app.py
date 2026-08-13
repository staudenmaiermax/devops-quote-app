from flask import Flask
import random

app = Flask(__name__)

QUOTES = [
    "It works on my machine! - Every Dev ever",
    "Kubernetes is just Docker with a management degree.",
    "There is no cloud, just other people's computers.",
    "Deploying on Friday is living life on the edge."
]

@app.route('/')
def home():
    quote = random.choice(QUOTES)
    return f"<h1>DevOps Quote of the Day:</h1><p>'{quote}'</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)