from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def invoke(self):
        pass