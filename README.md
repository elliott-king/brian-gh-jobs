More stuff over the internet. 

# Github Jobs CLI
We will parse the [Github Jobs API](https://jobs.github.com/api). When we scraped Wikipedia, it returned HTML. However, an Application Programming Interface will usually give you something more structured than HTML. In this case, it will be JSON (Javascript Object Notation - which basically looks like a Python dict).

We will first request a bunch of positions, then will use a CLI to interact with them. Take a quick look @ the documentation. We are just going to use the `/positions` endpoint, and also add some [query parameters](https://branch.io/glossary/query-parameters/) for pagination. __Note__ it says pagination starts at page 0, but I am pretty sure that's wrong, it starts at 1.

Go to `https://jobs.github.com/positions.json`. This is what we will be using. It may look hard to follow, but it is very structured. I recommend installing [this Chrome extension](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) if you are on Chrome.

You can refer to the json to look at the structure of each job description.

## Extensions
If you want to complicate it a bit, you can:
- search more than just the job title
- allow for multiple search options (eg, title: "developer", location: "new york")

## Some follow-up questions
- line 22
- Why does the script take so long before it gives you the initial prompt?
  - requesting a bunch of information
  - multiple requests for multiple urls
- What are some things we could do to make that part faster?
  - stop requesting once there are no more jobs
  - save everything to file, only read from file (caching)

# Flask App
Flask is a python library that will run a server on your computer. When you go to a website, you are accessing somebody else's server. Here we will run our own locally, that only we can access.

Install [Flask](https://flask.palletsprojects.com/en/1.1.x/). You do not need to create a new project folder.

You can check if you are inside a Python venv - [here](https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv) are some different ways to do so. YOU SHOULD ONLY BE INSIDE THE VENV WHILE WORKING ON THIS PROJECT. Whenever you open a new command line (Windows), it will not be in a venv. Terminals in VSCode may or may not be.

Create a new python file, this will be the Flask app. I recommend you try the simple example they have before getting anything more complex.

Build an app that just has one route - the root `/` (like in the example). This app should do a few things when you visit it:
- Import the `GithubParser` & show the jobs that have been parsed by it.
- Use at the [url parameters](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object) for search and limit terms. You can use whatever phrase/word you want as the keys.
  - Filter the displayed results by the search term.
  - Limit the results by the limit (or 25, whichever is smaller)
  - Both of these terms are optional
- Make sure the results are in JSON form.

Idk how comfortable you are with this, it may be either very easy or very hard. If you have troubles, try to break it down as simply as possible (eg, hard-code the initial filter & limit)

## Redirecting Back to the Homepage with Your Search Results

So you know how to use URL parameters (we used them to filter a json response) and also how to use html templates. I would like to make your current jobsearch form usable with html (but a little cleaner). The expected functionality is pretty close to the current `app_html.py`, you will just need to modify the jobsearch function from `job_search.py` a bit:

- Going to the root `'/'` will show a link, and also a list of job titles (already done in `app_html.py`)
  - the job titles will be dependent on the query strings/url params
  - This can be tested by directly typing `localhost:5000?search=whatever&limit=a_number`
- Going to the `/jobsearch` endpoint will show a form (you have this done in `job_search.py`)
- POSTing to the `/jobsearch` endpoint will extract the search query and limit from the form, then redirect to the index
  - The index page should reflect the given search query and limit
  - You can pass query strings in the `url_for` method

## Adding a new route for each job

You can also create a route to show a job. You will want to look at the [variable rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules) section. I made the html template, so you just need to create the route.

The description will probably look a bit crappy, because the html won't correctly parse the `<p>` tag. If you need a reminder of the json format of the jobs, look [here](https://jobs.github.com/positions.json).

# Next Steps

If you have this down, we will go into the concept of 'databases' next. We will follow the more intense [Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/) to learn how to create databases & a larger project, then we will make a job board using the Github Jobs. If you want to jump ahead, feel free to start following the tutorial.