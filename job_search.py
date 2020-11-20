from flask import Flask, render_template, request, redirect
from cli_gh import GithubParser

app = Flask(__name__)
GH = GithubParser()
GH.scrape_jobs()

@app.route("/")
def hello():
    job_init = GH.jobs
    print('job init', len(job_init))
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
        filtered_jobs = GH.search_jobs(job_title, int(search_limit))

        # redirect to '/' and also with filtered_jobs
        return render_template('index.html', job_init=filtered_jobs)