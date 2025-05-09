from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "InfoNaija App is running. Configuration is complete, but you need Python 3.11 to run the full application."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50505) 