import flask

app = flask.Flask(__name__)

@app.route("/")
def frontPage():
    return flask.send_file("index.html")

if __name__=="__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
    print("App closed")