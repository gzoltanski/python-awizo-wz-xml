from . import *

class Buyer(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Buyer',
                 iln='ILN'):
        super().__init__(desadv_file,
                         node,
                         iln=iln)
