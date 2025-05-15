from dataclasses import dataclass
from src.model.self.desadv.LineItem import LineItem
from src.model.self.desadv.PackageIdentification import PackageIdentification
from .base import DesadvBase

@dataclass
class Line(DesadvBase):
    line_item: LineItem
    package_identification: PackageIdentification