from dataclasses import dataclass
from datetime import date

@dataclass 
class Medicament:
    id: int 
    nom: str
    prix: float
    quantite: int 
    date_expiration: date

def __post_init__(self, id, nom, prix, quantite, date_expiration) -> None:
        if prix <= 0:
            raise ValueError("Le prix doit être positif")
        if quantite < 0:
            raise ValueError("La quantité ne peut pas être négative")
        self.id = id
 
        self.nom=self.nom.strip()
        self.prix = prix
        self.quantite = quantite
        self.date_expiration = date_expiration


@dataclass
class client:
     id: int 
     nom: str 
     telephone: int 
def __init__(self, idt, nom, contact) -> None:
        self.id = id
        self.nom =self.nom.strip()
        self.contact = contact


class vente:
      id: int 
      medicament_id: int 
      quantite: int 
      date: date 
      total: float
      client_id: client
      medicament_id: Medicament

def __init__(self, id, client, medicament_id, quantite, date_vente: date) -> None:
        if quantite <= 0:
            raise ValueError("La quantité vendue doit être positive")
        if medicament_id.quantite < quantite:
            raise ValueError("Stock insuffisant pour cette vente")

        self.id = id
        self.client = client
        self.medicament_id = medicament_id
        self.quantite = quantite
        self.date_vente = date_vente
        self.total = medicament_id.prix * quantite

        # Mise à jour du stock du médicament
        medicament_id.quantite -= quantite
      



      


