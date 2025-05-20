from .import *

class DeliveryPoint(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='DeliveryPoint',
                 iln='ILN'
                 ):
        super().__init__(desadv_file,
                         node,
                         iln=iln
                         )
