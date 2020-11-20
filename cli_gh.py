import requests

class GithubParser:

    url_base = "https://jobs.github.com/positions.json"

    def __init__(self):
        self.jobs = []

    def scrape_page(self, page_num):
        # TODO: complete this. You can access self.url_base.
        url = self.url_base + "?page=" + str(page_num)
        req = requests.get(url)    
        # This converts the json in the response to a list or dict
        list_of_jobs = req.json() 
        return list_of_jobs
    
    def scrape_jobs(self):
        for page_num in range(1, 20):
            jobs_in_page = self.scrape_page(page_num)
            if jobs_in_page:
                self.jobs += jobs_in_page
            else:
                break
            # why do we call += instead of append()? 
            # Because you cannot append a list to a another list. We are not adding 1 particular item or index to the list but rather another list

    def search_jobs(self, keyword, max_count):
        # TODO: filter the jobs that have the keyword in their title.
        # Try not to be case sensitive.
        filtered_jobs = []
        for job in self.jobs:
            if keyword.lower() in job['title'].lower():
                filtered_jobs.append(job)
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
        count = 10
        print(self.gh.search_jobs(res, count))
        # TODO: print the names of the top ten jobs that match the search       

    def request_loop(self):
        # TODO: continue running until the user indicates they want to stop.
        # Feel free to refer to the tictactoe game
        self.ask_search()
        if self.ask_continue():
            self.request_loop()

if __name__ == '__main__':
    terminal = InteractiveTerminal()
    terminal.request_loop()
