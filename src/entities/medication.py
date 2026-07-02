from dataclasses import dataclass, field
from typing import Optional
from datetime import date


@dataclass
class Medicament:
    id: Optional[int] = None
    prix: float = 0.0
    quantite: int = 0 
    date_expiration: Optional[date] = 0 

def __post_init__(self,) -> None:
    if self.prix < 0:
        raise ValueError("Le prix ne peut pas etre négatif ")
    
    if self.quantite < 0:
        raise ValueError("La quantité ne peut pas etre négative ")
    if self.date_expiration is not None and self.date_expiration < date.today ():
        raise ValueError("Le médicament est expiré")
    