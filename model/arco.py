from dataclasses import dataclass
from database.Prodotto import Prodotto

@dataclass
class Arco:
    u : Prodotto
    v : Prodotto
    weight : int
