#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)

def fetch_url_title(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.text)
	if hasattr(soup, "title"):
		return soup.title.text

	return ""

@app.route("/")
def index():
	return "Index!"

@app.route("/title")
def title():
	title = fetch_url_title(request.args["url"])
	return title

if __name__ == "__main__":
	app.run(debug=True)