from src.repo.reports.html_generator import HTMLGenerator
from src.repo.reports.markdown_generator import MarkdownGenerator

class BadReportsGenerator():

    @classmethod
    def build(cls, type, repos):
        if type == 'HTML':
            return HTMLGenerator.build(repos)
        elif type == 'MARKDOWN':
            return MarkdownGenerator.build(repos)
        else:
            return 'Invalid report type'