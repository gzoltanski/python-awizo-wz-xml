from dataclasses import dataclass
from src.model.desadv.LineItem import LineItem
from src.model.desadv.PackageIdentification import PackageIdentification

@dataclass
class Line:
    line_item: LineItem
    package_identification: PackageIdentification
