from dataclasses import dataclass

@dataclass(frozen=True)
class ObjectDegree:
    def __init__(self, degree):
        self.id: int = degree.id
        self.name: str = degree.name


