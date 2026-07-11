from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class Sale:
    id: Optional[int] = None
    client_id: Optional[int] = None
    quantite: int = 0
    date_vente: Optional[date] = None
    total: float = 0.0
