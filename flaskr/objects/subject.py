from dataclasses import dataclass

@dataclass(frozen=True)
class ObjectSubject:
    def __init__(self, subject):
        self.id: int = subject.id
        self.name: str = subject.name
        self.field_id: int = subject.field_id


