from dataclasses import dataclass

@dataclass
class SalesHeader:
    no: str
    reference: str
    customer_no: str
    payer_no: str
    order_date: str
    shipment_date: str
    document_status: str
    twz: str

    def __repr__(self) -> str:
        return (
            f"\nDane nagłówka zamówienia:\n"
            f"--------------------------\n"
            f"nr: {self.no},\n" 
            f"nr zam. nabywcy: {self.reference},\n" 
            f"nr płatnika: {self.payer_no},\n" 
            f"data zamówienia: {self.order_date},\n" 
            f"data dostawy: {self.shipment_date},\n" 
            f"status dokumentu: {self.document_status},\n" 
            f"TWZ: {self.twz}\n"
        )
