from abc import ABC, abstractmethod
from src.entities.medication import Medication

class PharmacyRepo(ABC):
    @abstractmethod
    def save(self, medication:Medication) -> Medication:
        ...

    