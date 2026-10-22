import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

@app.route("/")
def index():
    return render_template("index.html", laureates=laureates)

@app.route("/laureates")
def laureate():
    return jsonify(laureates)

if __name__ == "__main__":
    app.run(debug=True)