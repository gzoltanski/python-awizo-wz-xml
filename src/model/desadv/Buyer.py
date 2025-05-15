import xml.etree.ElementTree as ET
from .base import DesadvBase

class Buyer(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Buyer")

        self.i_l_n = self.node.findtext("ILN")

    def get_i_l_n(self) -> str | None:
        return self.i_l_n

    def set_i_l_n(self, value: str | None) -> None:
        self._set_xml_text("ILN", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)