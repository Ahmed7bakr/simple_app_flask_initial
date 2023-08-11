from flask import Flask

app = Flask(__name__)

app.config.from_object('config')



@app.route("/")

def hello():
    return "hello world"

if __name__ == "__main__":

    app.run(port=app.config["PORT"],debug=app.config["DEBUG"])

    # app.run()
    # app.run()
    # app.run(debug=True)
