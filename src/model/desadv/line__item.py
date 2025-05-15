import xml.etree.ElementTree as ET
from .base import DesadvBase

class LineItem(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Line-Item")

        self.best_before_date = self.node.findtext("BestBeforeDate")
        self.buyer_item_code = self.node.findtext("BuyerItemCode")
        self.e_a_n = self.node.findtext("EAN")
        self.item_description = self.node.findtext("ItemDescription")
        self.line_number = self.node.findtext("LineNumber")
        self.order_line_number = self.node.findtext("OrderLineNumber")
        self.quantity_despatched = self.node.findtext("QuantityDespatched")
        self.unit_of_measure = self.node.findtext("UnitOfMeasure")

    def get_best_before_date(self) -> str | None:
        return self.best_before_date

    def get_buyer_item_code(self) -> str | None:
        return self.buyer_item_code

    def get_e_a_n(self) -> str | None:
        return self.e_a_n

    def get_item_description(self) -> str | None:
        return self.item_description

    def get_line_number(self) -> str | None:
        return self.line_number

    def get_order_line_number(self) -> str | None:
        return self.order_line_number

    def get_quantity_despatched(self) -> str | None:
        return self.quantity_despatched

    def get_unit_of_measure(self) -> str | None:
        return self.unit_of_measure

    def set_best_before_date(self, value: str | None) -> None:
        self._set_xml_text("BestBeforeDate", value)

    def set_buyer_item_code(self, value: str | None) -> None:
        self._set_xml_text("BuyerItemCode", value)

    def set_e_a_n(self, value: str | None) -> None:
        self._set_xml_text("EAN", value)

    def set_item_description(self, value: str | None) -> None:
        self._set_xml_text("ItemDescription", value)

    def set_line_number(self, value: str | None) -> None:
        self._set_xml_text("LineNumber", value)

    def set_order_line_number(self, value: str | None) -> None:
        self._set_xml_text("OrderLineNumber", value)

    def set_quantity_despatched(self, value: str | None) -> None:
        self._set_xml_text("QuantityDespatched", value)

    def set_unit_of_measure(self, value: str | None) -> None:
        self._set_xml_text("UnitOfMeasure", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)