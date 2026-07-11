from uscase.interface.pharmacy_repo import PharmacyRepo
from src.entities.medication import Medication
from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class DeleteMedicationInput:
     medication_id = int
     nom: str
     prix: float
     quantite: int = 0 
     date_expiration: Optional[date] = 0


@dataclass 
class DeleteMedicationOutput:
     deleted : bool
     message : str 
     medication = Optional[Medication]


class DeleteMedication:
     def __init__(self, repository:PharmacyRepo) -> None:
        self.repository = repository

     def execute(self, add_data:DeleteMedicationInput) -> DeleteMedicationOutput:
          medication = Medication(nom=add_data.nom)
          if not medication: 
               return DeleteMedicationOutput(
               deleted=False,
               message=f"Pharmacy '{add_data.medication_id}' not found — nothing was deleted",
               medication = None
          )
          deleted = self.repository.delete(medication)
          return DeleteMedicationOutput(deleted=True, message="Medication deleted successfully", medication=deleted)

       