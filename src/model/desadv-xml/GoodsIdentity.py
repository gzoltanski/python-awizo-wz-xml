from . import *

class GoodsIdentity(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Goods-Identity'
                 ) -> None:
        super().__init__(desadv_file,
                         node,
                         type='Type',
                         range='Range'
                         )
