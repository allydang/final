from flask import Flask, render_template, request
import urllib.parse, urllib.request, urllib.error
from functions import get_score_data
import keys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit-page", methods=["POST"])
def submit_page():
    try:
        address = request.form["address"]
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])

        score_data = get_score_data(lat=latitude, lon=longitude, address=address, transit=1, bike=1)
        print(score_data)
        return render_template("results.html", score_data=score_data, address=address)
    except Exception as e:
        return render_template("error.html", error_msg=str(e))

