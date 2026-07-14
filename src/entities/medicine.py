from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Medicine:
    id: int
    nom: str
    prix: float
    quantite: int
    date_expiration: Optional[date] = None

    def __post_init__(self):
        if not self.nom or self.nom.strip() == "":
            raise ValueError("The drug name cannot be empty or consist solely of spaces...")
        if self.prix < 0:
            raise ValueError("The price of the drug cannot be negative.")
        if self.quantite < 0:
            raise ValueError("The quantity of the medication cannot be negativ.")

    def est_expire(self) -> bool:
        if self.date_expiration is None:
            return False
        return self.date_expiration < date.today()
