import utils
__all__ = ['BoyerMoore']


class BoyerMoore:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.badMatchTable = []
        for i in range(max(256)): self.badMatchTable.append(-1)
        for i in range(self.m): self.badMatchTable[ord(pattern[i])] = self.m - i - 1

        self.operation_amount = 0

    def search(self, **kwargs):
        shift = 0
        while (shift <= self.n - self.m):
            j = self.m - 1
            self.operation_amount += 1
            while j >= 0 and self.pattern[j] == self.text[shift + j]:
                j -= 1
            if j < 0:
                print("Match at : {}".format(shift))
                shift += (self.m - self.badMatchTable[ord(self.text[shift + self.m])]
                          if shift + self.m < self.n else 1)
            else:
                shift += max(1, j - self.badMatchTable[ord(self.text[shift + j])])
