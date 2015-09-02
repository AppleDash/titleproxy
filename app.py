#!/usr/bin/env python3
import requests

from escape import escape
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

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
	escape_mode = request.args.get("escape", "")
	try:
		title = fetch_url_title(request.args["url"])
		title = escape(title, escape_mode)

		return jsonify({
			"error": False,
			"title": title
		})
	except Exception as e:
		return jsonify({
			"error": True,
			"error_message": str(e),
			"error_cause": e.__class__.__name__
		})

if __name__ == "__main__":
	app.run(debug=True)