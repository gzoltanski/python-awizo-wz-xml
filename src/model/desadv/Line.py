from importlib.metadata import packages_distributions

from . import *

class Line(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Line'
                 ) -> None:
        super().__init__(desadv_file,
                         node,
                         line_item='Line-Item',
                         packages_identification='Package-Identification'
                         )
