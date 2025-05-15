import xml.etree.ElementTree as ET
from .base import DesadvBase

class Range(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Range")

        self.i_d__begin = self.node.findtext("ID-Begin")
        self.i_d__end = self.node.findtext("ID-End")

    def get_i_d__begin(self) -> str | None:
        return self.i_d__begin

    def get_i_d__end(self) -> str | None:
        return self.i_d__end

    def set_i_d__begin(self, value: str | None) -> None:
        self._set_xml_text("ID-Begin", value)

    def set_i_d__end(self, value: str | None) -> None:
        self._set_xml_text("ID-End", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)