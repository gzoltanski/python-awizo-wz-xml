from src.model.self.desadv.LineItem import LineItem
from src.model.self.desadv.PackageIdentification import PackageIdentification
from .base import DesadvBase

class Line(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.line = self.desadv.root.find(f'.//Line')
        self.line_item = self.line.find('./LineItem') or self.line.find('./LINE_ITEM')
        self.package_identification = self.line.find('./PackageIdentification') or self.line.find('./PACKAGE_IDENTIFICATION')
    line_item: LineItem
    package_identification: PackageIdentification