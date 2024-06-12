from dataclasses import dataclass

@dataclass(frozen=True)
class ObjectDegree:
    def __init__(self, degree):
        self.id: int = degree.id
        self.name: str = degree.name

    def __str__(self):
        print({"id": self.id, "name": self.name})


