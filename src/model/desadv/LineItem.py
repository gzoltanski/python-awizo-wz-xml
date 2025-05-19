from . import *

class LineItem(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Line-Item'
                 ):
        super().__init__(
            desadv_file,
            node,
            line_number='LineNumber',
            order_line_number='OrderLineNumber',
            ean='EAN',
            buyer_item_code='BuyerItemCode',
            quantity_despatched='QuantityDespatched',
            unit_of_measure='UnitOfMeasure',
            item_description='ItemDescription',
            best_before_date='BestBeforeDate'
        )
