from flask import Flask
from flask_cors import CORS  

PORT = 8000
MESSAGE = "Hello, world!\n"

app = Flask(__name__)
CORS(app)  


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
