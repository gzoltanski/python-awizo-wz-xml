from dataclasses import dataclass

@dataclass
class SSCC:
    no: str
    item_no: str
    charge_no: str
    bbd: str
    quantity: str
    weight_netto: str
    rest_quantity: str
    rest_weight: str

    def __repr__(self) -> str:
        return (
           f"nr: {self.no},\n" 
           f"nr zapasu: {self.item_no},\n" 
           f"nr partii: {self.charge_no},\n" 
           f"TPS: {self.bbd},\n" 
           f"ilość: {self.quantity},\n" 
           f"masa netto: {self.weight_netto},\n" 
           f"masa netto: {self.weight_netto},\n" 
           f"poz. ilość: {self.rest_quantity},\n" 
           f"poz. masa netto: {self.rest_weight},\n"
        )


