from . import *

class Parties(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='DespatchAdvice-Parties'
                 ):
        super().__init__(
            desadv_file,
            node,
            buyer='Buyer',
            seller='Seller',
            delivery_point='DeliveryPoint'
        )
