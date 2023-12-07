from src.github.client_good import GithubClient
from src.repo.parse import RepoParse
from src.repo.reports_generator import ReportsGenerator
from src.repo.reports.markdown_generator import MarkdownGenerator
from src.repo.reports.html_generator import HTMLGenerator
from src.repo.reports.writer import ReportWriter

from src.models.member import Members
from src.models.manager import Managers

username = 'matheuslealdeoliveira'
response = GithubClient.get_repos_by_user(username)

if response['status_code'] == 200:
    repos = RepoParse.parse(response['body'])
    markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
    html_report = ReportsGenerator.build(HTMLGenerator, repos)
    ReportWriter.write(html_report)
    print(html_report)
    print(markdown_report)
else:
    print(response['body'])

member = Members('matheuslealdeoliveira', 'matheus@test.com')
manager = Managers('manager', 'manager@test.com')

print(member.members())
print(member.work())
print(manager.work())
