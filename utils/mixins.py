
from abc import ABC, abstractmethod

class LoggerMixin:
    def log(self,msg):
        print("[LOG]",msg)

class BaseProcessor(ABC):
    @abstractmethod
    def process(self):
        pass
