from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,jsonify,render_template
import requests
import json
import datetime


app = Flask(__name__, template_folder='template')

@app.route("/Verify")
def Verify():
    
    return "Lead Endpoint Response Saved successfully"     



@app.route("/Scrapper")
def scrapper():
    return "Data ETL is running..."

@app.route("/")
def landing():
    return "Data ETL is running..."

if __name__ == "__main__":
    app.run()
