from dataclasses import dataclass

@dataclass
class PackageLoading:
    order_no: str
    item_no: str
    sscc: str
    charge_no: str
    charge_id: str
    bbd: str
    quantity: str
    weight_netto: str

    def __repr__(self) -> str:
        return (
            f"\nDane załadunku opakowań:\n"
            f"--------------------------\n"
            f"nr zamówienia: {self.order_no},\n" 
            f"nr zapasu: {self.item_no},\n" 
            f"nr sscc: {self.sscc},\n" 
            f"nr partii: {self.charge_no},\n" 
            f"id partii: {self.charge_id},\n" 
            f"TPS: {self.bbd},\n" 
            f"ilość: {self.quantity},\n" 
            f"masa netto: {self.weight_netto}\n"
        )