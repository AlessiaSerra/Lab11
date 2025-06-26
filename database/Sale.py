import datetime
from dataclasses import dataclass

@dataclass
class Sale():
    Retailer_code : int
    Product_number: int
    Order_method_code: int
    Date: datetime.date
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __hash__(self):
        return hash(self.Order_method_code)

    def __str__(self):
        return f"{self.Retailer_code} -- {self.Product_number} -- {self.Date}"

    def __eq__(self, other):
        return self.Product_number == other.Product_number
