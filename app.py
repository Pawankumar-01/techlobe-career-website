from re import DEBUG
import flask as flask
app = flask.Flask(__name__)
@app.route("/")
def hello():
    return("Hello World")
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)