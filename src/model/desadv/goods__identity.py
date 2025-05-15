import xml.etree.ElementTree as ET
from .base import DesadvBase

class GoodsIdentity(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Goods-Identity")

        child_node = self.node.find("Range")
        self.range = Range(desadv_file) if child_node is not None else None
        self.type = self.node.findtext("Type")

        return self.range

    def get_type(self) -> str | None:
        return self.type

    def set_range(self, value: str | None) -> None:
        self._set_xml_text("Range", value)

    def set_type(self, value: str | None) -> None:
        self._set_xml_text("Type", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)