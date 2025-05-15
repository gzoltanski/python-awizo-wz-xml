from .base import DesadvBase

class PackingReference(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.packingreference = self.desadv.root.find(f'.//PackingReference')
        self.package_id = self.packingreference.find('./PackageId') or self.packingreference.find('./PACKAGE_ID')
        self.package_number = self.packingreference.find('./PackageNumber') or self.packingreference.find('./PACKAGE_NUMBER')
        self.package_type = self.packingreference.find('./PackageType') or self.packingreference.find('./PACKAGE_TYPE')
        self.serial_number = self.packingreference.find('./SerialNumber') or self.packingreference.find('./SERIAL_NUMBER')
    package_id: str
    package_number: str
    package_type: str
    serial_number: str