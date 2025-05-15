from dataclasses import dataclass

@dataclass
class SalesLine:
    order_no: str
    line_no: str
    item_no: str
    customer_item_no: str
    item_description: str
    ean: str
    karton_ean: str
    quantity: str
    qty_to_ship: str
    uom: str
    qty_base: str
    qty_base_to_ship: str
    bbd_days: str
    bbd_date: str
    ship_release: str
    ordered_qty: str

    def __repr__(self) -> str:
        return (
            f"\nDane wiersza zamówienia:\n"
            f"--------------------------\n"
            f"nr zamówienia: {self.order_no}\n"
            f"nr wiersza: {self.line_no}\n"
            f"nr zapasu: {self.item_no}\n"
            f"nr zapasu nabywcy: {self.customer_item_no}\n"
            f"nazwa zapasu: {self.item_description}\n"
            f"EAN: {self.ean}\n"
            f"EAN kartonu: {self.karton_ean}\n"
            f"Ilość: {self.quantity}\n"
            f"Ilość do wysłania: {self.qty_to_ship}\n"
            f"JM: {self.uom}\n"
            f"Ilość bazowa: {self.qty_base}\n"
            f"Ilość bazowa do wysłania: {self.qty_base_to_ship}\n"
            f"TPS (dni): {self.bbd_days}\n"
            f"TPS (data): {self.bbd_date}\n"
            f"Zwolnienie wysyłki: {self.ship_release}\n"
            f"Ilość zamówiona: {self.ordered_qty}\n"
        )