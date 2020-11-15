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

