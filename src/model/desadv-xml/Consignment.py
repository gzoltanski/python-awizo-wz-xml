from . import *
from .PackingSequence import PackingSequence


class Consignment(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='DespatchAdvice-Consignment'
                 ):
        super().__init__(
            desadv_file,
            node,
            packing_sequence='Packing-Sequence'
        )
        # self.children: [PackingSequence] = self.children

    # def clear(self):
    #     self.clear()


