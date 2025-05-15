from .base import DesadvBase

class LineItem(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.lineitem = self.desadv.root.find(f'.//LineItem')
        self.line_number = self.lineitem.find('./LineNumber') or self.lineitem.find('./LINE_NUMBER')
        self.order_line_number = self.lineitem.find('./OrderLineNumber') or self.lineitem.find('./ORDER_LINE_NUMBER')
        self.ean = self.lineitem.find('./Ean') or self.lineitem.find('./EAN')
        self.buyer_item_code = self.lineitem.find('./BuyerItemCode') or self.lineitem.find('./BUYER_ITEM_CODE')
        self.quantity_despatched = self.lineitem.find('./QuantityDespatched') or self.lineitem.find('./QUANTITY_DESPATCHED')
        self.unit_of_measure = self.lineitem.find('./UnitOfMeasure') or self.lineitem.find('./UNIT_OF_MEASURE')
        self.item_description = self.lineitem.find('./ItemDescription') or self.lineitem.find('./ITEM_DESCRIPTION')
        self.best_before_date = self.lineitem.find('./BestBeforeDate') or self.lineitem.find('./BEST_BEFORE_DATE')
    line_number: str
    order_line_number: str
    ean: str
    buyer_item_code: str
    quantity_despatched: str
    unit_of_measure: str
    item_description: str
    best_before_date: str