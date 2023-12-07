from src.github.client import GithubClient
from src.repo.parse import RepoParse

username = 'matheuslealdeoliveira'
response = GithubClient.get_repos_by_user(username)

if response['status_code'] == 200:
    repos = RepoParse.parse(response['body'])
else:
    print(response['body'])