from flask import Flask, render_template, request, redirect, url_for
from cli_gh import GithubParser

app = Flask(__name__)
GH = GithubParser()
GH.scrape_jobs()

@app.route("/")
def index():
    search = request.args.get('search', '')
    limit = int(request.args.get('limit', '25'))
    jobs = GH.search_jobs(search, limit)
    # https://jinja.palletsprojects.com/en/2.11.x/templates/
    return render_template("index.html", jobs=jobs)
    
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
            search_limit = 25
        # filtered_jobs = GH.search_jobs(job_title, int(search_limit))
        # don't need the above line because the url parameters get passed into redirect into the index route
        return redirect(url_for("index", search=job_title, limit=search_limit))

@app.route("/job/<string:job_id>")
def job_page(job_id):
    for job in GH.jobs:
        if job['id'] == job_id:
            return render_template("job.html", job=job)