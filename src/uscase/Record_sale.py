from uscase.interface.pharmacy_repo import PharmacyRepo
from src.entities.sale import Sale
from dataclasses import dataclass
from typing import Optional
from datetime import date 

@dataclass
class RecordSaleInput:
     id: Optional[int] = None
     client_id: Optional[int] = None
     quantite: int = 0
     date_vente: Optional[date] = None
     total: float = 0.0


class RecordsaleOutput:
     message: str
     sale : Optional[Sale]
     

class RecordeSale:
     def __init__(self,repository:PharmacyRepo):
          self.repository = repository

     def execute(self, ):



