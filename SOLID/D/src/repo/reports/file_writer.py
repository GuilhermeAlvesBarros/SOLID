from src.repo.reports.report_writer_interface import ReportWriterInterface

class ReportFileWriter(ReportWriterInterface):

    @staticmethod
    def write(report):
        file = open('report.txt', 'w')
        file.write(report)
        file.close()