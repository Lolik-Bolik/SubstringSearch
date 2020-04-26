import utils
__all__ = ['BruteForce']
from .base import Results

class BruteForce:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)

        self.operation_amount = 0
        self.results = Results
        self.results.matches = []

    def search(self, several_matches=False):
        pass
