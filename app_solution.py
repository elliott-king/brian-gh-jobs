from flask import Flask, jsonify, request

from cli_solution import GithubParser

app = Flask(__name__)
GH = GithubParser()
GH.scrape_jobs()

@app.route('/')
def hello_world():
    search = request.args.get('search', '')
    limit = int(request.args.get('limit', '10'))
    return jsonify(GH.search_jobs(search, limit))
