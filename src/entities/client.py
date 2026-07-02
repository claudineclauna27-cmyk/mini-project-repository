from dataclasses import dataclass
from typing import Optional


@dataclass
class Client: 
    id: Optional[int] = None
    nom: str = ""
    contact: str = ""