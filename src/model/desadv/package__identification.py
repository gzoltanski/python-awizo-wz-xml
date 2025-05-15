import xml.etree.ElementTree as ET
from .base import DesadvBase

class PackageIdentification(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Package-Identification")

        child_node = self.node.find("Goods-Identity")
        self.goods__identity = GoodsIdentity(desadv_file) if child_node is not None else None

        return self.goods__identity

    def set_goods__identity(self, value: str | None) -> None:
        self._set_xml_text("Goods-Identity", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)