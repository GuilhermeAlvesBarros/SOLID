from abc import ABC, abstractmethod

class ReportWriterInterface(ABC):

    @abstractmethod
    def write(self, report):
        pass
