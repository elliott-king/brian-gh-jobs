import requests

class GithubParser:

    url_base = "https://jobs.github.com/positions.json"

    def __init__(self):
        self.jobs = []

    def scrape_page(self, page_num):
        # TODO: complete this. You can access self.url_base.
        url = "FIXME"
        req = requests.get(url)
        
        # This converts the json in the response to a list or dict
        list_of_jobs = req.json() 
        return list_of_jobs
    
    def scrape_jobs(self):
        for page_num in range(1, 20):
            jobs_in_page = self.scrape_page(page_num)
            self.jobs += jobs_in_page # why do we call += instead of append()?

    def search_jobs(self, keyword, max_count):
        # TODO: filter the jobs that have the keyword in their title.
        # Try not to be case sensitive.
        filtered_jobs = []
        return filtered_jobs[:max_count]

class InteractiveTerminal:

    def __init__(self):
        self.gh = GithubParser()
        self.gh.scrape_jobs()

    def ask_continue(self):
        res = input("Would you like to continue? (y/N) \n")
        if res == 'y' or res == 'Y':
            return True
        return False

    def ask_search(self):
        res = input("What kind of job would you like to search for? \n")
        # TODO: print the names of the top ten jobs that match the search
        pass

    def request_loop(self):
        # TODO: continue running until the user indicates they want to stop.
        # Feel free to refer to the tictactoe game
        pass

if __name__ == '__main__':
    terminal = InteractiveTerminal()
    terminal.request_loop()
