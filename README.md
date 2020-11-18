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
- What are some things we could do to make that part faster?

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