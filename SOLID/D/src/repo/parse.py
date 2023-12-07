from src.models.repo import Repo

class RepoParse():

    @classmethod
    def parse(cls, response):
        repos = []
        for i in range(len(response)):
            repo = response[i]
            repo = Repo(repo["id"], repo["name"], repo["stargazers_count"])
            repos.append(repo)
        return repos