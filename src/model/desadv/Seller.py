from . import *

class Seller(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Seller'
                 ):
        super().__init__(
            desadv_file,
            node,
            iln='ILN',
            code_by_buyer='CodeByBuyer'
        )
