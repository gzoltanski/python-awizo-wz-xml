from dataclasses import dataclass

@dataclass
class Header:
    despatch_advice_no: str
    despatch_advice_date: str
    estimated_delivery_date: str
    buyer_order_number: str
    despatch_number: str