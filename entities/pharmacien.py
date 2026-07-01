from dataclasses import dataclass, field
from datetime import date


@dataclass
class Medicament :
    def __init__(self, id:int, nom:str, prix:int, quantite:int, date_expiration: date) -> None:
        if prix <= 0:
            raise ValueError("Le prix doit être positif")
        if quantite < 0:
            raise ValueError("La quantité ne peut pas être négative")
        self.id = id
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        self.date_expiration = date_expiration

    def est_en_rupture(self):
        return self.quantite == 0

    def est_perime(self):
        return date.today() > self.date_expiration



class Client:
    def __init__(self, id:int, nom:str, contact:int) -> None:
        self.id = id
        self.nom = nom
        self.contact = contact



class Vente:
    def __init__(self, id:int, client: Client, medicament: Medicament, quantite, date_vente: date) -> None:
        if quantite <= 0:
            raise ValueError("La quantité vendue doit être positive")
        if medicament.quantite < quantite:
            raise ValueError("Stock insuffisant pour cette vente")

        self.id = id
        self.client = client
        self.medicament = medicament
        self.quantite = quantite
        self.date_vente = date_vente
        self.total = medicament.prix * quantite

        # Mise à jour du stock du médicament
        medicament.quantite -= quantite
