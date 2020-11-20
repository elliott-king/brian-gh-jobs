from flask import Flask, jsonify, request, render_template

from cli_solution import GithubParser

app = Flask(__name__)
GH = GithubParser()
GH.scrape_jobs()

@app.route('/')
def hello():
    search = request.args.get('search', '')
    limit = int(request.args.get('limit', '10'))
    jobs = GH.search_jobs(search, limit)
    # https://jinja.palletsprojects.com/en/2.11.x/templates/
    return render_template('sample.html', jobs=jobs)