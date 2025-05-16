from . import *

class PackingReference(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='Packing-Reference'
                 ):
        super().__init__(
            desadv_file,
            node,
            package_id='PackageId',
            package_number='PackageNumber',
            package_type='PackageType',
            serial_number='SerialNumber'
        )
