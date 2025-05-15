import xml.etree.ElementTree as ET
from .base import DesadvBase

class PackingSequence(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Packing-Sequence")

        child_node = self.node.find("Line")
        self.line = Line(desadv_file) if child_node is not None else None
        child_node = self.node.find("Packing-Reference")
        self.packing__reference = PackingReference(desadv_file) if child_node is not None else None

        return self.line

        return self.packing__reference

    def set_line(self, value: str | None) -> None:
        self._set_xml_text("Line", value)

    def set_packing__reference(self, value: str | None) -> None:
        self._set_xml_text("Packing-Reference", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)