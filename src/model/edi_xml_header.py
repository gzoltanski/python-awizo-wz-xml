from dataclasses import dataclass

@dataclass
class EdiXmlHeader:
    entry_no: str
    document_type: str
    reference_no: str
    delivery_date: str
    customer_gln: str
    dln: str
    status: str
    delivery_no: str
    customer_name: str
    customer_no: str

    def __repr__(self) -> str:
        return (
           f"nr zapisu: {self.entry_no},\n" 
           f"data dostawy: {self.delivery_date},\n" 
           f"nr nabywcy: {self.customer_no},\n"
           f"nazwa nabywcy: {self.customer_name},\n"
           f"GLN nabywcy: {self.customer_gln},\n"
           f"DLN: {self.dln},\n" 
           f"typ dokumentu: {self.document_type},\n" 
           f"nr referencji: {self.reference_no},\n" 
           f"nr WZ: {self.delivery_no},\n"
           f"status dok. EDI: {self.status},\n"
        )