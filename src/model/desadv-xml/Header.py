from . import *

class Header(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='DespatchAdvice-Header',
                 ):
        super().__init__(
            desadv_file,
            node,
            despatch_advice_no='DespatchAdviceNumber',
            despatch_advice_date='DespatchAdviceDate',
            estimated_delivery_date='EstimatedDeliveryDate',
            buyer_order_number='BuyerOrderNumber',
            despatch_number='DespatchNumber',
            despatch_date='DespatchDate'
        )
