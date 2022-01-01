from abc import ABC, abstractmethod
from enum import Enum


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass


class ProcessId(Enum):
    CHANNEL_ID = 'channel_id'
    SEARCH_KEY = 'search_key'
