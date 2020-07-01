from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/data", methods=["GET", "POST"])
def get_data():
    with open("fakedb.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
