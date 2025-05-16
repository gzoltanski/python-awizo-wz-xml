from . import *

class PackingSequence(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Packing-Sequence'
                 ):
        super().__init__(
            desadv_file,
            node,
            packing_reference='PackingReference',
            line='Line'
        )
