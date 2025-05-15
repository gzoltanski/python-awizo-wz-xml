import xml.etree.ElementTree as ET
from .base import DesadvBase

class DespatchAdviceTransport(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//DespatchAdvice-Transport")

        self.conveyance_reference_number = self.node.findtext("ConveyanceReferenceNumber")
        self.mode_of_transport = self.node.findtext("ModeOfTransport")
        self.terms_of_delivery = self.node.findtext("TermsOfDelivery")

    def get_conveyance_reference_number(self) -> str | None:
        return self.conveyance_reference_number

    def get_mode_of_transport(self) -> str | None:
        return self.mode_of_transport

    def get_terms_of_delivery(self) -> str | None:
        return self.terms_of_delivery

    def set_conveyance_reference_number(self, value: str | None) -> None:
        self._set_xml_text("ConveyanceReferenceNumber", value)

    def set_mode_of_transport(self, value: str | None) -> None:
        self._set_xml_text("ModeOfTransport", value)

    def set_terms_of_delivery(self, value: str | None) -> None:
        self._set_xml_text("TermsOfDelivery", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)