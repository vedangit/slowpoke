 
from flask import Flask
from slowpoke import monitor

app = Flask(__name__)
monitor(app)

@app.route("/")
def fast():
    return "Fast route"

@app.route("/slow")
def slow():
    import time; time.sleep(1.5)
    return "Slow route"

if __name__ == "__main__":
    app.run(debug=True)
