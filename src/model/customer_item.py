from dataclasses import dataclass

@dataclass
class CustomerItem:
    customer_name: str
    item_no: str
    buyer_item_code: str
    drobimex_increment: float
    customer_increment: float
    customer_uom: str

    def __repr__(self) -> str:
        return (
            f"\nDane zapasów nabywcy:\n"
            f"-----------------------\n"
            f"nabywca: {self.customer_name},\n" 
            f"nr zapasu: {self.item_no},\n" 
            f"nr zapasu nabywcy: {self.buyer_item_code},\n" 
            f"inkrement dx: {self.drobimex_increment},\n" 
            f"inkrement nabywcy: {self.customer_increment},\n" 
            f"JM nabywcy: {self.customer_uom}\n"
        )