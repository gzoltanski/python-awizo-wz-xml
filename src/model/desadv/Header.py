from .base import DesadvBase

class Header(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.header = self.desadv.root.find(f'.//Header')
        self.despatch_advice_no = self.header.find('./DespatchAdviceNo') or self.header.find('./DESPATCH_ADVICE_NO')
        self.despatch_advice_date = self.header.find('./DespatchAdviceDate') or self.header.find('./DESPATCH_ADVICE_DATE')
        self.estimated_delivery_date = self.header.find('./EstimatedDeliveryDate') or self.header.find('./ESTIMATED_DELIVERY_DATE')
        self.buyer_order_number = self.header.find('./BuyerOrderNumber') or self.header.find('./BUYER_ORDER_NUMBER')
        self.despatch_number = self.header.find('./DespatchNumber') or self.header.find('./DESPATCH_NUMBER')
    despatch_advice_no: str
    despatch_advice_date: str
    estimated_delivery_date: str
    buyer_order_number: str
    despatch_number: str