import xml.etree.ElementTree as ET
from .base import DesadvBase

class DespatchAdviceHeader(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//DespatchAdvice-Header")

        self.buyer_order_number = self.node.findtext("BuyerOrderNumber")
        self.despatch_advice_date = self.node.findtext("DespatchAdviceDate")
        self.despatch_advice_number = self.node.findtext("DespatchAdviceNumber")
        self.despatch_number = self.node.findtext("DespatchNumber")
        self.estimated_delivery_date = self.node.findtext("EstimatedDeliveryDate")

    def get_buyer_order_number(self) -> str | None:
        return self.buyer_order_number

    def get_despatch_advice_date(self) -> str | None:
        return self.despatch_advice_date

    def get_despatch_advice_number(self) -> str | None:
        return self.despatch_advice_number

    def get_despatch_number(self) -> str | None:
        return self.despatch_number

    def get_estimated_delivery_date(self) -> str | None:
        return self.estimated_delivery_date

    def set_buyer_order_number(self, value: str | None) -> None:
        self._set_xml_text("BuyerOrderNumber", value)

    def set_despatch_advice_date(self, value: str | None) -> None:
        self._set_xml_text("DespatchAdviceDate", value)

    def set_despatch_advice_number(self, value: str | None) -> None:
        self._set_xml_text("DespatchAdviceNumber", value)

    def set_despatch_number(self, value: str | None) -> None:
        self._set_xml_text("DespatchNumber", value)

    def set_estimated_delivery_date(self, value: str | None) -> None:
        self._set_xml_text("EstimatedDeliveryDate", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)