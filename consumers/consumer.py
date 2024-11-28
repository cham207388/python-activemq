from abc import ABC, abstractmethod


class Consumer(ABC):
    def __init__(self, queue: str):
        self.queue = queue

    @abstractmethod
    def process_message(self, message: str):
        pass
