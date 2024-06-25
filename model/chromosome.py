from dataclasses import dataclass

@dataclass
class Chromosome:
    number: int

    def __str__(self):
        return str(self.number)

    def __hash__(self):
        return hash(self.number)

