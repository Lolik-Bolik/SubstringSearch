from dataclasses import dataclass
from typing import Iterable

@dataclass
class Results:
    matches: Iterable
    n_operations: int = 0
    time: float = .0
