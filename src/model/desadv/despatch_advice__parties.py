import xml.etree.ElementTree as ET
from .base import DesadvBase

class DespatchAdviceParties(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//DespatchAdvice-Parties")

        self.buyer = self.node.findtext("Buyer")
        self.delivery_point = self.node.findtext("DeliveryPoint")
        self.seller = self.node.findtext("Seller")

    def get_buyer(self) -> str | None:
        return self.buyer

    def get_delivery_point(self) -> str | None:
        return self.delivery_point

    def get_seller(self) -> str | None:
        return self.seller

    def set_buyer(self, value: str | None) -> None:
        self._set_xml_text("Buyer", value)

    def set_delivery_point(self, value: str | None) -> None:
        self._set_xml_text("DeliveryPoint", value)

    def set_seller(self, value: str | None) -> None:
        self._set_xml_text("Seller", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)