from dataclasses import dataclass

@dataclass
class AssignedSSCC:
    order_no: str
    line_no: str
    sscc: str
    quantity: str
    weight_netto: str

    def __repr__(self) -> str:
        return (
            f"\nDane przypisania SSCC:\n"
            f"-------------------------\n"
            f"nr zamówienia: {self.order_no},\n" 
            f"nr wiersza: {self.line_no},\n" 
            f"SSCC: {self.sscc},\n" 
            f"ilość: {self.quantity},\n" 
            f"masa netto: {self.weight_netto}\n"
        )