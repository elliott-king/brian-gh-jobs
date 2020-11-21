from flask import Flask, jsonify, request, render_template

from cli_gh import GithubParser

app = Flask(__name__)
GH = GithubParser()
GH.scrape_jobs()

@app.route('/')
def hello():
    search = request.args.get('search', '')
    limit = int(request.args.get('limit', '20'))
    jobs = GH.search_jobs(search, limit)
    # https://jinja.palletsprojects.com/en/2.11.x/templates/
    return render_template('index.html', job_init=jobs)
