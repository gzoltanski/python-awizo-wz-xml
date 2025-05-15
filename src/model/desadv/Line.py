import xml.etree.ElementTree as ET
from .base import DesadvBase

class Line(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Line")

        child_node = self.node.find("Line-Item")
        self.line__item = LineItem(desadv_file) if child_node is not None else None
        child_node = self.node.find("Package-Identification")
        self.package__identification = PackageIdentification(desadv_file) if child_node is not None else None

        return self.line__item

        return self.package__identification

    def set_line__item(self, value: str | None) -> None:
        self._set_xml_text("Line-Item", value)

    def set_package__identification(self, value: str | None) -> None:
        self._set_xml_text("Package-Identification", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)