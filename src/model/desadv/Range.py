from . import *

class Range(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Range'
                 ) -> None:
        super().__init__(
            desadv_file,
            node,
            id_begin='ID-Begin'
        )