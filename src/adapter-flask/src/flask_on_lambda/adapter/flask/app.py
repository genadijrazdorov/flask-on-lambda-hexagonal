import flask


app = flask.Flask(__name__)


@app.get("/")
def home():
    return "Hello"


if __name__ == "__main__":
    app.run()
