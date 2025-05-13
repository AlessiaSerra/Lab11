from dataclasses import dataclass

@dataclass
class Prodotto():
    # def __init__(self):
    Product_number : int
    Product_line : str
    Product_type : str
    Product : str
    Product_brand : str
    Product_color : str
    Unit_cost: float
    Unit_price : float

    def __str__(self):
        return f"{self.product} --- {self.unit_price}"

    def __hash__(self):
        return hash(self.product_number)

    def _eq__(self, p2):
        return self.product_number == p2.product_number