from dataclasses import dataclass

@dataclass
class LineItem:
    line_number: str
    order_line_number: str
    ean: str
    buyer_item_code: str
    quantity_despatched: str
    unit_of_measure: str
    item_description: str
    best_before_date: str