from dataclasses import dataclass

@dataclass(frozen=True)
class ObjectField:
    def __init__(self, field):
        self.id: int = field.id
        self.name: str = field.name
        self.degree_id: int = field.degree_id


