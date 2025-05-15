import xml.etree.ElementTree as ET
from .base import DesadvBase

class DespatchAdviceConsignment(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//DespatchAdvice-Consignment")

        self.packing__sequence = self.node.findtext("Packing-Sequence")

    def get_packing__sequence(self) -> str | None:
        return self.packing__sequence

    def set_packing__sequence(self, value: str | None) -> None:
        self._set_xml_text("Packing-Sequence", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)