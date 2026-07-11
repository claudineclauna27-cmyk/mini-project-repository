from src.entities.medication import Medication
from uscase.interface.pharmacy_repo import PharmacyRepo
from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class AddMedicationtInput:
    medication_id = int
    nom: str
    prix: float
    quantite: int = 0 
    date_expiration: Optional[date] = 0

@dataclass 
class AddMedicationOutput:
    message : str
    medication : Optional[Medication]



class AddMedication: 
    def __init__(self, repository:PharmacyRepo):
        self.repository = repository

    def execute(self, add_data:AddMedicationtInput)  -> AddMedicationOutput: 
        medication = Medication(nom=add_data.nom, prix=add_data.prix, quantite=add_data.quantite, 
                                date_expiration=add_data.date_expiration)
        medication = self.repository.save(medication)
        return AddMedicationOutput(message="votre medicament a été ajouter avec sucess")
        

        