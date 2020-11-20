from flask import Flask, render_template, request, redirect
from cli_gh import GithubParser

app = Flask(__name__)

@app.route("/")
def hello():
    gh = GithubParser()
    job_scrape = gh.scrape_jobs
    job_init = gh.jobs
    return render_template("index.html", job_init = job_init)
    
@app.route("/jobsearch", methods=["GET","POST"])
def job_search():
    if request.method == "GET":
        return render_template("jobsearch.html")
    else:
        job_title = request.form.get("job_title")
        if not job_title:
            job_title = " "
        search_limit = request.form.get("search_limit")
        if not search_limit:
            search_limit = 20
        