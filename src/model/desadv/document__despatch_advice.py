import xml.etree.ElementTree as ET
from .base import DesadvBase

class DocumentDespatchAdvice(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Document-DespatchAdvice")

        self.despatch_advice__consignment = self.node.findtext("DespatchAdvice-Consignment")
        self.despatch_advice__header = self.node.findtext("DespatchAdvice-Header")
        self.despatch_advice__parties = self.node.findtext("DespatchAdvice-Parties")
        self.despatch_advice__transport = self.node.findtext("DespatchAdvice-Transport")

    def get_despatch_advice__consignment(self) -> str | None:
        return self.despatch_advice__consignment

    def get_despatch_advice__header(self) -> str | None:
        return self.despatch_advice__header

    def get_despatch_advice__parties(self) -> str | None:
        return self.despatch_advice__parties

    def get_despatch_advice__transport(self) -> str | None:
        return self.despatch_advice__transport

    def set_despatch_advice__consignment(self, value: str | None) -> None:
        self._set_xml_text("DespatchAdvice-Consignment", value)

    def set_despatch_advice__header(self, value: str | None) -> None:
        self._set_xml_text("DespatchAdvice-Header", value)

    def set_despatch_advice__parties(self, value: str | None) -> None:
        self._set_xml_text("DespatchAdvice-Parties", value)

    def set_despatch_advice__transport(self, value: str | None) -> None:
        self._set_xml_text("DespatchAdvice-Transport", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)