from . import *

class DespatchAdvice(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node=None
                 ):
        super().__init__(
            desadv_file,
            node,
            header='DespatchAdvice-Header',
            transport='DespatchAdvice-Transport',
            parties='DespatchAdvice-Parties',
            consignment='DespatchAdvice-Consignment'
        )
