from abc import ABC, abstractmethod

class Producer(ABC):
    def __init__(self, queue: str):
        self.queue = queue

    @abstractmethod
    def send_message(self, message: str):
        pass
